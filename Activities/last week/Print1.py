sum = 0
for i in range(1, 6):
    sum += i
print(sum)
print("The sum of numbers from 1 to 5 is:", sum)

num = int(input("Enter a number to check if it's a prime number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")

# HelloWorld("Print")

# function countDown(number) {
#     console.log(number);
#     if (number > 0) {
#         countDown(number - 1);
#     }
#     }
# countDown(5);