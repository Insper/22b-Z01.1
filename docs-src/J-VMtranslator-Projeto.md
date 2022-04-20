# I - VM Translator

| Entrega      |
|--------------|
| 09/06 - Quarta |

Nesse projeto iremos criar o programa *VM translator* que é responsável por traduzir os códigos escrito em linguagem VM de pilha para a linguagem assembly.

## Instruções 

As instruções técnicas referente ao projeto está no [lab 18](VMtranslator-Lab-1-old.md).

## Módulos a serem implementados

> **Apenas o `Code.java`.**

O projeto no total possui 5 módulos, sendo que o módulo `VMTranslator.java`, `VMtranslate.java`, `Parser.java`  e `Error.java` já estão foram entregues implementados.

> Os módulos estão listados de maneira Top - Down

---------------------------
 
- VMTranslator
    - **Arquivo**   : `VMTranslator.java`
    - **Descrição** : Main do projeto. Recebe como parâmetro o nome do arquivo `.vm` (ou diretório) e o nome do arquivo binário assembly (`.nasm`) a ser escrito, passa essas informações para a classe VMtranslate. 
    - **Dependências** : `VMtranslate.java`
    
- VMtranslate
    - **Arquivo**   : `VMtranslate.java`
    - **Descrição** : Classe responsável por criar o código assembly, ela que **efetivamente** faz a varredura do arquivo .vm de entrada e escreve o arquivo .nasm de saída, gerando a tradução vm -> nasm. 
    - **Dependências** : `Code.java`, `Parser.java`
    
- Code
    - **Arquivo**   : `Code.java`
    - **Descrição** :  Traduz comandos da linguagem vm para os comandos em nasm que a executam.
    - **Dependências** : None
  
- Parser
    - **Arquivo**   : `Parser.java`
    - **Descrição** : Encapsula o código de leitura. Carrega as instruções na linguagem vm, analisa, e oferece acesso as partes da instrução  (campos e símbolos). Além disso, remove todos os espaços em branco e comentários.
    - **Dependências** : none

## Sugestão de implementação (partes)

Sugerimos que o `VMTranslator` seja implementado em duas partes, a primeira implementa somente o *Parser.java* e operações aritméticas e `push/pop`. A segunda parte faz a implementação de funções, goto e chamada de funções.

## Parte 1 - Conceito C
   
- Code.writeArithmetic()
- Code.writePushPop()

## Parte 2 - Conceito B

- Code.writeGoto()
- Code.writeIf()

## Parte 3 - Conceito A

- Code.writeCall()
- Code.writeReturn()
- Code.writeFunction()

# Rubricas para avaliação de projetos

Cada integrante do grupo irá receber duas notas: uma referente ao desenvolvimento total do projeto (Projeto) e outra referente a sua participação individual no grupo (que depende do seu papel).

## Projeto

| Conceito |                                           |
|----------|-------------------------------------------|
| I        | - Menos da metade dos módulos funcionando |
|          |                                           |
| D        | - writeArithmetic OU writePushPop  |
|          |                                           |
| C        | - writeArithmetic E writePushPop           |
|          |                                           |
| B        | - writeLabel, writeGoto, writeIf          |
|          |                                           |
| A        | - writeCall, writeReturn, writeFunction   |

## Para testar 

A seguir os testes que devem passar para cada nota :

### C

- SimpleAdd
- SimpleNeg
- SimpleSub
- SimpleEq 
- SimpleGt 
- SimpleLt 
- SimpleAnd
- SimpleOr 
- SimplePushConst
- SimplePushTemp 
- SimplePushLocal
- SimplePushArg 
- SimplePushThis
- SimplePushThat
- SimplePopTemp 
- SimplePopLocal
- SimplePopThat 
- SimplePopThis 
- SimplePushAdd 
- SimplePopPointer
- ~StackTest~ (opcional) 

### B

- BasicLoop 

#### A

- SimpleFunction
- StaticsTest
- Mult 
- 1a-Add
- 1b-Add
- 2a-Calculadora 
- 2b-Calculadora 
- 2c-Calculadora 
- 2d-Calculadora 
- SimpleGoto 
- SimpleIfGoto


### Formulários
 - [Scrum Master](https://docs.google.com/forms/d/e/1FAIpQLSdKx-e5QB_YWYdH6n8P-PZsvwp2PJIGy6FOmBs2PCf_uRbuXw/viewform?usp=sf_link)
 - [Desenvolvedores](https://docs.google.com/forms/d/e/1FAIpQLSduO77Uzt0i8weuF1Jj-9T2dY868zRn_FWT4HdgE7dNf_VT4w/viewform?usp=sf_link)

