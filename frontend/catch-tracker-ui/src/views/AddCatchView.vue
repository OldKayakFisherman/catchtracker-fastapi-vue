<script setup>
import { onMounted, ref } from 'vue';
import LookupAPIService from '../services/lookupapiservice'
import CatchAPIService from '../services/catchapiservice'
import L from 'leaflet'

const baitsLookup = ref(null);
const rodsLookup = ref(null);
const skyLookup = ref(null);
const speciesLookup = ref(null);
const techniqueLookup = ref(null);
const terminalTackleLookup = ref(null);

// Form Fields
const ffLatitude = ref(null);
const ffLongitude = ref(null);
const ffDateCaught = ref(null);
const ffSpecies = ref(null);
const ffWeight = ref(null);
const ffWaterTemperature = ref(null);
const ffWaterDepth = ref(null);
const ffSkyCondition = ref(null);
const ffAirTemperature =ref(null);
const ffTerminalTackle = ref(null);
const ffTechnique = ref(null);
const ffBait = ref(null);
const ffRod =ref(null);
const ffFiles = ref(null);

function formatCatchMap(){
  ffLatitude.value = 38.895;
  ffLongitude.value = -77.0366;

  // Function to handle successful geolocation retrieval
  function handleGeolocation(position) {
      ffLatitude.value = position.coords.latitude;
      ffLongitude.value = position.coords.longitude;
      
      console.log(`User latitude: ${ffLatitude.value}, User longitude: ${ffLongitude.value}`);
     // You can now use these variables as needed.
  }

  // Function to handle geolocation error
  function handleGeolocationError(error) {
    console.error(`Error getting geolocation: ${error.message}`);
  }

  // Request geolocation on page load
  window.addEventListener('load', () => {
      if ('geolocation' in navigator) {
          navigator.geolocation.getCurrentPosition(handleGeolocation, handleGeolocationError);
      } else {
          console.error('Geolocation is not supported in this browser.');
      }
  });

  

  const map = L.map('mapContainer').setView([ffLatitude.value, ffLongitude.value], 10); // Set initial center and zoom level

  // Add a tile layer (you can replace this with your desired map provider)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  var marker;

  // Event listener for map clicks
  map.on('click', (e) => {
    ffLatitude.value = e.latlng.lat.toFixed(6);
    ffLongitude.value = e.latlng.lng.toFixed(6);
    
    if(marker !== undefined){
      map.removeLayer(marker);
    }

    marker = new L.Marker(e.latlng);
    map.addLayer(marker);

  });

}


onMounted(() =>{

  formatCatchMap();

  /*
  LookupAPIService.getLookups().then(
      (data) => {                
        baitsLookup.value = data.baits;
        rodsLookup.value = data.rods;
        skyLookup.value = data.sky;
        speciesLookup.value = data.species;
        techniqueLookup.value = data.techniques;
        terminalTackleLookup.value = data.terminal_tackle;
      }
  );   
  */

});



function addCatch(){

  let dataRecord = {

    latitude : ffLatitude.value,
    longitude : ffLongitude.value,
    catch_date : ffDateCaught.value,
    species : ffSpecies.value,
    weight : ffWeight.value,
    water_temperature : ffWaterTemperature.value,
    air_temperature : ffAirTemperature.value,
    water_depth : ffWaterDepth.value,
    sky_conditions : ffSkyCondition.value, 
    terminal_tackle : ffTerminalTackle.value,
    technique : ffTechnique.value,
    bait : ffBait.value,
    rod : ffRod.value
  };


  CatchAPIService.addCatch(dataRecord).then(
    (result) => {
      console.log(result);
    }
  );


}

function handleFileUpload(e){
  if(e.srcElement !== undefined && e.srcElement.files !== undefined){
    ffFiles.value = e.srcElement.files;
  }
}

</script>
<template>

<div class="row mt-3">

<div class="col-4">
    <!-- Create a map container with id "mapId" -->
    <div id="mapContainer" style="width: 400px; height: 400px;"></div>
    
    <div class="mt-5">
      <label for="formFileMultiple" class="form-label">Catch Media</label>
      <input id="fileUpload" v-on:change="handleFileUpload" class="form-control w-100" type="file"  multiple />
    </div>
