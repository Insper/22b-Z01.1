# Lab 18: Vm Translator

O VMTranslator é um programa escrito em Java que faz a tradução de códigos escrito na linguagem VM definida no curso e traduz para linguagem Assembly do computador Z01.

## Testando

Para testar, basta executar o comando:

``` bash
$ ./testeVMtraslator.py
```

O teste executa:

```
             genJAR.py
                 |   
                 |   
                 V
                 
            VMTranslator          Assembler            Z01-Simulator  ------------------
 arquivo.vm -------------> .nasm -----------> .hack  > ------------>  - Verifica saída -
                                                                      ------------------
                 ^
                 |   
                 |- Desenvolvido no projeto I 
                                                                    
```

Para isso foi criado alguns programas (`H-VM/src/vmExamples/`) em VM muito específicos que testam somente um comando, ou uma parte da tradução do `VMTranslator`. Por exemplo o teste `SimpleAdd` possui somente a seguinte linha:

``` jar
add
```

Esse teste foi criado para testar o `Code.writeArithmetic` no caso de um comando `add`. Para isso, antes da execução desse código, o simulador faz a inicialização da RAM, simulando valores na pilha e já configurando o SP para uma situação real. A memória antes da execução da instrução add é a seguinte:

``` 
    0 : 0000000100000010;
  256 : 0000000000000010;
  257 : 0000000000000100;
  258 : 0000000000000000;
```

!!! note
    `I-VM/tests/tst/SimpleAdd/SimpleAdd0_in.mif`

Espera-se o resultado final após a execução do comando add :

```
    0 : 0000000100000001
  256 : 0000000000000110
```

!!! note ""
    A seguir uma lista de como cada parte do VMTranslator é testado:

    - `code.writePushPop`
        - pop
            - SimplePopTemp  : pop temp ...
            - SimplePopLocal : pop local ...
            - SimplePopThat  : pop that ...
            - SimplePopThis  : pop this ...
        - push
            - SimplePushConst : push constant .... 
            - SimplePushTemp  : push tempo ....
            - SimplePushLocal : push local ....
            - SimplePushArg   : push argument ...
            - SimplePushThis  : push this ...
            - SimplePushThat  : push that ...
    - code.writeArithmetic
        - SimpleAdd : add
        - SimpleNeg : neg
        - SimpleSub : sub
        - SimpleEq  : eq
        - SimpleGt  : gt
        - SimpleLt  : lt
        - SimpleAnd : and
        - SimpleOr  : or


## Implementando

Vamos agora fazer a implementação do comando `push constant 3` no VMtranslator.

1. Crie o projeto no IntelliJ da mesma maneira que do projeto do `Assembler`
    - o arquivo maven está na pasta `I-VMTranslator/VMtranslator`

Nesse projeto vocês terão que mexer apenas no `code.java`, os demais módulos já estão prontos (similar ao projeto do Assembler, temos nesse o `parser`, `VMTranslator`, ...).

## Editando o `code.java`

No `code.java` encontre a implementação do método `push` , linha 121

```java

public void writePushPop(Parser.CommandType command, String segment, Integer index) {
...
...
...
 else if (command == Parser.CommandType.C_PUSH) {
            commands.add(String.format("; %d - PUSH %s %d", lineCode++ ,segment, index));

            if (segment.equals("constant")) {
            
            }

```

Essa método é chamado sempre que um comando `push/pop` for interpretado, exemplo:

`push constant 3`

Os parâmetros recebidos são:

- command: `C_PUSH`
- segment: `constant`
- Index: `3`

Precisamos agora traduzir a execução desse comando em `vm` para `nasm` para que ele possa ser executado no nosso hardawre, isso é pode ser feito seguindos os passos a seguir:

1. Carregar o valor da constante em um registrador disponível
2. Busca no StackPointer(SP) o endereço da posição vazia da stack
3. Mover o valor do Index (no caso 3) para essa posição vazia
4. Incrementa SP em um


!!! example "Implementando"
    Faça a tradução do comando `push constant nnn` de VM para nasm, 
    para cada linha nasm você deve chamar a função `commands.add`, como no exemplo 
    a seguir:
    
    ```java
    commands.add("movw %A, %D");
    ```
    
    A tradução deve ser escrita dentro do `if (segment.equals("constant")) {....}`

??? tip "Solução"
    ```java
    // carrega a constant em %A e move para %D
    commands.add("leaw $"+ index + ", %A");
    commands.add("movw %A, %D");

    // carrega o calor do SP e move a constant
    // para o topo da pilha
    commands.add("leaw $0,%A");
    commands.add("movw (%A),%A");
    commands.add("movw %D,(%A)");

    // altera stack pointer: SP = SP + 1
    commands.add("leaw $0,%A");
    commands.add("movw (%A),%D");
    commands.add("incw %D");
    commands.add("movw %D, (%A)");
    ```

Para testar o projeto VMtranslator, não há testes unitários disponíveis, no entanto, podemos já realizar o teste de integração direto (simulação), usando o `testeVMtranslator.py`. No caso do `push constant`, temos o teste SimplePushConst, bastando apenas habilitar este teste na config (`tests/config.txt`). Se observar o arquivo, irá perceber que existem diversos outros testes básicos, como `SimplePushLocal`, `SimplePopLocal` e outros que podem ser habilitados conforme estes recursos forem implementados no seu VMtranslator.

