from openpyxl import Workbook

excel_file = Workbook()
# 기본시트가 생성됨
print(excel_file.sheetnames)

excel_file.save("./crawl/data/test1.xlsx")