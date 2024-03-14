import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Send a GET request to the URL
response = requests.get(url)

html=BeautifulSoup(response.text,"html5lib")
panel_div=html.find(id="mw-panel-toc-list")

panel_data=[]

if panel_div:
    li_elements=panel_div.find_all(class_="vector-toc-list-item vector-toc-level-1")
    for li in li_elements:
        title=li.select(".vector-toc-text")[0].get_text()
        panel_data.append({"title": title.strip()})
    print(panel_data)
    