#!/usr/bin/env python
# coding: utf-8

# 1.Write a python program which searches all the product under a particular product from www.amazon.in.
# The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:


import selenium
import pandas as pd
import time


from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By


# In[ ]:


driver= webdriver.Chrome()


# In[ ]:


driver.get("https://www.amazon.in/")


# In[17]:


product=driver.find_element(By.ID,"twotabsearchtextbox")
product.send_keys('guitars')


# In[18]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div")
search.click()


# 2.In the above question, now scrape the following details of each product listed in first 3 pages of your search results and
# save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products 
# available under that product name. Details to be scraped are: "Brand
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.

# In[ ]:


def get_product_details(products):
    # Loop through each product and get its details
    
    for prod in products:
        try:
            brand = prod.find_element_by_xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]')\
                        .text.strip()
        except:
            brand = "-"

        try:
            name = prod.find_element_by_xpath('.//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')\
                        .text.strip()
        
        except:
            name = "-"

        try:
            price = prod.find_element_by_xpath('.//span[@class="a-price-whole"]').\
                        text.strip().replace(',', '')
        except:
            price = "-"

        try:
            returns = prod.find_element_by_xpath('.//div[@class="a-row a-size-small"]').\
                        text.strip()
        except:
            returns = "-"

        try:
            delivery = prod.find_element_by_xpath('.//div[@class="a-row a-size-base a-color-secondary"]').\
                        text.strip()
        except:
            delivery = "-"

        try:
            availability = prod.find_element_by_xpath('.//div[@class="a-section a-spacing-none a-spacing-top-micro"]')\
                             .text.strip()
        except:
            availability = "-"

        try:
            product_url = prod.find_element_by_xpath('.//a[@class="a-link-normal a-text-normal"]')\
                            .get_attribute('href')
        except:
            product_url = "-"

        # Add the product details to the DataFrame
        df.loc[len(df)] = [brand, name, price, returns, delivery, availability, product_url]

# Get the product to search from the user
product = input('Enter the product to search: ')

# Initialize a DataFrame to store the product details
df = pd.DataFrame(columns=['Brand Name', 'Product Name', 'Price', 'Return/Exchange', 'Expected Delivery', 'Availability', 'Product URL'])

            


# In[ ]:


# Set up Selenium WebDriver with Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Load the Amazon.in search results page for the specified product
driver.get(f"https://www.amazon.in/s?k={product.replace(' ', '+')}")

# Scrape the product details from the first 3 pages of search results
for page in range(1, 4):


    # Get all the products on the current page
    products = driver.find_elements(By.XPATH,('//div[@data-cel-widget="search_result_"]'))

    # Get the product details of the current page
    get_product_details(products)

    # Go to the next page if available
    try:
        next_btn = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-active"]')
        driver.execute_script("arguments[0].click();", next_btn)
    except:
        break

# Save the data into a CSV file
df.to_csv(f"{product.capitalize()} Search Results.csv", index=False)
print(f"{len(df)} products scraped and saved into {product.capitalize()} Search Results.csv")


# In[ ]:


df


# QUESTION-3

# In[27]:


import selenium
import pandas as pd
import time


from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException

from selenium.webdriver.common.by import By


# In[28]:


driver= webdriver.Chrome()


# In[29]:


driver.get("https://www.google.com/imghp")


# In[30]:


search_bar=driver.find_element(By.ID,"APjFqb")
search_bar.send_keys("keyword")

time.sleep(2)


# In[31]:


# Find and fill the search bar with the current keyword
# Set the search keywords
keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']


# Click the search button
search_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
search_button.click()



# Find and save the first max_images images
img_count = 0
for image in driver.find_elements(By.XPATH,'//img[@class="rg_i"]'):
    
# Get the image source URL
    img_url = image.get_attribute('src')
    

        # Skip if the image source URL cannot be retrieved
    if not img_url:
        continue

        # Save the image to the specified folder

urllib.request.urlretrieve(img_url, save_path)

        # Increment the image count and break if the maximum number of images has been reached
img_count += 1
if img_count == max_images:
    break


# Quit the WebDriver
driver.quit()


# QUESTION - 4

# In[59]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# In[60]:


driver= webdriver.Chrome()
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZE3ENS&marketplace=FLIPKART&q=iphone+11&store=tyy/4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_6_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_6_0_na_na_na&fm=organic&iid=e30aaa70-fe6e-466c-81d4-993e630ea913.MOBFWQ6BXGJCEYNY.SEARCH&ppt=hp&ppn=homepage&ssid=nseg9l47e80000001699187524593&qH=f6cdfdaa9f3c23f3")


# In[62]:


