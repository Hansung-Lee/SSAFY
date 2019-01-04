import requests
import bs4

url = "https://finance.naver.com/sise/"

response = requests.get(url)
doc = bs4.BeautifulSoup(response.text, 'html.parser')


print(doc.select_one('#KOSPI_now'))




