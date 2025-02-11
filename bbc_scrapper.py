import requests
from bs4 import BeautifulSoup
import csv

# BBC Website URL
url = "https://www.bbc.com"

# Request the page
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch the webpage. Status code:", response.status_code)
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all h2 elements
headlines = soup.find_all("h2")

# If no headlines are found, print message and exit
if not headlines:
    print("No headlines found!")
    exit()

# Prepare data for CSV
data = []
for h2 in headlines:
    title = h2.get_text(strip=True)
    link = h2.find_parent("a")["href"] if h2.find_parent("a") else "No link available"
    if link.startswith("/"):  # Convert relative link to full URL
        link = url + link
    data.append([title, link])

# Save to CSV
csv_filename = "bbc_headlines.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)

print(f"✅ Scraping complete! Data saved in {csv_filename}")