class FilaCircular:
    def __init__(self, capacidade):
        self.itens = [None] * capacidade
        self.capacidade = capacidade
        self.ini = 0
        self.fim = 0
        self.sequencia = 1

    def enfileirar(self, item):
        if self.cheia():
            raise Exception("Fila está cheia")
        self.itens[self.fim] = (self.sequencia, item)
        self.fim = (self.fim + 1) % self.capacidade
        self.sequencia += 1

    def desenfileirar(self):
        if self.vazia():
            raise Exception("Fila está vazia")
        item = self.itens[self.ini][1]
        self.itens[self.ini] = None
        self.ini = (self.ini + 1) % self.capacidade
        return item

    def vazia(self):
        return self.ini == self.fim and self.itens[self.ini] is None

    def cheia(self):
        return self.ini == self.fim and self.itens[self.ini] is not None

    def listar(self):
        if self.vazia():
            print("Fila vazia")
        else:
            lista = []
            for i in range(self.capacidade):
                if self.itens[i] is not None:
                    lista.append(str(self.itens[i]))
            inicio = self.ini
            fim = self.fim
            if inicio > fim:
                fim += self.capacidade
            elementos = "\n".join(lista)
            indicador = " " * (inicio * 4) + "^" + (fim - inicio - 1) * "    ^"
            print(f"{'Sequência':<10} {'Item':<10}")
            print(f"{elementos}")
            print(indicador)


fila = None


while True:
    print("\n==================================")
    print("         FILA CIRCULAR - MENU       ")
    print("==================================")
    print("\n1 - Criar Fila Circular")
    print("2 - Enfileirar um item")
    print("3 - Desenfileirar um item")
    print("4 - Verificar se a Fila está vazia")
    print("5 - Verificar se a Fila está cheia")
    print("6 - Listar Fila")
    print("7 - Sair")

    opcao = input("\nOpção: ")

    if opcao == "1":
        capacidade = int(input("Digite o tamanho da Fila: "))
        fila = FilaCircular(capacidade)
        print("\nFila criada com sucesso!✅")

    elif opcao == "2":
        if fila is None:
            print("\nFila ainda não foi criada ⚠️")
        else:
            item = input("Digite o item a ser enfileirado: ")
            try:
                fila.enfileirar(item)
                print(
                    f"\nItem '{item}' enfileirado com sucesso!✅(sequência: {fila.sequencia-1})")
            except Exception as e:
                print(f"\nErro ao enfileirar item ❌: {str(e)}")

    elif opcao == "3":
        if fila is None:
            print("\nFila ainda não foi criada ⚠️")
        else:
            try:
                item = fila.desenfileirar()
                print(f"\nItem '{item}' desenfileirado com sucesso!✅")
            except Exception as e:
                print(f"\nErro ao desenfileirar item ❌: {str(e)}")

    elif opcao == "4":
        if fila is None:
            print("\nFila ainda não foi criada ⚠️")
        elif fila.vazia():
            print("\nFila está vazia")
        else:
            print("\nFila não está vazia")

    elif opcao == "5":
        if fila is None:
            print("\nFila ainda não foi criada ⚠️")
        elif fila.cheia():
            print("\nFila está cheia")
        else:
            print("\nFila não está cheia")
    elif opcao == "6":
        if fila is None:
            print("\nFila ainda não foi criada")
        else:
            fila.listar()
    elif opcao == "7":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida, digite novamente.❌")
