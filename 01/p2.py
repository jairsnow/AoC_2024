list1 = []
list2_amounts = {}

with open('raw_input.txt', 'r') as file:
    for line in file:
        (list1_element, list2_element) = line.strip().split("   ")
        list1.append(int(list1_element))
        list2_element = int(list2_element)

        if list2_element in list2_amounts:
            list2_amounts[list2_element] += 1
        else:
            list2_amounts[list2_element] = 1

list1.sort()
similarity = 0

for element in list1:

    if element in list2_amounts:
        similarity += element * list2_amounts[element]

print(similarity)