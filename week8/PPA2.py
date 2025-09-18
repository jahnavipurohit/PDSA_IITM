'''Given a Python function Karatsuba(x, y) that implements Karatsuba's algorithm, 
that multiplies two integers x and y recursively. Length of integers x and y may or may not be same.
Refer the definition of function Karatsuba(x,y) and complete the Python function 
calculateAndAssign(x,y) that accepts two integers x and y and returns five variables 
that will be used in subsequent recursive calls to function Karatsuba(x,y).'''

def calculateAndAssign(x, y):
    """
    Prepares variables for Karatsuba's algorithm based on how
    Karatsuba(x, y) is currently written.
    """
    str_x = str(x)
    str_y = str(y)

    n = max(len(str_x), len(str_y))

    # Pad with zeros to ensure equal length
    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)

    # Split point
    k = n // 2

    # Split numbers into halves
    x1 = int(str_x[:n - k])
    x0 = int(str_x[n - k:])
    y1 = int(str_y[:n - k])
    y0 = int(str_y[n - k:])

    # Prepare variables for Karatsuba function
    var1 = x1 + x0        # (a+b)
    var2 = y1 + y0        # (c+d)
    var3 = Karatsuba(x1, y1)  # ac
    var4 = Karatsuba(x0, y0)  # bd
    var5 = k              # split length

    return var1, var2, var3, var4, var5



def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    var1, var2, var3, var4, var5 = calculateAndAssign(x, y)
    ad_plus_bc = Karatsuba(var1, var2) - var3 - var4
    return (10 ** (2*var5))*var3 + (10 ** var5)*ad_plus_bc + var4

x=int(input())
y=int(input())
print(Karatsuba(x,y))