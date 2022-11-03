# Testando

Para testar o projeto F-Computador é necessário:

1. Testar o `controUnit` e o `memoryIo` descomentando apenas as respectivas linhas no `config_testes.txt`:

``` bash
$ ./testeHW.py
```

> Somente após passar os testes anteriores e com a `CPU` implementada:

2. Testar o computador (`CPU`, `controlUnit` e `memoryIo`) com a execução de códigos em assembly:

``` bash
$ ./testeHW.py
```

 após descomentar a linha referente ao `CPU.vhd` no `config_testes.txt`.
 
!!! tip
    SE O TESTE TRAVAR: VERIFICAR DICAS AO FINAL DESSA PÁGINA

### Se o teste do CPU travar

Se por algum motivo o teste do CPU travar no primeiro teste, isso é sinônimo de que algo está errado com o seu HDL. Esse teste faz o seguinte para cada arquivo `.nasm` incluso no arquivo de configuração do **Projeto E**:

1. Compila o `.nasm` gerando o binário `.mif`
1. Carrega na ROM do seu computador (**Projeto F**) o binário
1. Executa o código
1. Verifica se o resultado está certo

Se por algum motivo algum módulo estiver com problema esse teste pode falhar, o que é aconselhado fazer: 

1. Comente todos os teste do **Projeto E** no arquivo de configuração (`E-Assembly/tests/config_testes_nasm.txt`) com **exceção**  o `mov.nasm`
    - Esse módulo testa todos os registradores
1. Execute o teste: `./testeHW.py` e analise o waveform com o GTKWave
    - **Análise as mensagens no terminal em busca de erros!**
1. Analise o que está acontecendo com o seu hardware, verifique a instrução que está entrando e o que deveria acontecer.
1. Corrija o HW quando encontrar o problema, teste novamente.
1. Descomente os módulos: `abs.nasm` e teste para saber se está :ok
    - Esse módulo testa o loadPC e saídas da ULA (ng e zr)
1. Descomente os demais módulos e teste tudo.


