import requests
from bs4 import BeautifulSoup
import os
import urllib

def scrape(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])
        
        extracted_text = ''
        for element in text_elements:
            extracted_text += element.get_text() + '\n'
        
        img_tags = soup.find_all('img')
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        for img_tag in img_tags:
            img_url = img_tag['src']
            img_name = os.path.basename(img_url)
            img_save_path = os.path.join(save_path, img_name)
            urllib.request.urlretrieve(img_url, img_save_path)
            print(f"Downloaded {img_name} to {img_save_path}")
        return extracted_text
    else:
        print("Failed to fetch.")
        return None

#------------------------------------------------

url = input("Enter URL: ")
save_path = input("Enter FULL save path: ")
text = scrape(url, save_path)
if (text):
    print("Success")
else:
    print("failed")