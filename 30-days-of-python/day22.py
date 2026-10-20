import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/dataset/53/iris'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)
