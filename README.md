# Web Scraping Challenge
Web Scraping Homework - Mission to Mars

![mission_to_mars](https://user-images.githubusercontent.com/74845016/113380752-a88efd80-9342-11eb-8b01-70e4394dabf9.png)


# Step 1 - Scraping
Complete your initial scraping using Jupyter Notebook,     BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


# NASA Mars News

* Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# JPL Mars Space Images - Featured Image

* Visit the url for the Featured Space Image site here.

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

* Make sure to find the image url to the full size .jpg image.

* Make sure to save a complete url string for this image.

# Mars Facts

* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.


# Mars Hemispheres

* Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# Output
<img width="586" alt="final_app" src="https://user-images.githubusercontent.com/74845016/113380818-d8d69c00-9342-11eb-80d7-b1b1b2086ad6.png">