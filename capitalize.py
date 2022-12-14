input_String = 'chris alan'
output_String = ''
listName = input_String.split(' ')# Split by spaces and makes a list of words
listName = [name.capitalize() for name in listName] # apply capitalize func for every name in the list

for i in range(len(listName)-1): # adding space items between names in list 
    listName.insert(2*i+1, ' ') 

output_String = output_String.join(listName)# list to string

print(output_String)