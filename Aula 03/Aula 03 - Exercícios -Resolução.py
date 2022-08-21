# Exercício 1
import pandas as pd
import matplotlib.pyplot as plt

dados = [['Estados Unidos', 15], ['Tanzânia', 1],
         ['Grã-Bretanha', 1], ['Itália', 4],
         ['Quênia', 9], ['Brasil', 2], ['Etiópia', 2],
         ['México', 4], ['Nova Zelândia', 1],
         ['África do Sul', 2], ['Marrocos', 1]]
tabela = pd.DataFrame(data=dados, columns=['Países', 'Frequência'])
print(tabela)
pizza = plt.pie(tabela['Frequência'], labels=tabela['Países'], autopct='%1.1f%%')
plt.show()
# Exercício 2
dados_simplificados = [['Américas', 21], ['Europa', 5],
                       ['África', 15], ['Oceania', 1]]
tabela = pd.DataFrame(data=dados_simplificados, columns=['Continentes', 'Frequência'])
plt.pie(tabela['Frequência'], labels=tabela['Continentes'], autopct='%1.1f%%')
plt.show()
# Exercício 3
# (A)
dados3 = [['Alemanha', 44], ['Grã-Bretanha', 69],
          ['EUA', 104], ['Rússia', 82], ['China', 88]]
tabela3 = pd.DataFrame(data=dados3, columns=['País', 'Medalhas'])
tabela3 = tabela3.sort_values(by='Medalhas', ascending=False)
pareto = plt.bar(tabela3['País'], tabela3['Medalhas'], color='red')
plt.ylabel('Número de Medalhas')
plt.title('Olímpiadas de Londres - 2012')
plt.show()
# (B)
dados_med = [['Drogas \nnão\n autorizadas', 27], ['Omissão', 54],
             ['Forma \nincorreta \nda droga', 2], ['Período \nincorreto', 37],
             ['Dose \ninadequada', 57], ['Deterioração', 2]]
tabela_med = pd.DataFrame(data=dados_med, columns=['Erros', 'Quantidade'])
tabela_med = tabela_med.sort_values(by='Erros', ascending=False)
pareto_med = plt.bar(tabela_med['Erros'], tabela_med['Quantidade'], color='cyan')
plt.ylabel('Quantidade de erros')
plt.title('Medicamentos com erros na composição\n(Tempo de duração da pesquisa: 2 meses)')
# tentando colocar o número de frequência dos erros.
# barras = pareto_med.patches
# freqs = tabela_med['Quantidade']
# for barra, freq in zip(barras, freqs):
#    altura = barra.get_height()
#    pareto_med.text(barra.get_x() + barra.get_width() / 2,
#                    altura, freq, ha='center', va='bottom')
plt.show()
# Exercícos 4
salmedio = pd.read_csv('aula3_ex04.csv')
print(salmedio.head(7))
plt.scatter(salmedio['alunos'], [salmedio['salario']])
plt.xlabel('N° Alunos')
plt.ylabel('Média salarial profs')
plt.title('Salário por n° de alunos')
plt.grid()
plt.show()

# Exercício 5
dados5 = pd.DataFrame({'Registros': [4.3, 4.9, 5.0, 5.4, 5.8, 6.2,
                                     6.7, 7.1, 7.8, 7.9, 8.2, 8.3]})
dados5.index = list(range(2000, 2012))

fig, registros = plt.subplots()
registros.plot(dados5.index, dados5['Registros'], 'bo-')
registros.set(xlabel='Ano',
              ylabel='Registros',
              title='Motos registradas entre os anos de:\n 2000 e 2011')
registros.tick_params(axis='y', colors='blue')
plt.grid()
plt.show()