</div>
<div class="col-6">

    <datalist id="dlTechniques">
      <option v-for="technique in techniqueLookup">{{ technique }}</option>
    </datalist>

    <datalist id="dlRods">
      <option>6'1" Bass Pro Medium Moderate Action Baitcaster with Daiwa Tatula 100 casting reel</option>
    </datalist>
    
    <datalist id="dlBaits">
      <option>Rapala Blue/Purple Jerkbait</option>
    </datalist>

    <datalist id="dlSpecies">
        <option>Bass</option>
        <option>Catfish</option>
        <option>Crappie</option>
        <option>Perch</option>
        <option>Bluegill</option>
    </datalist>

    <datalist id="dlSkyConditions">
      <option>Sunny</option>
      <option>Partly CloudY</option>
      <option>Overcast</option>
      <option>Light Rain</option>
      <option>Heavy Rain</option>
    </datalist>

    <datalist id="dlTerminalTackle">
      <option>Snap</option>
    </datalist>

    <form v-on:submit.prevent="addCatch">
        <div class="mb-3">
            <label for="txtLatitude" class="form-label">Latitude</label>
            <input v-model="ffLatitude" type="text" id="txtLatitude" class="form-control w-25" disabled required>
        </div>
        <div class="mb-3">
            <label for="txtLongitude" class="form-label">Longitude</label>
            <input v-model="ffLongitude" type="text" id="txtLongitude" class="form-control w-25" disabled required>
        </div>
        <div class="mb-3">
          <label for="dteDateCaught" class="form-label">Date Caught</label>
          <input v-model="ffDateCaught" type="date" id="dteDateCaught" name="dteDateCaught" class="form-control" required />
        </div>
        <div class="mb-3">
            <label for="species" class="form-label">Species</label>
            <input v-model="ffSpecies" list="dlSpecies" id="txtSpecies" name="txtSpecies" class="form-control" required />
        </div>
        <div class="mb-3">
            <label for="weight" class="form-label">Weight</label>
            <input v-model="ffWeight" type="text" id="weight" class="form-control w-25">
        </div>
        <div class="mb-3">
            <label for="waterTemperature" class="form-label">Water Temperature</label>
            <input v-model="ffWaterTemperature" type="text" id="waterTemperature" class="form-control w-25">
        </div>
        <div class="mb-3">
            <label for="waterDepth" class="form-label">Water Depth</label>
            <input v-model="ffWaterDepth" type="text" id="waterDepth" class="form-control w-25">
        </div>
        <div class="mb-3">
            <label for="skyConditions" class="form-label">Sky Conditions</label>
            <input v-model="ffSkyCondition" list="dlSkyConditions" id="txtSkyConditions" name="txtSkyConditions" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="airTemperature" class="form-label">Air Temperature</label>
            <input v-model="ffAirTemperature"  type="text" id="airTemperature" class="form-control w-25">
        </div>
        <div class="mb-3">
            <label for="txtTerminalTackle" class="form-label">Terminal Tackle</label>
            <input v-model="ffTerminalTackle" list="dlTerminalTackle" id="txtTerminalTackle" name="txtTerminalTackle" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="technique" class="form-label">Technique</label>
            <input v-model="ffTechnique" list="dlTechniques" id="txtTechnique" name="txtTechnique" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="dlBait" class="form-label">Bait</label>
            <input v-model="ffBait" list="dlBaits" id="txtBait" name="txtBait" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="txtRod" class="form-label">Rod</label>
            <input v-model="ffRod" list="dlRods" id="txtRod" name="txtRod" class="form-control" />
        </div>
        <!-- Add any additional fields as needed -->
        <div class="mt-3 mb-5">
          <button class="btn btn-secondary">Cancel</button>
          <input type="submit" class="btn btn-primary" value="Save">
        </div>
    </form>
    
</div>

</div>

</template>

<style>

</style>
