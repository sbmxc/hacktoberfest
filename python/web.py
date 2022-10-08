#python code to get the http REQUEST headers of a website

import requests

URL = 'https://www.google.com/search?q=microsoft'

def request(url):
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}, verify=True, allow_redirects=False)

        headers = response.headers

        for header in headers:
            print(header, headers[header])
            print('\n')

    except requests.exceptions.ConnectionError:
        print('Error: Connection Error')

request(URL)