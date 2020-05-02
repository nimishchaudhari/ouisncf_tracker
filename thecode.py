# Code for Parsing
import trainline
import csv

class data:
    data = []

data_obj = data()

results = 0
def find_train(dept_stat,arr_stat,from_date,to_date):
    results = trainline.search(
	departure_station=dept_stat,
	arrival_station=arr_stat,
	from_date=from_date,
	to_date=to_date)
    x = results.csv()
    data = x.split("\n")
    data = [i.split(";") for i in data]
    data_obj.data = data
    x=""
    for i in data:
        x = x + str(i) + '\n'
    return str(x)

def cheapest_ticket(dept_stat,arr_stat,from_date,to_date):
    head = data_obj.data.pop(0)
    data_obj.data.pop(-1)
    data = data_obj.data
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

    #print(min_prices) # Giving me the array locations ofthe minimum prices found

    cheapest_bookings = []
    for i in min_prices:
            cheapest_bookings.append(data[i])
    cheapest_bookings.insert(0,head)
    def print_op(list):
        x = ""
        for i in list:
            x = x + str(i) + '\n'
        return x
    return str(print_op(cheapest_bookings))


from sys import argv
if len(argv)!=5:
    print("Expected 4 arguments,got less or more!")
    print("Cheapest Tickets:")
    print(cheapest_ticket(
        "Bruxelles","Paris",
        "15/06/2020 10:00",
        "20/06/2020 08:00"
    ))
else:
    print(" Finding travel itineraries from {} to {} please wait".format(argv[1],argv[2]))
    print(find_train(argv[1],argv[2],argv[3],argv[4]))
    print(" Cheapest ones are here: ")
    print(cheapest_ticket(argv[1],argv[2],argv[3],argv[4]))


    #EG:
    #   Toulouse Perpignan "01/07/2020 10:00" "10/07/2020 15:00"