import pandas as pd
from bs4 import BeautifulSoup
import time
import requests

# 변수 선언
titles = []
names = []
teams = []
years = []
links = []
range_num = 0
request_headers = {
    "User-Agent": (
        'Your User-Agent')
}

# 함수 선언
def savingInfo(link):
    url_line = "https://academic.naver.com" + link

    while True:
        try:
            result = requests.get(url_line, headers=request_headers)
        except:
            print("nn")
            continue

        if result.status_code == 200:
            break
        if result.status_code == 404:
            print(url_line)
            links.append("서비스 종료")
            titles.append("서비스 종료")
            names.append("서비스 종료")
            teams.append("서비스 종료")
            years.append("서비스 종료")
            return

    soup_2 = BeautifulSoup(result.text, "lxml")
    main_box = soup_2.find("div", attrs={"container"}).find("div", attrs={"class": "main_style"})
    try:
        up_box = main_box.find("div", attrs={"class": "ui_listdetail"})
    except:
        links.append("서비스 종료")
        titles.append("서비스 종료")
        names.append("서비스 종료")
        teams.append("서비스 종료")
        years.append("서비스 종료")
        return

    elems = up_box.find("dl", attrs={"class": "ui_listdetail_list"}).find_all("dd", attrs={
        "class": "ui_listdetail_item_info"})

    tmp_names = elems[0].text.replace("[", "").replace("]", "")
    tmps = tmp_names.split(', ')

    for tmp in tmps:
        names.append(tmp)
        links.append(url_line)
        titles.append(up_box.find("h4", attrs={"id": "articleData"}).text)
        try:
            teams.append(elems[1].text)
        except:
            teams.append("none")
        try:
            tmps = elems[3].find_all("span")
            years.append(tmps[1].text)
        except:
            years.append("none")

# main
name = "민수민"
url = "https://academic.naver.com/search.naver?query=" + name + "&searchType=1&field=11&docType="
while True:
    try:
        result = requests.get(url, headers=request_headers)
    except:
        print("nn")
        continue

    if result.status_code == 200:
        break
soup = BeautifulSoup(result.text, "lxml")

navi = soup.find("div", attrs={"class": "tabnavi_area"}).find("li", attrs={"class": "ui_tabnavi_item"})
thenum = navi.find("span", attrs={"class": "ui_tabnavi_num"}).text
thenum_int = int(thenum.replace(',', ''))

if thenum_int % 10 == 0:
    range_num = int(thenum_int / 10)
else:
    range_num = int(thenum_int / 10) + 1

print(range_num)

# for i in range(1, 2):
for i in range(1, range_num + 1):
    url_num = url + "&page=" + str(i)

    while True:
        try:
            result = requests.get(url_num, headers=request_headers)
        except:
            print("nn")
            continue

        if result.status_code == 200:
            break
    soup = BeautifulSoup(result.text, "lxml")
    lines = soup.find("div", attrs={"class": "ui_listing_area"}).find("ul", attrs={"class": "ui_listing_list"}).find_all("li", attrs={"class": "ui_listing_item _list_item type2"})

    for line in lines:
        link = line.find("h4").a["href"]
        savingInfo(link)
        time.sleep(0.3)

# 최종 데이터 추출
papers = pd.DataFrame(
    {
        '논문 제목': titles,
        '저자': names,
        '소속': teams,
        '발행년도': years,
        'url': links
    })

papers.to_excel("D:/" + name + "_검색결과.xlsx", header=True, index=False)
