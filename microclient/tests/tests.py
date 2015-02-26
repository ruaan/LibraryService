from django.test import TestCase

from .client import BaseClient, UserService

class MicroServiceBaseClientTestCase(TestCase):

	def setUp(self):
		self.client = BaseClient('staging')

	def test_login(self):

		is_logged_in = self.client.login("admin", "a")
		assert is_logged_in == True, 'Expect login to have worked'

	def test_logout(self):

		is_logged_in = self.client.login("admin", "a")
		assert is_logged_in == True, 'Expect login to have worked'

		self.client.logout()
		assert self.client.token == None, 'Expect the user to be logged out'


class UserServiceTestCase(TestCase):

	def setUp(self):
		self.service = UserService('staging')

	def test_get_me(self):
		self.service.login("admin", "a")
		response = self.service.me()
		
		assert response.json().get("username") == "admin", 'Expect the current user to be returned'

