# Lab 18: Vm Translator - Praticando

O VMTranslator é um programa escrito em Java que faz a tradução de códigos escrito na linguagem VM definida no curso e traduz para linguagem Assembly do computador Z01.

## Praticando pilha

Acesse a planilha no [google sheets](https://docs.google.com/spreadsheets/d/1dywPIHgpUztDtpqzuEuGzAuTlcK9ryVUTp9-b84stJ4/edit?usp=sharing), faça uma cópia para a sua conta e comece a estudar e modificar ela, a primeira parte é para vocês trabalharem com o conceito de pilha e frame, para isso, faça apenas a primeira aba (pilha).

==Quando acabar volte para esse lab (é para fazer a primeira aba apenas)==

## Praticando tradução VM -> nasm 

!!! warning "Antes de começar"
    Esse laboratório não faz parte de um projeto, mas será necessário atualizar o repositório de vocês com o Z01 para buscarem a nova pasta (`upstream`). Escolham um do grupo para fazer isso, ele não será um scrum master!
    
    - ==Não seguir sem realizar a etapa anterior.==



Abra novamente a [planilha](https://docs.google.com/spreadsheets/d/1dywPIHgpUztDtpqzuEuGzAuTlcK9ryVUTp9-b84stJ4/edit?usp=sharing), agora vá para a aba ==Translator== e siga os passos ali indicados.

??? info "Como o teste funciona?"
    O teste executa:

    ```
                genJAR.py
                    |   
                    |   
                    V

                VMTranslator          Assembler            Z01-Simulator  ------------------
    arquivo.vm -------------> .nasm -----------> .hack  > ------------>  - Verifica saída -
                                                                          ------------------
                    ^
                    |   
                    |- Desenvolvido no projeto I 

    ```

    Para isso foi criado alguns programas (`H-VM/src/vmExamples/`) em VM muito específicos que testam somente um comando, ou uma parte da tradução do `VMTranslator`. Por exemplo o teste `SimpleAdd` possui somente a seguinte linha:

    ``` jar
    add
    ```

    Esse teste foi criado para testar o `Code.writeArithmetic` no caso de um comando `add`. Para isso, antes da execução desse código, o simulador faz a inicialização da RAM, simulando valores na pilha e já configurando o SP para uma situação real. A memória antes da execução da instrução add é a seguinte:

    ``` 
        0 : 0000000100000010;
      256 : 0000000000000010;
      257 : 0000000000000100;
      258 : 0000000000000000;
    ```

    !!! note
        `I-VM/tests/tst/SimpleAdd/SimpleAdd0_in.mif`

    Espera-se o resultado final após a execução do comando add :

    ```
        0 : 0000000100000001
      256 : 0000000000000110
    ```

    Nesse projeto vocês terão que mexer apenas no `code.java`, os demais módulos já estão prontos (similar ao projeto do Assembler, temos nesse o `parser`, `VMTranslator`, ...).
