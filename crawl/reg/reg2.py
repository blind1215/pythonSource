import re


print("*** {n} 사용법 ***")
pattern = re.compile("AD{2}A")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # <re.Match object; span=(0, 4), match='ADDA'>
print(pattern.search("ADDDDA"))  # None

print("*** {n,m} 사용법 ***")
pattern = re.compile("AD{2,6}A")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # <re.Match object; span=(0, 4), match='ADDA'>
print(pattern.search("ADDDDA"))  # <re.Match object; span=(0, 6), match='ADDDDA'>

print("\n*** [] 사용법 : 대괄호안에있는것중하나 ***")
pattern = re.compile("[abcdefgABCDEFG]")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))  # None
print()
pattern = re.compile("[a-g]")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))
print()
pattern = re.compile("[a-zA-Z]")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))  # <re.Match object; span=(0, 1), match='z'>
print()
pattern = re.compile("[a-zA-Z0-9]")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 1), match='Z'>
print(pattern.search("1234"))  # <re.Match object; span=(0, 1), match='1'>
print()
pattern = re.compile("[a-zA-Z0-9]+")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 5), match='a1234'>
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 5), match='Z1234'>
print(pattern.search("1234"))  # <re.Match object; span=(0, 4), match='1234'>
print()
pattern = re.compile("[^a-zA-Z0-9]") # ^ 제외하고 란뜻
print(pattern.search("a1234"))  # None
print(pattern.search("Z1234"))  # None
print(pattern.search("1234"))  # None
print(pattern.search("!@#$%^&")) # <re.Match object; span=(0, 1), match='!'>
print()
pattern = re.compile("[가-힣]")
print(pattern.search("안녕하세요")) # <re.Match object; span=(0, 1), match='안'>

