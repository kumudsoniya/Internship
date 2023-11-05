#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. 
#     You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data
# 

# In[66]:


get_ipython().system('pip install selenium')


# In[79]:


# import all the required libraries
import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[80]:


driver= webdriver.Chrome()


# In[81]:


driver.get("https://www.shine.com/")

           


# In[82]:


designation=driver.find_element(By.ID,"id_q")

designation.send_keys('Data Analyst')


# In[83]:


location= driver.find_element(By.ID,"id_loc")
location.send_keys("Bangalore")


# In[84]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[85]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[86]:


# scraping job title from given page
title_tags=driver.find_elements(By.XPATH,"//h2[@itemprop='name']")
for i in title_tags:
    title=i.text
    job_title.append(title)
#scraping job location
location_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_lists__fdnsc']//div[2]")
for i in location_tags:
    location=i.text
    job_location.append(location)

#scraping company name
company_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_cName__mYnow']")
for i in company_tags:
    company=i.text
    company_name.append(company)
    
#scraping job experience
experience_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_lists__fdnsc']//div[2]")
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)    


# In[87]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[88]:


import pandas as pd
df=pd.DataFrame({"Title": job_title,"Location":job_location,"Company_name":company_name,"Experience":experience_required})
df


# In[90]:


df[0:10]


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually

# In[105]:


# import all the required libraries
import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


# In[106]:


driver=webdriver.Chrome()


# In[107]:


driver.get("https://www.shine.com/")


# In[108]:


designation=driver.find_element(By.ID,"id_q")

designation.send_keys('Data Scientist')


# In[109]:


location= driver.find_element(By.ID,"id_loc")
location.send_keys("Bangalore")


# In[111]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[115]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[117]:


# scraping job title from given page
title_tags=driver.find_elements(By.XPATH,"//h2[@itemprop='name']")
for i in title_tags:
    title=i.text
    job_title.append(title)
#scraping job location
location_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_lists__fdnsc']//div[2]")
for i in location_tags:
    location=i.text
    job_location.append(location)

#scraping company name
company_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_cName__mYnow']")
for i in company_tags:
    company=i.text
    company_name.append(company)
    
#scraping job experience
experience_tags=driver.find_elements(By.XPATH,"//div[@class='jobCard_jobCard_lists__fdnsc']//div[2]")
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)   


# In[118]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[119]:


import pandas as pd
df=pd.DataFrame({"Title": job_title,"Location":job_location,"Company_name":company_name,"Experience":experience_required})
df


# In[120]:


df[0:10]


# In[ ]:




