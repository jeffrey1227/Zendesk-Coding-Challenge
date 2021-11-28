import unittest
from unittest.mock import patch
from ticketviewer import TicketViewer

class TestTicketViewer(unittest.TestCase):

	def test_isPageError(self):
		ticket_viewer = TicketViewer()
		
		ticket_viewer.start = 100
		ticket_viewer.count = 100
		self.assertTrue(ticket_viewer.isPageError())

		ticket_viewer.start = 0
		ticket_viewer.count = 0
		self.assertFalse(ticket_viewer.isPageError())

	def test_getEndAndPageNumber(self):
		ticket_viewer = TicketViewer()
		ticket_viewer.start = 100
		ticket_viewer.count = 101
		ticket_viewer.getEndAndPageNumber()

		self.assertEqual(ticket_viewer.end, 101)
		self.assertEqual(ticket_viewer.page_num, 5)

	
	


if __name__ == '__main__':
	unittest.main()