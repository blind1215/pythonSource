import csv

#csv = 콤마로 구별이 되어있는 
with open("./crawl/data/sample2.csv", "r") as f:
    reader = csv.reader(f,delimiter="|")
    next(reader)  # 헤더명 제거

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)