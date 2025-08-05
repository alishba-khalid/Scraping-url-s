# url_scraper.py

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin, urlparse

# Define the main function that will scrape links from a given URL.
# 'url' is a PARAMETER: it's the web address we want to scrape.
def get_all_links(url):
    """
    Fetches a webpage, extracts all unique internal URLs from it, and returns them.
    Handles basic request errors.
    """
    unique_internal_links = set() # Use a set to automatically store only unique URLs
    base_url_domain = urlparse(url).netloc # Extract the domain (e.g., "example.com")

    try: # <--- The 'try' block starts here. All code inside it must be indented.
        # Send an HTTP GET request to the URL.
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        # --- DEBUG STEP A: Print the raw HTML content (first 1000 characters) ---
        print(f"\n--- Raw HTML Content from {url} (First 1000 chars) ---")
        print(response.text[:1000]) # Print first 1000 characters of the raw HTML
        print("---------------------------------------------------\n")
        # --- END DEBUG STEP A ---

        # Parse the HTML content of the page using BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags (which contain links)
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href'] # Get the URL from the 'href' attribute

            # Construct an absolute URL (handles relative links)
            absolute_url = urljoin(url, href)

            # Parse the absolute URL to get its domain
            parsed_absolute_url = urlparse(absolute_url)
            current_link_domain = parsed_absolute_url.netloc

            # --- DEBUG STEP C: Print domains for comparison ---
            # print(f"  Base Domain: {base_url_domain}, Link Domain: {current_link_domain}, Link: {absolute_url}")
            # --- END DEBUG STEP C ---

            # Check if it's an internal link (same domain) and a valid HTTP/HTTPS link.
            if current_link_domain == base_url_domain and parsed_absolute_url.scheme in ('http', 'https'):
                unique_internal_links.add(absolute_url) # Add to set to ensure uniqueness

    except requests.exceptions.RequestException as e: # <--- This 'except' block MUST be at the same indentation level as 'try'.
        # Catch errors related to HTTP requests (e.g., network problems, bad URLs, timeouts)
        print(f"Error fetching {url}: {e}")
    except Exception as e: # <--- This 'except' block MUST also be at the same indentation level as 'try'.
        # Catch any other unexpected errors during parsing or processing
        print(f"An unexpected error occurred for {url}: {e}")

    # Convert the set of unique links back to a list before returning.
    return list(unique_internal_links) # This line should be at the same indentation level as 'try' and 'except'.

# --- Main program execution starts here --- (This part is outside the function)
if __name__ == "__main__":
    target_url = "https://www.scrapingbee.com/blog/" # Let's use this for a more realistic test
    print(f"Scraping links from: {target_url}")

    links_found = get_all_links(target_url)

    print(f"\nFound {len(links_found)} unique internal links:")
    for link in links_found:
        print(link)
    output_csv_filename = "unique_urls.csv"

    try:
        # Open the CSV file in write mode ('w')
        # 'newline='''' is CRITICAL for CSV files to prevent extra blank rows
        with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Write the header row
            csv_writer.writerow(['URL'])  # Write a list containing the header name

            # Loop through each link found and write it as a row
            for link in links_found:
                csv_writer.writerow([link])  # Each link is a row, so it's a list with one item

        print(f"\nSuccessfully saved {len(links_found)} links to '{output_csv_filename}'")

    except Exception as e:
        print(f"Error saving links to CSV: {e}")

    # Optional: Keep the terminal open for manual inspection if double-clicking from File Explorer.
input("\nPress Enter to exit...")