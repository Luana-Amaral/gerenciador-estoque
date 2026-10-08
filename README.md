# 📦 Sistema de Gerenciamento de Estoque (Terminal)

Programa em Python, executado no terminal, para controlar o estoque de uma loja ou pequeno comércio. Ele permite cadastrar produtos, consultar, atualizar, remover e gerar um relatório simples do estoque, com uma interface colorida criada com a biblioteca [Rich](https://github.com/Textualize/rich).

---

## ✨ Funcionalidades

Ao iniciar o programa, aparece um menu com 7 opções:

| Opção | O que faz |
|-------|-----------|
| **1 - Cadastrar produtos** | Cadastra um produto informando nome, quantidade em estoque e preço unitário. Depois de cada cadastro, o programa pergunta se você quer cadastrar outro. |
| **2 - Exibir estoque** | Mostra uma tabela com todos os produtos (em ordem alfabética), exibindo nome, quantidade, preço e valor total (quantidade × preço). |
| **3 - Atualizar estoque** | Altera a quantidade, o preço, ou os dois, de um produto já cadastrado. |
| **4 - Remover produto** | Remove um produto do estoque, pedindo uma confirmação antes. |
| **5 - Buscar produto** | Procura um produto pelo nome e mostra sua quantidade, preço e valor total. |
| **6 - Relatório do estoque** | Mostra a quantidade total de unidades, o valor total do estoque e a lista de produtos com menos de 5 unidades. |
| **7 - Sair** | Encerra o programa. |

---

## 📸 Demonstração

### Cadastro de produtos

<img width="1313" height="635" alt="Captura de tela 2026-10-08 080113" src="https://github.com/user-attachments/assets/14b8bcc0-0775-457b-b017-31d1831ef5b6" />

Demonstra o cadastro de um novo produto no estoque.

### Exibição do estoque

<img width="1315" height="636" alt="Captura de tela 2026-10-08 081919" src="https://github.com/user-attachments/assets/7d59beb6-7ac6-4f80-b50a-c27b6d414035" />

Apresenta os produtos cadastrados, suas quantidades, preços e valores totais.

### Atualização do estoque

<img width="1316" height="638" alt="Captura de tela 2026-10-08 083526" src="https://github.com/user-attachments/assets/4c9b4e6f-3c88-4fb8-a406-1b235896d10f" />

Demonstra a validação de entrada e a atualização da quantidade de um produto.

---

## 🧠 Como o programa funciona

### Dados
Os produtos ficam guardados em um dicionário Python (`estoque`), neste formato:

```python
estoque = {
    "NOME DO PRODUTO": {
        "quantidade": 10,
        "preco": 5.50
    }
}
```

> ⚠️ **Importante:** os dados ficam **apenas na memória**. Isso significa que, ao fechar o programa, todos os produtos cadastrados são perdidos. O código não salva em arquivo nem em banco de dados.

### Regras e validações
- **Nomes de produtos** são convertidos para MAIÚSCULAS e têm espaços extras removidos nas pontas. Por isso, `arroz`, `Arroz` e `ARROZ` são tratados como o mesmo produto.
- O nome **não pode ficar vazio** e **não pode ser repetido** no cadastro.
- A **quantidade** deve ser um número inteiro maior ou igual a zero.
- O **preço** deve ser um número maior ou igual a zero. Use **ponto** como separador decimal (exemplo: `10.50`, e não `10,50`).
- Se você digitar algo inválido, o programa mostra uma mensagem de erro e pede o valor novamente.
- A busca, a atualização e a remoção usam o **nome exato** do produto (não existe busca por parte do nome).
- Quando há **10 produtos ou menos** no estoque, as telas de atualizar, remover e buscar mostram a lista de produtos cadastrados para facilitar a digitação.
- Nas perguntas de confirmação, as respostas aceitas são: `S` ou `SIM` para confirmar, e `N`, `NAO` ou `NÃO` para negar (maiúsculas e minúsculas não fazem diferença).

### Mensagens
- Mensagens de **erro** aparecem em um painel com borda **vermelha**.
- Mensagens de **aviso** (por exemplo, "Nenhum produto cadastrado no estoque!") aparecem em um painel com borda **amarela**.
- Mensagens de sucesso aparecem em **verde**.

---

## 🚀 Como executar

### Pré-requisitos
- [Python 3](https://www.python.org/downloads/) instalado
- A biblioteca **Rich**

### Passo a passo

1. Clone este repositório (ou baixe o arquivo do programa):

   ```bash
   git clone https://github.com/Luana-Amaral/gerenciador-estoque.git
   cd gerenciador-estoque
   ```

2. Instale a dependência:

   ```bash
   pip install rich
   ```

3. Execute o programa:

   ```bash
   python gerenciador_estoque.py
   ```

O menu principal será exibido automaticamente.

---

## 📖 Exemplo de uso

1. Escolha a opção **1** e cadastre, por exemplo, o produto `CANETA` com quantidade `20` e preço `2.50`.
2. Escolha a opção **2** para ver a tabela com o produto e seu valor total (`R$50.00`).
3. Escolha a opção **3** para alterar a quantidade ou o preço de `CANETA`.
4. Escolha a opção **6** para ver o relatório. Se algum produto tiver menos de 5 unidades, ele aparecerá na lista de estoque baixo.

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **[Rich](https://github.com/Textualize/rich)** – painéis, tabelas e textos coloridos no terminal
- Módulo `time` (`sleep`) da biblioteca padrão – pequenas pausas entre as mensagens

---

## 🗂️ Organização do código

O programa está em um único arquivo, com funções divididas por responsabilidade:

**Funções do menu principal**
- `menu()` – exibe o menu e chama a função da opção escolhida
- `cadastrar_produtos()`
- `exibir_estoque()`
- `atualizar_estoque()`
- `remover_produto()`
- `buscar_produto()`
- `relatorio_estoque()`

**Funções de apoio**
- `atualizar_quantidade(produto)` e `atualizar_preco(produto)` – pedem e validam o novo valor
- `confirmar_remocao(produto)` – pede confirmação antes de remover
- `continuar_operacao(msg)` – pergunta se o usuário quer repetir a operação
- `msg_erro(msg)` e `msg_aviso(msg)` – exibem os painéis de erro e aviso
- `pausa_execucao(tempo)` – pausa a execução por um curto período (padrão: 1,5 segundo)
- `linha_separacao(caractere, tamanho)` – desenha uma linha separadora no terminal
