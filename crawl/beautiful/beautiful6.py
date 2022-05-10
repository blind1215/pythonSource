from bs4 import BeautifulSoup

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# select_one() : css선택자
b = soup.select_one("p.title> b")  # p태그 타이틀의(>)자식태그 (one)하나만 갖고오겠다
print(b)
print(b.string)
print(b.get_text())
print(b.text)

print()
link1 = soup.select_one("#link1")
print(link1)
print(link1.text)

print()
link2 = soup.select("p.story>a")  # 결과는 리스트로 반환
print(link2)

for li2 in link2:
    print(li2.string)

print()
link3 = soup.select(
    "p.story > a:nth-of-type(2)"
)  # 자식중에 두번째꺼 가져와 그치만 하나만가져와도 select기 때문에 리스트로 반환
print(link3)

print()
link4 = soup.select("p.story")
print(link4)

print()
for i in link4:
    temp = i.find_all("a")
    
    if temp:
        for v in temp:
            print("-----",v)
            print("-----",v.string)
    else:
        print("----",i)
        print("----",i.string)