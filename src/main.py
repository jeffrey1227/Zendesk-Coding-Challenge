from ticketfetcher import TicketFetcher
from ticket import Ticket
from ticketviewer import TicketViewer


def main():
	ticket_viewer = TicketViewer()

	# define acceptable commands
	actions = {'1': ticket_viewer.showAllTickets,
			   '2': ticket_viewer.showTicketById,
			   'menu': ticket_viewer.showMenu,
			   'quit': ticket_viewer.quitProgram
			   }

	while True:
		action = ticket_viewer.readInput()
		if action in actions:
			actions[action]()
		else:
			# if user input a invalid command, tell the user it was invalid, and make them try again
			ticket_viewer.showCommandIsInvalid()

	return



if __name__ == '__main__':
	main()