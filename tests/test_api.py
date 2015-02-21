# -*- coding: utf-8 -*-
import unittest

from api import application


class TestApi(unittest.TestCase):
    def setUp(self):
        application.app.config['TESTING'] = True
        self.app = application.app.test_client()

    def test_hello_endpoint(self):
        response = self.app.get('/api/hello')
        assert response.status_code == 200
        assert response.data == b'Hello, world!'

if __name__ == '__main__':
    unittest.main()
