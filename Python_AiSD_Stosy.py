'''class Stack:
    #variable
    __stack = []

    #methods
    def __init__(self):
        self.__stack= []

    def push(self, object):
        self.__stack.append(object)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def isEmpty(self):
        if not self.__stack:
            return True
        else:
            return False

    def size(self):
        return len(self.__stack)

stos = Stack()
stos.push(4)
stos.push(3)
stos.push(2)
stos.push(1)
print(stos.pop())
print(stos.peek())
print(stos.peek())
print(stos.isEmpty())
print(stos.size(), "\n\n")

#-------------------------------------------------INFIX TO POSTFIX---------------------------------------------------------------

def plus_minus():
    while operation:
        if(operation[-1] is not "("):
            print(operation.pop(), end = "")
        else:
            break;
    operation.append(i)
def mnozenie_dzielenie():
    while operation:
        if (operation[-1] is "*"):
            print(operation.pop(), end = "")
        elif (operation[-1] is "/"):
            print(operation.pop(), end = "")
        else:
            break;
    operation.append(i)

operation = []
#intput = ["(", "a", "+", "b", ")", "*", "c"]
intput = ["a", "*", "b", "+", "c", "/", "(", "(", "d", "-", "e", ")", "*", "f", ")"]
#intput = ['a', '*', '(', 'b', '+', 'c', ')', '-', 'd', '/', '(', 'e', '-', 'f', ')']

for i in intput:
    if (i is "("):#DODAWANIE ( DO STOSU
        operation.append(i)

    elif (i is ")"):#WYPISYWANIE OPERACJI ZE STOSU DO ZNAKU (. DODATKOWO ZNAK ( JEST ANIHILOWANY
        while (operation[-1] is not "("):
            print(operation.pop(), end="")
        operation.pop()

    elif (i is "+"):
        plus_minus()

    elif (i is "-"):
        plus_minus()

    elif (i is "*"):
        mnozenie_dzielenie()

    elif (i is "/"):
        mnozenie_dzielenie()

    else:# WYPISANIE LITEREK NA EKRAN
        print(i,end="")

while operation:# NA SAMYM KONCU WYPISUJE TO CO ZOSTALO W STOSIE
    print(operation.pop(), end="")'''

#--------------------------------------------------------SOLVING EQUATIONS WRITTEN IN POSTFIX--------------------------------------

#equation = [6,5,15,"*","+"]
equation = [6, 5, "-", 8, 4, "-", "*", 4, 3, "-", "/"]
numbers = []
zmienna1 = 0
zmienna2 = 0

for i in equation:
    if (i is "+"):
        zmienna2 = numbers.pop()
        zmienna1 = numbers.pop()
        numbers.append(zmienna1 + zmienna2)

    elif (i is "-"):
        zmienna2 = numbers.pop()
        zmienna1 = numbers.pop()
        numbers.append(zmienna1 - zmienna2)

    elif (i is "*"):
        zmienna2 = numbers.pop()
        zmienna1 = numbers.pop()
        numbers.append(zmienna1 * zmienna2)

    elif (i is "/"):
        zmienna2 = numbers.pop()
        zmienna1 = numbers.pop()
        numbers.append(zmienna1 / zmienna2)

    else:
        numbers.append(i)

print(numbers)