import requests
from bs4 import BeautifulSoup

def scrape_golf_courses(zip_code):
    url = f'https://www.google.com/maps/search/golf+courses/{zip_code}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        golf_courses = []
        for link in soup.find_all('a'):
            if link.get('aria-label'):
                name = link.get('aria-label').split(',')[0]
                address = link.get('aria-label').split(',')[1]
                golf_courses.append({'name': name, 'address': address})
        return golf_courses
    else:
        return None