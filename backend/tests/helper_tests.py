import unittest
from database.models import SearchIndex
from helpers import assign_variables_from_dict, assign_dict_from_variables



class HelperTests(unittest.TestCase):

    def test_assign_variables_from_dict(self):

        model = SearchIndex()

        values = {
            "data": "test data",
            "catch_detail_id": 1
        }

        eval_record = assign_variables_from_dict(model, values)

        self.assertEquals(model.data, "test data")
        self.assertEquals(model.catch_detail_id, 1)

    def test_assign_dict_from_variables(self):

        model = SearchIndex()

        model.catch_detail_id = 1
        model.data = "test data" 

        
        eval_dict = assign_dict_from_variables(model)

        self.assertIsNotNone(eval_dict['catch_detail_id'])
        self.assertIsNotNone(eval_dict['data'])
        self.assertEquals(eval_dict['catch_detail_id'], 1)
        self.assertEquals(eval_dict['data'], "test data")
        self.assertEquals(len(eval_dict.keys()), 4) 
