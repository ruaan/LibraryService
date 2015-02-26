from django.core.urlresolvers import reverse
from django.conf import settings
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
from models import Book, BookRegistry

import requests 
import responses

def mock_auth_success():

	url = '{0}/users/me/' . format(settings.USER_SERVICE_BASE_URL)		
	response_string = '{"username": "TEST"}'
	responses.add(responses.GET, url,
              body=response_string, status=200,
              content_type='application/json')

def mock_auth_failure():

	url = '{0}/users/me/' . format(settings.USER_SERVICE_BASE_URL)		
	responses.add(responses.GET, url,
              body='', status=401,
              content_type='application/json')


class BookModelTestCase(TestCase):

	def test_create_book_creates_BookRegistry(self):

		data = {
			"title": "Some book",
			"purchase_url": "http://amazon.com"
		}

		book = Book.objects.create(**data)

		assert book.bookregistry_set.count() == 1, 'Expect a \'requested\' BookRegistry item to exist'
		assert book.bookregistry_set.all()[0].action == 'Requested', 'Expect item action to be \'Registered\''


class BookAPITestCase(TestCase):

	def setUp(self):

		data = {
			"title": "Some book",
			"purchase_url": "http://amazon.com"
		}
		self.book = Book.objects.create(**data)
		self.client = Client()

	@responses.activate
	def test_get_book(self):
		mock_auth_success()
		url = reverse('book-detail', args=[self.book.pk])
		response = self.client.get(url)	

		assert response.status_code == status.HTTP_200_OK, 'Expect 200 OK'
		print response.content


