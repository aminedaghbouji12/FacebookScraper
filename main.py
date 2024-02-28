from fastapi import FastAPI
from facebook_scraper import get_posts
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client["FacebookScrapedData"]
collection = db["FacebookData"]

@app.get("/")
async def root():
    return "Welcome to my Facebook scraping service"

@app.get("/scrap/{page_name}")
def scrap(page_name, save: bool = True):
    scraped_posts = [post for post in get_posts(page_name, pages=None)]
    
    if save:
        try: 
            collection.insert_many(scraped_posts)
            return "Scraped posts saved successfully in the database. Please check your MongoDB database to view your data."
        except Exception as e:
            return "Saving error"
        
    return {"scrapedPosts": scraped_posts}

