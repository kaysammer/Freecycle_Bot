import requests
from lxml import html

USERNAME = "kayfelix"
PASSWORD = "*******"

LOGIN_URL = "https://www.freecycle.org/login"
URL = "https://www.freecycle.org/home/dashboard"

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

    print(result.content)


if __name__ == '__main__':
    main()
