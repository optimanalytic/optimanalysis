"""
Web Scraping and HTML Basics
Demonstrating various web scraping features for educational purposes...
This code is part of the IBM Data Engineering Professional Certificate course on Coursera

"""

# Required Libraries
import requests
from bs4 import BeautifulSoup

# Suppress warnings
import warnings

def warn(*args, **kwargs):
    pass

warnings.warn = warn
warnings.filterwarnings('ignore')

# Helper function to display a section heading
def display_heading(title):
    print("\n" + "=" * 80)
    print(f"{title.center(80)}")
    print("=" * 80)

# URL to scrape
url = 'https://en.wikipedia.org/wiki/IBM'

# Step 1: Fetch HTML Content
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve {url}. Status Code: {response.status_code}")
    exit()

html_content = response.text

# Step 2: Parse HTML Content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract Page Title
display_heading("Page Title")
print(soup.title.string)

# Step 4: Extract Meta Information (URL and Routes)
display_heading("Page URL and Routes")
print(f"URL: {url}")
print(f"Route: {url.split('/')[-1]}")

# Step 5: Extract All Headings (h1, h2, h3, etc.)
display_heading("Headings on the Page")
for heading in soup.find_all(['h1', 'h2', 'h3']):
    print(f"{heading.name}: {heading.text.strip()}")

# Step 6: Extract All Image Titles and Sources
display_heading("Images with Titles and Sources")
images = soup.find_all('img')
for idx, img in enumerate(images, 1):
    title = img.get('title', 'No title available')
    src = img.get('src', 'No source available')
    print(f"Image {idx}: Title: {title}, Source: {src}")

# Step 7: Extract All Links with Text
display_heading("Links and Their Names")
links = soup.find_all('a')
for idx, link in enumerate(links[:10], 1):  # Show the first 10 links
    href = link.get('href', 'No href available')
    text = link.text.strip() or "No text available"
    print(f"Link {idx}: Text: {text}, Href: {href}")

# Step 8: Count and Display Different Tags
display_heading("Tag Counts on the Page")
tag_counts = {}
for tag in soup.find_all(True):  # Find all tags
    tag_counts[tag.name] = tag_counts.get(tag.name, 0) + 1
for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{tag}: {count}")

# Step 9: Summary of Features
display_heading("Script Features Summary")
print("""
1. Extracts and displays:
   - Page title
   - URL and routes
   - All headings (h1, h2, h3, etc.)
   - Image titles and sources
   - Link names and hrefs
   - Count of different HTML tags
2. Provides a clean, structured, and educational script for web scraping.
3. Demonstrates Python's capabilities with BeautifulSoup for HTML parsing.
""")
