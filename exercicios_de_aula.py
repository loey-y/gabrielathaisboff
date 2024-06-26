# -*- coding: utf-8 -*-
"""exercicios de aula.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13XRmqng5dEuVohTSL6crwMxIhsoHmv1d
"""

print('Olá, mundo!')

preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco * (p/100)
final = preco - desconto

print('O preço do produto é {}. Desconto será de {}%'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

print('Bem-vindos ao estabelecimento da Gabriela Thaís Boff')
preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100)% para <200 unidades:'))

"""#1º Exercício da atividade prática"""

print('Bem-vindos ao estabelecimento da Gabriela Thaís Boff')
valor_produto = float(input('Entre com o valor desejado:'))
quantidade_produto = int(input('Entre com a quantidade desejada'))
desconto_produto = 0
if quantidade_produto <= 200:
  desconto_produto = 0.00
elif quantidade_produto>=200 and quantidade_produto < 1000:
  desconto_produto = 0.05 #porcentagem feita com números decimais
elif quantidade_produto>=1000 and quantidade_produto < 2000:
  desconto_produto = 0.10 #porcentagem feita com números decimais
else:
  desconto_produto = 0.15 #porcentagem feita com números decimais

total_sem_desconto = valor_produto * quantidade_produto
print('O valor total do pedido sem desconto é de R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total do pedido com desconto é de R$ {:.2f}'.format(total_com_desconto))

"""#2º Exercício"""

#2º Exercício da atividade prática
print('               Bem-vindos a sorveteria da Gabriela Thaís Boff')
print(' ---------------------------------CARDÁPIO---------------------------------------- ')
print('|NRO DE BOLAS | Sabor tradicional (tr) | Sabor premium (pr) | Sabor Especial (es) |')
print('|      1      |         R$6,00         |        R$7,00      |        R$8,00       |')
print('|      2      |         R$11,00        |       R$13,00      |        R$15,00      |')
print('|      3      |         R$15,00        |       R$18,00      |        R$21,00      |')
print(' --------------------------------------------------------------------------------- ') #no exercício e na imagem modelo os valores estão diferentes
acumulador = 0
while True:
  sabor = input('Entre com o sabor desejado (tr/pr/es):')
  if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
    print('Opção inválida. Digite corretamente a opção de sabor.')
    continue #se o cliente digitar a opção errada o código volta para while

  quantidade = input('Entre com a quantidade de bolas de sorvete desejadas (1/2/3):')
  if quantidade != '1' and quantidade != '2' and quantidade != '3':
    print('Opção inválida. Digite corretamente a quantidade de bolas de sorvete.')
    continue #se o cliente digitar a opção errada o código volta para while

  if sabor == 'tr' and quantidade == '1':
    print('Você escolheu 1 bola de sorvete com o sabor tradicional')
    acumulador = acumulador + 6 #valor do acumulador some com 6 do pedido atual

  elif sabor == 'tr' and quantidade == '2':
    print('Você escolheu 2 bolas de sorvete com o sabor tradicional')
    acumulador = acumulador + 11

  elif sabor == 'tr' and quantidade == '3':
    print('Você escolheu 3 bolas de sorvete com o sabor tradicional')
    acumulador = acumulador + 15

  elif sabor == 'pr' and quantidade == '1':
    print('Você escolheu 1 bola de sorvete com o sabor premium')
    acumulador = acumulador + 7

  elif sabor == 'pr' and quantidade == '2':
    print('Você escolheu 2 bolas de sorvete com o sabor premium')
    acumulador = acumulador + 13

  elif sabor == 'pr' and quantidade == '3':
    print('Você escolheu 3 bolas de sorvete com o sabor premium')
    acumulador = acumulador + 18

  elif sabor == 'es' and quantidade == '1':
    print('Você escolheu 1 bola de sorvete com o sabor especial')
    acumulador = acumulador + 8

  elif sabor == 'es' and quantidade == '2':
    print('Você escolheu 2 bolas de sorvete com o sabor especial')
    acumulador = acumulador + 15

  elif sabor == 'es' and quantidade == '3':
    print('Você escolheu 2 bolas de sorvete com o sabor especial')
    acumulador = acumulador + 21

  pedir_mais = input('Deseja pedir algo a mais ? (S/outra tecla):')
  pedir_mais = pedir_mais.upper() #se caso a pessoa digitar com letras maiúsculas ou minúsculas não terá problema
  if pedir_mais == 'S':
    continue
  else:
    print('O valor total a ser pago é de R${:.2f}'.format(acumulador))
  break

"""#Exercício 3 da atividade prática"""

