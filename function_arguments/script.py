from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Defined calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'): #default argument for shipping type in case customers forget to add a type
 from_lat, from_long = from_coords #unpacking tuples into new variables
 to_lat, to_long = to_coords #unpack these too
 #now we need to get our distance
 distance = get_distance(from_lat, from_long, to_lat, to_long)
 #now to get the rate
 shipping_rate = SHIPPING_PRICES[shipping_type]
 #now we get our price
 price = distance * shipping_rate 
 return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)
#passed!

#task 9
def calculate_driver_cost(distance, *drivers): #the star means there can be multiple positional arguments passed to this, as there many be multiple drivers
  cheapest_driver = None 
  cheapest_driver_price = None 

  for driver in drivers :
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time

    #now we want to check if the current driver is the cheapest available

    #if it == none then it's probably just the first one we've checked, so set it to equal cheapest
    if cheapest_driver == None :
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver

    #update to equal the cheapest driver
    elif price_for_driver < cheapest_driver_price :
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver

      #return our cheapest one
  return cheapest_driver_price, cheapest_driver


# Test the function by calling 
test_function(calculate_driver_cost)
#passed!

def calculate_money_made(**trips) : #the double asterisk means it can take several Trip IDs as arguments

  #start counter
  total_money_made = 0 

  #iterate through each trip_id in trips dict
  for trip_id, trip in trips.items() : 
    trip_revenue = trip.cost - trip.driver.cost 
    total_money_made += trip_revenue

  return total_money_made

#now to test it
test_function(calculate_money_made)
#passed!
