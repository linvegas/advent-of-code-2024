first_list = [3, 4, 2, 1, 3, 3]
second_list = [4, 3, 5, 3, 9, 3]
# first_list = [1, 9, 2, 2, 4, 6]
# second_list = [2, 7, 5, 6, 8, 3]

first_list.sort()
second_list.sort()

total_distance = 0

for i, _ in enumerate(first_list):
    if first_list[i] > second_list[i]:
        total_distance += first_list[i] - second_list[i]
    else:
        total_distance += second_list[i] - first_list[i]

print(total_distance)
