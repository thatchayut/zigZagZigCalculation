# Deal with input
input_list = []
check_end_input = False
input_command = None

while (check_end_input is False):
    check_valid_input = False
    while (check_valid_input is False):

        input_string = input(" Enter 2 value separated by white space : ")

        if (input_string == "Zig-Zag") or (input_string == "Zag-Zig"):
            input_command = input_string
            check_valid_input = True
            check_end_input = True
        else:
            input_values = input_string.split(" ")
        
            # check if the number of input value is exactly 2
            if (len(input_values) is 2):
                check_valid_input = True
                input_list.append(input_values)
            else:
                print(" # INVALID INPUT : The number of input values exceed 2.")
print(input_values)
# Calculation Process
print(" # PROCESS : Calculation")
print(" INPUT =>")
for value_pair in input_list:
    print(value_pair[0], end = " ")
    print(value_pair[1], end = " ")
    print()

list_for_find_min = []
list_for_find_max = []
minimum = None
maximum = None

if (input_command == "Zag-Zig"):
    number_of_value_pair = len(input_list)

    for value_pair_index in range(0, number_of_value_pair):
        x = int(input_list[value_pair_index][0])
        y = int(input_list[value_pair_index][1])

        if (value_pair_index % 2 == 0):
            list_for_find_min.append(y)
            list_for_find_max.append(x)
        else:
            list_for_find_min.append(x)
            list_for_find_max.append(y)
else:
    number_of_value_pair = len(input_list)

    for value_pair_index in range(0, number_of_value_pair):
        x = int(input_list[value_pair_index][0])
        y = int(input_list[value_pair_index][1])

        if (value_pair_index % 2 == 0):
            list_for_find_max.append(y)
            list_for_find_min.append(x)
        else:
            list_for_find_max.append(x)
            list_for_find_min.append(y)


print(" List used to find minimum : " + str(list_for_find_min))
print(" List used to find maximum : " + str(list_for_find_max))

minimum = min(list_for_find_min)
maximum = max(list_for_find_max)

print(" # RESULE : ")
print(str(minimum) + " " + str(maximum))


