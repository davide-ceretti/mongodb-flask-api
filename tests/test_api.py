# -*- coding: utf-8 -*-
import unittest
import json

from api import application


def resp_data_to_dict(response, encoding='utf-8'):
    return json.loads(response.data.decode(encoding))


class TestApi(unittest.TestCase):
    def setUp(self):
        application.app.config['TESTING'] = True
        self.app = application.app
        self.mongo = application.mongo
        self.client = self.app.test_client()

    def test_hello_endpoint(self):
        response = self.client.get('/api/hello')
        assert response.status_code == 200
        assert response.data == b'Hello, world!'

    def test_post_create_user_returns_201(self):
        data = json.dumps({'username': 'luke88', 'age': 26})
        response = self.client.post(
            '/api/user',
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        assert response.status_code == 201

    def test_post_create_user_returns_valid_data(self):
        data = json.dumps({'username': 'luke88', 'age': 27})
        response = self.client.post(
            '/api/user',
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        response_data = resp_data_to_dict(response)
        assert response_data.pop('username') == 'luke88'
        assert response_data.pop('age') == 27
        assert isinstance(response_data.pop('id'), str)
        assert response_data == {}


if __name__ == '__main__':
    unittest.main()
