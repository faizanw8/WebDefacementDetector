import requests
from bs4 import BeautifulSoup
import time
from difflib import ndiff

# Function to fetch the content of a web page
def fetch_page(url):
    response = requests.get(url)
    return response.text

# Function to extract the DOM structure from HTML content
def extract_dom(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return str(soup)

# Function to compare two DOM structures and calculate the change ratio
def calculate_dom_change_ratio(old_dom, new_dom):
    d = ndiff(old_dom.splitlines(), new_dom.splitlines())
    diff_count = sum(1 for line in d if line.startswith('+ ') or line.startswith('- '))
    total_lines = max(len(old_dom.splitlines()), len(new_dom.splitlines()))
    return diff_count / total_lines

# Function to check for web page defacement
def check_for_defacement(url, interval_minutes, change_threshold):
    print("Monitoring", url, "for defacement...")
    previous_dom = None

    while True:
        # Fetch current DOM
        current_html = fetch_page(url)
        current_dom = extract_dom(current_html)

        # Compare with previous DOM
        if previous_dom is not None:
            change_ratio = calculate_dom_change_ratio(previous_dom, current_dom)

            # Convert percentage threshold to decimal
            threshold_decimal = change_threshold / 100.0

            if change_ratio >= threshold_decimal:
                print("ALERT: Web page may have been defaced!")

        # Update previous DOM
        previous_dom = current_dom

        # Wait for the specified interval
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    url = input("Enter the URL of the web page to monitor: ")
    interval_minutes = int(input("Enter the interval in minutes for checking: "))
    change_threshold = float(input("Enter the change threshold for triggering an alert (0 to 100): "))

    check_for_defacement(url, interval_minutes, change_threshold)
