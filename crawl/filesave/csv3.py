import csv

#csv = 콤마로 구별이 되어있는 
with open("./crawl/data/sample1.csv", "r") as f:
    # 한 행을 기준으로 dict 형태로 읽어오기
    reader = csv.DictReader(f)
    next(reader)  # 헤더명 제거

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)
        for k,v in c.items():
            print(k,v)
        print()