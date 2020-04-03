import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=15, width=200)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """
('Aula 10 - Dicionarios')\n")
("Dicionários não possuem uma noção de índice e não podem ser fatiados.")\n')
("Dicionários são mutáveis de forma que a qualquer momento você pode inserir ou remover itens.")\n')
("Criando Dicionários")\n')
("Dicionários são criados colocando")\n')
("os pares chave: valor entre chaves {} das seguinte forma:")\n')
("Nomes são as chaves e as linguagens de programação são os valores associados as chaves.")\n')
("Outra forma de gerar o mesmo dicionário acima é com ditc(x) onde x")\n')
("pode ser uma lista de tuplas do tipo (chave, valor) como mostrado abaixo:")\n')

("di = dict([(‘Julio’, ‘Pascal’), (‘Bruno’, ‘Python’), (‘Ana’, ‘Ruby’), (‘Luisa’, ‘Java’), (‘Mauro’, ‘PHP’)])")\n')

("Um dicionário vazio")\n')
("é criado com as chaves em branco:")\n')
("di = {}")\n')

("Acessando itens de um dicionário")\n')
("Para acessar um item do dicionário devemos usar sua chave entre colchetes [ ],")\n')
("")\n')
(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java}")\n')
(">>> di[Ana]")\n')
("Ruby")\n')
(">>> x = di[Julio]")\n')
(">>> print(x)")\n')
("C")\n')
(">>>")\n')

lb9 = Label(janela9, text='print("Recuperando um valor no dicionário com o método get()")\n')
lb9 = Label(janela9, text='print("Para recuperar um valor no dicionário podemos usar o método get")\n')
lb9 = Label(janela9, text='print("passando como argumento a chave do valor que queremos recuperar:")\n')

(">>> di = {Ana: Ruby, Paulo: C++, Mauro: Swift, Julio: Pascal, Luisa: Java, Bruno: Python}")\n')
(">>> linguagem = di.get(Ana)")\n')
(">>> print(linguagem)")\n')
("Ruby")\n')
(">>>")\n')

("Percorrendo dicionários com for")\n')
("Podemos percorrer um dicionário com "for")\n')

('#Programa para percorrer um dicionário\n')
("linguagens =  {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
("for chave in linguagens:")\n')
("    print(chave, programa em:, linguagens[chave])")\n')

("Alterando um valor em um dicionário")\n')
("Para alterar uma valor em um dicionário use o nome do dicionário")\n')
("com a chave entre colchetes e associe um novo valor a chave:")\n')

(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> di[Jaime] = PHP")\n')
(">>> di")\n')
("{Luisa: Java, Bruno: PHP, Julio: Pascal, Mauro: PHP, Ana: Ruby}")\n')
(">>>")\n')

("Inserindo um item em um dicionário")\n')
("Para inserir um item em um dicionário basta declarar o dicionário colocando")\n')
("entre colchetes a nova chave e atribuindo uma valor a ela:")\n')

(">>> di = {França: Paris, Espanha: Madri, Itália: Roma}")\n')
(">>> print(di)")\n')
{Espanha: Madri, França: Paris, Itália: Roma}")\n')
(">>> di[Russia] = Moscou")\n')
(">>> print(di)")\n')
("{Espanha: Madri, França: Paris, Itália: Roma, Russia: Moscou}")\n')
(">>>")\n')

("Inserindo itens ou alterando itens em um dicionário com o método update()")\n')
("O método update tem a seguinte sintaxe di.update(t) onde di e t são dicionários")\n')
("e cada par chave, valor de t é adicionado. Se uma chave de t já estiver definida em di ela recebe o valor t:")\n')

(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> print(di)")\n')
("{Ana: Ruby, Bruno: Python, Mauro: PHP, Luisa: Java, Julio: Pascal}")\n')
(">>> di.update({Paulo: C++, Mauro: Swift})")\n')
(">>> print(di)")\n')
("{Ana: Ruby, Paulo: C++, Mauro: Swift, Julio: Pascal, Luisa: Java, Bruno: Python}")\n')
(">>>")\n')

("Removendo um par chave, valor de um dicionário usando o comando del")\n')
("Use del aplicado a o nome do dicionário com a chave")\n')
("entre colchetes para apagar um par chave, valor do dicionário:")\n')

(">>> di = {Luisa: Java, Bruno: Python, Julio: Pascal, Mauro: PHP, Ana: Ruby}")\n')
(">>> del di[Mauro]")\n')
(">>> di")\n')
("{Luisa: Java, Bruno: Python, Julio: Pascal, Ana: Ruby}")\n')
(">>>")\n')

("Removendo e obtendo um par chave, valor com o método pop()")\n')
("Parecido com listas pop remove o par chave, valor retornando o valor associado,")\n')
("mas, como dicionários não são ordenados, deve-se passa-los como argumento a chave k do par a ser removido:")\n')

(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> v = di.pop(Bruno)")\n')
(">>> print(v)")\n')
("Python")\n')
(">>>")\n')

("Podemos ainda adicionar um parâmetro extra pop(a, b) onde o parâmetro extra")\n')
("substitui o valor retornado caso a chave k não conste do dicionário:")\n')

(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> b = di.pop(Eduarda, Não existe)")\n')
(">>> print(b)")\n')
("Não existe")\n')
(">>>")\n')

("Visualizações de dicionários")\n')
("método descrição keys()")\n')
("Retorna uma visualização de todas as chaves de um dicionário.")\n')
("values() Retorna uma visualização de todas os valores de um dicionário.")\n')
("items()	Retorna uma visualização de todos pares (chave, valor) de um dicionário.")\n')
("Abaixo no interpretador python3 vemos uma visão x criada a partir do dicionário di:")\n')
(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> x = di.keys()")\n')
(">>> print(x)")\n')
("dict_keys([Julio, Laura, Mauro, Ana, Bruno])")\n')

("Visualizações continuam atreladas ao dicionário")\n')
("Em Python 2 estes métodos retornavam uma lista, mas, em Python 3 eles passaram a retornar visões.")\n')
("A grande diferença e que as visões ou visualizações e que elas continuam atreladas ao dicionário e")\n')
("Criando uma visão x dos valores do dicionário di abaixo")\n')
("e depois apagar o par (Ana, Ruby), veja os resultados pelo interpretador abaixo:")\n')

(">>> di = {Julio: Pascal, Bruno: Python, Ana: Ruby, Luisa: Java, Mauro: PHP}")\n')
(">>> x = di.values()")\n')
(">>> print(x)")\n')
("dict_values([Pascal, Java, PHP, Python, Ruby])")\n')
(">>> del di[Ana]")\n')
(">>> print(x)")\n')
("dict_values([Pascal, Java, PHP, Python])")\n')
(">>>")\n')
('##fim da aula 10##\n')
"""
T.insert(tk.END, quote)
tk.mainloop()