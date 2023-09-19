#!/usr/bin/python

# Import CGI and CGIT module
import cgi, cgitb

# to create instance of FieldStorage
# class which we can use to work
# with the submitted form data
form = cgi.FieldStorage()

major = form.getvalue('major')
advisor = form.getvalue('advisor')
room = form.getvalue('room')
time = form.getvalue('time')
fullabstract = form.getvalue('fullabstract')
posters = form.getvalue('posters')

firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname')
wordsintitle = form.getvalue('wordsintitle')
wordsinabstract = form.getvalue('wordsinabstract')


print ("Content-type: text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>First CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h1>Executing CGI script</h1>")

print ("<h2>Major: %s</h2>"% (major))
print ("<h2>Advisor: %s</h2>"% (advisor))
print ("<h2>Room: %s</h2>" % (room))
print ("<h2>Time: %s</h2>" % (time))
print ("<h2>Display Full Abstract: %s</h2>" % (fullabstract))
print ("<h2>Display Posters or Talks: %s</h2>" % (posters))

print ("<h2>First Name: %s</h2>" % (firstname))
print ("<h2>Last Name: %s</h2>" % (lastname))
print ("<h2>Words in Title: %s</h2>" % (wordsintitle))
print ("<h2>Words in Abstract: %s</h2>" % (wordsinabstract))

print ("</body>")
print ("</html>")
