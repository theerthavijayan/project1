from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
# from rest_framework import status



class TestSample(TestCase):
    def setUp(self): # called before the invocation of each test method in the given class.
        self.client = APIClient()

        """API Client means the software that acts as the interface between Agency's computer and the server.
        A client is the person or program using the API. The client makes requests to the API in order to 
        retrieve some information or change something within the application. Your web browser is a client — 
        it interacts with APIs different websites to get page content from them.
        APIClient eg: postman
        
        we will import the Client class. This is a testing browser that enables us to make http requests
        within Django tests."""
    def get_client(self):
        return self.client

    def test_index(self): # method name should start with test
        url = reverse('index') # to get the correct url.....check in views home func
        #  The reverse function is imported in order to return a url when the url’s name is passed in as an argument.
        print(url)
        res = self.client.get(self = url) # call url and save it to variable
        print(res)
        # print(res.data)
        
        self.assertEquals(res.status_code, 200)# the test pass only when status code = 200 which represent success
        self.assertEquals(res.data, "hello")# the test pass only when msg eqauls that given in views
