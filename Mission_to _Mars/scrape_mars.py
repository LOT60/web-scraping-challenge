import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# define the function to return srapped values

def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Define url  and set up config splinter to the site 
    #Create a function that takes the url and return the soup 
    def create_soup(url):
        browser.visit(url)
        # Create BeautifulSoup object; parse with 'html.parser'
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    

    url = 'https://redplanetscience.com/'
    soup = create_soup(url)

    title = soup.find('div' , class_="content_title").text

    news_p = soup.find('div', class_="article_teaser_body").text

    news_dict = {'title':title,
                'news_p':news_p}

    news_dict


    space_url = 'https://spaceimages-mars.com/'
    soup = create_soup(space_url)   


    try:
        target = 'button[class="btn btn-outline-light"]'
        browser.find_by_tag(target).click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image_src = soup.find('img', class_="fancybox-image")['src']

    except:
         print('can\'t find the image')    
    featured_image_url = space_url + image_src   

    featured_image_url 


    mars_url = 'https://galaxyfacts-mars.com/'
   # using pandas read html
    tables = pd.read_html(mars_url)
    mars_fact_df = tables[0] 

    mars_fact_df.columns = ['Description','Mars', 'Earth']
    mars_fact_df = mars_fact_df.iloc[1:]
    mars_fact_df.set_index('Description', drop=True , inplace= True)

    mars_fact_df.head() 



    # set url
    hem_url = 'https://marshemispheres.com/'
    soup = create_soup(hem_url)
# get soup
    items = soup.find_all('div', class_="item")
    hemisphere_urls = []

    for item in items:
        hmsphere = {}
        name = item.h3.text
#       link = item.a['href']

    # get full image
        try:
             browser.links.find_by_partial_text(name).click()
             print(browser.url)
             html2 = browser.html
             imgsoup = BeautifulSoup(html2, 'html.parser')
             imgsoup
             img = imgsoup.find('img', class_="wide-image")
        
             hmsphere['title'] = name[:-9]
             hmsphere['img_url'] = hem_url + img['src']
          
        except:
             print("Could not get Image Link")   
        
        hemisphere_urls.append(hmsphere)    
        browser.back()

    browser.quit()

    print(hemisphere_urls)   

    mars_data = {
                'news_title' : title,
                'news_p':news_p,
                'featured_image':featured_image_url,
                'hemisphere_image_urls':hemisphere_urls,
                'table': mars_fact_df
                 }

    return mars_data   