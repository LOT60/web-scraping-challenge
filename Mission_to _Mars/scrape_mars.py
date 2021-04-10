import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

def get_soup(url):
    # Initialize Browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(url)

    html = browser.html

    soup = bs(html, 'html.parser')

    return browser, soup


def mars_news():
    # set url
    url = 'https://redplanetscience.com/'
    
    # get soup
    browser, soup = get_soup(url)

    # Retrieve news element
    news = soup.find('div', id='news')

    # get all list dates
    list_dates = news.find_all('div', class_='list_date')

    maxdate = max([dt.datetime.strptime(ldate.text.strip(), '%B %d, %Y') for ldate in list_dates])

    # get articles
    articles = news.find_all('div', class_='list_text')

    for article in articles:
        list_date = article.select_one(".list_date").text.strip()

        if dt.datetime.strptime(list_date, '%B %d, %Y') == maxdate:
            newsa = article
            title = newsa.select_one(".content_title").text.strip()
            news_p = newsa.select_one(".article_teaser_body").text.strip()
            
    # prepare output
    news_dict = {'title':title,
                    'news_p':news_p}

    browser.quit()

    return news_dict


def featured_img():
    space_url = 'https://spaceimages-mars.com/'
    browser, soup = get_soup(space_url)

     
    featured_image = soup.find('img', class_='headerimage fade-in')

    featured_image_url = space_url + featured_image['src']

    browser.quit()

    return featured_image_url


def mars_facts():
    mars_url = 'https://galaxyfacts-mars.com/'
    # using pandas read html
    tables = pd.read_html(mars_url)
    mars_fact_df = tables[0]


    mars_fact_df.columns = ['','Mars', 'Earth']
    mars_fact_df = mars_fact_df.iloc[1:]
    mars_fact_df.set_index('', drop=True , inplace= True)

    facts = mars_fact_df.to_dict()

    return facts


def hemispheres():
    hem_url = 'https://marshemispheres.com/'
    browser, soup = get_soup(hem_url)
# get soup


    items = soup.find_all('div', class_="item")

    hemisphere_urls = []

    for item in items:
        hmsphere = {}
        name = item.h3.text
      # link = item.a['href']

    # get full image
        try:
            browser.links.find_by_partial_text(name).click()
            print(browser.url)
            html2 = browser.html
            imgsoup = bs(html2, 'html.parser')
            imgsoup
            img = imgsoup.find('img', class_="wide-image")
        
            hmsphere['title'] = name[:-9]
            hmsphere['img_url'] = hem_url + img['src']
            
        except:
            print("Could not get Image Link")   
        
        hemisphere_urls.append(hmsphere)    
        browser.back()

    browser.quit()

    return hemisphere_urls


def scrape():

    results = {}

    results['news'] = mars_news()

    results['featured_img'] = featured_img()

    results['mars_facts'] = mars_facts()

    results['hemispheres'] = hemispheres()

    return results