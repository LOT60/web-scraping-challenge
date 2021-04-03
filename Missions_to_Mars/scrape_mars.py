import pandas as pd
import datetime as dt
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#Site Navigation
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless = False)
 

# NASA Mars News
def mars_news():
    browser_ur = 'https://redplanetscience.com/'
    browser.visit(browser_ur)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    output = [news_title, news_p]
    return output

#JPL Mars Space Images - Featured Image
def featured_img ():
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find('img', class_='headerimage fade-in')
    featured_image_url = image_url + image['src']
    return featured_image_url

#Mars Facts
def mars_facts():
    import pandas as pd
    browser_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(browser_url)
    df = tables[0]
    df.columns = ['','Mars','Earth']
    df = df.iloc[1:]
    df = df.replace(':','',regex=True)
    df.set_index('', inplace=True)
    facts_more = df.to_dict()
   
    return facts_more


# Mars Hemispheres
def hemispheres():
    import time 
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = 'https://marshemispheres.com/' + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        dictionary = {"title": title, "img_url": image_url}
        mars_hemisphere.append(dictionary)
    
    return mars_hemisphere

# Scrape
def scrape():
    final_data = {}
    output = mars_news()
    final_data['mars_news'] = output()
    final_data['mars_image'] = featured_img()
    final_data['mars_facts'] = mars_facts()
    final_data['mars_hemisphere'] = hemispheres()

    return final_data

