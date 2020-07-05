#InputOutput
#Output
#end,sep
print("hello",'hey',end=';')
print(1254162)
print(123,23.234,end= ' ')
print(123,13,'hey','bye',sep='bk')
print(12236523)
print(123123,234234)
print('316348628346')
print("Some Message",234,sep = ':')
#--------------------------------------------------------
#Input -----
#input() --- by default, everything recieved is a 'string'!
#Data types ---- used when type casting is required
x = int(input("Enter Some Number:  "))
y = float(input("Enter Again: "))
print(type(x),type(y))
print(x+y)
#eval() ---- evaluate 2 things ----
#1. identify the data type of numeric data and type cast it into one.
#2. some string expression
x = eval(input("Enter Something: "))
y = eval(input("Enter Again: "))
print(x+y)
n = input("Enter some expression: ")
print("Result is: ",eval(n))














