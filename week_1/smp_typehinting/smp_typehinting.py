name = 'Lord Gwyn'
age : int  =  69
currency ='Euro'
balance : float =  420.69
cards: list = ['Lordran', 'Anor Londo', 'The Kiln of the First Flame']

# useless ugly ass function form DLO that didn´t even run
def ugly_calculator(param1, param2, param3, param4, param5, param6):
    print(f"Welcome, {param4}.")
    if param1 == "square":
        area = param2 * param3
        print(f"Area is: {area}")
        return area
    if param1 == "cube":
        content = param2 * param3 * param5
        print(f"Content is : {content}")
        return content
    
# ugly_calculator("square", 2, 2, name, age, currency)

# function with type hinting

def calculator(num1: int, operator: str, num2: int) -> int :
    answer = 0
    if num1 != int : 
        print("Num1 not a number!")
    if operator != '*' or '-' or '+' or '/':
        print("Operator not valid")
    if num2 != int : 
        print("Num2 not a number!")
    match operator:
        case '*':
            answer = num1 * num2
        case '/':
            answer = num1 / num2
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case other: 
            print("unknown computation")
    print(f"Answer is: {answer}")        
    return answer
    
calculator(2, '*', 2)