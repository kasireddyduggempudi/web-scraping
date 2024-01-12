import requests
from bs4 import BeautifulSoup


def extract_links_from_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (links) on the webpage
            links = soup.find_all('a')

            # Extract and print the href attribute of each link
            file = open("links.txt", "w")
            links_dict = []
            for link in links:
                href = link.get('href')
                if href and href not in links_dict:
                    file.write(href + "\n")
                    print(href)
                    links_dict.append(href)
            file.close()

        else:
            print(f'Error: Unable to fetch the webpage. Status code: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')

# Example usage:
website_url = input("Enter main url: ")
extract_links_from_website(website_url)
