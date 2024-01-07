def collatz(number):
    odd_or_even = number % 2
    
    if odd_or_even == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


user_input = int(input("Enter a number: "))
while user_input != 1:
    user_input = collatz(user_input)
