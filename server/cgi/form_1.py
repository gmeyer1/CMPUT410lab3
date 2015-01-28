#!/usr/bin/env python

# CMPUT 410 - Winter 2015
# Glenn Meyer
# gmeyer1

print """Content-type: text/html

<title>Name & Family</title>
<form method="post" action="form_2.py">
Name:<br>
<input type="text" name="name"><br>
Family:<br>
<input type="text" name="family"><br>
<input type="submit" value="Submit"><br>
</form>
"""

import cgi
form = cgi.FieldStorage()
birthdate=form.getvalue('birthdate')
hobby=form.getvalue('hobby')
print "Birthdate: "
print birthdate
print "<br/>"
print "Main Hobby: "
print hobby
print "<br/>"
