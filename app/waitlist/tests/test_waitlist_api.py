from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import WaitList

WAIT_LIST_CREATE_URL = reverse('waitlist:create')


class PublicWaitListApiTests(TestCase):
    """Test the waitlist add"""

    def setUp(self):
        self.client =APIClient()

    def test_create_wait_list_successful(self):
        """Test if user is able to create wait list"""
        payload = {
            'email': 'Anil.ambani@relience.com',
            'name': 'Anil Ambani',
        }
        res = self.client.post(WAIT_LIST_CREATE_URL, payload)

        exists = WaitList.objects.filter(
            name=payload['name']
        ).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_create_wait_list_invalid(self):
        """Test creating wait list without email"""
        payload = {'name': ''}
        res = self.client.post(WAIT_LIST_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


