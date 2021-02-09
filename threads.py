import threading
from time import time

"""
def contar(num_hilo, **datos):
    contador = datos['inicio']
    incremento = datos['incremento']
    limite = datos['limite']
    while contador<=limite:                
        print('hilo:', num_hilo, 'contador:', contador)        
        contador+=incremento
for num_hilo in range(3):
    hilo = threading.Thread(target=contar, args=(num_hilo,),kwargs={'inicio':0, 
                                    'incremento':1,
                                    'limite':10})
    hilo.start()
"""

def cal(x):
    y = 0
    for i in range(1,x):
        y += i
    return y

def cal_p():
    v = []
    for i in range(1, 50):
        x = cal(i)
        v.append(x)  
    return sum(v)

init_time = time()
"""
v = []
for i in range(1, 50):
    x = cal(i)
    print(x)
    v.append(x)
print(sum(v))
"""

num_hilo = 10
for n_hilo in range(num_hilo):
    hilo = threading.Thread(name=n_hilo, target=cal_p)
    hilo.start()


final_time = time()
execution_time = final_time - init_time
print(f"The execution time is: {execution_time}")

#======== Análisis =========
#A only proccess of 10,000 datas. time 17.14