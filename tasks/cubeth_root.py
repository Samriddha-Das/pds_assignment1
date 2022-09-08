# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 14:57:38
#  * @modify date 2022-08-26 14:57:38
#  * @desc [description]
#  */
# Actual code starts below this line
# --------------------------------------------------------------


def find_cube_root(num : int) -> int:
    """
    This function finds the cube root of a number
    Input : num
    Output : Your function should return the cube root of the given number
    """
    # Write your code here
    
    if num > 0:
        c = num ** (1/3)
    if c.is_integer() == True:
        print("The cube root is ", int(c))
    else:
        print("Invalid input, Enter a perfect cube number")
    return c
    


