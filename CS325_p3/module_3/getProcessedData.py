#This module uses the Reddit API to extract comments data from a subreddit and writes those comments to a text file named "processed.txt"
#located in the processed subfolder in Data.

import requests #allows us to make HTTP requests
from bs4 import BeautifulSoup #allows us to web scrape
import sys #allows us to use command line args
import praw
from praw.models import MoreComments

saveDir = "C:\\Users\\12242\\Desktop\\CS325_p3\\Data\\\\processed\\processed.txt" #this is where the output text file will go

redditCommentFile = open("websiteData.txt", "w")

reddit_read_only = praw.Reddit(client_id="o4gdzZa2AGpARW1htVDMcg", #initializes connection to API
                               client_secret="HDSYgES1OHiZL5KjVHj4mgBo7dnjwQ",
                               user_agent="David Dupuis")

subreddit = reddit_read_only.subreddit(sys.argv[1]) #takes subreddit name via CLI

print("Subreddit Name: ", subreddit.display_name)
print("Subreddit Description: ", subreddit.description)

url = sys.argv[2]

submission = reddit_read_only.submission(url=url) #creates submission object

comments = submission.comments #loads comments into a variable

def extractComments(comments, level=0):

    for comment in comments: #for each comment...

        commentBody = comment.body

        with open(saveDir, 'a') as commentFile: #write each comment to the output file at the given directory

            commentFile.write('Reply: ' * level + commentBody + "\n")
        
        if comment.replies: #if there are replies...

            extractComments(comment.replies, level + 1) #print replies in a hierarchical format


extractComments(comments)

    


