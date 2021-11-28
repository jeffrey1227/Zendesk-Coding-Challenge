class Ticket:
	def __init__(self, ticket):
		# define what to store and show on the UI
		self.ticket_id = str(ticket['id'])
		self.subject = ticket['subject']
		self.submitter_id = str(ticket['submitter_id'])

