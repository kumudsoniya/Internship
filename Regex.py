#!/usr/bin/env python
# coding: utf-8

# Question1: sample text:Python Exercises, Php exercises.'

# In[30]:


import re
def replace_characters(string):
    replacements={" ",",","."}
    for char in replacements:
        string=string.replace(char,":")
        
    return string

#Example

input_string="Python exercises, Php exercises."
output_string=replace_characters(input_string)

print(f"output string:{output_string}")


# Question2:

# In[33]:


import re
# find_word_starting_with_a_e(string):
    
string="Apple and Eggplant are fruits. Eagle is a bird"
pattern=r"\b[ae]\w+\b"

Result=re.findall(pattern,string ,flags=re.IGNORECASE)


print(Result)


# Question3:

# In[6]:


import re
# find word atleast 4 characters
string= "This is a sample string with words of different lengths."
pattern=re.compile(r"\b\w{4,}\b")

Result=re.findall(pattern, string)
print(Result)


# Question4:

# In[13]:


#find3,4 & 5 characters in string
import re

input_string="we moved in new house but some works are pending."
pattern=re.compile(r"\b\w{3,5}\b")

Result=re.findall(pattern,input_string)
print(Result)


# Question5:

# In[83]:


import re

def remove_parentheses(text_list):
    # Create a compiled regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\([^)]*\)')
    
    # Iterate through the list of strings and remove the matched patterns
    modified_list = [pattern.sub('', text) for text in text_list]
    
    return modified_list

# Sample text list
sample_text = ["example(.com)", "hr@fliprobo(.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Remove parentheses and print the modified list
modified_text = remove_parentheses(sample_text)
for text in modified_text:
    print(text)


# Question6:

# In[95]:


import re
input_text=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

file= open("input_text.txt","w")
file.write("input_text.txt")
file.close()

def remove_parentheses(text_list):
    # Create a compiled regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\([^)]*\)')
    
    # Iterate through the list of strings and remove the matched patterns
    modified_list = [pattern.sub('', text) for text in text_list]
    
    return modified_list
with open('input_text.txt', 'r') as file:
    input_text = file.read()



# Remove parentheses and print the modified list
modified_text = remove_parentheses("input_text.txt")

print("Text with parentheses removed and saved in 'input_text.txt'")


# Question7:

# In[47]:


import re
text= "ImportanceOfRegularExpressionsInPython"
x=re.findall(r"[A-Z][a-z]*",text)
print(x)


# Question8:

# In[34]:


import re 
def insert_space_between_numbers(text):
    #use regular expression to find words starting with numbers
    text="RegularExpression1IsAn2ImportantTopic3InPython"
    pattern=r"(?<=\D)(?=\d)"
    new_text=re.sub(pattern," ",text)
    return new_text
result=insert_space_between_numbers(text)

print(result)


# Question9:

# In[57]:


import re 
def insert_space_between_numbers(text):
    
    pattern=r"(?<=\D)(?=\d)|(?<=\d)(?=\D)"
    new_text=re.sub(pattern," ",text)
    
    return new_text
text="RegularExpression1IsAn2ImportantTopic3InPython"
result=insert_space_between_numbers(text)
print(result)


# Question10:

# In[39]:


import re

text= "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com." 
file=open("text.txt","w")
file.write("text.txt")
file.close()

email_pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email_adresses=re.findall(email_pattern,text)

for email in email_adresses:
    print(email)
    



# Question11:

# In[69]:


import re

strings=["Helloeorld123",
       "hello_world","12345",
       "Hello_World!","abc123_","_"]

pattern= r"^[a-zA-Z0-9_]+$"

for string in strings:
    match=re.search(pattern,string)
    if match:
        print(f"{string} is a valid string.")
    else:
        print(f"{string} is not a valid string.")


# Question12:

# In[84]:


import re

string ="1234Hello"
number = 1234

if string.startswith(str(number)):
    print(f"The srting {string} starts with the number{number}.")
    
else:
    print(f"The string {string} does not start with the number{number}.")


# Question13:

# In[85]:


import re

ip_address = "192.168.001.001"

octets = ip_address.split(".")
normalized_octets = [str(int(octet)) for octet in octets]

normalized_ip=".".join(normalized_octets)

print(f"original IP address:{ip_address}")
print(f"Normalized IP address:{normalized_ip}")


# 
# Question14:

# In[34]:


text =  "On August 15th 1947 that India was declared independent from British colonialism,and the reins of control were handed over to the leaders of the Country"



# In[38]:


import re 

pattern =r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(\d{4})\b"

with open ("python_file.txt","r") as file:
           text=file.read()
           match=re.search(pattern, text)
if match:
                day=match.group(1)
                year=match.group(2)
                date=f"{day}th {year}"
                print(date)
           
        


# Question15:

# In[45]:


import  re

text="'The quick brown fox jumps over the lazy dog"

patterns=["fox","dog","horse"]

for pattern in patterns:
    print("searching for '%s' in '%s' ->"% (pattern,text),)
if re.search(pattern,text):
          print("Matched")
else:
      
          print("No matched")             
                        


# Question16:

# In[3]:


import re
text="The quick brown fox jumps over the lazy dog."
pattern="fox"

match = re.search(pattern,text)

s=match.start()
e=match.end()

print("Found '%s' in '%s' from %d to %d" %\
    
    (match.re.pattern,match.string,s,e))


# Question17:

# In[5]:


import re

text= "python excercise,PhP excercise,c#excercise"

pattern= r"\bexcercise\b"

matches= re.findall(pattern,text)

if matches:
    print("substring found:",matches)
else:
    print("substring not found")


# Question18:

# In[9]:


import re
text = 'Python file, PHP file, csv file'
pattern = 'exercises'
for match in re.findall(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# Question19:

# In[10]:


date= "2023-09-25"

year,month,day = date.split("-")

#recontruct the date in the desired format

new_date = f"{day}-{month}-{year}"

print("original date :",date)
print("converted date:",new_date)      


# Question20:

# In[12]:


import re

def find_decimal_numbers(string):
    pattern = re.compile(r'\d+\.\d{1,2}')
    decimal_numbers = re.findall(pattern, string)
    return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)


# Question21:

# In[14]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 90 sizes. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# Question22:

# In[16]:


import re

string= " My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
pattern=r"\d+"

numbers = re.findall(pattern,string)

if numbers:
    max_number = max(numbers,key=int)
    max_value = int(max_number)
    print("Maximum numeric value:",max_value)
    
else:
    print("No numeric value found in the string")
    


# Question23:

# In[22]:


import re

str1="RegularExpressionIsAnImportantTopicInPython"
def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("RegularExpressionIsAnImportantTopicInPython"))




