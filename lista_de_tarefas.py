tarefas = [
    {"Titulo":"Estudar", "Conclusão":"Não", "Prioridade":"Alta"},
    {"Titulo":"Ler", "Conclusão":"Sim", "Prioridade":"Baixa"},
    {"Titulo":"Cuidar do pet", "Conclusão":"Sim", "Prioridade":"Alta"},
    {"Titulo":"Guardar as compras", "Conclusão":"Não", "Prioridade":"Baixa"}
]

def mostrar_todas():
    print(tarefas)

def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["Conclusão"] == "Sim":
            print(tarefa)

def mostrar_pendentes():
    for tarefa in tarefas:
        if tarefa["Conclusão"] == "Não":
            print(tarefa)

def mostrar_prioridade():
    prioridade_digitada = input("Você quer tarefas de prioridade Alta ou Baixa: ")
    for tarefa in tarefas:
        if tarefa["Prioridade"] == prioridade_digitada:
            print(tarefa)

def tarefa_nova():
    cadastro_tarefa = input("Nome da nova tarefa: ")
    conclusao_tarefa = input("Você já concluiu a tarefa? ")
    prioridade_tarefa = input("A prioridade da sua tarefa é: ")

    nova_tarefa = {
        "Título": cadastro_tarefa,
        "Conclusão": conclusao_tarefa,
        "Prioridade": prioridade_tarefa
    }
    tarefas.append(nova_tarefa)
    print(tarefas)

def finalizar_tarefas():
    for tarefa in tarefas:
            if tarefa["Conclusão"] == "Não":
                print(tarefa)
    titulo_digitado = input("Qual tarefa você quer finalizar: ")
    for tarefa in tarefas:
        if tarefa["Titulo"] == titulo_digitado:
            tarefa["Conclusão"] = "Sim"
            print(tarefa)

def remover():
    print(tarefas)
    remover_tarefa = input("Digite a tarefa que você quer excluir: ")
    for tarefa in tarefas:
        if tarefa["Titulo"] == remover_tarefa:
            tarefas.remove (tarefa)
            print(tarefas)

def sair():
    print("Saindo do Sistema...")



#Alternatiavs

while True:
    print("! ---> Lista de Tarefas <--- !")
    print("1 - Mostras todas as tarefas")
    print("2 - Mostrar tarefas concluidas")
    print("3 - Mostrar tarefas pendentes")
    print("4 - Mostrar tarefas com Prioridade")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefa")
    print("0 - Sair do sistema!")


#Digitando Opções

    opcao = input("Seleione uma das opções a cima! ")

    if opcao == "1":
        mostrar_todas()

    elif opcao == "2":
        mostrar_concluidas()

    elif opcao == "3":
        mostrar_pendentes()

    elif opcao == "4":
        mostrar_prioridade()

    elif opcao == "5":
        tarefa_nova()

    elif opcao == "6":
        finalizar_tarefas()

    elif opcao == "7":
        remover()

    elif opcao == "0":
        sair()
        