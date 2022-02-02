# VM - jump

Goto é a maneira de desviarmos uma execução em vm, e possui a seguinte sintaxe:

- **goto** LABEL
- **if-goto** LABEL

podemos utilizar dois tipos : 

- goto : incondicional , salta sem condição
- if-goto : condiconal, salta se o último valor da pilha for True

!!! example "Exemplo: Salto para igual se 3 = 2"
    ```
    push constant 3
    push constant 2
    eq
    if-goto IGUAL
    ..
    ..
    label IGUAL
    ..
    ..
    ```


!!! example "Exemplo: Contador utilizando for utilizando goto"
    ```vm
    // for(i=0; i<10; i++)
    //     x = x+1;

    push constant 0
    pop temp 0         
    push constant 1
    pop temp 1
    label LOOP_START
    push temp 0
    push constant 10
    eq
    if-goto END       // se temp0 = 10 salta para o fim
    push temp 0
    push constant 1
    add
    pop temp 0
    push temp 1
    push constant 1
    add
    pop temp 1
    goto LOOP_START  // If counter > 0, goto LOOP_START
    label END
    ```
### labels

 Os labels são definidos pela keyword **label** + nome :
 
 - **label** nome
