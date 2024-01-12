import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links_recursive(url, max_depth=3, current_depth=0, visited=set()):
    try:
        # Check if the URL has already been visited to avoid infinite loops
        if url in visited:
            return

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (links) on the webpage
            links = soup.find_all('a')

            # Extract and print the href attribute of each link
            # file = open("links.txt", "w")
            links_dict = []
            for link in links:
                href = link.get('href')
                if href and href not in links_dict:
                    absolute_url = urljoin(url, href)  # Convert relative URLs to absolute URLs


                    if absolute_url.startswith("https://dex."):
                        print(absolute_url)
                        links_dict.append(href)

                    # Recursively extract links from the new URL if depth allows
                        if current_depth < max_depth:
                            extract_links_recursive(absolute_url, max_depth, current_depth + 1, visited)

        else:
            print(f'Error: Unable to fetch the webpage. Status code: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')

# Example usage:
website_url = input("Enter main url: ")
extract_links_recursive(website_url, max_depth=2)
