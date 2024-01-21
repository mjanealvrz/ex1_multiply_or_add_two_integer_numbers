#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.



#Pseudocode

# Ask user to input two integer numbers
input_num1 = int(input("Enter 1st Number: "))
input_num2 = int(input("Enter 2nd number: "))

# Create function with if-else statement
def mutiply_or_add(input_num1,input_num2):

    #calculate the product of two integer numbers
    product = input_num1 * input_num2

    # using if-else statement define if the product is lower or equal to 1000
    if  product <=  1000:

        # if true, return the product
        return (" The Product is " + str(product))
    
     # if false, return the sum of input_num1 and input_num2    
    else: 
        return ("The Sum is  " + str(input_num1 +  input_num2) )
       
   
#  Call the multiply_or_add function with user-input values
result = mutiply_or_add(input_num1, input_num2)  

# Print result 
print("Result:", result)