def get_product_details(products):
    
    # Loop through each product and get its details


    for prod in products:
        try:
            
            brand, name = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[1]').\
                                text.strip().split(' ')
        except:
            brand, name = "-", "-"

        try:
            color = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[1]')\
                            .text.strip().split(': ')[1]
        except:
            color = "-"

        try:
            ram = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[2]')\
                            .text.strip().split(': ')[1]
        except:
            ram = "-"

        try:
            rom = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[3]')\
                            .text.strip().split(': ')[1]
        except:
            rom = "-"

        try:
            prim_cam = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[4]')\
                               .text.strip().split(': ')[1]
        except:
            prim_cam = "-"

        try:
            sec_cam = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[5]')\
                              .text.strip().split(': ')[1]
        except:
            sec_cam = "-"

        try:
            disp_size = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[6]')\
                              .text.strip().split(': ')[1]
        except:
            disp_size = "-"

        try:
            batt_cap = prod.find_element_by_xpath('.//div[@class="_2kHMtA"]/div[2]/ul/li[7]')\
                             .text.strip().split(': ')[1]
        except:
            batt_cap = "-"

        try:
            price = prod.find_element_by_xpath('.//div[@class="_30jeq3 _1_WHN1"]')\
                          .text.strip().replace(',', '')
        except:
            price = "-"

        try:
            prod_url = prod.find_element_by_xpath('.//a[@class="_1fQZEK"]')\
                           .get_attribute('href')
        except:
            prod_url = "-"

        # Add the product details to the DataFrame
        df.loc[len(df)] = [brand, name, color, ram, rom, prim_cam, sec_cam, disp_size, batt_cap, price, prod_url]

# Get the smartphone to search from the user
smartphone = "iphone 11"

# Initialize a DataFrame to store the product details
df = pd.DataFrame(columns=['Brand Name', 'Smartphone Name', 'Colour', 'RAM', 'Storage(ROM)', 'Primary Camera',
                           'Secondary Camera', 'Display Size', 'Battery Capacity', 'Price', 'Product URL'])

# Set up Selenium WebDriver with Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Load the Flipkart search results page for the specified smartphone
driver.get(f"https://www.flipkart.com/search?q={smartphone.replace(' ', '%20')}")

# Handle login if required


# Scrape the product details from the search results
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2kHMtA"]')))
get_product_details(driver.find_elements(By.XPATH,('//div[@class="_2kHMtA"]')))

# Save the data into a CSV file and print the DataFrame
df.to_csv(f"{smartphone.capitalize()} Search Results.csv", index=False)
print(f"{len(df)} products scraped and saved into {smartphone.capitalize()} Search Results.csv\n")
print(df)

# Quit the WebDriver
driver.quit()


# In[63]:


df


# QUESTION -5

# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


city = input("Enter a city name:")

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps')


# In[ ]:


search_box = driver.find_element(By.CLASS_NAME,"pzfvzf")
search_box.send_keys(city)


# Wait for the map to load and get the HTML content of the page
driver.implicitly_wait(10)
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")

# Find the div that contains the latitude and longitude
lat_long_div = soup.find("div", {"class": "section-info-attribute-group"})

# Get the latitude and longitude
latitude = lat_long_div.find_all("div")[0].text.strip()
longitude = lat_long_div.find_all("div")[1].text.strip()

# Print the latitude and longitude
print("Latitude:", latitude)
print("Longitude:", longitude)

# Close the ChromeDriver
driver.quit()


# QUESTION -6

# In[3]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
# Provide the path to your ChromeDriver executable

driver = webdriver.Chrome()


# In[4]:


driver.get('https://www.digit.in/top-products/best-gaming-laptops-40.html')

# Allow time for the page to load
time.sleep(2)

laptop_name=[]
laptop_spec=[]

# Find all the laptop details on the page
laptop_list = driver.find_elements(By.CLASS_NAME,'TopNumbeHeading')

# Extract and print the details for each laptop
for laptop in laptop_list:
    laptop_name = laptop.find_element(By.CLASS_NAME,'TopNumbeProductdetail').text.strip()
    laptop_spec = laptop.find_elements(By.CLASS_NAME,'TopNumbeListText')

    print("Laptop Name:", laptop_name)
for spec in laptop_spec:
    
    feature_name = spec.find_element(By.CLASS_NAME,'TopNumbeName').text.strip()
    feature_value = spec.find_element(By.CLASS_NAME,'TopNumbeHits').text.strip()
    print(f"{feature_name}: {feature_value}")
print()


# QUESTION-7

# In[45]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
# Provide the path to your ChromeDriver executable

driver = webdriver.Chrome()


# In[46]:


driver.get('https://www.forbes.com/billionaires/')

time.sleep(5)


# In[23]:


# Find the table containing the billionaire details
table = driver.find_element(By.CLASS_NAME, "IntroHeading_logoContainer__Kv_rN")

