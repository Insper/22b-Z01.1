# Lab 6: Adders

!!! success "2020-2"
    Material atualizado.

!!! warning "Antes de começar"
    Toda vez que um novo projeto começar será necessário realizar algumas configurações no repositório do grupo, vocês devem seguir para o documento: [`Util/Começando novo Projeto`](https://insper.github.io/Z01.1/Util-Comecando-novo-projeto/) e depois voltar para esse lab.

    - Não seguir sem realizar a etapa anterior.

!!! note "Sugestão"
    1. Realizar o lab individualmente
    1. Ficar no canal do grupo e tirar dúvidas entre os colegas!

## Half-adder

O half-adder é um dispositivo somador binário que possui duas entradas binárias (a,b) e duas saídas binária (soma dos bits (Soma) e o carry (vaium)). A tabela verdade desse componente é detalhada a seguir:

| a | b | Soma | Vaium |
|---|---|------|-------|
| 0 | 0 |    0 |     0 |
| 0 | 1 |    1 |     0 |
| 1 | 0 |    1 |     0 |
| 1 | 1 |    0 |     1 |

Com a tabela verdade podemos extrair as duas equações que descreve esse componente: Soma e Vaium.

-  `soma = a xor b`
-  `vaium = a and b`

!!! note
    Leia a teoria: Aritmética Binaria para mais informações.

!!! tip
    $\bar{a} b + a \bar{b} = a \oplus b$

1. Agora com a equação definida é possível realizarmos uma descrição em `VHDL` do componente `halfadder`. Abra o arquivo  `C-UnidadeLogicaAritmetica/src/HalfAdder.vhd` e modifique sua arquitetura para implementar a equação do halfadder. 
2. Edite o arquivo de configuração do teste `config_testes.txt` e descomente a linha referente ao `halfadder`.
3. Valide a implementação executando o script de testes: `testeULA.py`

### Implementando

Abra o projeto do Quartus e note que o `toplevel` faz uso do `HalfAdder`:

``` vhdl
begin

  u1 : HalfAdder port map(a => SW(0), b=> SW(1), soma => LEDR(0), vaium => LEDR(1));
  
```

```
                 ------
SW(0) -->  a -->|      |--> Soma  --> LEDR(0)
                |  HA  |
SW(1) -->  b -->|      |--> Carry --> LEDR(1)
                 ------
                                  toplevel
```

!!! example "Tarefa"
    - Implemente o VHDL
    - Compile o projeto
    - Gere e analise o RTL

    No insper? Faça também:
    
    - Programe a FPGA
    - Mexa nas chaves, o resultado é o esperado?
    
    (**filme e mostre para os seus colegas!!**)

## Full-Adder

Você deve fazer a mesma coisa com o fulladder: 

1. Extrair a equação do FullAdder
1. Transcrever para o arquivo: `FullAdder.vhd`
1. Testar (`./testeULA.py`)

Com o módulo passando nos testes, editar o `toplevel` para utilizar no lugar do HalfAdder o FullAdder recém implementando!

``` vhdl
begin

  u1 : FullAdder port map(a => SW(0), b=> SW(1), c=> SW(2), soma => LEDR(0), vaium => LEDR(1));

end rtl;
```

!!! example "Tarefa"
    - Implemente o VHDL
    - Compile o projeto
    - Gere e analise o RTL

    No insper? Faça também:
    
    - Programe a FPGA
    - Mexa nas chaves, o resultado é o esperado?
    
    (**filme e mostre para os seus colegas!!**)
    
## Somador

Agora com o FullAdder (FAD) feito podemos construir um somador mais completo, que soma dois vetores de bits. Para isso iremos precisar de dois FullAdders conectados da seguinte maneira:

```
           x1 y1  ----------    x0 y0 '0'
            |  |  |        |     |  |  |
            v  v  v        |     v  v  v
           ----------      |   ----------
          | a  b  c  |     |  |  a  b  c |
          |          |     |  |          |
 Carry <--|vaium     |     <--|vaium     |
          |     soma |        |     soma |
           ----------          ----------
             |                   |
             v                   v
            s1                  s0
```

Nessa ligação, estamos somando dois vetores de dois bits cada: `x(1 downto 0) + y(1 downto 0)` que resulta em uma soma de dois bits: `s(1 downto 0)` e um `carry`.

!!! question
    Explique o que está acontecendo para o seu colega, você entendeu o porque dessa ligação?

Utilizando `port map` construa o circuito anterior, utilize como entrada X as chaves `[SW(1) SW(0)]` e como entrada Y as chaves `[SW(3) SW(2)]`, para visualizar coloque a saída S nos leds `[LEDR(1) LEDR(0)]` e o carry no `LEDR(3)`

!!! example "Tarefa"
    - Implemente o VHDL
    - Compile o projeto
    - Gere e analise o RTL

    No insper? Faça também:
    
    - Programe a FPGA
    - Mexa nas chaves, o resultado é o esperado?
    
    (**filme e mostre para os seus colegas!!**)
    
!!! tip
    Você deve utilizar `port map` para isso, inicializando dois componentes FullAdder
