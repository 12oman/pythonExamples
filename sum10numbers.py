# take 10 numbers as input from user and find their sum and average

# makes more sense to generalise it to any number of numbers :)
# define a function which takes n number of int as input
def sum_avg(n):
    # take n numbers as input from user
    num_list = []
    for i in range(n):
        num = int(input("Enter a number: "))
        num_list.append(num)
    # find the sum of the numbers
    sum = 0
    for j in range(n):
        sum = sum + num_list[j]
    # find the average of the numbers
    avg = sum/n
    # print the sum and average
    print("The sum of the numbers is:", sum)
    print("The average of the numbers is:", avg)


sum_avg(10)
