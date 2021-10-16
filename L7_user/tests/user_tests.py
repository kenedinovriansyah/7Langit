import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from core.utils.logging import logger
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from faker import Faker

faker = Faker()

# Author : Kenedy Nopriansyah
# Email : kenedinovriansyah@gmail.com
# description : Don't forgot to happy :D

with open('tests/token.txt', 'r') as r:
    readme = r.read()

token = None
try:
    token = VerifyJSONWebTokenSerializer().validate({'token': readme})
except:
    pass

class UserTests(unittest.TestCase):
    def setUp(self):
        self.e = APIClient()

    @unittest.skipIf(not User.objects.count(), 'not have user')
    def test_login_user(self):
        user = User.objects.first()
        urls = reverse('authtoken')
        data = {
            'username': user.username,
            'password': 'yourpassword'
        }
        response = self.e.post(urls,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], None)
        with open('tests/token.txt', 'w') as w:
            w.write(response.data['token'])
        logger.info("Accounts has been log in")

    @unittest.skipIf(not token, 'not have token or token is invalid')
    def test_refresh_token(self):
        urls = reverse('authtoken-refresh')
        data = {
            'token': readme
        }
        response = self.e.post(urls,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'],None)
        logger.info('Refresh token has been successfully')

    @unittest.skipIf(not token, 'not have token or token is invalid')
    def test_verify_token(self):
        urls = reverse('authtoken-verify')
        data = {
            'token': readme
        }
        response = self.e.post(urls,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], None)
        logger.info('Verify token has been successfully')

    def test_user_create(self):
        urls = reverse('user-list')
        data = {
            'username': faker.name(),
            'email': faker.email(),
            'password': 'yourpassword',
            'confirmation': 'yourpassword'
        }
        response = self.e.post(urls,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['message'], None)
        logger.info('Accounts has been created')
    def test_user_all(self):
        self.e.credentials(HTTP_AUTHORIZATION='Bearer ' + readme)
        urls = reverse('user-list')
        response = self.e.get(urls,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info('Get all user counts : {}'.format(len(response.data)))