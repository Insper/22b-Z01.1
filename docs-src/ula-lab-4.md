# Lab 9: Pequena CPU

!!! tip "Sugestão de trabalho"
    1. Cada um faz na sua máquina 
    simultaneamente com os demais integrantes do grupo, discutindo no vídeo.
    
    1. Um integrante faz na sua máquina e compartilha a tela com os demais (todos comentam o mesmo código)

!!! info "Tempo"
    Tempo estimando no lab: 45 min

## Começando

Este lab está disponível em um novo repositório, para começarem trabalhar clonem o repositório para sua máquina, iremos trabalhar coma ele neste lab.

```
cd ~
https://github.com/Insper/Z01.1-Lab-Pequena-CPU
```

## CPU

O objetivo desse lab é o de começarmos entender como a ULA pode ser utilizada por um programa para realizar ações de um programa. Nas CPUs a ULA é controlada por um bloco chamado de Unidade de Controle (`control unit`), que é responsável por interpretar as instruções e comandar a ULA!

Para entender como isso funciona vamos usar a ULA desenvolvida por vocês em uma arquitetura de CPU muito simples, mas que servirá de exemplo (o nosso computador não será assim). Essa arquitetura de CPU possui uma entrada do usuário (que pode ser por exemplo as chaves da placa) que são conectados a entrada `Y` da ULA e uma saída (que pode ser os LEDs) conectada a saída (out), a entrada X é conectada a um registrador que recebe o valor da saída da ULA. 

Na CPU deste lab iremos trabalhar com o conceito de registrador acumulador, onde o resultado da ULA será sempre salvo em `REG_C`, consforme diagrama a seguir:

![](figs/D-ULA/ula-aplicada.svg){width=600}

!!! note
    Registrador é o termo utilizado para uma unidade simples de memória
    capaz de armazenar apenas uma unidade de dados (nesse caso 16 bits).
    
    Nesse caso, a cada operação do sistema (clock) o registrador salvo
    o resultado da ULA.
    
!!! tip
    O `REG_C` guarda um resultado da operação da ULA até a próxima instrução (clock)


## Control Unit

A unidade de controle (UC) é o hardware responsável por ler as instruções a serem executadas (que estão em binário) e comandar toda a CPU para executar o que deve ser feito. Nesse exemplo a UC comanda apenas a ULA, mas ela poderia controlar outras coisas também (mux, pipeline, ...).

A UC apenas transcreve instruções (programa) em controle da CPU, para isso temos que definir uma linguagem de máquina.

## Programa

Linguagem de máquina é uma palavra de 4 bits de largura que descreve qual operação deve ser realizada na CPU, no exemplo fornecido temos as seguintes operações definidas:

| Linguagem de maquina | Instrução               | OP CODE |
|----------------------|-------------------------|---------|
| `0000`               | `REG_C` = `REG_C`       | nop     |
| `0001`               | `REG_C` = `0`           | mov 0,C |
| `1000`               | `REG_C` = !`REG_C`      | not C   |
| `1001`               | `REG_C` = `REG_C` + 1   | add 1,C |
| `1010`               | `REG_C` = `REG_C` + `Y` | add Y,C |
| `1011`               | `REG_C` = `REG_C` - 1   | sub 1,C |

!!! tip
    `OP CODE` é o termo usado para descrever uma instrução, 
    programas escritos em assembly fazem uso de opcodes 
    para facilitar a programação.

!!! note
    `nop` = No Operation (não faz nada/ não modifica nada!) 

### Exemplo

Vamos pensar em um programa muito simples que faz o seguinte:

1. Carrega `0` em `REG_C`
1. `REG_C` + `1`

O código disso em assembly (usando os opcodes) seria:

```nasm 
mov 0, C
add 1, C
nop
```

!!! note
    Esse `nop` é implementando pelo comando que faz com que a entrada `X` passe pela ULA (sem modificação), assim `REG_C` = `REG_C`, ou seja, não faz nada.

!!! info
    Uma instrução (linha do programa assembly) é executada a cada clock.

Para executarmos esse programa, devemos traduzir o programa assembly em linguagem de máquina que é de fato o que a CPU é capaz de ler (lembre que no final é tudo uns e zeros), para  isso temos que ter a memória (ROM) inicializada com os seguintes valores:

```
0:   0001     <--- O Programa começa na linha 0
1:   1001     |     e a cada 'clock' executa para próxima linha
2:   0000     v
```

!!! info
    O programa responsável por traduzir linguagem assembly em "binário" é chamado de montador ou assembler.

