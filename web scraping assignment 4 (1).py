#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: A) Rank
B) Name
C) Artist
D) Upload date
E) Views


# In[107]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By


# In[108]:


driver= webdriver.Chrome()


# In[110]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
table = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[3]')


# In[118]:


ranks=[]
names=[]
artists=[]
upload_date=[]
views=[]



# In[119]:


rank_tags = driver.find_elements(By.XPATH,'//th[@class="headerSort headerSortUp"]')
for i in rank_tags[0:10]:
    rank=i.text
    ranks.append(rank)


name_tags = driver.find_elements(By.XPATH,'//th[@class="headerSort"]')
for i in name_tags[0:10]:
    name=i.text
    names.append(name)
artist_tags = driver.find_elements(By.XPATH,'//th[@class="headerSort"]')
for i in artist_tags[0:10]:
    artist=i.text
    artists.append(artist)


    
upload_tags = driver.find_elements(By.XPATH,'/th[@class="headerSort"]')  
for i in upload_tags[0:10]:
    upload=i.text
    upload_date.append(upload)


view_tags = driver.find_elements(By.XPATH,'//th[@class="headerSort headerSortUp"]')
for i in view_tags[0:10]:
    view=i.text
    views.append(view)
    
    

   


# In[120]:


print(len(ranks),len(artists),len(names),len(upload_date),len(views))


# In[ ]:


df=pd.DataFrame({"Rank":ranks,"Name":names, "Upload_date": upload_date,"Views":views})
df                


# In[ ]:


2. Scrape the details team India’s international fixtures from bcci.tv.
Url = https://www.bcci.tv/.
You need to find following details:
A) Series
B) Place
C) Date
D) Time
Note: - From bcci.tv home page you have reach to the international fixture page through code.


# In[98]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
import numpy as np


# In[99]:


driver= webdriver.Chrome()


# In[100]:


driver.get('https://www.bcci.tv/')



# In[101]:


nav = driver.find_element(By.XPATH,"//li[@class='nav-item']")
nav.click()
time.sleep(3)


# In[102]:


driver.find_element(By.XPATH, "//a[text()='Fixtures']").click()


# In[103]:


Series=[]
Place=[]
Date=[]
Time=[]


# In[104]:


Series_tags = driver.find_elements(By.XPATH,'//div[@class="match-card-top"]')
for i in Series_tags[0:4]:
    
    Series.append(i.text)


place_tags = driver.find_elements(By.XPATH,'//div[@class="match-place"]')
for i in place_tags[0:4]:
    
    Place.append(i.text)
    


    
Date_tags = driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')  
for i in Date_tags[0:4]:
    
    Date.append(i.text)
Time_tags = driver.find_elements(By.XPATH,'//div[@class="match-time ng-binding"]')
for i in Time_tags[0:4]:
    
    Time.append(i.text)
    

    


# In[105]:


len(Series),len(Place),len(Date),len(Time)


# In[ ]:


df=pd.DataFrame({"Series":Series,"Place":Place,"Date":Date,"Time":Time})
df


# 3.Scrape the details of State-wise GDP of India from statisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details: A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.

# In[74]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select


# In[75]:


driver= webdriver.Chrome()


# In[76]:


driver.get("http://statisticstimes.com/")


# In[80]:


driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]").click()

driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div").click()

driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div").click()



# In[84]:


ranks = []
states = []
gsdp1819s = []
gsdp1920s = []
shares1819s = []
gdps = []

gdp_table = driver.find_element(By.XPATH, "//table[@id='table_id']")

for row in gdp_table.find_elements(By.TAG_NAME, "tr")[1:]:
    cells = row.find_elements(By.TAG_NAME, "td")

    # extract the rank, state, GSDP(18-19), GSDP(19-20), share(18-19), and GDP
    rank = cells[1].text.strip()
    state = cells[1].text.strip()
    gsdp1819 = cells[2].text.strip()
    gsdp1920 = cells[3].text.strip()
    share1819 = cells[4].text.strip()
    gdp = cells[5].text.strip()

    # add the state-wise GDP details to their corresponding lists
    ranks.append(rank)
    states.append(state)
    gsdp1819s.append(gsdp1819)
    gsdp1920s.append(gsdp1920)
    shares1819s.append(share1819)
    gdps.append(gdp)


# In[ ]:





# In[ ]:


4.Scrape the details of trending repositories on Github.com.
Url = https://github.com/
You have to find the following details:
A) Repository title
B) Repository description
C) Contributors count
D) Language used


# In[1]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# In[2]:


driver= webdriver.Chrome()


# In[3]:


driver.get("https://github.com/")


# In[4]:


trending_section = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[2]/div/h1")


# In[ ]:


titles = []
descriptions = []
contributors = []
languages = []

for repo in repository_boxes:
    title = repo.find_element(By.XPATH, ".//h1/a").text.split()[0]
    titles.append(title)

    description = repo.find_element(By.XPATH, ".//p").text.strip()
    descriptions.append(description)

    contributor_count = repo.find_element(By.XPATH, ".//a[contains(@href, '/stargazers')]").text.strip()
    contributors.append(contributor_count)

    language = repo.find_element(By.XPATH, ".//span[@itemprop='programmingLanguage']")
    languages.append(language.text if language else 'unknown')


# In[ ]:


data = {'Title': titles, 'Description': descriptions, 'Contributors': contributors, 'Language': languages}
df = pd.DataFrame(data)


# In[ ]:


df


