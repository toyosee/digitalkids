try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[0])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound