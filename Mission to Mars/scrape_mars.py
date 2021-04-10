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
    url = 'https://redplanetscience.com/'

    browser, soup = get_soup(url)

    news = soup.find('div', id='news')

    list_dates = news.find_all('div', class_='list_date')

    maxdate = max([dt.datetime.strptime(ldate.text.strip(), '%B %d, %Y') for ldate in list_dates])


    articles = news.find_all('div', class_='list_text')

    for article in articles:
        list_date = article.select_one(".list_date").text.strip()

        if dt.datetime.strptime(list_date, '%B %d, %Y') == maxdate:
           newsa = article
           title = newsa.select_one(".content_title").text.strip()
           news_p = newsa.select_one(".article_teaser_body").text.strip()

news_dict = {'title':title,
                'news_p':news_p}

browser.quit()

return news_dict




def scrape():

    output = {}
   
    output['news'] = mars_news()


    return output
    