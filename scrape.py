import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time 
def scrape_website(website):
    print("Launching chrome browser...")
    chrome_driver_path = "chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    
    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(3)
        return html
    finally:
        driver.quit()

# Function to extract the body content from the HTML
def extract_body_content(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the body content
    body_content = soup.body
    
    # Return the body content as a string if it exists, otherwise return an empty string
    if body_content:
        return str(body_content)
    return ""

# Function to clean the body content by removing scripts and styles
def clean_body_content(body_content):
    # Parse the body content using BeautifulSoup
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove all script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # Get the text content and separate lines with a newline character
    cleaned_content = soup.get_text(separator="\n")
    
    # Remove leading and trailing whitespace from each line and filter out empty lines
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    # Return the cleaned content
    return cleaned_content

# Function to split the DOM content into chunks of a specified maximum length
def split_dom_content(dom_content, max_length=6000):
    # Split the DOM content into chunks of the specified maximum length
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]