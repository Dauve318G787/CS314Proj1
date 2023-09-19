import requests #allows us to make HTTP requests
from bs4 import BeautifulSoup #allows us to web scrape
import sys #allows us to use command line args

def downloadText(url):

    try:

        response = requests.get(url) #sends an HTTP requests to the website and gets a response

        if response.status_code == 200: #if the response is a code 200, all is well- download text data from website.

            parsedContent = BeautifulSoup(response.text, 'html.parser')

            websiteText = parsedContent.getText() #gets text from parsed HTML

            print(response) #print response code

            return websiteText #returns parsed text
        
        else: #if the response is not a code 200, something is wrong, don't download text data.

            print("Failed to download data- could not reach desired website.") 

            print(response) #print response code

    except Exception as e:

        print("An error occurred, check your Internet connection.") #prints error message
        return None #returns nothing

if __name__ == "__main__":

    url = sys.argv[1] #takes URL as first argument (argument after dupuisproj1.py)

    textData = downloadText(url) #pass URL into downloadText to get text, store text in textData

    fileToWriteTo = open("websiteData.txt", "w") #open websiteData.txt for writing

    if textData: #if websiteData.txt is open for writing...

        fileToWriteTo.write(textData) #write text data to websiteData.txt!
        

    else: #otherwise, print error message.

        print("Could not download text data.")

