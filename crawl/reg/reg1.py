# 정규 표현식
import re

# 패턴 정의
pattern = re.compile("D.A")

# search()
result = pattern.search("DAA")
print(result)  # <re.Match object; span=(0, 3), match='DAA'>

result = pattern.search("D1A")
print(result)  # <re.Match object; span=(0, 3), match='D1A'>

result = pattern.search("D00A")
print(result)  # None

result = pattern.search("DA")
print(result)  # None

result = pattern.search("d0A")
print(result)  # None

result = pattern.search("d0A D1A 0999")
print(result)  # <re.Match object; span=(4, 7), match='D1A'>

print("*** ? 의미 : 최소 0~1 ***")
pattern = re.compile("D?A")

print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(27, 29), match='DA'>

print("*** * 의미 : 최소 0~무한대 ***")
pattern = re.compile("D*A")

print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(27, 29), match='DA'>

print()
pattern = re.compile("AD*A")
print(pattern.search("AA"))  # <re.Match object; span=(0, 2), match='AA'>
print(pattern.search("ADA"))  # <re.Match object; span=(0, 3), match='ADA'>
print(
    pattern.search("ADDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(0, 19), match='ADDDDDDDDDDDDDDDDDA'>


print("*** + 의미 : 최소 1~무한대 ***")
pattern = re.compile("D+A")

print(pattern.search("A"))  # None
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA")
)  #  <re.Match object; span=(0, 29), match='DDDDDDDDDDDDDDDDDDDDDDDDDDDDA'>
