import requests

from bs4 import BeautifulSoup


request=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
request.raise_for_status()
data=request.text
# print(data)

soup=BeautifulSoup(data,"html.parser")
# print(soup.find_all(name="h3"))

find_all=[ i.getText() for i in soup.find_all(name="h3")]
ab=find_all[::-1]

# print(find_all)
print(ab)

#
with open(file="movies.txt",mode="w",encoding="utf-8") as file:
    for i in range(len(find_all)-1,-1,-1):
        print(find_all[i])
        file.write(f"{find_all[i]}\n")
