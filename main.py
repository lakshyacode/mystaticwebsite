# step 0:install all the requirements
import requests
from bs4 import BeautifulSoup
# url="https://fundamental.in/"
# url="https://codewithharry.com/"
url="https://www.ajio.com/"

# step 1:get the html
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)


# step 2: parsing the html content
soup=BeautifulSoup(htmlContent,"html.parser")
# print(soup.prettify)
divs = soup.find_all('div')
classes = [div.get('class') for div in divs]
print(classes)
# step 3:Tree traversal
# title=soup.title
# print(title)
# print(type(soup))

# Getting the class
paras=soup.find_all('p')
print(soup.find('p') ) 

# All the classes
# print(soup.find('body')['class'])

classes=soup.find_all('class')
# print(classes)
# print(soup.find('class'))

# All the images
image1=soup.find_all("img")
print(image1);