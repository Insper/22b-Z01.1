# Sequencial

Como trabalhar com lógica sequência em VHDL

## Process VHDL

Em VHDL quando desejamos fazer algo sequencial é necessário usarmos uma estrutura chamada de process, que possui a declaração a seguir:

``` vhdl
process (optional sensitivity list)
	declarations
begin
	sequential statements
end process;
```

Nesse **process** possuímos a lista de sensibilidade (`sensitivity list`) que indica quando o process será executado. Podemos pensar da seguinte maneira, sempre que algum sinal que está listado nessa lista de sensibilidade mudar de valor (`0` -> `1`, `1` -> `0`) o processo será executado. Vamos ver o exemplo a seguir:

``` vhdl
process(A)
begin
  Q <= A;
end process;
```

!!! tip "Entendendo"
    Sempre que o sinal A (sinal ou porta) alterar de valor o sinal Q será atribuído com o seu valor

Agora vamos criar um outro processo (**esse estará errado**):

``` vhdl
process(A)
begin
  Q <= A and B;
end process;
```

A ideia por traz desse processo seria que o sinal `Q` receba o sinal `A` e `B` sempre que algum dos dois sofram alguma alteração, porém essa implementação não irá funcionar já que `B` não faz parte da lista de sensibilidade e se B mudar de valor o processo não será chamado, o sinal `Q` só será atualizado quando `A` mudar de valor.

!!! example "Tarefa"
    Reescreva no `codeshare` do grupo o módulo anterior corrigido.
    
    - Chame um professor para validar!

## Clock

Para inserirmos um clock (um sistema síncrono) precisamos necessariamente usar um `process`, e a arquitetura é a seguinte:

``` vhdl
process(clock)
begin
  if(rising_edge(clock)) then
     Q <= D;
  end if;
end process;
```

Sempre que o clock sofrer variação (`0` -> `1`, `1` -> `0`) o process é chamado e verifica-se se a transição foi de borda de subida (`rising_edge`) se for, atribui o sinal A ao sinal Q, caso contrário Q mantém seu último valor.

!!! note 
     Em FPGA um sinal digital não deve sofrer atualização em ambas as bordas: subida (`rising_edge`) e de descida (`falling_edge`) pois **não será suportado por hardware**. Salvo em registradores DDR (duble data rate) especiais, exemplo do que não deve ser feito!:

    ``` vhdl
    process(clock)
    begin
      if(rising_edge(clock)) then
        Q <= D;
      elsif(falling_edge(clock)) then
        Q <= D;
      end if;
    end process;
    ```
