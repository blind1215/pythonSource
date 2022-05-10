import re
import openpyxl

# 엑셀 파일 로드
work_book = openpyxl.load_workbook("./crawl/data/train.xlsx")

# 현재 활성화된 시트 가져오기
sheet1 = work_book.active

# 패턴 정의
# pattern = re.compile(r" [A-Za-z]+\.")
pattern = re.compile(r" Mr\.")


for each_row in sheet1.rows:
    if len(pattern.findall(each_row[3].value))>0 : # [Bishop, MR. Dickinson H],[]
        if pattern.findall(each_row[3].value)[0].strip() ==  "Mr.":
            print(each_row[3].value)
    # print(each_row[3].value)
    # print(pattern.findall(each_row[3].value))


work_book.close()