Legal né? Mas para isso funcionar a Unidade de Controle deve ser capaz de ler a instrução (4 bits) e controlar a ULA para executar tal comando. A unidade foi fornecida apenas com duas instruções implementadas: `mov 0,C`, `add 1,c`.

Para testar o projeto com o código exemplo anterior basta executar o comando a seguir no terminar:

`./testeLab.py`.

<!--
O teste deve passar, como a seguir:

<script id="asciicast-rnFQXSSGiHuCGuUD3vVJw5I1Z" src="https://asciinema.org/a/rnFQXSSGiHuCGuUD3vVJw5I1Z.js" async></script>
-->

!!! tip
    Execute o comando com `-g` e verifique a forma de onda (e todos os sinais internos da CPU)

## Terminando o Control Unit

Nossa primeira atividade do lab será a de termina de implementar a Unidade de Controle, para poder executar todas as instruções anteriores. A versão disponível para vocês só possui as instruções: `mov 0,C`, `add 1,C` e `nop`, vamos implementar as demais?

Para isso será necessário modificar o arquivo `/src/ControlUnit.vhd`, nele stá implementando a lógica que traduz instruções em comando do hardware. O control unit lê o a instrução que está salva na memória (`op`) e aciona a ULA (`ula`) para realizar tal operação.

A saída do controlUnit (`ula out std_logic_vector`) é um vetor composto pelos sinais de controle da ula: [`zx`, `nx`, `zy`, `ny`, `f`, `no`] e pelo 'en' que controla se iremos salvar a informação no registrador C (`en <= '1'`) ou não iremos armazenar a informação que sai da ULA (`en<='0'`).

``` vhdl

entity controlunit is
	port (
			op:  in std_logic_vector(3 downto 0);
            en:  out std_logic;
            ng:  in  std_logic;
            zr:  in  std_logic;
			ula: out std_logic_vector(5 downto 0)
	);
end entity;

architecture  rtl of controlunit is

  signal control : std_logic_vector(6 downto 0);

begin

  ula <= control(6 downto 1);
  en  <= control(0);

  control <=
    "101010" & '1' when op = "0001" else -- mov 0, C
    "011111" & '1' when op = "1001" else -- add 1, C
    "000000" & '1' when op = "0000" else -- nop
    "101000" & '0'; -- qualquer coisa!

end architecture;
```

!!! example
    Quando a instrução for `0001` (`mov 0,C`) o controlUnit irá acionar a ula: `zx=1`, `nx=0`, `zy=1`, `ny=1`, `f=1`, `no=0` para que a sua saída seja 0 e então salvar o valor no registrador C ('en=1')
    
!!! example "Tarefa"
    Você deve implementar as instruções que estão faltando no ControlUnit:
    
    1. `not C`
    2. `add Y,C`
    3. `sub 1,C`

!!! tip
    Você precisa adicionar os casos a serem implementando no when do ControlUnit.

Agora para testar os novos comandos você deve aplicar o patch a seguir que modifica o teste do laboratório inserindo os novos comandos, execute no terminar:

```bash
 git apply teste1.patch
```
   
E então teste:

```bash
./testeLab.py
```
   
## Analisando CPU

Discuta em grupo as limitações dessa nossa CPU, e o que poderia ser feito para melhorar:

1. Essa CPU é capaz de realizar qualquer tipo de cálculo?
1. Quais limitações você percebe nela?
1. Temos condicionais? Como implementar?
1. ....

<!--
Responda o formulário com a resposta do grupo após discussão (pode ser uma resposta por grupo ou uma mais de uma, vocês que escolhem):

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSf9E3FFm7BxbeLG6C-YxsPattmbwfZz_MVnKwrZ_kkc-k1R1A/viewform?embedded=true" width="640" height="769" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
-->

## Adicionando condicional 

Vamos agora adicionar uma instrução de condicional a nossa CPU, será algo bem simples e pouco funcional na prática, mas vai dar a ideia de como as coisas funcionam. Para isso iremos criar uma nova instrução que copia a entrada Y para `REG_C` apenas se Y for menor ou igual a zero. Como a seguir:

```
if Y<=0:
    REG_C = Y
else
    REG_C = REG_C
```

Vamos atribuir a está operação o valor `1111`. Para realizarmos essa operação teremos que fazer a leitura dos valores `ng` e `zr` que a ULA fornece para nós e então tomarmos a decisão se iremos salvar Y em `REG_C` (`en=1`) ou não (`en=0`).

!!! example "Tarefa"
    1. Implemente a nova funcionalidade no ControlUnit, lembre que agora é necessário verificar o valor de `ng` e `zr` para saber se o valor de Y é menor ou igual a zero.
