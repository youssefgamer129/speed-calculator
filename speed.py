                    #Calculate car speed
print("Hello, this program calculates the speed of a car")
#Data entry
Distance = float(input("Enter distance traveled (km) :"))

Time = float(input("Enter time taken (hrs) : "))
#Calculate speed
Speed = Distance / Time    
#Show result
print("Your speed is" , Speed , "km/h")
#Transform to miles
Speed = Speed / 3.6
#Show result
print("Your speed is" , Speed , "m/s" ) 