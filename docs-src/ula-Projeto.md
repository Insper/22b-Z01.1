# C - ULA

| Entrega      |
|--------------|
| 20/09 - Terça |

![ULA](figs/D-ULA/D-sistema-ula.png)

Neste projeto seu grupo terá que desenvolver os componentes para a implementação de uma unidade lógica e aritmética (ULA) de 16 bit (proposta pelo livro texto) que será capaz de realizar operações binárias muito simples porém que possibilitará realizarmos muitas coisas!

!!! warning
    O grupo deve eleger um novo scrum master para essa entrega (diferente do projeto B).

!!! note 
    Nas discussões com o grupo, o scrum master deverá definir 
    os módulos que cada integrante irá desenvolver. 
    Crie uma rotina para commits e pull-requests.
  
!!! tip
    Você é `Scrum Master` e não sabe por onde começar? 
    De uma olhada nessas dicas:
    [Vixi! Sou Scrum Master](https://insper.github.io/Z01.1/Util-Comecando-novo-projeto/)
    
!!! tip
    Sempre teste os módulos e verifique se está funcionando como o esperado.

## Instruções 

A pasta do projeto C, no repositório Z01, possui a seguinte estrutura:

```bash
/C-ULA
    testeULA.py
    programFPGA.py
    /Quartus
    /src
        *.vhd
    /teste_cocotb
        tests.py
```

1. Quartus: Projeto Quartus que faz uso dos arquivos VHDL localizados em src/rtl/*.vhd;
1. testeULA.py: Scripts em python que automatizam a execução dos testes;
1. src/*.vhd: Arquivos VHDL que serão implementados pelo grupo;
1. teste_cocotb/tests.py: Arquivo python que realizam o teste lógico nos arquivos do rtl.

### Executando o Script de Teste 

Abra o terminal na pasta `C-UnidadeLogicaAritmetica/`  e execute o script python localizado nessa pasta:

```bash
$ ./testeULA.py
```

O mesmo irá compilar os arquivos `src/rtl/*.vhd` e executar os testes unitários em cada um deles. Nesse momento do teste, como os módulos não estão implementados, o resultado deverá ser falho.

Esse comando executa um teste unitário em cada um dos módulos, verificando se sua implementação está correta. O resultado é exibido na tela como : **Passed** ou **Failed**.

# O que deve ser feito: 

Além de implementar os módulos, deve-se gerar uma imagem com a forma de onda de cada um desses módulos. Para cada nova implementação deve-se criar um novo branch e remover o comentário do arquivo: `tests/config.txt` somente o módulo que está sendo implementado. 

Note que é possível reaproveitar, via **port map**, os módulos do projeto anterior (C). Esses módulos anteriores **já estão incluídos automaticamente (pelo script)** na compilação dos módulos do projeto C.

## Módulos 

!!! note
    Esses arquivos estão localizados em `C-UnidadeLogicaAritmetica/src/`

Deve-se implementar os seguintes circuitos combinacionais:

- HalfAdder
    - **Arquivo**   : `HalfAdder.vhd`
    - **Descrição** : Adiciona dois bits que resulta em um bit de soma e outro de carry out.
    - **Dependência**: Não tem.
 
- FullAdder
    - **Arquivo**   : `FullAdder.vhd`
    - **Descrição** : Adiciona três bits, dois referentes às entradas e o outro referente ao carry in. O resultado é um bit com a soma e outro com o carry out.
     - **Dependência**: Não tem.

- Add16
    - **Arquivo**   : `Add16.vhd`
    - **Descrição** : Adiciona dois vetores de 16 bits resultando em um vetor de 16 bits (sem carry out do bit mais significativo - MSB).
    - **Dependência**: `FullAdder`
    
!!! note
    Deve utilizar o `FullAdder` via port map.
  
- Inc16 
    - **Arquivo**   : `Inc16.vhd`
    - **Descrição** : Adiciona '1' a um vetor de 16 bits resultando em um vetor de 16 bits (sem carry out).
    - **Dependência**: `Add16`
    
!!! note
    Deve utilizar o `add16` via `port map`.
    
- Inversor16 
    - **Arquivo**   : `Inversor16.vhd`
    - **Descrição** : Inverte um vetor de entrada quando o bit de controle **n** (nx ou ny) for igual a '1', e não modifica o vetor de entrada caso contrário. O resultado é um novo vetor de 16 bits.
    - **Dependência**: Não tem.
    
- Zerador16
    - **Arquivo**   : `Zerador16.vhd`
    - **Descrição** : Zera um vetor de entrada quando o bit de controle **z** (zx ou zy) for igual a '1'. Não modifica o vetor de entrada se o bit for '0'. O resultado é um novo vetor de 16 bits.
    - **Dependência**: Não tem.
    
- Comparador16
    - **Arquivo**   : `Comparador16.vhd`
    - **Descrição** : Verifica se o vetor de saída (16 bits) é igual a zero (**zr**) e se menor que Zero (**ng**). Caso igual a zero, faz com que o sinal **zr** seja igual a '1' e caso contrário '0'. Se o sinal de entrada for negativo faz com que **ng** receba '1' e '0' caso contrário.
    - **Dependência**: Não tem.
    
Pseudo código :

```python
if(a == 0):
  zr = 1
else:
  zr = 0
  
if (a < 0):
  ng = 1
else:
  ng = 0
```
    
- ALU
    - **Arquivo**   : `ALU.vhd`
    - **Descrição** : A entidade que faz o mapeamento de todas as demais, interligando os blocos (zerador, comparador, inversor, Add ....) em um único bloco.
    - **Dependência**: `Comparador16`, `Zerador16`, `Inversor16`, `Add16`, 

!!! note
    Deve utilizar os módulos via via `port map`.

Para implementar a ALU será necessário usar os blocos desenvolvidos neste projeto e os blocos desenvolvidos no projeto anterior: `And16`, `Mux16`. O script de compilação e teste já faz a inclusão deles. A arquitetura da ULA pode ser vista abaixo:



![ULA](figs/D-ULA/D-ula.png)

## Forma de onda

Para cada teste realizado, deve-se carregar a interface gráfica e tirar um print da forma de onda do módulo com os testes aplicados a ele (LAB-7). Essa imagem deve ser salva na mesma pasta dos arquivos VHDL (src/) e com o mesmo nome dos módulos. A pasta no final do projeto deve possuir os seguintes arquivos:

``` bash
/src/
         Add16.vhd
         Add16.png
         ALU.vhd
         ALU.png
         Comparador16.vhd
         Comparador16.png
         FullAdder.vhd
         FullAdder.png
         HalfAdder.vhd
         HalfAdder.png
         Inc16.vhd
         Inc16.png
         Inversor16.vhd
         Inversor16.png
         Zerador16.vhd
         Zerador16.png
```

## Testando em HW

Para testar os módulos em hardware, deve-se abrir o projeto (`C-UnidadeLogicaAritmetica/Quartus`). Ele já inclui todos os módulos desta entrega e também os módulos da entrega passada. O arquivo localizado em `src/toplevel.vhd` já faz o mapeamento dos pinos da FPGA para os pinos da ULA. Para testar no hardware basta compilar e programar a FPGA.

## Rubricas para avaliação de projetos

Cada integrante do grupo irá receber duas notas: uma referente ao desenvolvimento total do projeto (Projeto) e outra referente a sua participação individual no grupo (que depende do seu papel).

## Projeto

!!! warning
    Não fazer rubrica A e B na master, criar um novo branch para isso!


| Conceito |                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------|
| A+       | - Modifique a ULA adicionando a operação de shift left/right                                          |
|          | - Modifique o `toplevel` para mostrar o resultado da ULA nos displays de 7s (em hexa)                 |
|          |                                                                                                       |
| B+       | - Modifique a ULA adicionando o sinal de estouro da soma (carry) a saída da ULA                       |
|          | - Modifique a ULA adicionando a operação: X xor Y                                                     |
|          | - Compila no Quartus a ULA do grupo e faz um vídeo demonstrando o seu funcionamento (FPGA).           |
|          |                                                                                                       |
| C+       | - Configurou o Actions para testar o projeto                                                          |
|          | - Todos os modulos implementando e passam nos testes                                                  |
|          | - Faz reaproveitamentos dos módulos via `port map` sempre que possível                                |
|          | - Possui a forma de onda de todos os módulos (.png).                                                  |
|          |                                                                                                       |
| D        | - Implementou todos os módulos menos a ULA.                                                           |
|          |                                                                                                       |
| I        | - Não implementou os módulos Add16, ULA, Comparador, FullAdder, HalfAdder, Inc16, Inversosr, Zerador. |



!!! note
    1. Para os conceitos B e A, o grupo deve gravar um vídeo da FPGA demonstrando que as modificações funcionam.
    1. Para os conceitos B e A, o grupo deve modificar o teste da ULA para que comprove o funcionamento dos recursos adicionados (sinais, operações), ou seja, testá-los tentando abordar todos os casos comuns de uso. 

    1. Os conceitos são incrementais: primeiro deve atingir o C :arrow_right: B :arrow_right: A.
    

### Desenvolvedor e Scrum Master

As rubricas a serem seguidas serão comuns a todos os projeto e está descrito no link:

 - [Rubricas Scrum e Desenvolvedor](/Sobre-Rubricas/)

### Formulários
<!--
 - [Scrum Master](https://forms.gle/WD769e2jLR9bzLTb6)
 - [Desenvolvedores](https://forms.gle/jTrSaBegjKZZF6za6)
-->
