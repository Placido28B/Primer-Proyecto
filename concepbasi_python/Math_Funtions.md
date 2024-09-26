
# 
# [Math Funtions](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/15824542#overview) --- [Video](https://youtu.be/JW05xyoIsaM)

#
## [Python Modules](https://www.programiz.com/python-programming/modules)
#
What is math module in Python?
The math module is a standard module in Python and is always available. To use mathematical functions under this module, you have to import the module using import math.

It gives access to the underlying C library functions. For example,

## Square root calculation

import math
#
math.sqrt(4)
#
Run Code
#
This module does not support complex datatypes. The cmath module is the complex counterpart.

Functions in Python Math Module
Here is the list of all the functions and attributes defined in math module with a brief explanation of what they do.

## [Ejemplos basicos]()

    print(type(6))
    print(type(2 - 4))
    print(type(2 * 4))
    print(type(2 / 4)) #0.5
    print(type(2 ** 3))
    print(type(5 // 4))
    print(type(6 % 4))




# List of Functions in Python Math Module
# Function	- - - Description
### [ceil(x)]()  Returns the smallest integer greater than or equal to x.
### [copysig]()  (x, y)	Returns x with the sign of y
### [fabs(x)]()  Returns the absolute value of x
### [factori]()  l(x)	Returns the factorial of x
### [floor(x]()  	Returns the largest integer less than or equal to x
### [fmod(x,]()  y)	Returns the remainder when x is divided by y
### [frexp(x]()  	Returns the mantissa and exponent of x as the pair (m, e)
### [fsum(it]()  rable)	Returns an accurate floating point sum of values in the iterable
### [isfinit]()  (x)	Returns True if x is neither an infinity nor a NaN (Not a Number)
### [isinf(x]()  	Returns True if x is a positive or negative infinity
### [isnan(x]()  	Returns True if x is a NaN
### [ldexp(x]()   i)	Returns x * (2**i)
### [modf(x)]()  Returns the fractional and integer parts of x
### [trunc(x]()  	Returns the truncated integer value of x### 
### [exp(x)]()  Returns e**x
### [expm1(x]()  	Returns e**x - 1
### [log(x[,]()  b])	Returns the logarithm of x to the base b (defaults to e)
### [log1p(x]()  	Returns the natural logarithm of 1+x
### [log2(x)]()  Returns the base-2 logarithm of x
### [log10(x]()  	Returns the base-10 logarithm of x
### [pow(x, ]()  )	Returns x raised to the power y
### [sqrt(x)]()  Returns the square root of x
### [acos(x)]()  Returns the arc cosine of x
### [asin(x)]()  Returns the arc sine of x
### [atan(x)]()  Returns the arc tangent of x
### [atan2(y]()   x)	Returns atan(y / x)### 
### [cos(x)]()  Returns the cosine of x
### [hypot(x]()   y)	Returns the Euclidean norm, sqrt(x*x + y*y)### 
### [sin(x)]()  Returns the sine of x### 
### [tan(x)]()  Returns the tangent of x
### [degrees]()  x)	Converts angle x from radians to degrees
### [radians]()  x)	Converts angle x from degrees to radians
### [acosh(x]()  	Returns the inverse hyperbolic cosine of x
### [asinh(x]()  	Returns the inverse hyperbolic sine of x
### [atanh(x]()  	Returns the inverse hyperbolic tangent of x
### [cosh(x)]()  Returns the hyperbolic cosine of x
### [sinh(x)]()  Returns the hyperbolic cosine of x
### [tanh(x)]()  Returns the hyperbolic tangent of x### 
### [erf(x)]()  Returns the error function at x
### [erfc(x)]()  Returns the complementary error function at x
### [gamma(x)]()  	Returns the Gamma function at x
### [lgamma()]()  	Returns the natural logarithm of the absolute value of the Gamma function at x 
### [pi()]()  matematical constant, the ratio of circumference of a circle to it's diameter (3.14159...### )
### [e()]()  matematical constant e (2.71828...)