#プロジェクト
import requests
from bs4 import BeautifulSoup
#映画を検索したページ
url = "https://eiga.com/search/翔んで埼玉/"
print(url)
#requestでURLの情報を取得
url_info = requests.get(url)
CSSselector_movie1 ="#rslt-movie > ul > li:nth-of-type(1) > a"

#soupにはwebの情報が全て入っている
soup = BeautifulSoup(url_info.content, "html.parser")
#そのページの住所情報の取得(webの検証でアドレスをとってきた、おそらく統一的にされているはずだから使い回し)
soup = soup.select(CSSselector_movie1)
print(soup)
#contentsでそのリストからタイトルだけを取り出す
#htlmがリスト化されている
#今回取り出すのはURLなのでこの形で取り出す
address_movie1 = soup[0].attrs['href']

#検索した映画のページ
print("\n")
url = f"https://eiga.com{address_movie1}"
print(url)
#requestでURLの情報を取得
url_info2 = requests.get(url)
CSSselector_director ="#staff-cast > div.row > div:nth-child(1) > dl > dd:nth-child(2) > a"
#soupにはwebの情報が全て入っている
soup2 = BeautifulSoup(url_info2.content, "html.parser")
#監督の住所だけセレクタで
soup2 = soup2.select(CSSselector_director)
print(soup2)
#contentsでそのリストからURLを取り出す
address_director = soup2[0].attrs['href']
print(address_director)

#監督のページ
print("\n")
url = f"https://eiga.com{address_director}"
print(url)
#requestでURLの情報を取得
url_info2 = requests.get(url)
CSSselector_movie2 ="#u_next > div"
#soupにはwebの情報が全て入っている
soup2 = BeautifulSoup(url_info2.content, "html.parser")
#監督の住所だけセレクタで
soup2 = soup2.select(CSSselector_movie2)
print(soup2)
#contentsでそのリストからURLを取り出す
##address_directer = soup2[0].attrs['href']
##print(address_directer)





#print(soup.select("p"))
##frame=[q1,q2,q3,q4,q5]
##frame=[q1,q2,q3:"abx",q4,q5]

##url = f"https://eiga.com/search/{作品名}/"
###requestでURLの情報を取得
##r = requests.get(url)
##k="#rslt-movie > ul > li:nth-of-type(1) > a"
###soupにはwebの情報が全て入っている
##soup = BeautifulSoup(r.content, "html.parser")
###そのページの住所情報の取得
##soup=soup.select(k)
###contentsでそのリストからタイトルだけを取り出す
##print(soup[0].attrs['href'])
