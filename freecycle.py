import json

import requests
from lxml import html
import re

USERNAME = "kayfelix"
PASSWORD = "*******"

LOGIN_URL = "https://www.freecycle.org/login"
URL = "https://www.freecycle.org/home/dashboard"


def convert_html_to_dict(txt_html):
    """Read in free cycle html as a string output a dictionary.

    keys are:
        'count', 'posts', 'tags', 'towns', 'blockedUsers', 'criteria', 'suppressAds'
    """
    txt_html = txt_html.replace('&quot;', '"')
    ss = re.search("<fc-data :data=\"(.*)\" :limit=\d+ context=\"posts\".*?</fc-data>", txt_html)
    txt_reduced = ss.groups()[0]

    # Read text as in as json format and return a dictionary
    data = json.loads(txt_reduced)
    return data


def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "user": USERNAME, 
        "password": PASSWORD,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    freecycle_dict = convert_html_to_dict(result.text)
    print(freecycle_dict)


if __name__ == '__main__':
    main()
