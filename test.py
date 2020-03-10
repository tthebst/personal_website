import json
import unittest

from app import app



class FlaskBookshelfTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 
    

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_wallpaper_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/wallpapers') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_wallpaper_all_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/wallpapers_all') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 
if __name__ == '__main__':
  unittest.main()