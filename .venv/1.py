total_amount = int(input())
amount_of_silver = 96.0
amount_of_gold = amount_of_silver/16
price_of_silver = 48
price_of_gold = (total_amount - amount_of_silver*price_of_silver)/amount_of_gold
print(int(price_of_gold))