agenda = [] # Criando uma lista vazia.

#Definição das funções

# Descrição: Este procedimento cria um novo contato na agenda.
# Nome: novo()
# Tipo: Procedimento
def novo():
    global agenda # Definindo variavel agenda como Global.
    nome = p_nome() # Chamando a função p_nome() para pegar o nome do contato.
    celular = input("Digite o número do celular: ") # Solicitando ao usuário o número do celular.
    email = input("Digite o e-mail: ") # Solicitando ao usuário o e-mail.
    agenda.append([nome, celular, email]) # Adicionando o contato na agenda.
    print("Contato adicionado com sucesso!") # Mensagem de sucesso.

# Descrição: Este procedimento solicita ao usuário o nome do contato.
# Nome: p_nome()
# Tipo: Procedimento
def p_nome():
    return(input("Digite o nome do contato: "))

# Descrição: Este procedimento lista um registro.
# Nome: listar_dados(nome, celular, email)
# Tipo: Procedimento
def listar_dados(nome, celular, email):
    print(f"Nome: {nome}")
    print(f"Celular: {celular}")
    print(f"Email: {email}")

# Descrição: Este procedimento lista todos os contatos da agenda.
# Nome: listar()    
# Tipo: Procedimento
def listar(): #Função para listar os contatos da agenda.
    global agenda # Definindo variavel agenda como Global.
    if len(agenda) == 0: # Verificando se a agenda está vazia.
        print("Agenda vazia!") # Mensagem de aviso.
    else:
        for contato in agenda: # Percorrendo a lista de contatos.
            listar_dados(contato[0], contato[1], contato[2]) # Chamando a função listar_dados() para listar os dados do contato.
            print("--------------------") # Separador entre os contatos.

# Descrição: Este procedimento busca um contato na agenda.
# Nome: pesquisa(nome): int
# Tipo: Função
def pesquisa(nome): #Função para pesquisar um contato na agenda.
    global agenda # Definindo variavel agenda como Global.
    for i, contato in enumerate(agenda): # Percorrendo a lista de contatos.
        if contato[0].lower() == nome.lower(): # Verificando se o nome do contato é igual ao nome pesquisado.
            return i # Retornando o índice do contato encontrado.
    return None # Retornando None caso o contato não seja encontrado.

# Descrição: Este procedimento exibe o registro ou mensagem de insucesso
# Nome: pesquisar()
# Tipo: Procedimento
def pesquisar(): #Função para pesquisar um contato na agenda.
    # pesquisa o contato na agenda
    p = pesquisa(p_nome()) # Chamando a função pesquisa() para pesquisar o contato.
    if p is not None: # Verificando se o contato foi encontrado.
        listar_dados(agenda[p][0], agenda[p][1], agenda[p][2]) # Chamando a função listar_dados() para listar os dados do contato.
    else:
        print("Contato não encontrado!") # Mensagem de aviso.

# Descrição: Este procedimento apaga um contato da agenda.
# Nome: apagar()
# Tipo: Procedimento
def apagar(): #Função para apagar um contato da agenda.
    global agenda # Definindo variavel agenda como Global.
    nome = p_nome() # Chamando a função p_nome() para pegar o nome do contato.
    p = pesquisa(nome) # Chamando a função pesquisa() para pesquisar o contato.
    if p is not None: # Verificando se o contato foi encontrado.
        del agenda[p] # Apagando o contato da agenda.
        print("Contato apagado com sucesso!") # Mensagem de sucesso.
    else:
        print("Contato não encontrado!") # Mensagem de aviso.

# Descrição: Este procedimento altera um contato da agenda.
# Nome: editar()
# Tipo: Procedimento
def editar(): #Função para editar um contato da agenda.
    p = pesquisa(p_nome()) # Chamando a função pesquisa() para pesquisar o contato.
    if p is not None: # Verificando se o contato foi encontrado.
        nome = agenda[p][0] # Pegando o nome do contato.
        celular = agenda[p][1] # Pegando o número do celular do contato.
        email = agenda[p][2] # Pegando o e-mail do contato.
        print("Digite os novos dados do contato:") # Mensagem de aviso.
        nome = p_nome() # Chamando a função p_nome() para pegar o nome do contato.
        celular = input("Digite o número do celular: ") # Solicitando ao usuário o número do celular.
        email = input("Digite o e-mail: ") # Solicitando ao usuário o e-mail.
        agenda[p] = [nome, celular, email] # Alterando os dados do contato na agenda.
        print("Contato alterado com sucesso!") # Mensagem de sucesso.
    else:
        print("Contato não encontrado!") # Mensagem de aviso.

# Descrição: Esta função valida se o item digitado foi valido.
# Nome: validar(pergunta,inicia, fim): int
# Tipo: Função
def validar(pergunta, inicia, fim): #Função para validar a entrada do usuário.
    while True: # Loop infinito.
        try: # Tentando executar o código.
            valor = int(input(pergunta)) # Solicitando ao usuário a entrada de um número inteiro.
            if valor >= inicia and valor <= fim: # Verificando se o número digitado está dentro do intervalo permitido.
                return valor # Retornando o número digitado.
            else:
                print(f"Digite um número entre {inicia} e {fim}.") # Mensagem de aviso.
        except ValueError: # Caso ocorra um erro de valor.
            print("Digite um número válido.") # Mensagem de aviso.

# Descrição: Esta função retorna o item do menu ou 0 para invalido
# Nome: menu(pergunta, inicia, fim): int
# Tipo: Função
def menu(): #Função para exibir o menu de opções.
    print("1 - Adicionar novo contato") # Opção 1 do menu.
    print("2 - Listar contatos") # Opção 2 do menu.
    print("3 - Pesquisar contato") # Opção 3 do menu.
    print("4 - Apagar contato") # Opção 4 do menu.
    print("5 - Editar contato") # Opção 5 do menu.
    print("0 - Sair") # Opção 0 do menu.
    return validar("Escolha uma opção: ", 0, 5) # Chamando a função validar() para validar a entrada do usuário. 

# PROGRAMA PRINCIPAL
while True: # Loop infinito.
    opcao = menu() # Chamando a função menu() para exibir o menu de opções.
    if opcao == 1: # Verificando se a opção escolhida é 1.
        novo() # Chamando a função novo() para adicionar um novo contato.
    elif opcao == 2: # Verificando se a opção escolhida é 2.
        listar() # Chamando a função listar() para listar os contatos da agenda.
    elif opcao == 3: # Verificando se a opção escolhida é 3.
        pesquisar() # Chamando a função pesquisar() para pesquisar um contato na agenda.
    elif opcao == 4: # Verificando se a opção escolhida é 4.
        apagar() # Chamando a função apagar() para apagar um contato da agenda.
    elif opcao == 5: # Verificando se a opção escolhida é 5.
        editar() # Chamando a função editar() para editar um contato da agenda.
    elif opcao == 0: # Verificando se a opção escolhida é 0.
        print("Saindo do programa...") # Mensagem de aviso.
        break # Saindo do loop infinito.