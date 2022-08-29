from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt

# Exercício 01 -
'''
A) Histograma 2     B) Histograma 1
C) Histograma 4     D) Histograma 3
'''

# Exercício 02 -
'''
1) 12, 12, 13, 14, 14, 15, 15, 15,
   16, 16, 16, 16, 18.
   Média=14,7  Mediana=15  Moda=16
   
2) 39, 40, 41, 42, 42, 42, 44, 44,
   44, 44, 44, 45, 45, 47.
   Média=43,0  Mediana=44  Moda=44
   
3) 12, 18, 26, 28, 31, 33, 40, 44, 45, 49,
   61, 63, 75, 80, 80, 89, 96, 103, 125, 125.
   Média=61,15  Mediana=55  Moda=80 e 125
   
4) 17, 21, 21, 25, 26, 30, 31, 31,
   31, 34, 34, 34, 35, 36, 37, 38.
   Média=30,06  Mediana=31  Moda=31 e 34  
'''

# Exercício 03
'''
A) Moda= Óculos. A maioria escolheu os "óculos" como
         resposta, tornando a Moda a melhor medida
         para explicar o gráfico. 
B) Moda= No Facebook, acha-o válido. Por se tratar de 
         tópicos diferentes a moda mostra aquele que 
         mais foi escolhido.  
'''

# Exercício 04
'''
Histograma 1) Moda, Mediana, Média.

Histograma 2) Média, Mediana, Moda.
'''

# Exercício 05
'''
soma das (notas x pesos) / soma dos pesos

1) 8.900 / 100 = 89 de nota.
2) 42 / 12 = 3,5 é o rendimento médio do estudante.
'''

# Exercício 06
classes = pd.interval_range(start=22, end=52, freq=6)

print(classes)

medios = [classe.mid for classe in classes]

print(medios)

freqs = [16, 2, 2, 3, 1]

tabela = pd.DataFrame({'Classe': classes, 'Médios': medios, 'Frequência': freqs})

display(tabela)

plt.bar(tabela['Médios'], tabela['Frequência'])

plt.xticks(medios)

plt.yticks(range(0, 21, 2))

tabela['x*f'] = tabela['Médios'] * tabela['Frequência']

display(tabela)

media = tabela['x*f'].sum() / tabela['Frequência'].sum()
plt.ylabel('Frequência')
plt.xlabel('Distância percorrida (em milhas por galão')
plt.title('Econômia de Combustível')

plt.show()

# Exercício 07
"""
5,59 / 5,59 / 6,00 / 6,02 / 6,03 / 6,40

A) Média= 6,071  Mediana= 6,01

5,59 / 5,59 / 6,02 / 6,03 / 6,04 / 6,40

B) Média= 6,078  Mediana= 6,025

C)  A média foi a mais afetada pelo erro
    de medição.
"""

# Exercício 08
'''
10,9 /13,8 /14,2 /16,0 /24,4 /25,9 /27,5 /27,8 /29,9 /31,2 /
42,4 /42,9 /43,4 /49,2 /55,9 /65,7 /103,9 /198,4 /280,9.   
A) Média= 58,12  Mediana= 31,2

'Sem Canadá'
10,9 /13,8 /14,2 /16,0 /24,4 /25,9 /27,5 /27,8 /29,9 /
31,2 /42,4 /42,9 /43,4 /49,2 /55,9 /65,7 /103,9 /198,4 /
B) Média= 45,74  Mediana= 30,55 / A média foi a mais
                                  afetada.
'Com Índia'
0,9 /13,8 /14,2 /16,0 /21,5 /24,4 /25,9 /27,5 /27,8 /29,9 /
31,2/42,4 /42,9 /43,4 /49,2 /55,9 /65,7 /103,9 /198,4 /280,9.
C) Média= 56,29  Mediana= 30,55 / A média foi a mais
                                  afetada.                
'''

# Exercício 09
'''
Carro A) Média= 30,4  Mediana= 30,0  Moda= 28,0
Deverá usar a Média como melhor desempenho.

Carro B) Média= 30,2  Mediana= 31,0  Moda= 31,0
Deverá usar a Moda como melhor desempenho.

Carro C) Média= 30,2  Mediana= 30,0  Moda= 32,0
Deverá usar a Moda como melhor desempenho
'''
