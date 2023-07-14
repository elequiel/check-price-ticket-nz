from unittest import main, TestCase
from nz_tickets_job import get_prices, send_message
import os


TICKET_URL = os.getenv('TICKET_URL')

class TestGetPrices(TestCase):
    def test_if_returns_list(self):
        result = get_prices()
        
        self.assertIsInstance(result, list)
        
    def test_if_returns_null_list(self):
        result = len(get_prices())
        
        self.assertIsNotNone(result)
        
    def test_if_object_has_two_fields(self):
        result = len(get_prices()[0])
        
        self.assertEqual(result, 2)
        
# class TestSendMessage(TestCase):
#     def test_if_msg_is_sended(self):
#         result = send_message()
        
#         self.assertEqual(result["ok"], "true")
        
if __name__ == '__main__':
    main()