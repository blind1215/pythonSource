from bs4 import BeautifulSoup

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())


# -------------------------------------------------------------------------------------
# title 태그
print("title>>{}".format(soup.title))
print("title text >>{}".format(soup.title.string))
print("title parent>> {}".format(soup.title.parent))

# -------------------------------------------------------------------------------------
# h1 태그
print("h1>>{}".format(soup.h1))
print("h1 text >>{}".format(soup.h1.string))

# -------------------------------------------------------------------------------------
# h2 태그
print("h2>>{}".format(soup.h2))
print("h2 text >>{}".format(soup.h2.string))

# -------------------------------------------------------------------------------------
# 첫번째 p 태그
p1 = soup.p
print("첫번째 p >>{}".format(p1))
print("p text >>{}".format(p1.string))
print("p class name >>{}".format(p1["class"]))
# -------------------------------------------------------------------------------------
# 두번째 p 태그
p2 = p1.find_next_sibling("p")
print("두번째 p >>{}".format(p2))
print("p text >>{}".format(p2.get_text()))
print("p class name >>{}".format(p2["class"]))
# -------------------------------------------------------------------------------------
# 세번째 p 태그
p3 = p2.find_next_sibling("p")
print("세번째 p >>{}".format(p3))
print("p text >>{}".format(p3.get_text()))
print("p class name >>{}".format(p3["class"]))
# -------------------------------------------------------------------------------------
# b 태그
print("b태그 >>{}".format(soup.b))
print("b태그 text>>{}".format(soup.b.string))
# -------------------------------------------------------------------------------------
# 첫번째 a태그 - 태그, 문자
a1 = soup.a
print("첫번째 a태그 >> {}".format(a1))
print("첫번째 a text >>{}".format(a1.string))

# -------------------------------------------------------------------------------------
# 두번째 a태그
a2 = a1.find_next_sibling("a")
print("두번째 a태그 >>{}".format(a2))
print("두번째 a text >>{}".format(a2.string))
# -------------------------------------------------------------------------------------
# 세번째 a태그
a3 = a2.find_next_sibling("a")
print("세번째 a태그 >>{}".format(a3))
print("세번째a text >>{}".format(a3.string))