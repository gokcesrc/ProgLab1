
#lesson1
from sympy import Symbol
x=Symbol("x")
print(x+x+1)



from sympy import Symbol
x=Symbol("x")
y=Symbol("y")
s=x*y+x*y
print (s)



#working with expression
from sympy import factor #factor çarpanlarına ayırır
expr=x**2-y**2
print(factor(expr))




from sympy import expand #expand denklemi sadeleştirir.
factors=factor(expr)
print(expand(factors))



#printing series
from sympy import pprint
x=Symbol("x")
series=x
n=5
x_value=10
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series) #pprint günlük yazıma dönüştürür
series_value=series.subs({x:x_value})
print(series_value)




expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2}) #sub ile sembollere,değişkenlere değer atarız
print(res)





#lesson2
#sympy examples
#gauss denklemi ile grafik çizdik
import sympy as sym
from sympy import Symbol
from sympy import pprint




get_ipython().run_line_magic('matplotlib', 'notebook')
import sympy.plotting as syp




sigma=Symbol("sigma") #sembolleri oluşturduk
x=Symbol("x")
mu=Symbol("mu")





part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function=part_1*part_2
pprint(my_gauss_function)





syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-5,5),title="gauss") #grafik çizimi için kullanılır fonk kendisi,araık değerleri,başlık



#yukarıdaki fonksiyonu döngü ile yazarsak
x_values=[]
y_values=[]
for value in range(-10,10):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)
    


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()