import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def scrap_page(reviews_url):
    html_datas = reviewsHtml(reviews_url)
    reviews = []
    for html_data in html_datas:
        
        # Grab review data
        review = getReviews(html_data)
        
        # add review data in reviews empty list
        reviews += review
        # Create a dataframe with reviews Data
        df_reviews = pd.DataFrame(reviews)
    df_reviews["Review"] = df_reviews["Title"]+ df_reviews["Description"]
    df_reviews = df_reviews[["Review", "Stars"]]
    return df_reviews
    # df_reviews.to_csv('scrapedReviews.csv', index=False)


def reviewsHtml(url):
    # Header to set the requests as a browser requests
    headers = {
        'authority': 'www.amazon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    # Empty List define to store all pages html data
    soups = []
    # parameter set as page no to the requests body
    params = {
        'ie': 'UTF8',
        'reviewerType': 'all_reviews',
        'filterByStar': 'critical',
        'pageNumber': 2,
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    soups.append(soup)
    return soups

# Grab Reviews name, description, date, stars, title from HTML
def getReviews(html_data):

    # Create Empty list to Hold all data
    data_dicts = []
    
    # Select all Reviews BOX html using css selector
    boxes = html_data.select('div[data-hook="review"]')
    
    # Iterate all Reviews BOX 
    for box in boxes:
        
        # Select Name using css selector and cleaning text using strip()
        # If Value is empty define value with 'N/A' for all.
        try:
            name = box.select_one('[class="a-profile-name"]').text.strip()
        except Exception as e:
            name = 'N/A'

        try:
            stars = box.select_one('[data-hook="review-star-rating"]').text.strip().split(' out')[0]
        except Exception as e:
            stars = 'N/A'   

        try:
            title = box.select_one('[data-hook="review-title"]').text
            title = re.sub(r"\d.\d out of 5 stars", " ", title)
        except Exception as e:
            title = 'N/A'

        try:
            # Convert date str to dd/mm/yyy format
            datetime_str = box.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
            date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
        except Exception as e:
            date = 'N/A'

        try:
            description = box.select_one('[data-hook="review-body"]').text.strip()
        except Exception as e:
            description = 'N/A'

        # create Dictionary with al review data 
        data_dict = {
            'Name' : name,
            'Stars' : stars,
            'Title' : title,
            'Date' : date,
            'Description' : description
        }

        # Add Dictionary in master empty List
        data_dicts.append(data_dict)
    
    return data_dicts

def web_scrapper(inp):
    pattern = r"(https:\/\/www\.amazon\.in\/[^\/]+)\/dp\/([^\/]+)\/?\??.*"
    match = re.match(pattern, inp)

    if match:
        product_url, product_id = match.groups()
        reviews_url = f"{product_url}/product-reviews/{product_id}/"
        print(reviews_url)
        return scrap_page(reviews_url)
    else:
        print("Invalid URL format")
