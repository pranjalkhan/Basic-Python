a=int(input("Enter a number: "))

if a>=18:
    print("You are eligible to vote.")

elif a<18:
    print("You are not eligible to vote.")

elif a==18:
    print("You are eligible to vote but you need to register first.")

else:
    print("Invalid input.")

    