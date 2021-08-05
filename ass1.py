from scipy.optimize import linprog
obj = [-50,-120]
A_ieq = [[7000,2000],[10,30],[1,1]]
B_ieq = [700000,1200,110]
boundarie=[(0,float("inf")),(0,float("inf"))]
optimise = linprog(c=obj,A_ub=A_ieq,b_ub=B_ieq,bounds=boundarie,method="Simplex")
x,y=optimise.x
profit = (50*round(x))+ (120*round(y))
print(f'{round(x)}')
print(f'{round(y)}')
print(f'Profit :{ profit}')