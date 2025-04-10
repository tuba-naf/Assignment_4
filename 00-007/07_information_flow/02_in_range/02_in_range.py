def in_range():
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    value_name = int(input("Enter a number"))
    low= 10
    high=100
    if    value_name >= low and    value_name <= high:
        return True
    
    return False

if __name__ == '__main__':
    
  result = in_range()
    
    # Output based on the result of in_range()
if result:
        print("The number is in range!")
else:
        print("The number is out of range.")