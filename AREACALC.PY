print("*****AREA CALCULATOR******")
while True:
    print("""press 1 to get the area of square
          press 2 to get the area of rectangle
          press 3 to get the area of circle
          press 4 to get the area of triangle""")
        
    print("----------------------------------------------")
    
    choice = int(input("ENTER YOUR CHOICE FROM 1-4: "))

    if choice == 1:
        while True:
            side = float(input("ENTER THE LENGTH OF ONE SIDE: "))
            area = side**2
            print("the area of square is ",area)

            repeat = input("Do you want to continue square area calculation ?(yes/no): ").lower()
            if repeat == "no":
                print("--------------------------------------------------")
                break

    elif choice == 2:
        while True:
            radius = float(input("ENTER THE RADIUS OF THE CIRCLE: "))
            area =(22/7) * radius **2
            print("THE AREA OF THE CIRCLE IS : ",area)

            repeat = input("Do you want to continue circle area calculation?(yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break
    
    elif choice == 3:
        while True:
            length = float(input("ENTER THE LENGTH OF THE RECTANGLE: "))
            breadth = float(input("ENTER THE BREADTH OF THE RECTANGLE: "))
            area = length * breadth
            print("THE AREA OF THE RECTANGLE IS:",area)

            repeat = input("Do you want to continue rectangle area calculation?(yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break

    elif choice == 4 :
        while True:
            base = float(input("ENTER THE BASE OF THE TRIANGLE :"))
            height = float(input("ENTER THE HEIGHT OF THE TRIANGLE: "))
            area = 0.5 * base * height
            print("THE AREA OF THE TRIANGLE IS:",area)

            repeat = input("Do you want to continue triangle area calculation?(yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break
    else:
        print("Invalid Choice ! Please select between 1-4")
        print("--------------------------------------------------")

    repeat_menu = input("Do you want to display the menu again?(yes/no): ").lower()
    if repeat_menu == "no":
        print("THANK YOU FOR USING AREA CALCULATOR! ")
        break

    print("-------------Calculation end here--------------------")
    





        