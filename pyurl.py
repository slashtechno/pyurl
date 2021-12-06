#!/bin/python3
import os
import json
import git
from git.refs import remote #  pip install GitPython

def configure():
	configuration = {"hosting": "", "ssh_address": ""}
	hosting = input("Should this program automatically use Git to push to a repo?\n\"YES\" or \"NO\"\n")
	print("\n")
	if hosting == "YES":
		ssh_address=input("What is the ssh address of your Git repository?\nFor example, git@github.com:slashtechno/pyurl.git\n")
		print("\n")
		configuration.update({"hosting": True, "ssh_address": ssh_address})
		os.chdir("redirects")
		os.system("git remote add origin "+ssh_address)
		os.chdir(main_directory)
	else:
		print("It seems you either responded \"NO\" or an invalid response\nProgram is proceeding as if \"NO\" was set\n")
		configuration.update({"hosting": False, "ssh_address": ""})
	with open("config.json", "w") as config_file:
			configuration_json = json.dumps(configuration, indent=4)
			config_file.write(configuration_json)

	
		

def create_redirect():
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

def push_to_git():
	os.chdir("redirects")
	os.system("git add .")
	os.system("git commit -m \"Automated commit\"")
	os.system("git push origin")
	os.chdir(main_directory)

main_directory = os.getcwd()

# Create redirects folder
if not os.path.exists("redirects"):
	os.makedirs("redirects")
	os.chdir("redirects")
	os.system("git init")
	os.chdir(main_directory)
else:
	pass

if os.path.exists("config.json"):
	with open("config.json", "r") as config_file:
		config_json = config_file.read()
	configuration = json.loads(config_json)
else:
	configure()
	with open("config.json", "r") as config_file:
		config_json = config_file.read()
	configuration = json.loads(config_json)

while True:
	if configuration["hosting"] == True:
		git.rmtree("redirects")
		# os.chdir("redirects")
		os.system("git clone "+configuration["ssh_address"]+" redirects")
		print("\n")
		os.chdir(main_directory)
	action = int(input("What would you like to do?\n1) Shorten a URL\n2) Configure this program\n3) List redirects\n4) Delete a redirect\n5) Exit program\n"))
	print("\n")
	if action == 1:
		create_redirect()
		push_to_git()
	if action == 2:
		configure()
	if action == 3:
		os.listdir("redirects")
		print("\n")
	if action == 4:
		os.listdir("redirects")
		print("\n")
		redirect_to_remove = input("What redirect would you like to remove\n")
		os.remove("redirects/"+redirect_to_remove)
	if action == 5:
		exit()