x = 10         #Global Variable
 
def function():
    global x     #Takes global vairiable and the next line changes the global value of the variable
    x=4             #
    y = 5    #Local Variable
    print(y)



function()
print(x)