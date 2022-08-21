from sys import displayhook
from tkinter import Grid
import pandas as pd
from math import ceil

data = pd.Series([35, 51, 44, 42, 37, 38, 36, 39,
                  44, 43, 40, 40, 32, 39, 41, 38,
                  42, 39, 40, 46, 37, 35, 41, 39])
print(data)
v_max = data.max()
v_min = data.min()
n_classes = 5

dist_freq = data.value_counts(bins=n_classes).sort_index()
print(dist_freq)

nova_dist_freq = pd.DataFrame(dist_freq)
nova_dist_freq = nova_dist_freq.reset_index()
nova_dist_freq.columns = ['Classe', 'Frequência']
amplitude = ceil((v_max - v_min) / n_classes)
classes = pd.interval_range(start=v_min, end=v_max + amplitude,
                            freq=amplitude)
print(classes)
nova_dist_freq['Classe'] = classes
displayhook(nova_dist_freq)

pts_medios = [classe.mid for classe in classes]
print(pts_medios)
nova_dist_freq['Pontos médios'] = pts_medios
n_dados = len(data)
nova_dist_freq['Freq relativa'] = nova_dist_freq['Frequência'] / n_dados
nova_dist_freq['Freq Acum'] = nova_dist_freq['Frequência'].cumsum()
displayhook(nova_dist_freq)

histograma = data.hist(bins=[classe.left for classe in classes] +
                            [nova_dist_freq['Classe'][n_classes - 1].right],
                       color='cyan', edgecolor='black', grid=False)
histograma.set(xlabel='Nível de Ardência',
               ylabel='Frequência \nDo "ardor" das Pimentas',
               title='Distribuição da frequência da Ardência'
                     'das pimentas',
               xticks=pts_medios)
#Número da frequência.
barras = histograma.patches
freqs = nova_dist_freq['Frequência']
for barra, freq in zip(barras, freqs):
    altura = barra.get_height()
    histograma.text(barra.get_x() + barra.get_width() / 2,
                    altura, freq, ha='center', va='bottom')

import matplotlib.pyplot as plt

#fic_esq = [pts_medios[0] - amplitude]
#fic_dir = [pts_medios[-1] + amplitude]
#x_data = fic_esq + pts_medios + fic_dir
#y_data = [0] + list(nova_dist_freq['Frequência']) + [0]
#plt.plot(x_data, y_data, 'go--',)
#plt.xlabel("Nível de Ardência")
#plt.ylabel("Frequência \nDo 'ardor' das Pimentas")
#plt.title("Distribuição de frequências da ardência das Pimentas")
#plt.xticks(x_data)
#plt.yticks(range(0, nova_dist_freq['Frequência'].max() + 2, 2))
#plt.grid()
