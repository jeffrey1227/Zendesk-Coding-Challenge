import requests
from requests.auth import HTTPBasicAuth


class TicketFetcher:

	def __init__(self):
		self.api = 'https://zccticketsviewersupport.zendesk.com/api/v2/tickets/'
		self.username = 'yuchunc7@uci.edu/token'
		self.token = 'OQsv7Jvwl4bbCUktmJPMWOmwd0KqJEOAfk0eBjb8'

	def fetchOneTicketById(self, ticket_id):
		try:
			self.res = requests.get(self.api + ticket_id + '.json', verify=True, auth=HTTPBasicAuth(self.username, self.token))
		except requests.exceptions.RequestException as e:
			raise SystemExit("### Sorry, we are unable to retrieve ticket info at the time. ###")
		# change response to dict
		self.res_dict = self.res.json()
		if self.checkResError():
			return None

		return self.res_dict

	def fetchAllTickets(self):
		try:
			self.res = requests.get(self.api, verify=True, auth=HTTPBasicAuth(self.username, self.token))
		except requests.exceptions.RequestException as e:
			raise SystemExit("### Sorry, we are unable to retrieve ticket info at the time. ###")
		self.res_dict = self.res.json()
		if self.checkResError():
			return None

		return self.res_dict

	def checkResError(self):
		# error handling messages
		if 'error' in self.res_dict:
			if self.res_dict['error'] == "Couldn't authenticate you":
				print("### Wrong username or token. Please try again. ###")
			if self.res_dict['error'] == "RecordNotFound":
				print("### Ticket not found. Please try again. ###")
			return True
		return False

	def printError():
		pass