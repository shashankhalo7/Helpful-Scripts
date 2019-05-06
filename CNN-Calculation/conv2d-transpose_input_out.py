i=float(input('Input Size'))
p=float(input('Padding'))
f=float(input('Filter/Kernel Size'))
s=float(input('Stride Value'))
out=((i-1)*s)+f-(2*p)
print("Output Size:",out)

