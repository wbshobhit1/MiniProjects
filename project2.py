"""""
Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples.
 These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.


Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not.
If mn=mx, show that this is not a range, and mn
 is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20
"""
while True:
    try:
        n = int(input("Enter the number of apples Harry had :"))
        mn = int(input("Minimum range of the apples req that Harry asked for :"))
        mx = int(input("Maximum range of the apples req that Harry asked for :"))

        if mn == mx:
            print("This is not in a range")

        if mn > mx:
            print("Worng range bound")

        for i in range(mn, mx + 1):
            if n % i == 0:
                print(f"{i} is a divisor of {n}")
            else:
                print(f"{i} is not a divisor of {n}")

        print("Press Q to quit OR C to continue")
        opt1 = ""
        while (opt1 != "q" and opt1 != "c") or (opt1 != "q" and opt1 != "c"):
            opt1 = input()
            if opt1 == "c" or "C":
                continue
            elif opt1 == "q" or "Q":
                exit()



    except:
        print("Invalid input, Try again")

