<script setup>
    
    import { onMounted, ref } from 'vue';
    import StatApiService from '../services/statapiservice'

    let ytd_overall_show_no_data = ref(false);
    let ytd_top_techniques_has_data = ref(false);
    let pry_top_techniques_has_data = ref(false);
    let ytd_top_baits_has_data = ref(false);
    let pry_top_baits_has_data = ref(false);

    onMounted(() => {
        
      StatApiService.getStats().then(
            (data) => {                
                ytd_overall_show_no_data.value = ref((data.ytd_catch_stats_overall.length == 0));
                ytd_top_techniques_has_data.value = (data.ytd_top_techniques.length > 0);
                pry_top_techniques_has_data.value = (data.prior_yr_top_techniques.length > 0); 
                ytd_top_baits_has_data.value = (data.ytd_top_baits.length > 0);
                pry_top_baits_has_data.value = (data.prior_yr_top_baits > 0);
            }
        );
    });


</script>

<template>
    <div class="row">

        <!-- Sidebar -->
        <div class="col-3">
            
                <h5 class="mt-3">YTD Catch Stats</h5>
                <h5 v-if="ytd_overall_show_no_data">No Data</h5>
                
                <!--
                <ul class="list-group">
                    <li class="list-group-item">
                        <a href="#"><span class="badge text-bg-primary">105</span></a> <small>Total Catches</small>
                    </li>
                </ul>
                -->
</div>

<!-- Main Body -->
<div class="col-9 mt-3">
    <!-- Row 1 -->
    <div class="row">
      <div class="col-3">
          <div class="card">
           <div class="card-header">
            YTD top techniques
           </div>

          <ul v-if="ytd_top_techniques_has_data" class="list-group list-group-flush">
            <li class="list-group-item"><a href="#" class="link-dark">Shakey Head</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Slowroll</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Aggressive Jerkbait Retrieve</a></li>
          </ul>
          </div>
      </div>
      <div class="col-3">
          <div class="card">
          <div class="card-header">
            Prior Year Top Techniques
          </div>
          <ul v-if="pry_top_techniques_has_data" class="list-group list-group-flush">
            <li class="list-group-item"><a href="#" class="link-dark">Texas Rig</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Slowroll</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Swimming Worm</a></li>
          </ul>
          </div>
      </div>  
    </div>                  
    <!-- Row 3 -->
    <div class="row mt-3">
      <div class="col-3">
          <div class="card">
          <div class="card-header">
            YTD top Baits
          </div>
          <ul v-if="ytd_top_baits_has_data" class="list-group list-group-flush">
            <li class="list-group-item"><a href="#" class="link-dark">Shakey Head</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Slowroll</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Aggressive Jerkbait Retrieve</a></li>
          </ul>
          </div>
      </div>
      <div class="col-3">
          <div class="card">
          <div class="card-header">
            Prior Year Top Baits
          </div>
          <ul v-if="pry_top_baits_has_data" class="list-group list-group-flush">
            <li class="list-group-item"><a href="#" class="link-dark">Texas Rig</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Slowroll</a></li>
            <li class="list-group-item"><a href="#" class="link-dark">Swimming Worm</a></li>
          </ul>
          </div>
      </div>  
    </div>

</div>

</div>

</template>

<style>

</style>
