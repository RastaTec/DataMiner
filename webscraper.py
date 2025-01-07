import requests
from bs4 import BeautifulSoup
import pandas as pd


#Define the URL of the website to scrape
url='https://www.bbc.com/news'

#Send a GET request to the website
response=requests.get(url)

#check if the request was successful
if response.status_code == 200:
    #Parse the HTML content of the website
    soup=BeautifulSoup(response.content, 'html.parser')
    
    #Find all articles on the page
    articles=soup.find_all('h3', class_='gs-c-promo-heading__title')
    
    #Create lists to store the data
    titles=[]
    urls=[]
    
    #Extract the title and url of each article
    for article in articles:
        title=article.text.strip()
        link=article.find_parent('a')['href']
        
        #Ensure the link is absolute
        if not link.startswith('http'):
            link='https://www.bbc.com' + link
        
        titles.append(title)
        urls.append(link)
        
        #Create a dataframe from the data
        data=pd.DataFrame({
            'Title': titles,
            'URL': urls 
        })
        
        #Save the dataframe to a CSV file
        data.to_csv('articles.csv', index=False)
        
        print('Data successfully scraped and saved to articles.')
    else:
        print('Failed to retieve the website')