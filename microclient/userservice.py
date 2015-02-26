from .client import BaseClient 

class UserService(BaseClient):

	service = "UserService"

	def me(self):
		return self.call(self.service, '/users/me/')