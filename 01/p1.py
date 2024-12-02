list1 = []
list2 = []

with open('raw_input.txt', 'r') as file:
    for line in file:
        (list1_element, list2_element) = line.strip().split("   ")
        list1.append(int(list1_element))
        list2.append(int(list2_element))

list1.sort()
list2.sort()

distance = 0
for i, element in enumerate(list1):
    distance += abs(element - list2[i])

print(distance)