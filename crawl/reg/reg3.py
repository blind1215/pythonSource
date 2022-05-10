import re

# search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 리턴
# match(): 문자열 처음부터 정규식과 매친되는 패턴을 찾아서 리턴
# sub() : 패턴을 찾고 바꾸기
# findall() : 정규 표현식과 매칭되는 모든 문자열을 리스트로 리턴
# split() : 찾은 정규표현식 패턴 문자열을 기준으로 문자열 분리

pattern = re.compile("[a-z]+")
print("match(): ", pattern.match("Dave"))  # None # 처음매칭이 안되어서 뒤를 아예 보지도 않음
print(
    "search(): ", pattern.search("Dave")
)  # <re.Match object; span=(1, 4), match='ave'>

print()
data = "DDA D1A DDA DA"
# re.sub(패턴, 바꿀문자열, 원본문자열)
print(re.sub("D.A", "DAVE", data))  # DAVE DAVE DAVE DA

print()
print(pattern.findall("Game of Life in Python"))  # ['ame', 'of', 'ife', 'in', 'ython']
pattern = re.compile("[A-Za-z]+")
print(
    pattern.findall("Game of Life in Python")
)  # ['Game', 'of', 'Life', 'in', 'Python']


pattern = re.compile("[a-z]+")
findalled = pattern.findall("GAME")
if len(findalled) > 0:
    print("정규표현식에 맞는 문자열 존재")
else:
    print("정규표현식에 맞는 문자열 존재하지 않음")


print()
pattern = re.compile(":")
print(pattern.split("java:python"))