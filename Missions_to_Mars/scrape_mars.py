from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    def create_soup(url):
        browser.visit(url)
        # Create BeautifulSoup 
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        return soup


    url = 'https://redplanetscience.com/'
    soup = create_soup(url)


    # grab the title
    title = soup.find('div' , class_="content_title").text
    
    # Grab the paragraph
    news_p = soup.find('div', class_="article_teaser_body").text

    title
    news_p 

    
    space_url = 'https://spaceimages-mars.com/'
    soup = create_soup(space_url)

    featured_image = soup.find('img', class_='headerimage fade-in')

    featured_image_url = space_url + featured_image['src']
    
    featured_image_url
  


    mars_url = 'https://galaxyfacts-mars.com/'
    # using pandas
    tables = pd.read_html(mars_url)
    len(tables)

    mars_fact_df = tables[0]

    mars_fact_df.columns = ['Description' , 'Mars', 'Earth']
    mars_fact_df.set_index('Description' , drop=True , inplace= True)

    mars_fact_df

    browser.quit()

    mars_data = {
            'news_title' : title,
            'news_p':news_p,
            'featured_image':featured_image_url,
            'table': mars_fact_df
             }

    return mars_data


