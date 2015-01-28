#!/usr/bin/env python

print """Content-type: text/html

<title>Birthdate & Hobby</title>
<form method="post" action="form_1.py">
Birthdate:<br>
<input type="date" name="birthdate"><br>
Main Hobby:<br>
<input type="text" name="hobby"><br>
<input type="submit" value="Submit"><br>
</form>
"""

import cgi
form = cgi.FieldStorage()
name=form.getvalue('name')
family=form.getvalue('family')
print "Name: "
print name
print "<br/>"
print "Family: "
print family
print "<br/>"
