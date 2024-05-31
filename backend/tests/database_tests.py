import unittest
from database.session import get_db_session
from database.models import CatchDetail
from database.repositories import LookupRepository, CatchRepository, StatRepository
from tests.utilities import create_test_catch_records
from tests.utilities import get_db_test_session
from datetime import datetime

class SessionTests(unittest.TestCase):

    def test_get_db_session(self):
        self.assertIsNotNone(get_db_session())

class LookupRepositoryTests(unittest.TestCase):

    def test_get_unique_techniques(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_techniques(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 4)

    def test_get_unique_species(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_species(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 4)

    def test_get_unique_sky_conditions(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_sky_conditions(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 3)


    def test_get_unique_terminal_tackle(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_terminal_tackle(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 5)

    def test_get_unique_baits(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_baits(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 4)

    def test_get_unique_rods(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_rods(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 3)

class StatsRepositoryTests(unittest.TestCase):

    def test_ytd_catch_stats_overall(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(5)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now()

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records_count: int = stat_repo.ytd_catch_stats_overall(db)

            self.assertIsNotNone(stat_records_count)
            self.assertEquals(stat_records_count, 5)

    def test_ytd_catch_stats_species(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(5)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now()
                #assign species
                catch_record['species'] = "Bass"

            #Add some more
            for catch_record in create_test_catch_records(6):
                #assign them current dates
                catch_record['catch_date'] = datetime.now()
                #assign species
                catch_record['species'] = "Perch"

                raw_catch_records.append(catch_record)
                
            #Add some more
            for catch_record in create_test_catch_records(10):
                #assign them current dates
                catch_record['catch_date'] = datetime.now()
                #assign species
                catch_record['species'] = "Crappie"

                raw_catch_records.append(catch_record)


            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records = stat_repo.ytd_catch_stats_by_species(db)

            self.assertIsNotNone(stat_records)
            
            for db_record in stat_records:
                if db_record[0] == "Bass":
                    self.assertEquals(db_record[1], 5)
                if db_record[0] == "Perch":
                    self.assertEquals(db_record[1], 6)
                if db_record[0] == "Crappie":
                    self.assertEquals(db_record[1], 10)

    def test_ytd_top_techniques(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()


        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(500)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now()            


            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records = stat_repo.ytd_top_techniques(db)

            self.assertIsNotNone(stat_records)
            self.assertEquals(len(stat_records), 3)


    def test_prior_yr_top_techniques(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()

        current_year = datetime.now().year

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(500)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now().replace(year=(current_year -1))            

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records = stat_repo.prior_yr_top_techniques(db)

            self.assertIsNotNone(stat_records)
            self.assertEquals(len(stat_records), 3)

    def test_ytd_top_baits(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()


        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(500)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now()            


            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records = stat_repo.ytd_top_baits(db)

            self.assertIsNotNone(stat_records)
            self.assertEquals(len(stat_records), 3)


    def test_prior_yr_top_baits(self):

        catch_repo = CatchRepository()
        stat_repo = StatRepository()

        current_year = datetime.now().year

        with get_db_test_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(500)

            for catch_record in raw_catch_records:
                #assign them current dates
                catch_record['catch_date'] = datetime.now().replace(year=(current_year -1))            

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)
    
            #test the stat
            stat_records = stat_repo.prior_yr_top_baits(db)

            self.assertIsNotNone(stat_records)
            self.assertEquals(len(stat_records), 3)