# In[ ]:


5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/ You have to find the following details:
A) Song name
B) Artist name
C) Last week rank
D) Peak rank
E) Weeks on board
Note: - From the home page you have to click on the charts option then hot 100-page link through code


# In[65]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# In[66]:


driver= webdriver.Chrome()


# In[67]:


driver.get("https://www.billboard.com/charts/hot-100")


# In[68]:


song_names = []
artists = []
last_week_ranks = []
peak_ranks = []
weeks_on_board = []


# In[69]:


song_rows = driver.find_elements(By.XPATH, "//li[contains(@class, 'chart-list__element')]")

for row in song_rows:
    
    song_name = row.find_element(By.XPATH, ".//span[contains(@class, 'chart-element__information__song')]").text
    song_names.append(song_name)

    
    artist = row.find_element(By.XPATH, ".//span[contains(@class, 'chart-element__information__artist')]").text
    artists.append(artist)

    
    last_week_rank = row.find_element(By.XPATH, ".//span[contains(@class, 'chart-element__meta text--center color--secondary')][1]").text
    last_week_ranks.append(last_week_rank)

    
    peak_rank = row.find_element(By.XPATH, ".//span[contains(@class, 'chart-element__meta text--center color--secondary')][2]").text
    peak_ranks.append(peak_rank)
   
    weeks_on_board = row.find_element(By.XPATH, ".//span[contains(@class, 'chart-element__meta text--center color--secondary')][3]").text
    weeks_on_board.append(weeks_on_board)

#create a dataframe 
data = {'Song Name': song_names, 'Artist': artists, 'Last Week Rank': last_week_ranks,
        'Peak Rank': peak_ranks, 'Weeks on Board': weeks_on_board}

df = pd.DataFrame(data)
df


# In[ ]:


6. Scrape the details of Highest selling novels.
A) Book name
B) Author name
C) Volumes sold
D) Publisher
E) Genre
Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare


# In[17]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# In[18]:


driver= webdriver.Chrome()


# In[19]:


driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[20]:


book_names = []
author_names = []
volumes_sold = []
publishers = []
genres = []

book_rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'in-article sortable')]/tbody/tr")

for row in book_rows:
    # extract the book name
    book_name = row.find_element(By.XPATH, ".//td[2]").text
    book_names.append(book_name)

    # extract the author name
    author_name = row.find_element(By.XPATH, ".//td[3]").text
    author_names.append(author_name)

    # extract the volumes sold
    volumes = row.find_element(By.XPATH, ".//td[4]").text
    volumes_sold.append(volumes)
     # extract the publisher
    publisher = row.find_element(By.XPATH, ".//td[5]").text
    publishers.append(publisher)

    # extract the genre
    genre = row.find_element(By.XPATH, ".//td[6]").text
    genres.append(genre)

#  create a dataframe 
data = {'Book Name': book_names, 'Author Name': author_names, 'Volumes Sold': volumes_sold,
        'Publisher': publishers, 'Genre': genres}

df = pd.DataFrame(data)


# In[21]:


df


# In[ ]:


7. Scrape the details most watched tv series of all time from imdb.com.
Url = https://www.imdb.com/list/ls095964455/ You have to find the following details:
A) Name
B) Year span
C) Genre
D) Run time
E) Ratings
F) Votes


# In[121]:


from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# In[122]:


driver=webdriver.Chrome()


# In[123]:


driver.get("https://www.imdb.com/list/ls095964455/")


# In[131]:


tv_series_names = []
year_spans = []
genres = []
run_times = []
ratings = []
votes = []

tv_series = driver.find_elements(By.XPATH, "//div[contains(@class, 'lister-item-content')]")

for series in tv_series:
    # extract the tv series name
    tv_series_name = series.find_element(By.XPATH, "//h3/a").text
    tv_series_names.append(tv_series_name)

    # extract the year span of the tv series
    year_span = series.find_element(By.XPATH, "//span[contains(@class, 'lister-item-year')]").text
    year_spans.append(year_span)

    # extract the genre of the series
    genre = series.find_element(By.XPATH, "//span[contains(@class, 'genre')]").text.strip()
    genres.append(genre)
        # extract the run time of the series
    run_time = series.find_element(By.XPATH, "//span[contains(@class, 'runtime')]").text
    run_times.append(run_time)

    # extract the rating of the series
    rating = series.find_element(rating = series.find_element(By.XPATH, "//div[contains(@class, 'ratings-bar')]").text

    ratings.append(rating)

    # extract the votes of the series
    vote = series.find_element(By.XPATH, "//span[contains(@name, 'ir')]").get_attribute("data-value")
    votes.append(vote)

#  create a dataframe
data = {'TV Series Name': tv_series_names, 'Year Span': year_spans, 'Genre': genres,
        'Runtime': run_times, 'Ratings': ratings, 'Votes': votes}

df = pd.DataFrame(data)


# In[ ]:


8. Details of Datasets from UCI machine learning repositories.
Url = https://archive.ics.uci.edu/ You have to find the following details:
A) Dataset name
B) Data type
C) Task
D) Attribute type
E) No of instances
F) No of attribute G) Year
Note: - from the home page you have to go to the Show All Dataset page through code


# In[61]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import requests


# In[62]:


driver=webdriver.Chrome()


# In[63]:


driver.get("https://archive.ics.uci.edu/")


# In[ ]:


dataset_names=[]
data_types = []
tasks = []
attribute_types = []
num_instances = []
num_attributes = []
years = []



