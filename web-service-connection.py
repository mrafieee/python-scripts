from jalali import gregorian_to_jalali
from datetime import date
jdate = gregorian_to_jalali(date.today().year,date.today().month,date.today().day)


# TODO: creating spicified commandline usable class for this funtionality
# 1. sending requests to specified address using POST
# 2. verifying bank transaction results and generating specified responses to user
# 3. report if needed


def bank_request():
	return True

def bank_verify(request):
	if request.method == 'POST':
		state = request.POST["State"]
		refNum = request.POST["RefNum"]
		resNum = request.POST["ResNum"]
		mid = request.POST["MID"]
		traceNo = request.POST["TRACNO"]
		print state

		if mid == "ACCNUM":
			############ using SOAPpy
			# from SOAPpy import WSDL
			# wsdl ='https://acquirer.samanepay.com/payments/referencepayment.asmx?WSDL'
			# server = WSDL.Proxy(wsdl)
			# server.soapproxy.config.dumpSOAPOut = 1
			# server.soapproxy.config.dumpSOAPIn = 1
			# result = server.verifyTransaction(refNum,'ACCNUM')

			############ using SUDS
			from suds.client import Client
			c = Client('https://acquirer.samanepay.com/payments/referencepayment.asmx?wsdl')
			response = c.service.verifyTransaction(refNum,'ACCNUM')
	return True