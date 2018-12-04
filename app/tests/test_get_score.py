from unittest import TestCase
from api.score.get import get_score_by_cookie_id

class TvsApiTestCase(TestCase):
    def test_get_by_existing_cookie_id(self):
        """Does API return json list for an existing DPID"""
        cookie_id = 9130470
        result = get_score_by_cookie_id(cookie_id)
        # self.assertTrue(False)
        self.assertEqual(len(result),2)
