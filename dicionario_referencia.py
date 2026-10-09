clientes = [
    {"nome":"Ana","cel":"3490","empresa":"FIAT"},
    {"nome":"Maria","cel":"3090","empresa":"INTEL"},
    {"nome":"Lucas","cel":"9034","empresa":"SEBRAE"},
    {"nome":"Felipe","cel":"9030","empresa":"INTEL"}
]

empresa_digitada = input("Digite o nome da empresa")
for cliente in clientes:
    if cliente["empresa"] == empresa_digitada:
        print(cliente)

#cadastrar cliente

pessoa = input("Qual nome da pessoa a ser cadastrada? ")
telefone = input("Qual o telefone da pessoa? ")
empresa = input("Qual o nome da empresa? ")

novo_cliente = {
    "nome": pessoa,
    "cel": telefone,
    "empresa": empresa
}

clientes.append(novo_cliente)
print(clientes)

#remover cliente

nome_cliente = input("Digite o nome do cliente a ser excluido ")
for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove(cliente)
        break

print(clientes)