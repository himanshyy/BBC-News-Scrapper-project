# BBC-News-Scrapper-project
This project is a web scraping script that extracts the latest news headlines and links from the BBC website. Using Python and BeautifulSoup, it fetches news articles, processes the data, and stores it in a CSV file for easy access and analysis.
🛠 Technologies Used

Python (for scripting)

BeautifulSoup (for web scraping)

Requests (to fetch web page content)

CSV Module (to store data in a structured format)

🚀 Features

✔ Scrapes Latest News – Extracts headlines and article links from BBC News.
✔ Stores Data in CSV – Saves the collected news in a structured format.
✔ Handles Missing Data – Avoids errors when headlines or links are unavailable.
✔ Efficient & Fast – Fetches and processes data in seconds.

💡 How It Works

⿡ Fetches HTML content from the BBC News page.
⿢ Parses the page using BeautifulSoup.
⿣ Extracts all <h2> headlines and their corresponding article links.
⿤ Saves the results in a bbc_headlines.csv file.
⿥ Handles errors if headlines or links are missing.

🌍 Real-World Applications

✅ News Aggregation – Collect news headlines from multiple sources.

✅ Data Analysis – Analyze news trends over time.

✅ Automated Reporting – Generate daily news reports automatically.

✅ Freelancing/Portfolio – Showcase web scraping skills for clients or job applications.

📌 How to Run the Project?

⿡ Install dependencies:

pip install requests beautifulsoup4

⿢ Run the script:

python bbc_scraper.py

⿣ Open bbc_headlines.csv to view the extracted news.



