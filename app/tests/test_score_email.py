from unittest import TestCase
from api.scoreEmail.get import get_Score_Email_by_dp_id

class TvsApiTestCase(TestCase):
    def test_get_Score_Email_by_dp_id(self):
        """Does API return json list for an existing DPID"""
        dp_id = 1
        result = get_Score_Email_by_dp_id(dp_id)
        # self.assertTrue(False)
        self.assertEqual(len(result[0]),3)
