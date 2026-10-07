from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

estoque = {}

def atualizar_quantidade(produto):
    """
    Atualiza a quantidade de um produto no estoque.

    Solicita uma nova quantidade ao usuário e valida se o valor informado
    é um número inteiro não negativo. Caso seja informado um valor inválido,
    solicita uma nova entrada. Ao final, atualiza a quantidade do produto
    no estoque.
    """
    while True:
        try:
            nova_quantidade = int(input("Quantidade atualizada: "))

        except ValueError:
            msg_erro("Digite um valor válido.")
            continue

        if nova_quantidade < 0:
            msg_erro("A quantidade não pode ser negativa.")
            continue
        break

    estoque[produto]['quantidade'] = nova_quantidade


def atualizar_preco(produto):
    """
    Atualiza o preço de um produto.

    Solicita um novo preço e valida se o valor informado é válido
    e não negativo. Após a validação, atualiza o preço do produto
    no estoque.
    """
    while True:
        try:
            novo_preco = float(input("Preço atualizado: "))

        except ValueError:
            msg_erro("Digite um valor válido.")
            continue

        if novo_preco < 0:
            msg_erro("O preço não pode ser negativo.")
            continue
        break

    estoque[produto]['preco'] = novo_preco


def confirmar_remocao(produto):
    """
    Confirma com o usuário a remoção de um produto do estoque.

    Solicita uma confirmação antes de remover o produto informado.
    Caso a remoção seja confirmada, remove o produto do estoque e
    exibe uma mensagem de sucesso. Caso contrário, mantém o produto
    no estoque. Também trata entradas inválidas, solicitando uma nova
    resposta.
    """
    while True:
        linha_separacao()
        console.print("(Responda com SIM ou NÃO)", style="bold")
        escolha = input(f"Tem certeza que deseja remover '{produto}'? ").strip().upper()

        if escolha in ["S", "SIM"]:
            console.print(f"Removendo {produto}...", style="yellow")
            pausa_execucao()

            estoque.pop(produto)

            console.print(f"'{produto}' removido com sucesso!", style="green")
            pausa_execucao()

        elif escolha in ["N", "NAO", "NÃO"]:
            console.print(f"Conforme desejado: [green]'{produto}' não foi removido![/]")
            pausa_execucao()

        else:
            msg_erro("Digite uma opção válida.")
            continue
        break


def continuar_operacao(msg = "Deseja continuar essa operação?"):
    """
    Solicita ao usuário uma confirmação para continuar uma operação.

    Aceita "S" ou "SIM" para continuar e "N", "NAO" ou "NÃO"
    para cancelar. Caso uma opção inválida seja informada, solicita
    uma nova resposta.
    """
    while True:
        linha_separacao()
        console.print("(Responda com SIM ou NÃO)", style="bold")
        escolha = input(msg).strip().upper()
        linha_separacao()

        if escolha in ["S", "SIM"]:
            return True

        elif escolha in ["N", "NAO", "NÃO"]:
            console.print("Operação finalizada com sucesso!", style="green")
            console.print("Retornando ao menu...", style="yellow")
            pausa_execucao()
            return False

        else:
            msg_erro("Digite uma opção válida.")


def msg_erro(msg = "Ocorreu um erro."):
    """
    Exibe uma mensagem de erro no terminal.

    A mensagem é apresentada em um painel com o título "ERRO"
    e borda vermelha. Após a exibição, o programa é pausado
    por um curto período.
    """
    console.print(
        Panel(
            msg,
            title="ERRO",
            style="bright_white",
            border_style="red",
            width=50
        )
    )
    pausa_execucao()


def msg_aviso(msg = "Ocorreu um empecilho."):
    """
    Exibe uma mensagem de aviso no terminal.

    A mensagem é apresentada em um painel com o título "AVISO"
    e borda amarela. Após a exibição, o programa é pausado
    por um curto período.
    """
    console.print(
        Panel(
            msg,
            title="AVISO",
            style="bright_white",
            border_style="yellow",
            width=50
        )
    )
    pausa_execucao()


