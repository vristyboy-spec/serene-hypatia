clean_prices = ["10", "25", "99", "5"]

expensive_prices = [int(price) for price in clean_prices if int(price) > 20]

print(expensive_prices)