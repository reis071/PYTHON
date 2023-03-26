from Carro import Carro

con = []
loop = True

while loop:
    
    '''Aqui começa o programa no qual o usuario
    vai poder executar as opções presentes'''

    carro = Carro()
    print('(1) Cadastrar carro')
    print('(2) Listar carro')
    print('(3) Remover carro')
    print('(4) Modificar Carro')
    print('(5) Pesquisar Carro')
    print('(6) Encerrar programa')
    enter = input('Digite o numero: ')

    match enter:
        
        case '1':
            
            '''A 1° opção consiste em cadastrar o veiculo'''
            print('=== CADASTAR ===')
            nome_add = input('Digite o NOME do carro: ').title()

            while True:
              placa_add = input('Digite a PLACA do carro: ').upper()

              if len(placa_add) == 7:
                break

              else:
                print('Tem que ter total de 7 caracteres para registrar a PLACA!')

            fabricante_add = input('Digite o FABRICANTE do carro: ').title()
            modelo_add = input('Digite o MODELO do carro: ').title()
            cor_add = input('Digite o COR do carro: ').title()

            carro.add(nome_add,placa_add,fabricante_add,modelo_add,cor_add)
            
            con.append(carro.__dict__)
            
            
        case '2':
          '''A 2° opção consiste em imprimir todos os carros cadastrados'''
          print('{:<12} {:<12} {:<12} {:<15} {:<12} {:<12}'.format('Posição','Nome','Placa',
                                                                   'Fabricante','Modelo','Cor'))
          for b,p in enumerate(con):
            print('{:<12} {:<12} {:<12} {:<15} {:<12} {:<12}'.format(b,p['nome'],p['_Carro__placa'],
                                                           p['_Carro__fabricante'],p['modelo'],p['cor']))
            
            
        
        case '3':

          '''A 3° opção consiste em remover qualquer veiculo registrado'''

          remover = input('Digite a placa do carro que sera REMOVIDO!: ')

          encontrado = False

          for b,c in enumerate(con):
             if remover == c['_Carro__placa']:
                confirmacao = input('Certeza que deseja remover este veiculo? ')
                if confirmacao[0] in 'Ss':
                  encontrado = True
                  con.pop(b)
                  print('removido')

                elif confirmacao[0] in 'Nn':
                  encontrado = True
                  print('Remoção cancelada!')
                  
          if encontrado == False:
             print('Carro não encontrado')


        case '4': 
          '''A 4° opção é para modificar qualquer veiculo registrado'''

          alterar = input('Digite a PLACA do carro que sera MODIFICADO!: ').upper()

          encontrado = False

          for c in con:
             if alterar == c['_Carro__placa']:
                encontrado = True
                
                print('(1) Nome')
                print('(2) Placa')
                print('(3) Fabricante')
                print('(4) Modelo')
                print('(5) Cor')
                print('(6) Alterar todos atributos do carro')
                print('(7)Cancelar alteração')
                alter = input('Digite a opção para alterar oque deseja: ')

                match alter:
                   case '1':
                    nome_alt = input('ALTERE o NOME do carro: ').title()
                    c['nome'] = nome_alt

                   case '2':
                    while True:
                      placa_alt = input('Digite a PLACA do carro: ').upper()

                      if len(placa_alt) == 7:
                        c['_Carro__placa'] = placa_alt
                        break
                      
                      else:
                        print('Tem que ter total de 7 caracteres para MODIFICAR a PLACA!')

                   case '3':
                    fabricante_alt = input('ALTERE o FABRICANTE do carro: ').title()
                    c['_Carro__fabricante'] = fabricante_alt

                   case '4':
                    modelo_alt = input('ALTERE o MODELO do carro: ').title()
                    c['modelo'] = modelo_alt
                   
                   case '5':
                    cor_alt = input('ALTERE a COR do carro: ').title()
                    c['cor'] = cor_alt

                   case '6':
                     nome_alt = input('ALTERE o NOME do carro: ').title()
                     c['nome'] = nome_alt

                     while True:
                      placa_alt = input('Digite a PLACA do carro: ').upper()

                      if len(placa_alt) == 7:
                        c['_Carro__placa'] = placa_alt
                        break
                      
                      else:
                        print('Tem que ter total de 7 caracteres para MODIFICAR a PLACA!')

                     fabricante_alt = input('ALTERE o FABRICANTE do carro: ').title()
                     c['_Carro__fabricante'] = fabricante_alt

                     modelo_alt = input('ALTERE o MODELO do carro: ').title()
                     c['modelo'] = modelo_alt

                     cor_alt = input('ALTERE a COR do carro: ').title()
                     c['cor'] = cor_alt

                   case '7':
                     print('Alteração cancelada!')
                     break
                    
                   case _:
                    print('Tente novamente!')

                break
             
          if encontrado == False:
             print('Carro não encontrado')
              
        case '5':
          '''A 5° opção é para pesquisar e imprimir um carro registrado'''

          procurar = input('Digite a PLACA do carro que sera PESQUISADO!').upper()

          encontrado= False

          for b,c in enumerate(con):
            if procurar == c['_Carro__placa']:
             encontrado = True
             print('{:<12} {:<12} {:<12} {:<15} {:<12} {:<12}'.format('Posição','Nome','Placa',
                                                                   'Fabricante','Modelo','Cor'))
             print('{:<12} {:<12} {:<12} {:<15} {:<12} {:<12}'.format(b,c['nome'],c['_Carro__placa'],
                                                           c['_Carro__fabricante'],c['modelo'],c['cor']))
             
          if encontrado == False:
            print('Veiculo inexistente!')
            break

        case '6':
          '''A 6° opção encerra o programa'''
          print('Volte sempre!')
          loop = False

        case _:
          print('Tente novamente')
          
