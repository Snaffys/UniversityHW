def cube_of_natural_number(value):
    try:
        num = int(value)
        if(num.is_integer() and num > 0):
            return num ** 3
        else:
            return "undefined. Not a natural number"
    except(ValueError, TypeError):
        return "undefined. Not a natural number"

def main():
    input_value = input("Write down natural number: ")
    print("Cube of this number:", cube_of_natural_number(input_value))
    
if __name__ == "__main__":
    main()