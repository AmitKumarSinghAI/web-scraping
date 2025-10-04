import pandas as pd
import numpy as  np
from bs4 import BeautifulSoup 
import requests
import matplotlib.pyplot as plt

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(
    "https://www.flipkart.com/search?q=face%20serum&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off",
    headers=headers,)

soup = BeautifulSoup(response.text, "lxml")


serum_name = []
Price = []
Rating = []

c = soup.find_all("a",class_="wjcEIp")
p = soup.find_all("div",class_="Nx9bqj")
r = soup.find_all("span",class_="Y1HWO0")

for i in range(min(len(c), len(p), len(r))):  
      serum_name.append(c[i].get("title"))
      Price.append(p[i].text.strip().replace("₹", "").replace(",", ""))
      Rating.append(r[i].text.strip())  

dict = {
    "Serum": serum_name,
    "Price (₹)": pd.to_numeric(Price,"coerce"),  
    "Rating": pd.to_numeric(Rating,"coerce") 
}

lis = pd.DataFrame(dict)
print(lis)

file_name = lis.to_csv("List of the serum.csv",index=False)
print(f"CSV file '{file_name}' created successfully!")


plt.figure(figsize=(12, 6))
plt.bar(np.array(lis["Serum"]),np.array(lis["Price (₹)"]), color="skyblue")
plt.ylabel('Price (₹)')
plt.title('Price of Face Serums')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

