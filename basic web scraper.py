import requests
from bs4 import BeautifulSoup


def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information from the HTML, adjust this part based on the structure of the webpage
        # Here, we are extracting all the text within <p> tags
        paragraphs = soup.find_all('p')

        # Display the extracted information
        print("Extracted Information:")
        for i, paragraph in enumerate(paragraphs, start=1):
            print(f"{i}. {paragraph.text.strip()}")

    else:
        print(
            f"Failed to retrieve the webpage. Status code: {response.status_code}")


if __name__ == "__main__":
    # Example URL, replace it with the URL of the website you want to scrape
    target_url = "https://en.wikipedia.org/wiki/Luka_Don%C4%8Di%C4%87" #Enter URL you want to scrape

    # Call the web scraper function with the target URL
    simple_web_scraper(target_url)

