i=float(input('Input Size'))
p=float(input('Padding'))
f=float(input('Filter/Kernel Size'))
s=float(input('Stride Value'))
out=((i-f+2*p)/s)+1
print("Output Size:",out)