# Find all the rows of the table (excluding the header row)
rows = table.find_elements('tag name', 'tr')[1:]

# Iterate over each row and scrape the required details
for row in rows:
    rank = row.find_element(CLASS_NAME, 'rank').text.strip()
    name = row.find_element(CLASS_NAME, 'name').text.strip()
    net_worth = row.find_element(CLASS_NAME, 'networth').text.strip()
    age = row.find_element(CLASS_NAME, 'age').text.strip()
    citizenship = row.find_element(CLASS_NAME, 'citizenship').text.strip()
    source = row.find_element(CLASS_NAME, 'source').text.strip()
    industry = row.find_element(CLASS_NAME, 'category').text.strip()

    # Print the scraped details
    print("Rank:", rank)
    print("Name:", name)
    print("Net Worth:", net_worth)
    print("Age:", age)
    print("Citizenship:", citizenship)
    print("Source:", source)
    print("Industry:", industry)
    print()



# QUESTION-8

# In[47]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# In[48]:


driver = webdriver.Chrome()
driver.maximize_window()

# Load the YouTube video page to be scraped
driver.get('https://www.youtube.com/watch?v=BHH83IzFHcg')



# In[49]:


# Scroll down to load more comments
comment_section = driver.find_element(By.XPATH,'//*[@id="comments"]')
driver.execute_script("arguments[0].scrollIntoView();", comment_section)

# Create a DataFrame to store comments data
comments_df = pd.DataFrame(columns=['Comment', 'Like Count', 'Time'])

# Extract comments from the page
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
 # Click 'Load more' button until it disappears
    try:
        load_more = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="comments"]//paper-button[@id="more"]/yt-formatted-string')))
            
        
        load_more.click()
    except:
        break

    # Wait for the page to load
    time.sleep(1)

    # Extract comments from the page
    comments = driver.find_elements(By.XPATH, '//*[@id="comment"]')
    for comment in comments:
        try:
            comment_text = comment.findElement(By.XPATH, './/yt-formatted-string[@id="content-text"]')
            like_count = comment.findElement(By.XPATH, './/span[@class="style-scope ytd-comment-action-buttons-renderer"]')
            time = comment.findElement(By.XPATH, './/a[@class="yt-simple-endpoint style-scope yt-formatted-string"]').text

            # Add extracted data to the DataFrame
            comments_df.loc[len(comments_df)] = [comment_text.text, like_count.text, time]
        except:
            continue

    # Scroll down to load more comments
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
      # Break if end of page is reached
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Save the DataFrame to a CSV file
comments_df.to_csv('YouTubeComments.csv', index=False)

# Print the comments DataFrame
print(comments_df)

# Quit the WebDriver
driver.quit()


# QUESTION-9

# In[32]:


from selenium import webdriver
from selenium.webdriver.common.by import By


import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 


# In[33]:


driver=webdriver.Chrome()
driver.get("https://www.hostelworld.com/")
time.sleep(5)


# In[34]:


hostel_list =driver.find_elements(By.CLASS_NAME, "property-card-inner-wrap")

# Loop through each hostel and scrape the relevant details
for hostel in hostel_list:
    # Hostel name
    hostel_name = hostel.find_element(By.CLASS_NAME, "title-6").text.strip()

# Distance from city centre
    distance = hostel.find_element(By.CLASS_NAME, "description").text.strip()

    # Ratings
    rating = hostel.find_element(By.CLASS_NAME, "score").text.strip()

    # Total reviews
    total_reviews = hostel.find_element(By.CLASS_NAME, "reviews").text.strip()

    # Overall reviews
    overall_reviews = hostel.find_element(By.CLASS_NAME, "rating").text.strip()
    # Privates from price
    privates_price = hostel.find_element(By.CLASS_NAME, "price").text.strip()

    # Dorms from price
    dorms_price = hostel.find_element(By.CLASS_NAME, "price-qualifier").text.strip()

    # Facilities
    facilities_list = hostel.find_elements(By.CLASS_NAME, "facilities-label__item")

    facilities = []
    for facility in facilities_list:
        
        facilities.append(facility.text.strip())

    

    # Property type
    property_type = hostel.find_element(By.CLASS_NAME, "property-type").text.strip()

    # Print the details of the hostel
    print("Name:", hostel_name)
    print("Distance from city centre:", distance)
    print("Rating:", rating)
    print("Total reviews:", total_reviews)
    print("Overall reviews:", overall_reviews)
    print("Privates from price:", privates_price)
    print("Dorms from price:", dorms_price)
    print("Facilities:", facilities)
    print("Property type:", property_type)

# Close the ChromeDriver
driver.quit()


# In[ ]:




