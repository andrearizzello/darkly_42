import requests
from bs4 import BeautifulSoup


def scrape_folder(response):
    soup = BeautifulSoup(response.content)
    for a_tag in soup.find_all('a', href=True)[1:]:
        if a_tag['href'] == 'README':
            print(response.request.url + a_tag['href'])
        else:
            r = requests.get(response.request.url + a_tag['href'])
            scrape_folder(r)


if __name__ == '__main__':
    r = requests.get("http://192.168.56.101/.hidden/")
    scrape_folder(r)
