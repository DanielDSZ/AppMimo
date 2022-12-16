ride_type = 'fast'
credits = 4

ride_price = 0
final_prince = 0

if ride_type == 'Dooberx':
    ride_price = 20.5
elif ride_type == 'Black':
    ride_price = 37.9
else:
    ride_price = 18.7

print('Ride price:')
print(ride_price)

if credits > 0:
    final_prince = ride_price - credits
    