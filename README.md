<div align="center">

# 📒 Agenda de Contatos

**Agenda de contatos em linha de comando, escrita em Python puro.**
Cadastre, liste, pesquise, edite e apague contatos direto pelo terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-4D4D4D?style=for-the-badge&logo=gnubash&logoColor=white)
![Dependências](https://img.shields.io/badge/Depend%C3%AAncias-nenhuma-2EA44F?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-conclu%C3%ADdo-2EA44F?style=for-the-badge)

</div>

---

## 📖 Sobre o projeto

Projeto de estudo focado nos fundamentos de programação em Python: **funções, listas, laços, tratamento de erros e validação de entrada**. Tudo em um único arquivo (`agenda.py`), sem bibliotecas externas, para que o fluxo do programa possa ser lido de cima para baixo.

O código é organizado em **procedimentos** (executam uma ação) e **funções** (devolvem um valor), e cada bloco traz um cabeçalho de comentário com descrição, nome e tipo.

## ✨ Funcionalidades

| Opção | Ação | O que faz |
|:-----:|------|-----------|
| `1` | Adicionar contato | Pede nome, celular e e-mail e grava na agenda |
| `2` | Listar contatos | Mostra todos os contatos, ou avisa que a agenda está vazia |
| `3` | Pesquisar contato | Busca por nome, sem diferenciar maiúsculas de minúsculas |
| `4` | Apagar contato | Remove o contato encontrado pelo nome |
| `5` | Editar contato | Substitui nome, celular e e-mail de um contato existente |
| `0` | Sair | Encerra o programa |

Além disso, o menu **valida a entrada**: letras, campos vazios ou números fora do intervalo não quebram o programa, ele apenas pede de novo.

## 🚀 Como executar

**Pré-requisito:** [Python 3.8 ou superior](https://www.python.org/downloads/) instalado.

```bash
# 1. Clonar o repositório
git clone https://github.com/TrueBrick/agenda-contatos-cli.git

# 2. Entrar na pasta do projeto
cd agenda-contatos-cli

# 3. Executar
python agenda.py
```

> No Linux/macOS, use `python3 agenda.py` caso `python` não esteja disponível.

## 🖥️ Exemplo de uso

```text
1 - Adicionar novo contato
2 - Listar contatos
3 - Pesquisar contato
4 - Apagar contato
5 - Editar contato
0 - Sair
Escolha uma opção: 1
Digite o nome do contato: Ana Souza
Digite o número do celular: (34) 99999-1111
Digite o e-mail: ana@email.com
Contato adicionado com sucesso!

Escolha uma opção: 2
Nome: Ana Souza
Celular: (34) 99999-1111
Email: ana@email.com
--------------------

Escolha uma opção: 3
Digite o nome do contato: ana souza
Nome: Ana Souza
Celular: (34) 99999-1111
Email: ana@email.com

Escolha uma opção: 9
Digite um número entre 0 e 5.

Escolha uma opção: abc
Digite um número válido.
```

## 🧩 Como o código funciona

| Função | Tipo | Responsabilidade |
|--------|------|------------------|
| `novo()` | Procedimento | Coleta os dados e adiciona o contato à lista |
| `p_nome()` | Procedimento | Solicita o nome do contato ao usuário |
| `listar_dados(nome, celular, email)` | Procedimento | Imprime um único contato formatado |
| `listar()` | Procedimento | Percorre a agenda e imprime todos os contatos |
| `pesquisa(nome)` | Função | Devolve a posição do contato na lista, ou `None` |
| `pesquisar()` | Procedimento | Usa `pesquisa()` e exibe o resultado |
| `apagar()` | Procedimento | Usa `pesquisa()` e remove o contato com `del` |
| `editar()` | Procedimento | Usa `pesquisa()` e substitui os dados do contato |
| `validar(pergunta, inicia, fim)` | Função | Repete a pergunta até receber um inteiro válido no intervalo |
| `menu()` | Função | Exibe as opções e devolve a escolha validada |

Mais detalhes sobre estrutura, fluxo e decisões em [ARQUITETURA.md](ARQUITETURA.md).

## 🎓 Conceitos aplicados

- Funções com e sem retorno (procedimentos x funções)
- Listas aninhadas (`[nome, celular, email]`) e `enumerate()`
- Laços `while True` com `break`
- Tratamento de exceções com `try` / `except ValueError`
- Variável global com `global`
- Comparação sem diferenciar maiúsculas/minúsculas com `.lower()`
- f-strings e entrada de dados com `input()`

## ⚠️ Limitações conhecidas

- **Os dados vivem apenas na memória.** Ao encerrar o programa, a agenda é perdida.
- Contatos são localizados **pelo nome**; nomes repetidos retornam sempre o primeiro encontrado.
- Não há validação de formato para celular e e-mail.

## 🗺️ Próximos passos

- [ ] Salvar a agenda em arquivo (CSV ou JSON) para persistir os dados
- [ ] Ou migrar para banco de dados (SQLite)
- [ ] Validar formato de e-mail e telefone
- [ ] Trocar a lista de listas por dicionários ou classes (POO)
- [ ] Criar testes automatizados com `pytest`

## 👤 Autor

**Rodrigo Oliveira**
Em transição de carreira para Engenharia de Software · FIAP

[![GitHub](https://img.shields.io/badge/GitHub-TrueBrick-181717?style=flat-square&logo=github)](https://github.com/TrueBrick)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rodrigo%20Oliveira-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/rodrigo-oliveira-a923b8412/)