def pausa_execucao(tempo = 1.5):
    """
    Pausa a execução do programa por um determinado período de tempo.

    Utiliza a função sleep() para interromper temporariamente a execução.
    Caso nenhum tempo seja informado, a pausa padrão será de 1,5 segundos.
    """
    sleep(tempo)


def linha_separacao(caractere = "-", tamanho = 50):
    """
    Exibe uma linha de separação no terminal.

    O caractere e o tamanho da linha podem ser personalizados.
    Por padrão, utiliza o caractere "-" e 50 repetições.
    """
    console.print(caractere * tamanho, style="grey50")


def menu():
    """
    Controla o sistema de gerenciamento de estoque.

    Exibe as opções disponíveis, recebe a escolha do usuário e executa
    a funcionalidade correspondente até que a opção de saída seja selecionada.
    """
    while True:
        console.print(
            Panel(
                "1 - Cadastrar produtos\n"
                "2 - Exibir estoque\n"
                "3 - Atualizar estoque\n"
                "4 - Remover produto\n"
                "5 - Buscar produto\n"
                "6 - Relatório do estoque\n"
                "7 - Sair",
                title="[blue]MENU[/]",
                style="bright_white",
                border_style="cyan",
                width=50
            )
        )

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))

            except ValueError:
                msg_erro("Digite um valor válido.")
                continue

            if opcao < 1 or opcao > 7:
                msg_erro("Digite uma opção válida.")
                continue
            break

        if opcao == 1:
            cadastrar_produtos()
        elif opcao == 2:
            exibir_estoque()
        elif opcao == 3:
            atualizar_estoque()
        elif opcao == 4:
            remover_produto()
        elif opcao == 5:
            buscar_produto()
        elif opcao == 6:
            relatorio_estoque()
        elif opcao == 7:
            console.print("Programa finalizado com sucesso!", style="green")
            console.print("Até breve.", style="yellow")
            break


def cadastrar_produtos():
    """
    Cadastra produtos no estoque.

    Solicita o nome do produto, a quantidade em estoque e o preço unitário.
    Ao final, permite ao usuário cadastrar outro produto ou retornar ao menu principal.
    """
    linha_separacao()
    console.print("Cadastro de produtos".center(50), style="bold blue")
    linha_separacao()

    while True:
        while True:
            nome = input("Nome do produto: ").strip().upper()

            if not nome:
                msg_erro("O nome não pode ficar vazio.")
                continue

            elif nome in estoque:
                msg_erro(f"'{nome}' já foi cadastrado.")
                continue
            break

        while True:
            try:
                quantidade = int(input("Quantidade em estoque: "))

            except ValueError:
                msg_erro("Digite um valor válido.")
                continue

            if quantidade < 0:
                msg_erro("A quantidade não pode ser negativa.")
                continue
            break

        while True:
            try:
                preco = float(input("Preço unitário: "))

            except ValueError:
                msg_erro("Digite um valor válido.")
                continue

            if preco < 0:
                msg_erro("O preço não pode ser negativo.")
                continue
            break

        estoque[nome] = {
            'quantidade': quantidade,
            'preco': preco
        }

        console.print("Cadastro efetuado com sucesso!", style="green")
        pausa_execucao()

        if not continuar_operacao("Deseja cadastrar outro produto? "):
            return


def exibir_estoque():
    """
    Exibe as informações dos produtos cadastrados no estoque.

    Mostra o nome, a quantidade, o preço e o valor total de cada produto.
    Caso não exista nenhum produto cadastrado, informa o usuário.
    """
    linha_separacao()
    console.print("Exibição do estoque".center(50), style="bold blue")
    linha_separacao()

    if not estoque:
        msg_aviso("Nenhum produto cadastrado no estoque!")

    else:
        tabela = Table(
            header_style="cyan",
            border_style="grey50"
        )

        tabela.add_column("Nome")
        tabela.add_column("Quantidade")
        tabela.add_column("Preço")
        tabela.add_column("Valor total")

        for nome, dados_produto in sorted(estoque.items()):
            quantidade = dados_produto['quantidade']
            preco = dados_produto['preco']
            valor_total = dados_produto['quantidade'] * dados_produto['preco']

            tabela.add_row(
                nome,
                f"{quantidade}",
                f"R${preco:.2f}",
                f"R${valor_total:.2f}",
                style="bright_white"
            )

        console.print(tabela)

    input("Pressione Enter para retornar ao menu.")
    console.print("Retornando ao menu...", style="yellow")
    pausa_execucao()


