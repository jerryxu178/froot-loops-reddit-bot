import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "gost bee's froot loop bot v0.1")
	return r

def run_bot(r):
	for comment in r.subreddit('test').comments(limit = 25):
		if "fruit loop" in comment.body:
			print "string found!"
			comment.reply("You've misspelled froot loops!")
	time.sleep(10)

# [here](www.google.com)
# comment.id
# comment.author

r = bot_login()
run_bot(r)