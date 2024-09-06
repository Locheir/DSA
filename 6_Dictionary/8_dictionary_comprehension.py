# Dictionary Comprehension : 
import random
city_names = ['Pune','Mumbai','Amravati','Nagpur','Akurdi']

city_temps = {city:random.randint(20, 30) for city in city_names}
print(city_temps)

# Dictionary Comprehension using if condition :
new_city_temps = {key:value for key,value in city_temps.items() if value > 25}
print(new_city_temps)