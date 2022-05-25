# Task 1

Projeto realizado em python3 por Amanda Lucio e Nayara Gomes.

## Table of Contents:
- [Sobre](#Sobre)
- [Como usar](#Como-usar)
- [Como rodar](#Como-Rodar)
- [Exemplo entrada e saída](#Exemplo)


## Sobre

O projeto 3 calcula o valor do y aproximado referente a um xi de entrada.

## Como usar

O projeto possui uma pasta para [inputs](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/files/inputs), na mesma você precisará alterar o conteúdo dos arquivos .dat referente ao pairs. Além disso, é necessário alterar o arquivo de [configurações](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/blob/master/files/inputs/config.json) para selecionar qual método será utilizado e o valor de xi para qual deseja calcula y. Além disso, se o método escolhido for regressão, é nessário adaptar os termos da lista retornada na função [fatores_function](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/blob/master/src/utils/matrix_operations.py#L368) e os fatores da função [value_function](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/blob/master/src/utils/matrix_operations.py#L372)

## Como rodar

Para rodar basta usar o comando abaixo:

```sh
$ python runner.py
> Escolha a task desejada
```

Desta forma, basta digitar o número da task correspondente:

- 1. [Task1](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/src/task_1)
- 2. [Task2](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/src/task_2)
- 3. [Task3](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/src/task_3)

## Exemplo

- [Entrada](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/files/inputs/Teste_3)
- [Saída](https://github.com/AmandaACLucio/Algebra-Linear-Computacional/tree/master/files/outputs/Teste_3)