num=int(input("Enter your number: "))
sum=0

temp=num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")