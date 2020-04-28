# Code for Parsing
import trainline
import csv
#import openpyxl

results = trainline.search(
	departure_station="Toulouse",
	arrival_station="Bordeaux",
	from_date="15/06/2020 08:00",
	to_date="17/06/2020 21:00")
# x = results.csv()
# data = x.split("\n")
# data = [i.split(";") for i in data]
# #print(len(data),data)
# op = []
# for i in data:
#    print(str(j)+"\t" for j in i)
def find_train(dept_stat,arr_stat,from_date,to_date):
    results = trainline.search(
	departure_station=dept_stat,
	arrival_station=arr_stat,
	from_date=from_date,
	to_date=to_date)
    x = results.csv()
    data = x.split("\n")
    data = [i.split(";") for i in data]
    return str(data)

def cheapest_ticket(dept_stat,arr_stat,from_date,to_date):
    results = trainline.search(
    departure_station=dept_stat,
    arrival_station=arr_stat,
    from_date=from_date,
    to_date=to_date)
    x = results.csv()
    data = x.split("\n")
    data = [i.split(";") for i in data]
    head = data.pop(0)
    data.pop(-1)
    prices = []
    for i in data:                      #To make all the euro values integer
        price = i[4].split(",")
        i[4] = int(price[0])            #Splitted the price into two, taken first part
        prices.append(i[4])
    min_prices = []
    min_val = min(prices)
    for i in range(0,len(prices)):
        if min_val == prices[i]:
            min_prices.append(i)

    print(min_prices) # Giving me the array locations ofthe minimum prices found

    cheapest_bookings = []
    for i in min_prices:
            cheapest_bookings.append(data[i])
    cheapest_bookings.insert(0,head)
    return str(cheapest_bookings)