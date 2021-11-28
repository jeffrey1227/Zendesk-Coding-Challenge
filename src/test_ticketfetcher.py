import unittest
from unittest.mock import patch
from ticketfetcher import TicketFetcher
import requests
from requests.auth import HTTPBasicAuth


class TestTicketFetcher(unittest.TestCase):

	def test_fetchOneTicketById_true(self):
		ticket_fetcher = TicketFetcher()
		
		ticket_fetcher.fetchOneTicketById('2')
		self.assertTrue(ticket_fetcher.res.ok)
		self.assertEqual(ticket_fetcher.res.status_code, 200)

	def test_fetchOneTicketById_false(self):
		ticket_fetcher = TicketFetcher()
		
		ticket_fetcher.fetchOneTicketById('35354')
		self.assertEqual(ticket_fetcher.res.status_code, 404)


	def test_fetchAllTickets_true(self):
		ticket_fetcher = TicketFetcher()
		
		ticket_fetcher.fetchAllTickets()
		self.assertTrue(ticket_fetcher.res.ok)
		self.assertEqual(ticket_fetcher.res.status_code, 200)

	def test_fetchAllTickets_false(self):
		ticket_fetcher = TicketFetcher()
		
		ticket_fetcher.token = 'Invalid token'
		ticket_fetcher.fetchAllTickets()	
		self.assertEqual(ticket_fetcher.res.status_code, 401)


	def test_checkResError(self):
		ticket_fetcher = TicketFetcher()
		ticket_fetcher.username = 'email@example.com/token'
		ticket_fetcher.fetchAllTickets()
		self.assertTrue(ticket_fetcher.checkResError)

		ticket_fetcher.token = 'Invalid token'
		ticket_fetcher.fetchAllTickets()
		self.assertTrue(ticket_fetcher.checkResError)







if __name__ == '__main__':
	unittest.main()