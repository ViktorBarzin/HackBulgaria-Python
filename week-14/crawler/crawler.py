import requests
import matplotlib.pyplot as plt
# import numpy as np
from collections import defaultdict
from bs4 import BeautifulSoup


def extract_server(url):
    try:
        server = requests.head(url).headers['server']
    except Exception:
        return None
    else:
        return server


def get_all_hrefs(url):
    hrefs = []
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        hrefs.append(link.get('href'))
    return hrefs


def save_histogram(dictionary):
    plt.bar(list(range(len(dictionary))), dictionary.values(), align='center')
    plt.xticks(list(range(len(dictionary))), dictionary.keys())
    # plt.show()
    plt.savefig('test.svg')


def main():
    servers = defaultdict(int)
    # print(extract_server('https://hackbulgaria.com'))
    # hrefs = get_all_hrefs('http://register.start.bg/')
    # for href in hrefs:
    #     if href:
    #         server = extract_server(href)
    #         if server:
    #             servers[server] += 1
    servers = {'Apache': 12, 'Apache/2.2.3 (CentOS)': 4, 'Apache/2.4.6 (CentOS) PHP/5.4.16': 6, 'Apache/2.2.15 (CentOS)': 23, 'nginx/1.11.2': 1, 'Apache/2.4.23 (FreeBSD) OpenSSL/1.0.1p-freebsd PHP/5.6.26': 1, 'nginx': 1}
    print(dict(servers))
    save_histogram(dict(servers))


if __name__ == "__main__":
    main()