def atualizar_estoque():
    """
    Altera a quantidade, o preço ou ambos de um produto.

    Solicita o nome do produto e qual informação deseja alterar.
    Caso não existam produtos cadastrados ou o produto informado não seja encontrado, informa o usuário.
    """
    linha_separacao()
    console.print("Atualização do estoque".center(50), style="bold blue")
    linha_separacao()

    if not estoque:
        msg_aviso("Nenhum produto cadastrado no estoque!")
        input("Pressione Enter para retornar ao menu.")
        console.print("Retornando ao menu...", style="yellow")
        pausa_execucao()
        return

    while True:
        if len(estoque.keys()) <= 10:
            produtos_ordenados = sorted(estoque.keys())

            console.print(
                Panel(
                    "\n".join(produtos_ordenados),
                    title="[blue]PRODUTOS[/]",
                    style="bright_white",
                    border_style="cyan",
                    width=50
                )
            )

        while True:
            produto = input("Qual produto deseja atualizar: ").strip().upper()

            if not produto:
                msg_erro("O campo de busca não pode ficar vazio.")
                continue
            break

        if produto in estoque:
            console.print(
                Panel(
                    "1 - Atualizar quantidade\n"
                    "2 - Atualizar preço\n"
                    "3 - Atualizar quantidade e preço\n"
                    "4 - Retornar ao menu",
                    title="[blue]OPÇÕES[/]",
                    style="bright_white",
                    border_style="cyan",
                    width=50
                )
            )

            while True:
                try:
                    opcao = int(input("Escolha uma opção: "))

                except ValueError:
                    msg_erro("Digite um valor válido.")
                    continue

                if opcao not in [1, 2, 3, 4]:
                    msg_erro("Digite uma opção válida.")
                    continue
                break

            if opcao == 4:
                console.print("Retornando ao menu...", style="yellow")
                pausa_execucao()
                return

            linha_separacao()

            if opcao in [1, 3]:
                atualizar_quantidade(produto)

                if opcao == 1:
                    console.print("Atualizando quantidade...", style="yellow")
                    pausa_execucao()
                    console.print("Atualização efetuada com sucesso!", style="green")
                    pausa_execucao()

            if opcao in [2, 3]:
                atualizar_preco(produto)

                if opcao == 2:
                    console.print("Atualizando preço...", style="yellow")
                    pausa_execucao()
                    console.print("Atualização efetuada com sucesso!", style="green")
                    pausa_execucao()

                elif opcao == 3:
                    console.print("Atualizando quantidade e preço...", style="yellow")
                    pausa_execucao()
                    console.print("Atualização efetuada com sucesso!", style="green")
                    pausa_execucao()

        else:
            msg_aviso(f"'{produto}' não foi encontrado no estoque!")

        if not continuar_operacao("Deseja tentar atualizar outro produto? "):
            return


def remover_produto():
    """
    Excluir um produto do estoque.

    Solicita o nome do produto e confirma se o usuário deseja remover o produto do estoque.
    Caso não existam produtos cadastrados ou o produto informado não seja encontrado, informa o usuário.
    """
    linha_separacao()
    console.print("Remoção do produto".center(50), style="bold blue")
    linha_separacao()

    while True:
        if not estoque:
            msg_aviso("Nenhum produto cadastrado no estoque!")
            input("Pressione Enter para retornar ao menu.")
            console.print("Retornando ao menu...", style="yellow")
            pausa_execucao()
            return

        if len(estoque.keys()) <= 10:
            produtos_ordenados = sorted(estoque.keys())

            console.print(
                Panel(
                    "\n".join(produtos_ordenados),
                    title="[blue]PRODUTOS[/]",
                    style="bright_white",
                    border_style="cyan",
                    width=50
                )
            )

        while True:
            produto = input("Qual produto deseja remover: ").strip().upper()

            if not produto:
                msg_erro("O campo de busca não pode ficar vazio.")
                continue
            break

        if produto in estoque:
            confirmar_remocao(produto)

        else:
            msg_aviso(f"'{produto}' não foi encontrado no estoque!")

        if not continuar_operacao("Deseja tentar remover outro produto? "):
            return


