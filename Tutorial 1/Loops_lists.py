
# print(len(number_list)) #use to print the number of length
# print(sum(number_list)) # returns the sum of everything on the list
# print(number_list[0])
# print(number_list.append)
# print(number_list.remove())
#2 types of loop e.f For loops used when we are going to loop a limited number of time. i is for iterative and range 
number_list = [113431, 213, -4, -126, 8, 43, 4231, 1364, 96, 0, 5314, -4532.3, -513, -52]
for i in range(len(number_list), 1): #OR 0, 7, 1 to call range from 0 to 7 with 1 increment
    print(number_list[i]) 
for number in number_list: #when you need all the numbers without the position. for values
    print(number)


def Average (num_list):
    sum = 0
    for number in num_list:
        sum = sum + number
    average = sum / len(num_list)
    return average

number_list = [113431, 213, -4, -126, 8, 43, 4231, 1364, 96, 0, 5314, -4532.3, -513, -52]
print(Average(number_list))


def Maximum (num_list):
    max = 0 #OR use num-list[0] just to capture values less than zero in situation when there is no ero value
    for number in num_list:
        if max < number:
            max = number
    return max

number_list = [113431, 213, -4, -126, 8, 43, 4231, 1364, 96, 0, 5314, -4532.3, -513, -52]
print(Maximum(number_list))

#Assignment
def Swap(first, second):
    temp = second
    second = first
    first = temp
    return first, second 

def Sort(num_list):
    for i in range(len(num_list)): #OR IF YOU WANT IT TO LOOP THE FIRST 5 numbers, you can use  for i in range(5):
        for j in range(i, len(num_list)):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = Swap(num_list[i], num_list[j])
    return num_list

number_list = [1, 46, 13431, 213, -4, -126, 8, 43, 4231, 1364, 96, 0, 5314, -4532.3, -513, -52]
print(Sort(number_list))

#while loops
#ccccc
#hhhhhh