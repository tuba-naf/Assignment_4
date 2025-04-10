def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)
            
#For example, if num = 6:
#The loop will check i = 0, 1, 2, 3, 4, 5, and for each value of i, curr_divisor = i + 1 will result in checking 1, 2, 3, 4, 5, 6.

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


if __name__ == '__main__':
    main()