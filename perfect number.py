num_str = input("Enter a number \t")
num = int(num_str)

sum_div = 0

# check factors only till num/2
for i in range(1, int(num/2) + 1):
    if (num % i == 0):
        sum_div = sum_div + i

# check if number is perfect
if (sum_div == num):
    {
        print(str(num) + " is a Perfect Number")
    }
else:
    {
        print(str(num) + " is NOT a Perfect Number")
    }