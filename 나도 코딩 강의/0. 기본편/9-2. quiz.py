class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")
        
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses = []
houses.append(h1)
houses.append(h2)
houses.append(h3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()