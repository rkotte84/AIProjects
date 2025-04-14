
def dostuffwithNumbers(n):
    print(n)


def trycatchTest(n):
    input_list = [1, 2, 3, 4, 5]

    for i in range(n):
        try:
            dostuffwithNumbers(input_list[i])
        except IndexError:
            print("Index out of range") 

try:
    n = input("Enter a number: ")
    n = int(n)
    trycatchTest(n)
except ValueError:
    print("Type error: Please enter a valid number")


    