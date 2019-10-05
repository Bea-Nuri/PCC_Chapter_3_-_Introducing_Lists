cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort() #short list by change the order of the list to store them alphabeticaly PERMANENTLY (A-Z)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse = True) #short list in reverse order (Z-A)
print(cars)

#shorting a list temporarily with the shorted() function
#this function let you display your list in a particular order but doesn't affect the actual order of the list
cars = ["bmw", "audi", "toyota", "subaru"]
print ("Here is the original list:")
print (cars )
print ("Here is the shorted list:")
print (sorted(cars))
print ("Here is the original list again:")
print (cars)

#printing a list in a reverse order --> change order of list permanently
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)

#finding the length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
len(cars)
print (len(cars))
