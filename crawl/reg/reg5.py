import re
import openpyxl

# 원본 문자열 "python VS java" 일때 VS로 문자열 앞뒤 분리하기
pattern = re.compile(" [A-Z]{2} ")
print(pattern.split("python VS java"))


# 주민번호의 - 기호를 * 로 바꿔서 출력하기
# 801210-1011323
print(re.sub("-", "*", "801210-1011323"))
# pattern = re.compile("-")
# print(pattern.sub("*", "801210-1011323"))


# train.xlsx 를 읽어서 주민번호 뒷자리를 ****** 로 바꾸어 출력하기
# 엑셀파일 로드
work_book = openpyxl.load_workbook("./crawl/data/data_kr.xlsx")

# 현재 활성화된 시트 가져오기
sheet1 = work_book.active

pattern = re.compile("[0-9]{7}")

for each_row in sheet1.rows:
    print(re.sub(pattern, "*******", each_row[1].value))

work_book.close()