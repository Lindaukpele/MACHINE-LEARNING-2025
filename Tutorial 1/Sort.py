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