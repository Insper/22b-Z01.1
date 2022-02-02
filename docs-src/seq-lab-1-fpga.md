
## Testando na FPGA 

No Quartus atribua ao **toplevel** o arquivo `TopLevel.vhd` (mesmo passos anteriores), esse módulo irá mapear o FF recém criado para os pinos da FPGA:

``` vhd
Clock <= not KEY(0); -- os botoes quando nao apertado vale 1
                     -- e apertado 0, essa logica inverte isso
clear <= not KEY(1);
set   <= not KEY(2);

u0 : FlipFlopD port map (
		clock    => Clock,
		d        => SW(0),
		clear    => clear,
		preset   => set,
		q        => LEDR(0)
	);		
```

Note que nesse código estamos usando os botões (`KEY`) da FPGA, além dos LEDs e das Chaves (SW).

**COMPILE, PROGRAME E TESTE**

```diff
+ Chame um professor para validar
```

> Esse exemplo não segue as boas práticas de projetos em FPGA pois não se deve gerar um clock a partir de um pino qualquer da FPGA, a FPGA possui pinos específicos para a geração do clock. Porém é a melhor maneira didática de mostrar um FF operando.
>
> O correto seria colocarmos um pino de "enable" que ativaria ou não o FF quando o botão fosse pressionado.

e
