#Create a function to that will return the neighbors of an item in that list. The function can only take two arguments
#The item to check 
#The list it is in
#Ex: ([1 2 3 4], 1)=>[2 3]

def sumNeighbors(list):
    new_list = []
    new_list.append(list[0] + list[1])
    x = 1
    while x < len(list) - 1:
        new_list.append(list[x - 1] + list[x] + list[x + 1])
        x += 1
        new_list.append(list[x - 1] + list[x])
        return new_list

text = raw_input("Enter an integer(period to end): ")
list = []
while text != '.':
    textInt = int(text)
    list.append(textInt)
    text = raw_input("Enter an integer (period to end): ")

print ("List:", list)
print ("sum", sumNeighbors(list))