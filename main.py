import urllib
import praw
import re
from praw.models import MoreComments

enter_sub = input("Type a subbreddit name: ")
if len(enter_sub) < 1 : enter_sub = "soccer"

enter_user = input("\nEnter reddit username: ")
if len(enter_user) < 1 : enter_user = "jadartse"

r_url = "old.reddit.com"

reddit = praw.Reddit('bot1')
sub = reddit.subreddit(enter_sub)
username = reddit.redditor(enter_user)

for comment in username.comments.top():
    comment_str = str(comment.body)
    string = str(comment.permalink)
    full_url = r_url+string
    try:
        read_file = file.read()
    except:
        file = open('my-top-comments.pages','a')
        if str(comment.subreddit) == enter_sub:
            file.write("NEW COMMENT:\n\n")
            file.write("COMMENT BODY: " + comment_str + "\n")
            file.write("SUBMISSION ID: " + full_url + "\n\n")
