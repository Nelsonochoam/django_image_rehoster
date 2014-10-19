from django.test import TestCase

# Create your tests here.
class TestView(TestCase):

    def test_view(self):

    	resp = self.client.get('/view/')
    	self.assertEqual(resp.status_code,200)
    	self.assertTrue('ImgList' in resp.context)





