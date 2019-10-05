guest_list = ['ada lovelace', 'steve w', 'eric', 'jay', 'oprah', 'arnold', 'the rock']

i=0
while i < len(guest_list):
    i = i + 1

guest_list.insert(0, 'jokowi')
guest_list.insert(3, 'Susi')
guest_list.append('myself')
#using the data from exercise 3.6

i=0
while i < len(guest_list):
    print ("Hello " + guest_list [i] + " i can only invite 2 person, i am sorry")
    i = i + 1

print("\n\n")
#i am making this prettier when it is printed out

removed_guest = guest_list.pop(0)
print (removed_guest)
print('i am sorry you are not invited, ' + removed_guest + ".")

removed_guest_1 = guest_list.pop(1)
print (removed_guest_1)
print('i am sorry you are not invited, ' + removed_guest_1 + ".")

removed_guest_2 = guest_list.pop(2)
print (removed_guest_2)
print('i am sorry you are not invited, ' + removed_guest_2 + ".")


removed_guest_3 = guest_list.pop(3)
print (removed_guest_3)
print('i am sorry you are not invited, ' + removed_guest_3 + ".")


removed_guest_4 = guest_list.pop(4)
print (removed_guest_4)
print('i am sorry you are not invited, ' + removed_guest_4 + ".")

#if you can see the jump on .pop(), it skips the next name after the other (???)

removed_guest_5 = guest_list.pop(-1)
print (removed_guest_5)
print('i am sorry you are not invited, ' + removed_guest_5 + ".")

removed_guest_6 = guest_list.pop(-2)
print (removed_guest_6)
print('i am sorry you are not invited, ' + removed_guest_6 + ".")

removed_guest_7 = guest_list.pop(-3)
print (removed_guest_7)
print('i am sorry you are not invited, ' + removed_guest_7 + ".")

print(guest_list)
print("hi " + guest_list[0] + " you are still invited!")
print("hi " + guest_list[1] + " you are still invited!")

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)

