#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
birthdate=form.getvalue('birthdate')
hobby=form.getvalue('hobby')
print "Birthdate: <br/>"
print birthdate
print "Main Hobby: <br/>"
print hobby

print """Content-type: text/html

<title>Name+Family</title>
<form method="post" action="form_2.py">
Name:<br>
<input type="text" name="name"><br>
Family:<br>
<input type="text" name="family"><br>
<input type="submit" value="Submit"><br>
</form>
"""
