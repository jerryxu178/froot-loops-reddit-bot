import praw
import config
import time

def bot_login():
# log into the reddit account with credentials from config.py
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "froot loop bot v1.0")
	return r

def run_bot(r):
# run the bot on subreddit designated in config.py
	for comment in r.subreddit(config.sub_reddit).comments(limit = 25):
		if "fruit loops" in comment.body and comment.author != config.username:
			print "misspelling found!"
			comment.reply("""You've misspelled froot loops! Believe it or not, 
				[froot loops](https://en.wikipedia.org/wiki/Froot_Loops) 
				contain no real fruit and are actually all the same flavor.""")
			time.sleep(10)

r = bot_login()
while True:
	run_bot(r)