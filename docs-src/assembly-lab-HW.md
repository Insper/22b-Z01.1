# Programando FPGA

Ao final desse lab você deve ser capaz de:

1. Conectar o LCD na FPGA 
1. Programar a FPGA com o Z01.1
1. Programar um programa em nasm no Z01.1

## Conectando o LCD

![FPGA](figs/F-Assembly/placa.jpg)

## Programando a FPGA

A FPGA é um hardware que pode sr configurável para implementar 'qualquer' sistema digital, incluindo um computador. Iremos primeiramente prograr a FPGA com o Hardware do Z01 para então podermos programar o nosso código em assembly. Para isso, execute o script python:

``` bash
$ ./programFPGA.py
```

Esse script irá carregar na FPGA o hardware do Z01.1

!!! note
    Nossa FPGA é dita do tipo volátil, ela perde a configuração sempre que for desligada! 
    
    - Essa etapa deve ser realizada sempre que ela desligar.

## Programando o Z01.1

Agora com o Z01.1 configurado na FPGA podemos executar nosso programa no hardware, basta chamar o script `programSoftware.py` com o parâmetro `-n` e o caminho para o código `nasm`. Como no exemplo a seguir:

``` bash
./programSoftware.py -n src/examples/R-LCD.nasm
```

O mesmo deve executar um código no Z01 que escreve a letra **R** no LCD. 

Programe os exemplos a seguir:

- `pxLCD.nasm`: Escreve apenas 16 pixels no LCD (um ponto)
- `testeLED.nasm`: Um programa que exibe um contador binário nos LEDs da FPGA
- `testeSW.nasm`: Um programa que lê as chaves da FPGA e aciona os LEDs com base no seus resultados.

## Praticando

1. Grave na FPGA o programa `testeSW.nasm`

Mexa nas chaves SW e veja o que acontece com os LEDS. 

2. Altere o programa para ser o inverso do que foi programado.

Quando as chaves estiverem para baixo, o respectivo LED acende e quando a chave estiver para cima o LED apaga.

!!! tip
    - Valide na FPGA! Chame um professor
    - para mostrar.
