import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all postings under the "Search Postings" heading
postings = soup.find_all('div', class_='posting_item')

# Retrieve only the first 5 postings
postings = postings[:5]

# Initialize a list to store the results
results = []

# Extract the desired fields from each posting
for posting in postings:
    # Extract Est. Value Notes
    est_value_notes = posting.find('div', class_='est_value_notes').text.strip()
    
    # Extract Description
    description = posting.find('div', class_='posting_desc').text.strip()
    
    # Extract Closing Date
    closing_date = posting.find('div', class_='closing_date').text.strip()

    # Create a dictionary with the extracted information
    result = {
        'Est. Value Notes': est_value_notes,
        'Description': description,
        'Closing Date': closing_date
    }
    
    # Add the result to the list of results
    results.append(result)

# Print the results
for result in results:
    print(result)
