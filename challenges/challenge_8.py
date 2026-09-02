raw_prices = ["$10", "$25", "$99", "$5"]

clean_prices = [price.replace("$", "") for price in raw_prices]

print(clean_prices)