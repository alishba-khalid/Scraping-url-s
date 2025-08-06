 Web URL Scraper in Python
A beginner-friendly Python project that extracts all unique internal links from any given website and saves them into a CSV file.

This project uses the power of requests, BeautifulSoup, and urllib to navigate a webpage, find internal links (same domain), and export them for analysis or SEO research.

 ##Features##
✅ Scrapes all internal (same-domain) links from a webpage

✅ Filters only HTTP/HTTPS links

✅ Ensures uniqueness using Python sets

✅ Saves results to a .csv file

✅ Includes helpful error handling for bad URLs or network issues

✅ Clean, readable, and well-commented code

 ##Technologies Used##
requests – to fetch webpage content

BeautifulSoup (from bs4) – to parse HTML

urllib.parse – to handle URL paths and domains

csv – to export the scraped links

 ##File Output##
The program will create a file called:

unique_urls.csv

Each internal link found will be stored in its own row under the URL column.

 ##How to Run This Project##
1. Clone this repo or download the .py file
bash

git clone https://github.com/alishba-khalid/Scraping-url-s.git

2. Install the required libraries
bash

pip install requests beautifulsoup4
3. Run the script
bash

python your_script_name.py
You’ll be prompted to press Enter when it’s done scraping.

 Sample Target URL
Currently, the script is set to scrape from:
https://www.scrapingbee.com/blog/

You can change the target_url at the bottom of the script to scrape from any valid webpage.

 Example Output (console)
csharp

Scraping links from: https://www.scrapingbee.com/blog/

Found 42 unique internal links:
https://www.scrapingbee.com/blog/web-scraping-python/
https://www.scrapingbee.com/blog/beautifulsoup-guide/
...

Successfully saved 42 links to 'unique_urls.csv'
 ##About the Author##
Alishba Khalid
An aspiring Python developer on a mission to blend spiritual strength with technical excellence.
Follow my journey to become an extra ordinary pythonist , one line of Python at a time.



 License
This project is open-source and free to use under the MIT License.

 Contributions
Feel free to fork this project, submit pull requests, or suggest improvements.



