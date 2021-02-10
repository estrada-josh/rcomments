import urllib
import praw
import re
from praw.models import MoreComments

enter_sub = input("Type a subbreddit name: ")
if len(enter_sub) < 1 : enter_sub = "soccer"

enter_user = input("\nEnter reddit username: ")
if len(enter_user) < 1 : enter_user = "jadartse"


reddit = praw.Reddit('bot1')
sub = reddit.subreddit(enter_sub)
username = reddit.redditor(enter_user)

for comment in username.comments.new():
    if str(comment.subreddit) == enter_sub:
        print("##########################################\n")
        print("COMMENT BODY: ", comment.body, "\n")
        print("SUBMISSION ID: ", comment.submission, "\n")
