from bs4 import BeautifulSoup

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# find_all() : 결과를 무조건 리스트로 반환
# a=soup.find_all("a")
a = soup.find_all("a", limit=2)
print(a)

link = soup.find_all("a", class_="sister")
print(link)

print()
# string : 텍스트 노드 값을 지정해서 가져올 수 있음
link1 = soup.find_all("a", string=["Elsie"])
print(link1)

print()
link2 = soup.find_all("a", string=["Elsie", "Tillie"])
print(link2)