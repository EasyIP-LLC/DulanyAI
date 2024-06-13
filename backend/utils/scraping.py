import requests
from bs4 import BeautifulSoup
import re

def scrapeClaims(url, headers=None):
    """Scrapes claims 1-N from a given patent URL on Google Patents."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        response.encoding = 'utf-8'
        response_text = response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return ""

    soup = BeautifulSoup(response_text, "html.parser")
    claim_dependent_sections = soup.find_all(class_="claim")

    seen = set()  # Using a set for seen items
    newClaims = []

    # Extracting the claims from the patent
    for section in claim_dependent_sections:
        claim_text_sections = [
            claim_text.get_text(strip=True)
            for claim_text in section.find_all(class_="claim-text")
        ]

        for item in claim_text_sections:
            if item not in seen:
                seen.add(item)
                newClaims.append(item)

    return "\n".join(newClaims)  # Return the claims concatinated by newline chars

def scrapeAbstract(url, headers=None):
    """Scrapes abstract from a given patent URL on Google Patents."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        response.encoding = 'utf-8'
        response_text = response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
    soup = BeautifulSoup(response_text, "html.parser")
    abstract_element = soup.find('abstract')

    if abstract_element == None:
        return ""

    # Extract the text from the <abstract> element
    abstract_text = abstract_element.get_text(separator=' ', strip=True)

    return abstract_text

def scrapeDescription(url, headers=None):
    """Scrapes description from a given patent URL on Google Patents."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        # Ensure the response is decoded using UTF-8
        response.encoding = 'utf-8'
        response_text = response.text
        
    except requests.RequestException as e:
        # log the error:

        return ""
    
    soup = BeautifulSoup(response_text, "html.parser")

    description_element = soup.find_all(class_=re.compile(r'\bdescription\b'))

    if description_element is None:
        return ""
    
    descriptions = []  # Use a set to avoid duplicates

    for element in description_element:
        if element.find(class_=re.compile(r'\bdescription\b')):
            continue  # Skip this element if it contains nested description elements

        description_text = element.get_text(separator=' ', strip=True)
        descriptions.append(description_text)


    return "\n".join(descriptions)