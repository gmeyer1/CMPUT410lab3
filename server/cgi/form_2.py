#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
name=form.getvalue('name')
family=form.getvalue('family')
print "Name: "<br/>"
print name
print "Family: "<br/>"
print family
 
print """Content-type: text/html

<title>Birthdate+Hobby</title>
<form method="post" action="form_1.py">
Birthdate:<br>
<input type="date" name="birthday"><br>
Main Hobby:<br>
<input type="text" name="hobby"><br>
<input type="submit" value="Submit"><br>
</form>
"""
