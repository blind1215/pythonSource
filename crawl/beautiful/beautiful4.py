from bs4 import BeautifulSoup

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

# find() : 제일 처음 만나는 요소
title = soup.find("title")
print("title {}".format(title))
print("title text {}".format(title.string))
print("title parent{}".format(title.find_parent("head")))

# h1 찾기
h1 = soup.find("h1")
print("h1 {}".format(h1))
print("h1 text {}".format(h1.string))

# p 찾기
# p1 = soup.find("p")
p1 = soup.find("p", class_="title")
print("p {}".format(p1))
print("p text {}".format(p1.string))

# 두번째 p 찾기
p2 = soup.find("p", class_="story")
print("p {}".format(p2))
print("p text {}".format(p2.get_text()))

# 세번째 p 찾기
p3 = p2.find_next_sibling()
print("p {}".format(p3))
print("p text {}".format(p3.get_text()))


#b 찾기
b=soup.find("b")
print("b : {}".format(b))
print("b text : {}".format(b.string))

# a 찾기
a1 = soup.find("a",id="link1")
print("a {}".format(a1))
print("a text {}".format(a1.string))

# 두번째 a 찾기
a2 = soup.find("a",id="link2")
print("a {}".format(a2))
print("a text {}".format(a2.string))

# 세번째 a 찾기
a3 = soup.find("a",{"class":"sister","data-io":"link3"})
print("a {}".format(a3))
print("a text {}".format(a3.string))
print("a href {}".format(a3["href"]))