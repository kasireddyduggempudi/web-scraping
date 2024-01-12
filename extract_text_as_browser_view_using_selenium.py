from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def extract_text_from_website(url, filename):
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

        # Create a Chrome webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the webpage
        driver.get(url)

        # Wait for the page to load (adjust the sleep time if needed)
        driver.implicitly_wait(5)

        # Extract text content
        visible_text = driver.find_element(By.TAG_NAME, 'body').text

        lines_with_space = '\n\n'.join(visible_text.split('\n'))

        # Save the text content to a txt file
        with open(filename + '.txt', 'w', encoding='utf-8') as file:
            file.write(lines_with_space)

        print(f'Visible text content extracted and saved to output.txt')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        # Close the webdriver
        if driver:
            driver.quit()

# Example usage:
website_url = input("Enter web url: ")
filename = input("Enter file name: ")
extract_text_from_website(website_url, filename)