def buscar_produto():
    """
    Pesquisa um produto específico no estoque.

    Solicita o nome do produto e exibe sua quantidade, preço unitário
    e valor total em estoque. Caso não existam produtos cadastrados
    ou o produto informado não seja encontrado, informa o usuário.
    """
    linha_separacao()
    console.print("Buscador de produtos".center(50), style="bold blue")
    linha_separacao()

    if not estoque:
        msg_aviso("Nenhum produto cadastrado no estoque!")
        input("Pressione Enter para retornar ao menu.")
        console.print("Retornando ao menu...", style="yellow")
        pausa_execucao()
        return

    while True:
        if len(estoque.keys()) <= 10:
            produtos_ordenados = sorted(estoque.keys())

            console.print(
                Panel(
                    "\n".join(produtos_ordenados),
                    title="[blue]PRODUTOS[/]",
                    style="bright_white",
                    border_style="cyan",
                    width=50
                )
            )

        while True:
            produto = input("Qual produto deseja buscar: ").strip().upper()

            if not produto:
                msg_erro("O campo de busca não pode ficar vazio.")
                continue
            break

        if produto in estoque:
            dados_produto = estoque[produto]
            quantidade = dados_produto['quantidade']
            preco = dados_produto['preco']
            valor_total = quantidade * preco

            tabela = Table(title=produto,
                           title_style="blue",
                           border_style="grey50",
                           header_style="cyan")

            tabela.add_column("Quantidade")
            tabela.add_column("Preço")
            tabela.add_column("Valor total")

            tabela.add_row(f"{quantidade}",
                           f"R${preco:.2f}",
                           f"R${valor_total:.2f}",
                           style="bright_white")

            console.print(tabela)

        else:
            msg_aviso(f"'{produto}' não foi encontrado no estoque!")

        if not continuar_operacao("Deseja pesquisar outro produto? "):
            return


def relatorio_estoque():
    """
    Exibe um relatório completo do estoque.

    Mostra a quantidade total de produtos, o valor total do estoque e
    lista os produtos com menos de 5 unidades. Caso o estoque esteja
    vazio, o usuário será informado.
    """
    linha_separacao()
    console.print("Relatório do estoque".center(50), style="bold blue")
    linha_separacao()

    if not estoque:
        msg_aviso("Nenhum produto cadastrado no estoque!")

    else:
        quantidade_unidades = 0
        valor_estoque = 0
        estoque_baixo = []

        for nome, dados_produto in estoque.items():
            quantidade_unidades += dados_produto['quantidade']
            valor_estoque += dados_produto['preco'] * dados_produto['quantidade']

            if dados_produto['quantidade'] < 5:
                estoque_baixo.append(nome)

        if estoque_baixo:
            produtos_ordenados = sorted(estoque_baixo)
            produtos_estoque_baixo = "\n".join(produtos_ordenados)
        else:
            produtos_estoque_baixo = "[yellow]Nenhum produto com estoque baixo.[/]"

        console.print(
            Panel(
                f"Quantidade total de produtos: {quantidade_unidades}\n"
                f"{'-' * 46}\n"
                f"Valor total do estoque: R${valor_estoque:.2f}\n"
                f"{'-' * 46}\n"      
                f"Produtos com menos de 5 unidades:\n" 
                f"{produtos_estoque_baixo}",
                style="bright_white",
                border_style="cyan",
                width=50
            )
        )

    input("Pressione Enter para retornar ao menu.")
    console.print("Retornando ao menu...", style="yellow")
    pausa_execucao()


menu()