num = input("Number please:")

if "." in num:
        num = input("Whole number please:")

if num.isalnum():
        num = input("Whole number please")

if int(num) % 2==0:
        print("even")
else:
        print("odd")
