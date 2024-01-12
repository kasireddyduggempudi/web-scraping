import requests
from bs4 import BeautifulSoup

def extract_text_from_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract text content and concatenate text from the same element
            text_content = '\n'.join([element.get_text(strip=True, separator=' ') for element in soup.find_all(['p', 'divi', 'code', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
            
            # Save the text content to a txt file
            with open('output.txt', 'w', encoding='utf-8') as file:
                file.write(text_content)
            
            print(f'Text content extracted and saved to output.txt')
        else:
            print(f'Error: Unable to fetch the webpage. Status code: {response.status_code}')

    except Exception as e:
        print(f'Error: {e}')

website_url = input("Enter web url: ")
extract_text_from_website(website_url)

