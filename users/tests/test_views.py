from django.test import TestCase

# Test all urls that they are not returning any errors and are actually reachable
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
    
    def test_register_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertEqual(response.status_code, 200)

    def test_profile_loads_properly(self):
        """not authenticated should be unreachable"""
        response = self.client.get('http://127.0.0.1:8000/profile/')
        self.assertEqual(response.status_code, 302)

    def test_map_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/map')
        self.assertEqual(response.status_code, 200)

    def test_logout_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/logout/')
        self.assertEqual(response.status_code, 200)

        


        