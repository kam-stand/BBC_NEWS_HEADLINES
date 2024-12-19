import requests
from bs4 import BeautifulSoup

class ScraperHelper:
    @staticmethod
    def fetch_webpage(url):
        """
        Fetches the content of a webpage.

        Args:
            url (str): The URL of the webpage to fetch.

        Returns:
            BeautifulSoup: A BeautifulSoup object for the webpage content if successful, None otherwise.
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully fetched webpage: {url}")
                return BeautifulSoup(response.text, 'html.parser')
            else:
                print(f"Failed to fetch webpage. HTTP Status Code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error occurred while fetching webpage: {e}")
            return None

    @staticmethod
    def format_url(base_url, link):
        """
        Converts a relative URL to an absolute URL.

        Args:
            base_url (str): The base URL of the website.
            link (str): The relative or absolute URL.

        Returns:
            str: A complete absolute URL.
        """
        # TODO: Students will implement this method
        base_url = base_url.strip()
        link = link.strip()
        if link.startswith('http'):
            return link
        elif link.startswith('/'):
            return base_url + link
        else:
            return base_url + '/' + link
        

    @staticmethod
    def extract_headlines(soup, base_url, tag, class_name):
        """
        Extracts headlines and their corresponding links from the webpage.

        Args:
            soup (BeautifulSoup): A BeautifulSoup object containing the parsed HTML.
            base_url (str): The base URL for resolving relative links.
            tag (str): The HTML tag that contains headlines (e.g., 'a').
            class_name (str): The class name of the HTML elements containing headlines.

        Returns:
            list: A list of tuples, each containing a headline text and a full URL link.
        """
        # TODO: Students will implement this method
        headlines = []
        for headline in soup.find_all(tag, class_=class_name ):
            link = headline.get('href')
            headline_text = headline.text
            headlines.append((headline_text, ScraperHelper.format_url(base_url, link)))
        return headlines[9:17]
    

    @staticmethod
    def print_headlines(headlines):
        """
        Prints the headlines and their corresponding links in a clean format.

        Args:
            headlines (list): A list of tuples, each containing (headline_text, headline_link).
        """
        if not headlines:
            print("No headlines found.")
            return

        print("\nExtracted Headlines:")
        print("-" * 40)
        for i, (headline, link) in enumerate(headlines, start=1):
            print(f"{i}. {headline}\n   Link: {link}")
        print("-" * 40)
