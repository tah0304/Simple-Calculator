#Build a calculator where user can input - and + signs and do the operation


def calculator():
    while True:
        operation = input("1. Addition\n2. Subtraction\n3. Exit")

        if operation == "1":
            calculation = input("Enter your calculation: ")
            numbers = calculation.split("+")
            first_number = int(str(numbers[0]))
            second_number = int(str(numbers[1]))
            result = first_number + second_number

            if len(numbers) <= 2:
                print(result)

            elif len(numbers) > 2:
                i = 2
                while i < len(numbers):
                    third_number = int(numbers[i])
                    result += third_number
                    i+= 1
                print(result)

        elif operation == "2":
            calculation = input("Enter your calculation: ")
            numbers = calculation.split("-")
            first_number = int(str(numbers[0]))
            second_number = int(str(numbers[1]))
            result = first_number - second_number

            if len(numbers) <= 2 and result >= 0:
                print(result)

            elif len(numbers) > 2 and result >= 0:
                i = 2

                while i < len(numbers):
                    third_number = int(numbers[i])
                    result -= third_number
                    i+= 1
                print(result)

            else:
                print("Invalid operation, try again")

        elif operation == "3":
            break
                    
 
calculator()