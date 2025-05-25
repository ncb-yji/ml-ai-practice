# /python/02_sales_analysis.py
from collections import Counter, namedtuple, defaultdict

# 1. 주어진 데이터셋에서 튜플을 활용하여 다음 분석을 수행하세요
# 데이터: (연도, 분기, 제품, 가격, 판매량, 지역)
sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 120, "인천"),
    (2020, 3, "스마트폰", 850, 300, "서울"),
    (2020, 4, "노트북", 1300, 130, "부산"),
    (2020, 4, "스마트폰", 850, 350, "서울"),
    (2021, 1, "노트북", 1400, 110, "대구"),
    (2021, 1, "스마트폰", 900, 200, "서울"),
    (2021, 2, "노트북", 1400, 160, "인천"),
    (2021, 2, "스마트폰", 900, 270, "부산"),
    (2021, 3, "노트북", 1500, 130, "서울"),
    (2021, 3, "스마트폰", 950, 320, "대구"),
    (2021, 4, "노트북", 1500, 140, "부산"),
    (2021, 4, "스마트폰", 950, 370, "서울"),
]

Sale = namedtuple("Sale", ["year", "quarter", "product", "price", "sales", "region"])
sales_data_named = [Sale(*row) for row in sales_data]

# 연도별 판매량 계산
sales_by_year = defaultdict(int)
print("---------- 연도별 판매량 계산 ----------")
for s in sales_data_named:
    sales_by_year[s.year] += s.sales
for year, total_sales in sales_by_year.items():
    print(f"{year}년 총 판매량 합계 : {total_sales}")

# 제품별 평균 가격 계산
price_sum = defaultdict(int)
price_count = defaultdict(int)
for s in sales_data_named :
    price_sum[s.product] += s.price
    price_count[s.product] += 1
for product in price_sum:
    # print(f"제품: {product}, 평균 가격 : {price}")
    average = price_sum[product] / price_count[product]
    print(f"제품 : {product}, 평균 가격: {average:.2f}")

# 최대 판매 지역 찾기
counter = Counter(s.region for s in sales_data_named)
the_highest_region, sales_volume = counter.most_common(1)[0]
print("---------- 최대 판매 지역 ----------")
print(f"최대 판매 지역: {the_highest_region}, 판매량: {sales_volume}")

# 분기별 매출 분석
sales_by_quarter = defaultdict(int)
for s in sales_data_named:
    sales_by_quarter[s.quarter] += s.sales * s.price
print("---------- 분기별 매출 분석 ----------")
for quarter, total_sales in sales_by_quarter.items():
    print(f"{quarter}분기 매출 합계 : {total_sales}")