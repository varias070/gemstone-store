from django.test import TestCase


class ViewTest(TestCase):

    def test_check_bed_request_method(self):
        resp = self.client.get('http://127.0.0.1:8001/')
        self.assertEqual(resp.status_code, 400)

    # def test_check_request_method(self):
    #     resp = self.client.post('http://127.0.0.1:8001/')
    #     self.assertEqual(resp.status_code, 200)
    #
    def test_check_request_content_type(self):
        resp = self.client.post('http://127.0.0.1:8001/', CONTENT_TYPE='text/csv')
        self.assertEqual(resp.status_code, 500)
