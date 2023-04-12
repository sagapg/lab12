numbers = []
print('Enter 10 number =\n')
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

even_no = [num for num in numbers if num % 2 == 0]

print("The list of all number is= ", numbers)
print("The even numbers are= ", even_no)

sum_of_even = sum(even_no)
print("The sum of all even numbers is= ", sum_of_even