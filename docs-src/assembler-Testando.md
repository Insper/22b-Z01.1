A pasta do projeto H, possui a seguinte estrutura:

1. scripts: Scripts em python que automatizam a execução dos testes;
     - `compileNasmMyAssembler` : Compila os *nasms* do projeto **F-Assembly** com o assembler do grupo e salva o resultado em `bin/hack/`
     - `testeAssembler`: Compila os *nasms* com o assembler do grupo e executa a simulação no Z01.1 (**standard-professor**).
     - `testeAssemblerMyCPU`: Compila os *nasms* com o assembler do grupo e executa a simulação no Z01.1 do grupo (**projeto G-CPU**).
     - `genJAR`: Gera um Jar que será utilizado pelos testes anteriores a partir das fontes em `Assembler/src/main/` -> Salva em `Assembler/Z01-Assembler.jar`.
     - > Esses scripts de testes utilizam o projeto F-Assembly!
1. `bin/hack/*.hack`: Arquivos `.hack` convertidos via `Z01-Assembler.jar`
1. `Assembler/src/main/java/assembler`: Código fonte em java do assembler, que deve ser implementando por vocês!

## Testes

É disponibilizado dois tipos de testes: **Unitário** para as classes em java e de **Integração** para o Assembler como um todo. Os testes unitários das classes estão localizados em `Assembler/src/tsts/` e pode ser executado de duas maneiras:

1. Via IDE (Intellij)
2. Via **maven** na geração do jar (`genJAR.py**)

Já o teste de integração que considera como as classes foram utilizadas para a geração do Assembler é executado via script `testeAssembler.py`, executando os seguintes passos :

1. Gera o jar (``genJAR.py``)
     - input : `Assembler/src/main/java/assembler/*.java*`
     - output: `Z01-Assembler.jar`
2. Compila os nasms
     - input: `F-Assembly/src/nasm/*.nasm*`
     - output: `H-Assembler/bin/hack/*.mif*`
3. Executa os testes no hardware (usando o hardware de referência)
     - input: `F-Assembly/tests/*`
     - input: `H-Assembler/bin/hack/*.mif*`
     - output: `F-Assembly/tests/tst/name/*_end.mif*`
4. Compara resultado com esperado
     - input : `F-Assembly/tests/tst/name/*_tst.mif*`
     - output: Terminal

