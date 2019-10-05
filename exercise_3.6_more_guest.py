guest_list = ['ada lovelace', 'steve w', 'eric', 'jay', 'oprah', 'arnold', 'the rock']
print(guest_list)
i=0
while i < len(guest_list):
    print('hi ' + guest_list[i] + ', bigger table is available, we are inviting more people')
    i = i + 1
guest_list.insert(0, 'jokowi')
guest_list.insert(3, 'Susi')
guest_list.append('myself')
print(guest_list)
i=0
while i < len(guest_list):
    print('hi ' + guest_list[i] + ', bigger table is available, we are inviting more people, interested?')
    i = i + 1