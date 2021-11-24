import requests
from requests.auth import HTTPBasicAuth

TICKET_API = 'https://zccticketsviewersupport.zendesk.com/api/v2/tickets/'
USERNAME = 'yuchunc7@uci.edu/token'
TOKEN = 'OQsv7Jvwl4bbCUktmJPMWOmwd0KqJEOAfk0eBjb8'

def showInvalidCommand():
	print("###Invalid command, please try again###")
	return

def showWelcome():
	print("\nWelcome to the ticket viewer.")
	print("Type \"menu\" to view options or \"quit\" to exit.")
	return

def showMenu():
	print("\n\tSelect view options:")
	print("\t * Press 1 to view all tickets")
	print("\t * Press 2 to view a specific ticket")
	print("\t * Type \"quit\" to exit\n")
	return

def showPageOptions():
	print("\n\tSelect page options:")
	print("\t * Type \"pp\" for prev page")
	print("\t * Type \"np\" for next page")
	print("\t * Type \"c\" to continue\n")
	return

def showSingleTicket(ticket):
	ticket_id = str(ticket['id'])
	subject = ticket['subject']
	submitter_id = str(ticket['submitter_id'])
	print(f'{ticket_id: <8}{subject: <64}{submitter_id: <16}')
	return 

def pageError(start, count, next_page=True):
	if next_page and start+25 >= count:
		print("\n<That was already the last page>")
		return True
	elif not next_page and start-25 < 0:
		print("\n<That was already the first page>")
		return True
	return False

def showPage(res, start, count, next_page=True):
	if not pageError(start, count, next_page):
		start = start+25 if next_page else start-25
		page_num = start // 25 + 1
		print("\n<Page "+ str(page_num) + ">")
		print(f'{"ID": <8}{"Subject": <64}{"Submitted by": <16}')
		end = start + 25 if (count - start) // 25 else count
		for i in range(start, end):
			showSingleTicket(res['tickets'][i])
		print("<End of Page "+ str(page_num) + ">")
	
	return start


def pageThrough(res, start, count, page_num):
	showPage(res, start-25, count)
	while True:
		showPageOptions()
		page = input('> ')
		if page == "np":
			start = showPage(res, start, count, next_page=True)
		elif page == "pp":
			start = showPage(res, start, count, next_page=False)
		elif page == 'c':
			break
		else:
			showInvalidCommand()



def getTickets(ticket_id=None):
	
	if not ticket_id:
		res = requests.get(TICKET_API, verify=True, auth=HTTPBasicAuth(USERNAME, TOKEN))
		res = res.json()
		start, count = 0, res['count']
		pageThrough(res, start, count, 1)
			
	else:
		res = requests.get(TICKET_API + ticket_id + '.json', verify=True, auth=HTTPBasicAuth(USERNAME, TOKEN))
		res = res.json()
		if 'error' in res:
			print("Ticket not found")
			return
		print(f'{"ID": <8}{"Subject": <64}{"Submitted by": <16}')
		showSingleTicket(res['ticket'])
	return


def execOptions():
	while True:
		showMenu()
		option = input('> ')
		if option == '1':
			getTickets()
		elif option == '2':
			ticket_id = input("Enter ticket number: ")
			getTickets(ticket_id)
		elif option == 'quit':
			exitProgram()
		else:
			showInvalidCommand()
	return


def exitProgram():
	print("Thanks for using ticket viewer.")
	quit()



if __name__ == '__main__':
	showWelcome()
	while True:
		cmd = input('> ')
		if cmd == 'menu':
			execOptions()

		elif cmd == 'quit':
			exitProgram()

		else:
			showInvalidCommand()
			showWelcome()


