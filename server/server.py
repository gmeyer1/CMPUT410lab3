#!/usr/bin/env python

# CMPUT 410 - Winter 2015
# Glenn Meyer
# gmeyer1
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
