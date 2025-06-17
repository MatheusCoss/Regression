from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def potencia_tabel(tabela: list):
    soma_x = 0
    soma_y = 0
    soma_x_2 = 0
    soma_y_2 = 0
    soma_xy = 0
    for index,dado in enumerate(tabela):
        x = dado[0]
        y = dado[1]
        x_2 = x**2
        y_2 = y**2
        xy = x*y
        tabela[index].append(x_2)
        tabela[index].append(y_2)
        tabela[index].append(xy)

        soma_x += x
        soma_y += y
        soma_x_2 += x_2
        soma_y_2 += y_2
        soma_xy += xy
        

    
    total = [soma_x,soma_y,soma_x_2,soma_y_2,soma_xy]
        
    
    return {"total": total, "n": len(tabela)}


def calcular_correlacao(tabela):
    rxy = ((tabela['n'] * tabela['total'][4]) - (tabela['total'][0] * tabela['total'][1]))

    a = sqrt((tabela['n'] * tabela['total'][2]) - (tabela['total'][0] ** 2)) * sqrt((tabela['n'] * tabela['total'][3]) - (tabela['total'][1] ** 2))
    print(f"Rxy = {rxy} / {sqrt((tabela['n'] * tabela['total'][2]) - (tabela['total'][0] ** 2)):.3f} * {sqrt((tabela['n'] * tabela['total'][3]) - (tabela['total'][1] ** 2)):.3f} = {rxy / a:.3f}")

    return rxy / a


def calcular_coeficiente_angular(tabela):

    rxy = ((tabela['n'] * tabela['total'][4]) - (tabela['total'][0] * tabela['total'][1]))
    
    a = (tabela['n'] * tabela['total'][2]) - (tabela['total'][0] ** 2)
    print(f"B = {rxy} / {tabela['n'] * tabela['total'][2]} - {tabela['total'][0] ** 2}  = {rxy / a:.3f}")

    return rxy / a

def calcular_intercepto(totais,b):
    a = (totais['total'][1] - b*totais['total'][0]) / totais['n']
    print(f"A = {totais['total'][1] - b*totais['total'][0]} / {totais['n']} = {a}")
    return a

def calcular_estimativa(a,b,x):
    y = a + b * x
    print(f"Y = {a} + {b} * {x} = {y}")
    return y

tabela = [
    [12,25],
    [16,30],
    [20,35],
    [24,40],
    [28,50]
    
]


# Coefiente de Correlação
total = potencia_tabel(tabela)
r = calcular_correlacao(total)

# Regressão Linear
b = calcular_coeficiente_angular(total)
a = calcular_intercepto(total, b)

# Se ( R ) estiver próximo de +1, a correlação é positiva forte: a produção aumenta com a temperatura.
# Se ( R ) estiver próximo de -1, a correlação é negativa forte: a produção diminui com a temperatura.
# Se ( R ) estiver próximo de 0, não há correlação significativa

# Estimativas baseado na Regressão Linear



def main():
    while True:
        print(f"R = {r:.3f} B = {b} A = {a}")
        x = float(input("X: "))
        print(f"Estimativa para {x} = {calcular_estimativa(a,b,x)}")



def get_index(tabela,index):
    index_data = []
    for data in tabela:
        index_data.append(data[index])
    
    return index_data

def predict(xs):
    result = []
    for x in xs:
        result.append(calcular_estimativa(a,b,x))
    
    return result
        

def plot():
    plt.style.use('_mpl-gallery')

    print(f'{total['total']} n = {total['n']}')
    print(f"R = {r:.3f} B = {b} A = {a}")
    # plot
    fig, ax = plt.subplots()
    x = get_index(tabela,0)
    y = get_index(tabela,1)
    ax.plot(x, y, 'o', color='blue', label='Dados reais')
    ax.plot(x, predict(x), color='red', label='Regressão linear')
    plt.title('Relação entre Temperatura e Produção - Banana')
    plt.xlabel('Temperatura')
    plt.ylabel('Produção')
    plt.legend()
    plt.show()


#main()



if __name__ == "__main__":
    plot()