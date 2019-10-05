guest_list = ['ada lovelace', 'steve w', 'eric', 'jay', 'oprah', 'arnold', 'the rock']
print(guest_list)
guest_who_cant_make_it =guest_list[0]
guest_list[0] = 'Matthew'
print(guest_list)
print ("There is one guest who can't make it, her name is " + guest_who_cant_make_it + ".")
i=0
while i < len(guest_list):
    print('hi ' + guest_list[i] + ', you are invited to my amazing dinner')
    i = i + 1
