import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. URL of our Canteen webpage
url = "https://yashikasuhasaria-dotcom.github.io/Canteen-/"

# 2. Get webpage
response = requests.get(url)

# 3. Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# 4. Find all menu items
items = soup.find_all("div", class_="menu-item")

# 5. Store extracted data
data = []

for item in items:
    name=item.find("h3").text.strip()
    price=item.find(class_="price").text.strip()
   
    data.append({"Name": name, "Price": price})
# 6. Convert to DataFrame
df = pd.DataFrame(data)

# 7. Display data
print(df)

# 8. Save to CSV
df.to_csv("canteen_menu.csv", index=False)

print("Saved to canteen_menu.csv")

# Run the script
# Make sure your Flask server is running
# and the menu is available at
# http://127.0.0.1:5000/menu