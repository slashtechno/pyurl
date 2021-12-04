#!/bin/python3
import os
import json

# Create redirects folder
if not os.path.exists("redirects"):
	os.makedirs("redirects")

def createRedirect():
	# Get URl to shorten and shortend URL ending
	long_url=input("URL to shorten?\nRemember to start with https:// or http://\n")
	print("\n")
	redirect_ending=input("What would you like the redirect URL ending to be?\nFor example, for example.com/shorturl type \"shorturl\"\n")
	print("\n")
	if os.path.exists("redirects/"+redirect_ending+".html") == True:
		while os.path.exists("redirects/"+redirect_ending+".html") == True:
			print("A redirect with that ending already exists\nPlease pick a diffrent ending\n")
			redirect_ending=input("What would you like the redirect URL ending to be?\nFor example, for example.com/shorturl type \"shorturl\"\n")
			print("\n")
	# Create and write to redirect HTML file
	with open("redirects/"+redirect_ending+".html", "w") as redirect_file:
		with open("redirect-template-start", "r") as template_start:
			redirect_template_start=template_start.read()
		with open("redirect-template-end", "r") as template_end:
			redirect_template_end=template_end.read()
		redirect_file.write(redirect_template_start+long_url+redirect_template_end)

createRedirect()