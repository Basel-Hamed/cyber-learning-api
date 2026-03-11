import requests
from bs4 import BeautifulSoup


def get_site_data(url):

    try:

        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=10)

        soup=BeautifulSoup(r.text,"html.parser")

        texts=[]

        for tag in soup.find_all(["h1","h2","h3","p"]):

            t=tag.get_text().strip()

            if len(t)>40:

                texts.append(t)

            if len(texts)>=10:
                break

        return " ".join(texts)

    except:

        return "Unable to fetch learning data"
