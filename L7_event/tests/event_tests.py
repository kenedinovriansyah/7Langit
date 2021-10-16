import unittest
import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from L7_user.tests.user_tests import token, readme
from django.core.files import File
from faker import Faker
from core.utils.logging import logger


faker = Faker()

class EventTests(unittest.TestCase):
    def setUp(self):
        self.e = APIClient()

    @unittest.skipIf(not token, 'not have token or token is invalid')
    def test_event_create(self):
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        urls = reverse('event-list')
        files = File(open("20210615143026_60c8571292422.jpeg", "rb"))
        data = {
            'name_category': faker.name(),
            'status': random.randint(0,1),
            'start_date': faker.date(),
            'end_date': faker.date(),
            'name': faker.name(),
            'start_date': faker.date(),
            'end_date': faker.date(),
            'location': faker.secondary_address(),
            'address': faker.address(),
            'country': faker.country(),
            'province': faker.state(),
            'district': 'Online',
            'region': 'Online',
            'organization_name': faker.domain_name(),
            'user': token.get('user').id,
            'banner': files 
        }
        response = self.e.post(urls,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['message'], None)
        self.assertEqual(response.data['message'], 'Event has been created')
        logger.info('Event has been created')

    @unittest.skipIf(not token, 'not have token or token is invalid')
    def test_event_list(self):
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        urls = reverse('event-list')
        response = self.e.get(urls)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info('Event list counts : {}'.format(len(response.data)))
        logger.critical(response.data)