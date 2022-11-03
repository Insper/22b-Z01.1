# G - Assembler

| Entrega      |
|--------------|
| 24/11 - Quinta |

![Assembly](figs/H-Assembler/sistema-assembler.png)

Nesse projeto iremos criar o programa *assembler* que é responsável por traduzir os códigos escrito em Assembly para a linguagem de máquina.

## Instruções 

As instruções técnicas de como começar o projeto estão no laboratório 16.

## Módulos a serem implementados

O projeto no total possui 5 módulos, sendo que o módulo `AssemblerZ01.java` já está pronto.

!!! tip
    Os módulos estão listados de maneira Top - Down

---------------------------
 
- AssemblerZ01
    - **Arquivo**   : `AssemblerZ01.java`
    - **Descrição** : Main do projeto. Recebe como parâmetro o nome do arquivo `.nasm` e o nome do arquivo binário de máquina `.hack`. a ser escrito, passa essas informações para a classe Assemble. Essa classe que inicializa a tabela de símbolo (`fillSymbolTable`) e chama o método `generateMachineCode` para efetivamente gerar o arquivo de saída.
    - **Dependências** : `Assemble.java`
    
!!! tip
    Já está pronto, não precisa mexer.
    
- Assemble
    - **Arquivo**: `Assemble.java`
    - **Descrição**: Classe responsável por criar o código de máquina, ela que **efetivamente** faz a varredura do arquivo `.nasm` de entrada e escreve o arquivo `.hack` de saída, gerando o código de máquina. 
    - **Dependências**: `Code.java`, `Parser.java`, `SymbolTable.java`
    
- Code
    - **Arquivo**   : `Code.java`
    - **Descrição** :  Traduz mnemônicos da linguagem assembly para códigos binários da arquitetura Z0.
    - **Dependências** : none
  
- Parser
    - **Arquivo**   : `Parser.java`
    - **Descrição** : Encapsula o código de leitura. Carrega as instruções na linguagem assembly, analisa, e oferece acesso as partes da instrução  (campos e símbolos). Além disso, remove todos os espaços em branco e comentários.
    - **Dependências** : none

- SymbolTable
    - **Arquivo**   : `SymbolTable.java`
    - **Descrição** :  Mantém uma tabela com a correspondência entre os rótulos simbólicos e endereços numéricos de memória.
    - **Dependências** : none

## Rubrica

| Conceito |                                                                                      |
|----------|--------------------------------------------------------------------------------------|
| A        | - Insere automaticamente um NOP após instrução de JUMP que não é seguida de nop.      |
|          | - Imprime mensagem de alerta que isso foi feito.                                     |
|          |                                                                                      |
| B        | - Verifica se instrução de jump é seguida de NOP, caso contrário dá erro             |
|          |                                                                                      |
| C        | - Criado assembler a partir de estrutura de código disponibilizada                   |
|          | - Todos os testes unitários passam no teste                                          |
|          | - Os testes de integração passam nos testes                                          |
|          | - Actions configurado corretamente                                                    |
|          |                                                                                      |
| D        | - Teste unitário ou Teste integração não passa                                       |
|          |                                                                                      |
| I        | - Menos da metade dos módulos funcionando                                            |

<!--
| A        | Proponha alguma outra melhoria e converse com o professor para saber se é valida.    |
|          |                                                                                      |
| B        | - Implementando modo verbose (-v) que possibilita analisar o assembler e suas etapas |
-->


### Formulários
<!--
 - [Scrum Master](https://forms.gle/qgUh31sUxEPzgwCX9)
 - [Desenvolvedores](https://forms.gle/jTrSaBegjKZZF6za6)
-->
