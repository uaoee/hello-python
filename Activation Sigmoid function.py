from math import e
a=1
b=0
c=0.3
d=-0.1
alpha = 0.2
int_c = (a*c)+(b*d)
print(int_c)
function_x = 1/(1+(e**(-3*int_c)))
print(function_x)
int_d=function_x *alpha
print(int_d)
Out_d = 1/(1+(e**(-3*int_d)))
print(Out_d)
c=0.5
d=0.23
alpha=-0.2
print(c,d,alpha)
print(Out_d)