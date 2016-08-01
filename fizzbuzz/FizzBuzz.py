n = raw_input("Enter any integer ")
n = int(n)
print("Fizzbuzz counting up to " + str(n) + " ")
count = 0
while count < n:
    if count - (count / 3 * 3) == 0 and count - (count / 5 * 5) == 0:
        print("FizzBuzz")
    elif count - (count / 3 * 3) == 0: 
        print("Fizz")
    elif count - (count / 5 * 5) == 0:
        print("Buzz")
    else:
        print(count)
    count = count + 1y
