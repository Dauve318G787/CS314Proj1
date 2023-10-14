import requests #allows us to make HTTP requests
from bs4 import BeautifulSoup #allows us to web scrape
import sys #allows us to use command line args
import praw
from praw.models import MoreComments

redditCommentFile = open("websiteData.txt", "w")

reddit_read_only = praw.Reddit(client_id="o4gdzZa2AGpARW1htVDMcg",
                               client_secret="HDSYgES1OHiZL5KjVHj4mgBo7dnjwQ",
                               user_agent="David Dupuis")

subreddit = reddit_read_only.subreddit(sys.argv[1])

print("Subreddit Name: ", subreddit.display_name)
print("Subreddit Description: ", subreddit.description)

url = sys.argv[2]

submission = reddit_read_only.submission(url=url)

comments = submission.comments

def extractComments(comments, level=0):

    for comment in comments:

        commentBody = comment.body

        with open('websiteData.txt', 'a') as commentFile:

            commentFile.write('Reply: ' * level + commentBody + "\n")
        
        if comment.replies:

            extractComments(comment.replies, level + 1)


extractComments(comments)

    


