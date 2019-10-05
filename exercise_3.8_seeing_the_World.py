wish_list = ["iceland", "alaska", "kenya", "artic", "galapagos"]

#printing original list
print(wish_list)
print("\n")

#printing sorted wish list (temporarily)
sorted(wish_list)
print (sorted(wish_list))
print ("\n")
print(wish_list) #still an original list

#printing sorted wish list (temporarily) reverse
wish_list = ["iceland", "alaska", "kenya", "artic", "galapagos"]
print(wish_list)
wish_list.reverse()
print("\n")
print(wish_list)
#reverse to original order
wish_list.reverse()
print("\n")
print(wish_list)

#sort()
wish_list = ["iceland", "alaska", "kenya", "artic", "galapagos"]
wish_list.sort()
print("\n")
print(wish_list)


#sort() reverse
wish_list = ["iceland", "alaska", "kenya", "artic", "galapagos"]
wish_list.sort(reverse = True)
print("\n")
print(wish_list)