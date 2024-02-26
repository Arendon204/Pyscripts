hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0 

for i in prices:
  total_price += i  
  print(i)

size = len(prices)
print(size)

average_price = total_price / 8

print("average haircut price", average_price)

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0


for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  
  print(i)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices))]

print(cuts_under_30)
  
print("Total Revenue", total_revenue)

average_daily_revenue = total_revenue / 7

print(average_daily_revenue)