#exercício 3 da atividade prática
#início da função cachorro_peso()
def cachorro_peso():
  print('---------------Definição 1/3 - Peso do Cachorro---------------')
  while True:
    try:
      cachorro_peso = int(input('Digite o peso do cachorro (kg):'))
      if (cachorro_peso >=0)  and (cachorro_peso <= 3):
        return 40
      elif (cachorro_peso >3) and (cachorro_peso <=10):
          return 50
      elif (cachorro_peso >10) and (cachorro_peso <=30):
          return 60
      elif (cachorro_peso >30) and (cachorro_peso <=50):
          return 70
      else:
          print('Não comportamos cachorros maiores de 50kg.')
          continue #volta para o início
    except ValueError: #caso o usuário use letras ou números quebrados
        print('Valores não aceitos. Digite um número inteiro.')
#fim da função cachorro_peso()

#início da função cachorro_pelagem()
def cachorro_pelagem():
  print('---------------Definição 2/3 - Extras ------------------------')
  while True:
    cachorro_pelagem = input('Qual o tamanho do pelo do seu cachorro? \n' +
                            'c-curto\n' +
                            'm-médio\n' +
                            'l-longo\n' +
                             '>>')
    if (cachorro_pelagem == 'c'):
      return 1.0
    elif (cachorro_pelagem == 'm'):
      return 1.5
    elif (cachorro_pelagem == 'l'):
      return 2.0
    else:
      print('Digite c para pelo curto, m para pelo médio e l para pelo longo.')
#fim da função cachorro_pelo()

#início da função cachorro_extra()
def cachorro_extra():
  print('---------------Definição 3/3 - Extras ------------------------')
  acumulador = 0
  while True:
    cachorro_extra = input ('Deseja algum serviço extra?\n' +
                            '1- Cortar unhas\n' +
                            '2- Escovar os dentes\n' +
                            '3- Limpar as orelhas\n' +
                            '0- Nenhum extra\n'+
                            '>>')
    if cachorro_extra == '1':
      acumulador = acumulador + 10
    elif cachorro_extra == '2':
      acumulador = acumulador + 12
    elif cachorro_extra == '3':
      acumulador = acumulador + 15
    elif cachorro_extra == '0':
      return acumulador


#fim da função cachorro_extra()

#início do Main principal
print('Bem-vindo ao pet shop da Gabriela Thaís Boff')
peso= cachorro_peso()
pelo= cachorro_pelagem()
extra= cachorro_extra()
total= (pelo * peso) + extra
print('O valor total a ser pago é de R${:.2f}. (peso R$ {:.2f} , pelo R$ {:.2f} , extra R$ {:.2f}'.format(total,peso,pelo,extra))



"""#Exercício 4 da aula prática"""

#----------------Variáveis Globais-------------------
lista_colaborador = []
id_colaborador = [] #numerar todos os colaboradores c uma id global
#--------------Fim das Variáveis Globais-------------

#---------Início de cadastrar_colaborador []------------
def cadastrar_colaborador(id):
  print('Bem-vindo ao menu de cadastrar colaborador(es)')
  print('ID do colaborador: {}'.format(id))
  nome = input('Entre com o NOME do colaborador: ')
  id = input('Entre com a ID do colaborador: ')
  setor = int(input('Entre com o SETOR do colaborador: '))
  dicionario_colaborador = { 'id' : id_colaborador,
                            'nome' : nome,
                            'setor' : setor,
                            'setor' : setor}
  lista_colaborador.append(dicionario_colaborador.copy())
#---------Fim de cadastrar_colaborador []---------------

#---------Início de consultar_colaborador []------------
def consultar_colaborador():
  print('Bem-vindo ao menu de consultar colaborador(es)')
  while True:
    opcao_consultar = input('Escolha a opção desejada:\n'+
                         '1- Consultar todos os colaboradores\n'+
                         '2- Consultar por ID do(s) colaborador(es)\n'+
                         '3- Consultar por Setor do(s) colaborador(es)\n'+
                         '4- Retornar ao menu\n'+
                         '>>')
    if opcao_consultar == '1':
      print('Você escolheu consultar todos os coladoradores')
      for colaborador in lista_colaborador:
        print('--------------------------')
        for key, value in colaborador.items():
          print('{} : {}'.format(key,value))
        print('--------------------------')
    elif opcao_consultar == '2':
      print('Você escolheu consultar os coladoradores por ID')
      valor_desejado = input('Entre com a ID desejada: ')
      for colaborador in lista_colaborador:
        if colaborador['id'] == valor_desejado:
          print('--------------------------')
          for key, value in colaborador.items():
            print('{} : {}'.format(key,value))
          print('--------------------------')
    elif opcao_consultar == '3':
      print('Você escolheu consultar os coladoradores por Setor')
      valor_desejado = input('Entre com o setor desejado: ')
      for colaborador in lista_colaborador:
        if colaborador['setor'] == valor_desejado:
          print('--------------------------')
          for key, value in colaborador.items():
            print('{} : {}'.format(key,value))
          print('--------------------------')
    elif opcao_consultar == '4':
      return #sai da função consultar e volta para o menu
    else:
      print('Opção inválida. Digite novamente.')
      continue
