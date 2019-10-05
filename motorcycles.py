motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

#change the value of index 0
motorcycles [0] = 'ducati'
print(motorcycles)

#adding element to a list
#1. Appending element to end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#append() method makes it easy to build lists dynamiccaly
motorcycles = []
motorcycles.append('honda1')
motorcycles.append('yamaha2')
motorcycles.append('suzuki3')
print(motorcycles)

#inserting element into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0 , 'ducati') #0 is the position of where we want to insert the element
print(motorcycles)

#Removing element from a list
#Removing an item using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles [0] #honda which at index 0 is gone, because we indicate that we want to delete index 0,
#we can delete any element with any index position
print (motorcycles)

#removing an element using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
popped_motorcycle = motorcycles.pop() #we pop a value from the list and store that value in the variable
print(motorcycles) # has been removed from the list
print(popped_motorcycle)
#another sample
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle i owned was a " + last_owned.title() + ".")

#Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('the first motorcycle i owned was a ' + first_owned.title() + '.')
print(motorcycles)

#REMEMBER : each time use pop(), the item you work with is no longer stored in the list
#if you want to use an item as you remove it, use the pop()method

#Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

#sampe 2
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove (too_expensive)
print(motorcycles)
print('\n' + too_expensive.title() + ' is too expensive for me!')

