from lxml import html
import requests

page = requests.get('https://www.reddit.com')
tree = html.fromstring(page.content)
