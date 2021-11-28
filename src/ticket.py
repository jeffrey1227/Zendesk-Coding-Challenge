class Ticket:
	def __init__(self, ticket):
		self.ticket_id = str(ticket['id'])
		self.subject = ticket['subject']
		self.submitter_id = str(ticket['submitter_id'])

