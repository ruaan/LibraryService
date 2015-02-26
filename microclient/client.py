import requests
import json

class BaseClient:

	service_lookup = {
		"staging": {
			"UserService": "http://staging.userservice.tangentme.com"
		}
	}

	def __init__(self, environment="production"):
		self.environment = environment
		self.token = None

	def _get_base_url(self, service):
		return self.service_lookup.get(self.environment).get(service)


	def call(self, service, path, data={}, method="get"):
		
		base_url = self._get_base_url(service)
		url = "{0}{1}" .format(base_url, path)

		headers = {
	        'content-type': 'application/json',	        
		}
		if self.token is not None:
			headers.update({
				'Authorization':'Token {0}' . format (self.token)
			})

		http_method = getattr(requests, method)
		return http_method(url, data=json.dumps(data), headers=headers)


	def login(self, username, password):	
		self.token = None
		data={"username":username,"password":password}
		response = self.call('UserService', '/api-token-auth/', data, 'post')
		
		if response.status_code == 200:
			self.token = response.json().get("token")
			return True
		else:
			return False

	def logout(self):
		self.token = None

	def get(self, pk, data):
		pass

	def create(self, data):
		pass

	def update(self, pk, data):
		pass

	def delete(self, pk):
		pass




