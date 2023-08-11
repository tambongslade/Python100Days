from artcal import logo
print(logo)

def add (n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add, 
            "-":subtract, 
            "*":multiply,
              "/":divide,
            }
def calculator():

    num1=int(input("Enter the first number: "))
    for op in operations:
        print(op)
    should_continue=True
    while should_continue:
            
        symbol=input("Pick an operator from the line above: ")
        num2=int(input("Enter the next number: "))

        calculation_function=operations[symbol]
        first_answer= calculation_function(num1,num2)
     
        print(f"{num1} {symbol} {num2} = {first_answer}")
        if input(f"type 'y' to continue calculating with {first_answer} or N to stop e ")=="y":
            num1=first_answer
        else:
            should_continue=False
            calculator()
calculator()