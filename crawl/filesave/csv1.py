import csv

with open("./crawl/data/sample1.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더명 제거

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)