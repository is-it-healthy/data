from bs4 import BeautifulSoup
import requests
import re
import os
import json


class Scrape:
    def __init__(self, url: str) -> None:
        self.url = url
        self.data = {}

    @staticmethod
    def sanitize(a: str):
        a = a.strip()
        if '</a>' in a:
            a = re.sub(r'<a.*?</a>', '', a)
        kw = ("<strong>", "</strong>", "<em>", "</em>", "\n", "\t", "<i>", "</i>")
        for i in kw:
            a = a.replace(i, "")
        return a

    @staticmethod
    def keyName(a: str):
        a = a.strip().replace("E", "")
        return a

    @staticmethod
    def getAdditionalInfo(href):
        url = "https://www.food-info.net/uk/e/" + href
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        a = str(soup.find("td", bgcolor="white", valign="top", align="left", colspan="2")).strip()
        try:
            origin = Scrape.sanitize(a.split('<p><strong>Origin: <br/>')[1].split("</p>")[0])
        except:
            origin = ""
        try:
            characteristics = Scrape.sanitize(a.split('<p><strong>Function &amp; characteristics: <br/>')[1].split("</p>")[0])
        except:
            characteristics = ""
        try:
            products = Scrape.sanitize(a.split('<p><strong>Products: <br/>')[1].split("</p>")[0])
        except:
            products = ""
        try:
            daily_intake = Scrape.sanitize(a.split('<p><strong>Daily intake: <br/>')[1].split("</p>")[0])
        except:
            daily_intake = ""
        try:
            side_effects = Scrape.sanitize(a.split('<p><strong>Side effects: <br/>')[1].split("</p>")[0])
        except:
            side_effects = ""
        try:
            dietary_restrictions = Scrape.sanitize(a.split('<p><strong>Dietary restrictions: <br/>')[1].split("</p>")[0])
        except:
            dietary_restrictions = ""

        return {'origin': origin, 'characteristics': characteristics, 'products': products, 'daily_intake': daily_intake, 'side_effects': side_effects, 'dietary_restrictions': dietary_restrictions}

    def getMainPage(self):
        response = requests.get(self.url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        rows = soup.find_all('tr', {'bordercolor': '#009900'})[1:]
        data_list = []
        count = 0
        for row in rows:
            tds = row.find_all('td')
            number = tds[0].text.strip()
            href = str(tds[0].find('a')).split('href="')[-1].split('">')[0]
            name = tds[1].text.strip()
            function = tds[2].text.strip()
            data_list.append((number, name, function, href))

            moreInfo = Scrape.getAdditionalInfo(href=href)

            self.data[Scrape.keyName(a=number)] = {
                "code": number,
                "name": name,
                "href": href,
                "function": function,
                "more_info": {
                    "origin": moreInfo['origin'],
                    "characteristics": moreInfo['characteristics'],
                    "products": moreInfo['products'],
                    "daily_intake": moreInfo['daily_intake'],
                    "side_effects": moreInfo['side_effects'],
                    "dietary_restrictions": moreInfo['dietary_restrictions']
                }
            }

            count += 1
            if count == 5:
                break

        print(self.data)

    def saveData(self):
        if self.data is None:
            self.getMainPage()
        with open(os.path.join(os.getcwd(), 'data.json'), 'w', encoding='utf-8') as file:
            json.dump(self.data, file)


x = Scrape('https://www.food-info.net/uk/e/e100-200.htm')
x.getMainPage()
x.saveData()
