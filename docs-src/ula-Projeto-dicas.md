# C - Dicas (A,B)

Como não temos mais o hardware disponível, teremos que modificar os testes para podermos testar a novas funcionalidades da ULA.

1. Modificar a ULA
1. Modificar o arquivo: `tests/tst/tb_ULA.vhd`
    - Alterar o `component` da ULA (para bater com a `entity` da ula)
    - Alterar os testes existentes 
1. Testar

## Como fazer? Exemplo

Imagine uma ALU em que foi implementado a seguinte funcionalidade: multiplicar um número X por 2.
As alterações necessárias para esta operação foram feitas no arquivo da ULA (VHDL) do grupo.

No entanto, o teste implementado da ULA não verifica esta nova funcionalidade. 
Neste exemplo iremos ver como alterar o teste para validar esta nova função.

O teste de interesse é o arquivo presente em `C-UnidadeLogicaAritimetica/tests/tst/tb_ALU.vhd`. A sigla **tb** significa Testbench (bancada de testes).
Note que o arquivo é um arquivo em VHDL como qualquer outro, tendo como diferencial, o fato de utilizar a biblioteca **vunit_lib** que permite carregar alguns recursos para teste, olhe que na arquitetura, deve-se incluir a declaração do componente a ser testado e em seguida o mesmo é instanciado (igual quando feito um port-map).

Observe também que temos também alguns sinais (*signals*), estes são utilizados para alterar os valores que estamos colocando no componente a ser testado. A seguir, uma grande diferença do VHDL convencional que estamos acostumados se dá no seguinte trecho:

``` vhdl
main: process
begin
...
end
```

Esta diretiva **process** indica que o que está contido no begin-end será executado sequencialmente diferente do que viemos usando que é execução combinacional. Vocês terão uma aula dedicada ao uso de lógica sequencial, por enquanto, apenas pense que cada linha a seguir é executada após a outra.

A seguir, teremos vários trechos de códigos separados, cada trecho é um teste sendo feito.

``` vhdl
-- Teste: 1
      inX <= "0000000000000000"; inY <= "1111111111111111";
      inZX <= '1'; inNX <= '0'; inZY <= '1'; inNY <= '0'; inF <= '1'; inNO <= '0';
      wait for 100 ps;
      assert(outZR = '1' and outNG = '0' and outSaida= "0000000000000000")  report "Falha em teste: 1" severity error;
```

Por exemplo, neste teste acima, é colocado 0 na entrada X e -1 na entrada Y. É zerado o X, não negado o X, zerado Y e não negado Y. Escolhido operação de soma, e não inverte a saída. Ele verifica se obtem na saída o resultado 0, assim como flag do zerador ativo e flag de negativo desligado.

Enfim, como pode-se ver colocamos as entradas desejadas e verificamos se a saída é a esperada por nós. Caso não seja, o comando **assert** (condição de teste) irá falhar e executará o comando **report** que reportará ao usuário uma falha com severidade de erro.

No entanto, temos um problema a resolver, para poder incorporar a funcionalidade de multiplicar por 2, o projetista, decidiu alterar o MUX que existe no projeto da ALU para ser um seletor de 2 bits e portanto o sinal **f** agora possui 2 bits. 

Neste caso, teremos que alterar a declaração do componente referente ao sinal **f**
``` vhdl
f:     in STD_LOGIC_VECTOR(1 downto 0);                     -- se 00 calcula x & y, 01 x + y, 10 x*2
```

E corrigir o sinal inF para 2 bits e todos os testes pre-existentes também terão que ser corrigidos!
``` vhdl
signal inF: STD_LOGIC_VECTOR(1 downto 0);
``
Exemplo pro teste 1
``` vhdl
-- Teste: 1
      inX <= "0000000000000000"; inY <= "1111111111111111";
      inZX <= '1'; inNX <= '0'; inZY <= '1'; inNY <= '0'; inF <= "01"; inNO <= '0';
      wait for 100 ps;
      assert(outZR = '1' and outNG = '0' and outSaida= "0000000000000000")  report "Falha em teste: 1" severity error;
```

Feito isso agora vamos criar nossos testes para a funcionalidade outSaida = 2 * X. Colocando os testes no final do arquivo. Primeiro, testar 5 * 2 = 10.
``` vhdl
-- Teste: 20 - Testa 5 * 2= 10
      inX <= "0000000000000101"; inY <= "1111111111111111";
      inZX <= '0'; inNX <= '0'; inZY <= '0'; inNY <= '0'; inF <= "10"; inNO <= '0';
      wait for 100 ps;
      assert(outZR = '0' and outNG = '0' and outSaida= "0000000000001010")  report "Falha em teste: 1" severity error;
```

Colocamos X = 5 (em binário). Não zeramos X e escolhemos a opção correta no seletor **f**. Verificando o resultado outSaida = 10 (em binário) e os flags.

Depois vamos testar multiplicação por zero.
``` vhdl
-- Teste: 21 - Testa 0 * 2 = 0
      inX <= "0000000000000000"; inY <= "1111111111111111";
      inZX <= '0'; inNX <= '0'; inZY <= '0'; inNY <= '0'; inF <= "10"; inNO <= '0';
      wait for 100 ps;
      assert(outZR = '1' and outNG = '0' and outSaida= "0000000000000000")  report "Falha em teste: 1" severity error;
```

Enfim poderiamos fazer mais testes, envolvendo outros casos diferentes. O ideal é criar testes que peguem todas as possibilidades razoavelmente diferentes, note que se for fazer para todas possibilidades, só levando em conta o X teriamos 2^16 possibilidades... é inviável. Por isso teste apenas casos de *borda*, ou seja, quando o comportamento da saída pode mudar razoavelmente do normal (por isso testamos o zero aqui!)

Com isso feito, ao rodar o teste novamente na pasta, se a funcionalidade tiver sido implementada com sucesso, devemos obter um teste com exito! Parabéns!