#---------Fim de consultar_colaborador []---------------

#---------Início de remover_colaborador []--------------
def remover_colaborador():
    print('Bem-vindo ao menu de remover colaborador(es)')
    valor_desejado = int(input('Entre com a ID do colaborador que deseja remover: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == valor_desejado:
            lista_colaborador.remove(colaborador)  # Remove o colaborador da lista
            print('Colaborador removido')
            return  # Retorna após remover o colaborador
#---------Fim de remover_colaborador []-------------------

#-----------------Início de Main []-----------------------
print('Bem-vinda ao menu Gabriela Thaís Boff')
while True:
  opcao_principal = input('Escolha a opção desejada:\n'+
                         '1- Cadastrar colaborador\n'+
                         '2- Consultar colaborador(es)\n'+
                         '3- Remover colaborador\n'+
                         '4-Sair\n'+
                         '>>')
  if opcao_principal == '1':
    id_colaborador = id_colaborador
    cadastrar_colaborador(id_colaborador)
  elif opcao_principal == '2':
      consultar_colaborador()
  elif opcao_principal == '3':
      remover_colaborador
  elif opcao_principal == '4':
    break #encerra o menu principal
  else:
    print('Opção inválida. Digite novamente.')
    continue
#-------------------Fim de Main []------------------------

# ----------------Variáveis Globais-------------------
lista_colaborador = []
id_colaborador = 1  # Inicializa a ID do colaborador com 1
# --------------Fim das Variáveis Globais-------------

# ---------Início de cadastrar_colaborador []------------
def cadastrar_colaborador(id_colab):
    global id_colaborador  # Usar a variável global
    print('Bem-vindo ao menu de cadastrar colaborador(es)')
    print('ID do colaborador: {}'.format(id_colab))
    nome = input('Entre com o NOME do colaborador: ')
    setor = int(input('Entre com o SETOR do colaborador: '))
    dicionario_colaborador = {'id': id_colab,
                              'nome': nome,
                              'setor': setor}
    lista_colaborador.append(dicionario_colaborador)
    id_colaborador += 1  # Incrementa a ID para o próximo colaborador


# ---------Fim de cadastrar_colaborador []---------------

# ---------Início de consultar_colaborador []------------
def consultar_colaborador():
    print('Bem-vindo ao menu de consultar colaborador(es)')
    while True:
        opcao_consultar = input('Escolha a opção desejada:\n' +
                               '1- Consultar todos os colaboradores\n' +
                               '2- Consultar por ID do(s) colaborador(es)\n' +
                               '3- Consultar por Setor do(s) colaborador(es)\n' +
                               '4- Retornar ao menu\n' +
                               '>>')
        if opcao_consultar == '1':
            print('Você escolheu consultar todos os colaboradores')
            for colaborador in lista_colaborador:
                print('--------------------------')
                for key, value in colaborador.items():
                    print('{} : {}'.format(key, value))
                print('--------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu consultar os colaboradores por ID')
            valor_desejado = input('Entre com a ID desejada: ')
            for colaborador in lista_colaborador:
                if colaborador['id'] == valor_desejado:
                    print('--------------------------')
                    for key, value in colaborador.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu consultar os colaboradores por Setor')
            valor_desejado = int(input('Entre com o setor desejado: '))
            for colaborador in lista_colaborador:
                if colaborador['setor'] == valor_desejado:
                    print('--------------------------')
                    for key, value in colaborador.items():
                        print('{} : {}'.format(key, value))
                    print('--------------------------')
        elif opcao_consultar == '4':
            return  # sai da função consultar e volta para o menu
        else:
            print('Opção inválida. Digite novamente.')
            continue


# ---------Fim de consultar_colaborador []---------------

# ---------Início de remover_colaborador []--------------
def remover_colaborador():
    print('Bem-vindo ao menu de remover colaborador(es)')
    valor_desejado = int(input('Entre com a ID do colaborador que deseja remover: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == valor_desejado:
            lista_colaborador.remove(colaborador)  # Remove o colaborador da lista
            print('Colaborador removido')
            return  # Retorna após remover o colaborador
    print('Colaborador não encontrado')


# ---------Fim de remover_colaborador []-----------------

# -----------------Início de Main []-----------------------
print('Bem-vinda ao menu Gabriela Thaís Boff')
while True:
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1- Cadastrar colaborador\n' +
                            '2- Consultar colaborador(es)\n' +
                            '3- Remover colaborador\n' +
                            '4- Sair\n' +
                            '>>')
    if opcao_principal == '1':
        cadastrar_colaborador(id_colaborador)
    elif opcao_principal == '2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break  # encerra o menu principal
    else:
        print('Opção inválida. Digite novamente.')
        continue
# -------------------Fim de Main []------------------------