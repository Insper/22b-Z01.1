# Lab 8: ULA 

!!! note "Sugestão"
    1. Realizar o lab individualmente
    1. Ficar no canal do grupo e tirar dúvidas entre os colegas!

!!! tip
    Antes de seguir você deve ter lido a [Teoria/ULA](/Z01.1/Teoria-ULA/).

O objetivo desse laboratório é o de trabalharmos com o controle dos sinais da ULA para entendermos as operações da unidade de processamento do nosso computador. Para isso iremos:

1. Executando o simulador
1. Controlando ULA para realizar operações específicas (exercícios)

## Simulador

Iremos utilizar um simulador da ULA feito em python + Qt. Siga os passos a seguir:

```sh
cd ~
git clone https://github.com/eduardomarossi/z01.1-ula
cd z01.1-ula
pip3 install -r requirements.txt --user
python3 main.py
```

Você deve obter a seguinte interface:

![](https://raw.githubusercontent.com/eduardomarossi/z01.1-ula/master/image.png)

## Controlando ULA

Com o simulador podemos testar a ULA modificando seus sinais de controle. A seguir uma proposta de operações lógicas que devem ser realizadas na ULA, seus sinais de controle e resultados devem ser anotados nas tabelas.

!!! tip 
    O projeto **FIXA** as entradas da ULA com os valores:

    - X = 0x73  
    - Y = 0x5F

!!! example "Tarefa: `out = X`"
    - Configure os controles da ULA para fazer com que a saída da ULA seja a entrada **X**
    
    Para isso você deve mexer nas chaves da FPGA e verificar a saída nos leds.

!!! example "Tarefa: `out = Y`"
    - Configure os controles da ULA para fazer com que a saída da ULA seja a entrada Y

!!! example "Tarefa: `out = !Y`"
    - Configure os controles da ULA para fazer com que a saída da ULA seja a entrada a entrada Y negada

!!! example "Tarefa: `out = 0`"
    - Faça com que a saída da ULA seja 0

!!! example "Tarefa: `out = 1`"
    - Faça com que a saída da ULA seja 1

!!! example "Tarefa: `out = -1`"
    - Faça com que a saída da ULA seja -1 (em complemento de 2)

!!! example "Tarefa: `out = X+Y`"
    - Faça com que a saída da ULA seja a entrada X + a entrada Y

!!! example "Tarefa (difícil): `out = X or Y`"
    - Faça com que a saída da ULA seja X ou Y

!!! example "Tarefa (difícil): `out = X - Y`"
    - Faça com que a saída da ULA seja a entrada X menos a entrada Y
