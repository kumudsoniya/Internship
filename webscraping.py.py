#!/usr/bin/env python
# coding: utf-8

# In[56]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# 1.Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[57]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# making dataframe
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[58]:


soup= BeautifulSoup(page.content)
soup


# In[76]:


header_tags=[]

    # Find all header tags (h1, h2, h3, h4, h5, h6) on the page
header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Extract the text from the header tags
header_texts = [tag.get_text() for tag in header_tags]

    # making dataframe


# In[77]:


df = pd.DataFrame({'Header Tags': header_tags})


# In[78]:


df


# 2.Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame

# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page= requests.get("https://presidentofindia.nic.in/former-presidents.htm ")

page


# In[18]:


soup= BeautifulSoup(page.content)
soup


# In[19]:


president_names = []
for i in soup.find_all("div",class_="president-listing"):
    president_names.append(i.text)
    
president_names


Term_office=[]
for i in soup.find_all("div",class_="field-content"):
    Term_office.append(i.text)
    
    
Term_office 
      


# In[20]:


data={"president_names": president_names,
      "Term_office":Term_office}
df=pd.DataFrame(data)
df


# 3.Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating

# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URLs for the ODI rankings of teams, batsmen, and bowlers.
team_ranking_url = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
batsmen_ranking_url = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
bowlers_ranking_url =requests.get( "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")


team_ranking_url
batsmen_ranking_url
bowlers_ranking_url


# In[17]:


soup= BeautifulSoup(team_ranking_url.content)
soup


# In[21]:


team = []
        
for i in soup.find_all("div",class_="rankings-block__container full rankings-table"):
    team.append(i.text)
    
team    
batsmen=[]
for i in soup.find_all("div",class_="rankings-block__container full" ):
    batsmen.append(i.text)
    
batsmen    
    
bowler=[]

for i in soup.find_all("div",class_="rankings-block__container full "):
    bowler.append(i.text)
    
bowler    
    


# In[23]:


#making dataframe
data = {
      "team":team, 
      "batsmen": batsmen,
        "bowler": bowler}
df= pd.DataFrame(data)

df


# In[ ]:


4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
b) Top 10 women’s ODI Batting players along with the records of their team and rating.
c) Top 10 women’s ODI all-rounder along with the records of their team and rating


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[49]:


def scrape_and_create_dataframe(url, columns):
    response = requests.get(url)
    
soup = BeautifulSoup(response.text, 'html.parser')
data = []

        # Find the table containing the desired data
table = soup.find('table', {'class': 'table'})


# URL for the top 10 ODI teams in women's cricket
odi_teams_url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"

# Columns for the ODI teams DataFrame
odi_teams_columns = ['Position', 'Team', 'Matches', 'Points', 'Rating']

# URL for the top 10 women's ODI batting players
odi_batting_url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"

# Columns for the ODI batting players DataFrame
odi_batting_columns = ['Position', 'Player', 'Team', 'Rating']

# URL for the top 10 women's ODI all-rounders
odi_all_rounder_url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"

# Columns for the ODI all-rounders DataFrame
odi_all_rounder_columns = ['Position', 'Player', 'Team', 'Rating']

# Scrape data and create DataFrames
odi_teams_df = scrape_and_create_dataframe(odi_teams_url, odi_teams_columns)
odi_batting_df = scrape_and_create_dataframe(odi_batting_url, odi_batting_columns)
odi_all_rounder_df = scrape_and_create_dataframe(odi_all_rounder_url, odi_all_rounder_columns)

# Print DataFrames
print("Top 10 ODI Teams in Women's Cricket:")
print(odi_teams_df.head(10))

print("\nTop 10 Women's ODI Batting Players:")
print(odi_batting_df.head(10))

print("\nTop 10 Women's ODI All-rounders:")
print(odi_all_rounder_df.head(10))


# 5.Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
# i) Headline
# ii) Time
# iii) News Link

# In[25]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page= 'https://www.cnbc.com/world/?region=world'
response=requests.get(page)


# In[26]:


articles = soup.find_all('div',class_="PageBuilder-col-9 PageBuilder-col")

        # Initialize empty lists to store data
        
headlines = []
times = []
links = []

for article in articles:
            # Extract headline and link
            headline = article.find('h3').text.strip()
            link = 'https://www.cnbc.com' + article.find('a')['href']
            
            # Extract time (if available)
            time_element = article.find('time')
            

            headlines.append(headline)
            times.append(time)
            links.append(link)
            
            


# In[28]:


data = {'Headline': headlines,
                    'Time': times, 
                    'News Link': links}
df = pd.DataFrame(data)
df


# 6.Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page= "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response=requests.get(page)


soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize lists to store data
paper_titles = []
authors_list = []
published_dates = []
paper_urls = []

    # Find the article elements on the page
articles = soup.find_all("div", class_="pod-listing")

    # Iterate through the articles
for article in articles:
        # Extract the paper title
        paper_title = article.find("a", class_="pod-listing-header")
        paper_titles.append(paper_title.text.strip())

        # Extract authors
        authors = article.find("div", class_="pod-listing-authors")
        authors_list.append(authors.text.strip())

        # Extract published date
        published_date = article.find("div", class_="pod-listing-pub-date")
        published_dates.append(published_date.text.strip())

        # Extract the paper URL
        paper_url = article.find("a", class_="pod-listing-header")["href"]
        paper_urls.append(paper_url)

    # Create a DataFrame

data= { 'Paper Title': paper_titles,
        'Authors': authors_list,
        'Published Date': published_dates,
        'Paper URL': paper_urls}
    

df = pd.DataFrame(data)

    
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




