from asyncio.windows_events import NULL
from run import app
import unittest

# Test class
class FlaskTest(unittest.TestCase):

    #setUp() method to create a test client to inject made-up requests into the application for the purposes of testing
    def setUp(self):
        self.app = app.test_client()
    
    #Positive Test cases

    #Check for response 200 for initial load of webpage/server
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)     

    #retrieving the inital get_name page for following test cases below
    def getname(self, uname):
        return self.app.post(
        '/get_name',
        data=dict(username=uname),  
        follow_redirects=True   
        )
    
    #Check for valid username being entered in the username tag
    def test_valid_user(self):
        response = self.getname('Manasa')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello Manasa', response.data)

    #Check for presence of a tag with name "username"
    def test_field_form(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200) 
        html = response.get_data(as_text=True)
        self.assertIn('name="username"', html)

    #check if the validation works when user passes empty string to username field
    def test_null_user(self):
        response = self.getname('')
        self.assertIn(b'Please enter a Name', response.data)

    #Negative Test cases

    #Negative scenario where user clicks submit without entering any name, status code -400 returned
    def test_invalid_user(self):
        response = self.getname('Manasa123')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('name="username"', html)

    #Check to see if the user entered numerical value as input
    def test_numeric_user(self):
        response = self.getname('123')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('name="username"', html)

if __name__ == '__main__':
    unittest.main()

