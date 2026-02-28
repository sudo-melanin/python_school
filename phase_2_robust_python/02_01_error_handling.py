# To ensure we account for errors in our program, we use the try-except block
# It enables us to address an error before it crashes our program.

try:            # Phase: Execution - Try the 'Happy Path'
    age = int(input("Enter your age: "))
    result = age * 2
    print(f"In python years, you are {result} years old")

except ValueError:                          
    # Specific Catch: Triggers if the user types text instead of a number
    print("Enter a valid number....")

except ZeroDivisionError as e:              
    # Specific Catch: Triggers if a math error occurs (captured in 'e')
    print("Invalid number error: ", e)

else:                                       
    # Validation: Runs only if NO exceptions were raised in the 'try' block
    print("Process completed with no errors")

finally:                                    
    # Cleanup: Always executes (for closing files, DB connections, or logging exits)
    print("Exiting this try-except code blocks.... **sighs")