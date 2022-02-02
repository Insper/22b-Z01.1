# Lab 17: vm

!!! tip
    Realizar o laboratório individualmente. Mas trabalhar no grupo e trocar ideias.

Nesse lab iremos criar programas em VM para o nosso Z01.1, essa entrega é individual e não vale nota, mas será cobrado na última avaliação.

Esse laboratório mistura exercícios com leitura de teoria, é essencial que você realize as leituras recomendadas para cada secção e então voltar para fazer os exercícios. 

!!! warning "Antes de começar"
    Esse laboratório não faz parte de um projeto, mas será necessário atualizar o repositório de vocês com o Z01 para buscarem a nova pasta (`upstream`). Escolham um do grupo para fazer isso, ele não será um scrum master!
    
    - ==Não seguir sem realizar a etapa anterior.==

!!! warning "Z01-Tools"
    Atualizar Z01-Tools! antes de seguir...

## Treinando RPN

Abra o simulador online da calculadora [hp48](http://www.poleyland.com/hp48/) e realize os seguintes cálculos:

1. `12 + 34 + 56 – 78 + 90 – 12`
1. `(12 × 34) + (56 × 78) – (90 × 12)`
1. `3 × (4 + (5 × (6 + 7)))`   (Dica: comece pelo parentese mais interno)
1. $1/\sqrt{121}$

> Exercícios extraídos de: https://hansklav.home.xs4all.nl/rpn/

## VM Z01 - básico

!!! info "TEORIA"
    Leia a [Teoria/VM](/Z01.1/Teoria-vm/) antes de seguir.
    
Vamos agora trabalhar com a nossa vm, vocês terão que implementar os programas a seguir e testar com o script (`testeVm.py`). 

!!! info
    A descrição do que deve ser feito está no próprio código

- `Projetos/H-VM/src/vm/1a-Add`
- `Projetos/H-VM/src/vm/1b-Calculadora`

Você notou que nesses códigos pedimos para salvar o resultado em `temp 0`, fazemos
isso pela operação de `pop temp 0`. Vamos estudar um pouco a respeito disso:

!!! info "TEORIA"
    Leia a [Teoria/VM - Segmentos](/Z01.1/Teoria-vm-segmentos/) antes de seguir.

## goto (jump)

Nossa linguagem vm suporta realizar condições e loops, vamos ver como isso é feito e praticar um pouco!

!!! info "TEORIA"
    Leia a [Teoria/VM - jump](/Z01.1/Teoria-vm-jump/) antes de seguir.
    
Implementem os códigos a seguir

- `H-VM/src/vm/1c-loop`
- `H-VM/src/vm/1c-div`

!!! tip
    De uma olhada nos códigos de exemplo, tem coisa de condição lá!

## funções

Vamos agora fazer o uso de funções em VM, o que irá nos permitir fazer as seguintes operações: $10/2 + 15*3*\sqrt{121}/2^5$, lembre que no nosso hardware não possuímos os operadores de multiplicação, divisão, raiz quadrada e muito menos exponencial. Mas com o uso de funções podemos implementar isso em código e usar para implementar a equação anterior.

```
div(10,2) + div(mult(mult(15,3), sqrt(121.2))), exp(2,5))
``` 

- note que os operadores viraram chamadas de funções.

!!! info "TEORIA"
    Leia a [Teoria/VM - Funções](/Z01.1/Teoria-vm-funcoes/) antes de seguir.
    
Vamos agora trabalhar com funções na nossa VM, implementem os códigos a seguir:

- `H-VM/src/vm/2b-Calculadora`
- `H-VM/src/vm/2c-Calculadora`
- `H-VM/src/vm/2d-Calculadora`
