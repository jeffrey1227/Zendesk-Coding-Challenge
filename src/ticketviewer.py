from ticketfetcher import TicketFetcher
from ticket import Ticket


class TicketViewer:

	def __init__(self):
		self.showWelcome()
		self.ticket_fetcher = TicketFetcher()


	@staticmethod
	def showWelcome():
		print("\nWelcome to the Zendesk ticket viewer.")
		print("Type \"menu\" to view options or \"quit\" to exit.\n")

	@staticmethod
	def showMenu():
		print("\n\tSelect view options:")
		print("\t * Press 1 to view all tickets")
		print("\t * Press 2 to view a specific ticket")
		print("\t * Type \"quit\" to exit\n")

	@staticmethod
	def showCommandIsInvalid():
		print("### Invalid command, please try again. ###")

	@staticmethod
	def showPageOptions():
		print("\n\tSelect page options:")
		print("\t * Type \"pp\" for prev page")
		print("\t * Type \"np\" for next page")
		print("\t * Type \"c\" to continue\n")

	@staticmethod
	def quitProgram():
		print("Thanks for using Zendesk ticket viewer.")
		quit()
		
	@staticmethod	
	def readInput():
		return input('> ') 

	def showTicketById(self):
		ticket_id = input("Enter ticket number: ")
		ticket = self.ticket_fetcher.fetchOneTicketById(ticket_id)['ticket']
		print('-'*80)
		print(f'|{"ID": <8}{"Subject": <54}{"Submitted by": <16}|')
		self.listSingleTicket(Ticket(ticket))
		print('-'*80)

		self.showMenu()

	def getEndAndPageNumber(self):
		self.end = self.start + 25 if (self.count - self.start) // 25 else self.count
		self.page_num = self.start // 25 + 1


	def showAllTickets(self):
		tickets = self.ticket_fetcher.fetchAllTickets()['tickets']
		self.ticket_list = []
		self.start = 0
		self.count = len(tickets)
		self.getEndAndPageNumber()
		for i in range(self.count):
			self.ticket_list.append(Ticket(tickets[i]))
		
		self.showPage()
		self.pageThrough()
		self.showMenu()

	@staticmethod
	def listSingleTicket(ticket):
		print(f'|{ticket.ticket_id: <8}{ticket.subject: <54}{ticket.submitter_id: <16}|')

	def isPageError(self):
		if self.start == 0 and self.count == 0:
			return False
		if self.start >= self.count:
			print("\n<That was already the last page>")
			self.start -= 25
			return True
		elif self.start < 0:
			print("\n<That was already the first page>")
			self.start += 25
			return True
		return False

	def showPage(self):
		if not self.isPageError():
			
			print("\n<Page "+ str(self.page_num) + ">")
			print('-'*80)
			print(f'|{"ID": <8}{"Subject": <54}{"Submitted by": <16}|')
			
			for i in range(self.start, self.end):
				self.listSingleTicket(self.ticket_list[i])
			
			print('-'*80)
			print("<End of Page "+ str(self.page_num) + ">")


	def nextPage(self):
		self.start += 25
		self.getEndAndPageNumber()
		self.showPage()

	def prevPage(self):
		self.start -= 25
		self.getEndAndPageNumber()
		self.showPage()

	def pageThrough(self):
		actions = {'np': self.nextPage,
				   'pp': self.prevPage
				   }
		while True:
			self.showPageOptions()
			action = self.readInput()
			if action in actions:
				actions[action]()
			elif action == 'c':
				return
			else:
				self.showCommandIsInvalid()




