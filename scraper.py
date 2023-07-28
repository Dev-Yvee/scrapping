import requests
from bs4 import BeautifulSoup

try:
    req=requests.get("https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/") #URL of the website we want to scrape data from
    req.raise_for_status() #checking if the URL is wrong
 
    soup=BeautifulSoup(req.content,'html.parser')

    movieRank=soup.find("div",id="row-index-2",class_="countdown-index-responsive")
    
    movieName=soup.find("div",id="row-index-2").h2.a.text
    
    movieYear=soup.find("div",id="row-index-2").span.text.strip("()")
   
    movieRating=soup.find()

    print(movieRank,movieName,"Yvone",movieYear)


except Exception as e:
    print(e)

