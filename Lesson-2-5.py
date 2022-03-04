prices = [31.3, 40.5, 20.2, 10.9, 17.1, 10, 18.7, 30.2, 40.05]
prices_2 = []
for item in prices:
    rub = int(item)
    kop = round(100*(item - rub))
    prices_2.append(f"<{rub} руб {kop:02} коп>")
print(prices_2)
print(", ".join(prices_2))
id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)
prices_3 = sorted(prices, reverse=True)
print(sorted(prices_3[:5]))