# Question24:

# In[23]:


import re

pattern = r"[A-Z][a-z]+"
text= "Abc Def Ghi Jki"

matches = re.findall(pattern, text)
print(matches)


# Question25:

# In[25]:


import re 
sentence= "Hello hello world world"
clean_sentence= re.sub(r"\b(\w+)(\s+\1)+\b",r"\1",sentence)

print(clean_sentence)


# Question26:

# In[30]:


import re 

string1= "This is a sentence."
string2 = "This is a chapter11."
string3= "This is a chapter21."

pattern= r"^.*[a-zA-Z0-9]$"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3=  re.match(pattern,string3)

if match1:
    print(" string1 end with an alphanumeric chapter.")
else:
    print("string1 does not end with an alphanumeric chapter.")
    
if match2:    
    print("string2 end with an alphanumeric chapter.")
else:
    print("string2 does not end with an alphanumeric chapter.")
    
if match3:    
    print("string3 end with an alphanumeric chapter.")  
else:
    print("string3 does not end with an alphanumeric chapter.")
        


# Question27:

# In[68]:


import re

# Sample text
text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

# Regular expression pattern to match hashtags, including those within tags
pattern = r'#\w+|<[^>]*>#\w+'

# Find all hashtags in the text
hashtags = re.findall(pattern, text)

# Filter out the hashtags enclosed within tags
filtered_hashtags = [tag for tag in hashtags if not tag.startswith('<')]

# Print the extracted hashtags
print(filtered_hashtags)


# Question28:

# In[31]:


import re

input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
output_text = re.sub(pattern, "", input_text)

print(output_text)


# Question29:

# In[36]:


file=open("file.txt","w")
file.write("Ron was born on 12-09-1992 and he was admitted to school 15-12-1999")
file.close()

file_path= "file.txt"
with open(file_path,"r") as file:
    text=file.read()
pattern=r"\d{2/\d{2}/\d{4}"

dates = re.findall(pattern,text)

print(dates)



# Question30:

# In[30]:


import re 
string= "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    
words= string.split()
filterd_words=[words for words in words if len(words)>4]
    
cleaned_string="".join(filterd_words)
print(cleaned_string)


# In[ ]:





# In[ ]:




