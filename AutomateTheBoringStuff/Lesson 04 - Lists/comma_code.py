def join_list(input_list):
    if not input_list:
        return ""
    
    output_string = ""
    if len(input_list) == 1:
        output_string = input_list[0]
    elif len(input_list) == 2:
        output_string = input_list[0] + " and " + input_list[1]
    else:
        output_string = ""
        for i in range(len(input_list)):
            if i == len(input_list) - 1:
                output_string += "and " + input_list[i]
            else:
                output_string += input_list[i] + ", "
    
    return output_string


if __name__ == '__main__':
    print(join_list([]))
    print(join_list(['apples']))
    print(join_list(['apples', 'bananas']))
    print(join_list(['apples', 'bananas', 'tofu']))
    print(join_list(['apples', 'bananas', 'tofu', 'cats']))
