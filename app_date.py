
import datetime

now = datetime.datetime.now()

print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print ("Content-type: text/html\n\n")
print ("<html>\n<body>")
print ("div style=\"width: 100%; font-sixe: 40px; font-weight: bold; text-aling: center;\">")
print ("Python Script Test Page", now)
print ("</div>\n</body>\n</html>")


