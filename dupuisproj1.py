import requests #allows us to make HTTP requests
from bs4 import BeautifulSoup #allows us to web scrape
import sys #allows us to use command line args

def downloadText(url):

    try:

        response = requests.get(url) #sends an HTTP requests to the website and gets a response

        if response.status_code == 200: #if the response is a code 200, all is well- download text data from website.

            parsedContent = BeautifulSoup(response.text, 'html.parser')

            websiteText = parsedContent.getText()

            return websiteText
        
        else: #if the response is not a code 200, something is wrong, don't download text data.

            print("Failed to download data- could not reach desired website.") 

    except Exception as e:

        print("An error occurred, check your Internet connection.")
        return None

if __name__ == "__main__":

    url = sys.argv[1]

    textData = downloadText(url)

    fileToWriteTo = open("websiteData.txt", "w")

    if textData:

        fileToWriteTo.write(textData)
        

    else:

        print("Could not download text data.")

