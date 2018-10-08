from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'test', 'password': 'qwerty'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User was created successfullly.'}, json.loads(response.data))

    def test_register_login(self):
        def test_register_user(self):
            with self.app() as client:
                with self.app_context():
                    client.post('/register', data={'username': 'test', 'password': 'qwerty'})
                    auth_response = client.post('/auth',
                                               data=json.dumps({'username': 'test', 'password': 'qwerty'}),
                                               header={'Content-Type': 'application/json'})

                    self.assertIn('access_token', json.loads(auth_response.data).keys)

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': 'qwerty'})
                response = client.post('/register', data={'username': 'test', 'password': 'qwerty'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'User already exists'}, json.loads(response.data))