import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "froot loop bot v1.0")
	return r

def run_bot(r):
	for comment in r.subreddit('test').comments(limit = 25):
		if "fruit loop" in comment.body and comment.author != config.username:
			print "misspelling found!"
			comment.reply("""You've misspelled froot loops! Believe it or not, 
				[froot loops](https://en.wikipedia.org/wiki/Froot_Loops) 
				contain no real fruit and are actually all the same flavor""")
			time.sleep(10)

# [here](www.google.com)
# comment.id
# comment.author

r = bot_login()
# while true:
run_bot(r)