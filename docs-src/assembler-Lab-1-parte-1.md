# parte 1

Agora iremos desenvolver um programa em java que será capaz de ler nossos programas  `.nasm` e converter eles para `.hack` (binário). Nosso arquivo `.hack` é um arquivo de **texto** que possui apenas `1`s e `0`s. Cada linha desse arquivo `.hack` é uma instrução a ser armazenada na memória ROM e executado pela CPU.

Exemplo de um arquivo `.hack`:

```
000000000000000101
100101100000010000
000000000000000001
100000000000100000
000000000000001011
```

> Você pode abrir seus arquivos .hack, basta ir em `E-Assembly/bin/hack/` que vai encontrar seus binários (executáveis).

O arquivo `.hack` é um formato que não conseguimos fazer o download para a FPGA, então é necessário convertemos esse formato em um que o Quartus entenda. Esse formato do Quartus é chamado de `.mif` e é gerado automaticamente pelos scripts de teste, esse arquivo `.mif` é similar ao `.hack` salvo um cabeçalho e a indicação do endereço na qual a linha deve ser salva:

```
WIDTH=18;
DEPTH=5;

ADDRESS_RADIX=UNS;
DATA_RADIX=BIN;

CONTENT BEGIN
  0 : 000000000000000101;
  1 : 100101100000010000;
  2 : 000000000000000001;
  3 : 100000000000100000;
  4 : 000000000000001011;
END;
```

!!! info
    O Assembler de vocês deve gerar um arquivo `.hack`. A conversão para o `.mif` é feita pelos scripts em python já fornecidos (`./testeAssembly.py`)


```
       assembler        script python
.nasm ---------> .hack --------> .mif 
                                   v
                                   |---------> FPGA
                                   |---------> SIMULADOR
```

## Assembler

O assembler será um programa escrito em java e que foi estruturado em **quatro classes**:
    
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

Note que o 'orquestrador' da montagem (esse é o termo em português utilizado) é a classe 'Assemble', nela que estará toda a lógica de montagem acessoada pelas demais classes. 

### Próximos passos

Agora vamos configurar a ide para podermos trabalhar no código java, siga para a próxima parte.
