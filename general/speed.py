                     #Calculate car speed
print("Hello, this program calculates car speed")
#Data entry
Distance = float(input("Enter distance traveled (km) :"))
hours= float(input("Enter hours :") )
minutes = float(input("Enter minutes :"))
seconds = float(input("Enter seconds :"))
#Convert time to hours
Time = hours + minutes / 60 + seconds / 3600
#Calculate speed
Speed = Distance / Time    
#Show result
print("Your speed is" , Speed , "km/h")
#Convert to miles
Speed = Speed / 3.6
#Show result
print("Your speed is" , Speed , "m/s" ) 
