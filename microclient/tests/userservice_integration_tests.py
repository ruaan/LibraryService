from django.test import TestCase
from ..client import BaseClient
from ..userservice import UserService


class UserServiceTestCase(TestCase):

	def setUp(self):
		self.service = UserService('staging')

	def test_get_me(self):
		self.service.login("admin", "a")
		response = self.service.me()
		
		assert response.status_code == 200, 'Expect 200 OK'
		assert response.json().get("username") == "admin", 'Expect the current user to be returned'

