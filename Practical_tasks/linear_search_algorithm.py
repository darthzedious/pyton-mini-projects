def binary_search(input_list, target):
    left = 0
    right = len(input_list) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = input_list[middle_index]

        if middle_element == target:
            return middle_index
        if target > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


my_list = sorted([int(number) for number in input().split(", ")])
our_target = int(input())
print(f"When the list is sorted correctly the target number is at index: {binary_search(my_list, our_target)}")

'#For this algorithm to work properly, the given list must be sorted from lower to higher' \
  ', that is why we use the sorted function to ensure ourselves.'
'#We insert a list and a target, ' \
  'then we call the function to print the index where lays the target we are searching for.'
