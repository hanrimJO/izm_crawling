from bs4 import BeautifulSoup
import requests


# def single_kpop():
#     for i in range(1, 10):
#         url = f"http://www.izm.co.kr/contentList.asp?bigcateidx=8&subcateidx=10&view_tp=1&view_sort=1&subjectchr=&periodidx=&page={i}"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
url = "http://www.izm.co.kr/contentList.asp?bigcateidx=8&subcateidx=10&view_tp=1&view_sort=1&subjectchr=&periodidx=&page=1"
response = requests.get(headers=headers, url=url)
soup = BeautifulSoup(response.text, 'html.parser')
kpop_table = soup.select('td', {'class': 'size13'})
kpop_list = [(i.text).strip().replace('\n', '') for i in kpop_table]
print(kpop_list)