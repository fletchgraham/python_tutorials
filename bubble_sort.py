# define a bubble sort function that takes a list as an argument


def bubble_sort(a_list):
    # set a counter equal to the length of the list
    counter = len(a_list) - 1
    # while counter is greater than 1 the outer loop will keep going
    while counter > 1:
        # during each outer loop
        # for each index in a range of counter
        for i in range(counter):
            # if the value at that index is greater than the value at index+1
            if a_list[i] > a_list[i+1]:
                # then we switch them
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
        counter -= 1
    # return the newly sorted list
    return a_list

my_list = [1, 5, 10, 13, 6, 6, 8, 31, 32, 3]
my_other_list = [100, 90, 80, 21, 43, 2, 5, 7, 8]

print(bubble_sort(my_list))

print(bubble_sort(my_other_list))
