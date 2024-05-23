import unittest
from database.session import get_db_session
from database.repositories import LookupRepository, CatchRepository
from tests.utilities import create_test_catch_records
from tests.utilities import get_db_text_session

class SessionTests(unittest.TestCase):

    def test_get_db_session(self):
        self.assertIsNotNone(get_db_session())

class RepositoryTests(unittest.TestCase):

    def test_get_unique_techniques(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_text_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_techniques(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 2)

    def test_get_unique_species(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_text_session() as db:

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

        with get_db_text_session() as db:

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

        with get_db_text_session() as db:

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

        with get_db_text_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_baits(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 2)

    def test_get_unique_rods(self):

        catch_repo = CatchRepository()
        lookup_repo = LookupRepository()

        with get_db_text_session() as db:

            #Create some test catch records
            raw_catch_records = create_test_catch_records(100)

            #Persist those records
            catch_repo.add_catches(db, raw_catch_records)

            #test for unique records
            unique_records = lookup_repo.get_unique_catch_rods(db)

            self.assertIsNotNone(unique_records)
            self.assertGreater(len(unique_records), 0)
            self.assertLessEqual(len(unique_records), 3)


