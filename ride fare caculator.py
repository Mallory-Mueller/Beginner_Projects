ride_type= "black"
credits=4

ride_price=0
final_price=0

if ride_type=="ridex":
    ride_price=23.5
elif ride_type=="rideblack":
    ride_price=32
else: ride_price=17.5

print("Ride price:")
print (ride_price)

if credits > 0:
    final_price= ride_price-credits

print ("Final price:")
print (final_price)
