# Testando

Para testar o projeto F-CPU é necessário:

1. Testar o `controUnit` e o `memoryIo`:

``` bash
$ ./testeHW.py lib.tb_memoryio.all 
$ ./testeHW.py lib.tb_controlunit.all
```

> Somente após passar os testes anteriores e com a `CPU` implementada:

2. Testar o computador (`CPU`, `controlUnit` e `memoryIo`) com a execução de códigos em assembly:

``` bash
$ ./testeAssemblyMyCPU.py
```

!!! tip
    SE O TESTE TRAVAR: VERIFICAR DICAS AO FINAL DESSA PÁGINA

### Se o `testeAssemblyMyCPU.py` travar

Se por algum motivo o teste `testeAssemblyMyCPU.py` travar no primeiro teste, isso é sinônimo de que algo está errado com o seu HDL. Esse teste faz o seguinte para cada arquivo `.nasm` incluso no arquivo de configuração do **Projeto E**:

1. Compila o `.nasm` gerando o binário `.mif`
1. Carrega na ROM do seu computador (**Projeto F**) o binário
1. Executa o código
1. Verifica se o resultado está certo

Se por algum motivo algum módulo estiver com problema esse teste pode falhar, o que é aconselhado fazer: 

1. Comente todos os teste do **Projeto E** no arquivo de configuração (`E-Assembly/tests/config.txt`) com **exceção**  o `mov.nasm`
    - Esse módulo testa todos os registradores
1. Execute o teste com a parte do waveform: `./testeAssemblyMyCPU.py -g` 
    - **Análise o `transcript` em busca de erros!**
1. Inclua os sinais do Computador no waveform e execute o `vunit_run`
1. Analise o que está acontecendo com o seu hardware, verifique a instrução que está entrando e o que deveria acontecer.
1. Corrija o HW quando encontrar o problema, teste novamente.
1. Descomente os módulos: `abs.nasm` e teste para saber se está :ok
    - Esse módulo testa o loadPC e saídas da ULA (ng e zr)
1. Descomente os demais módulos e teste tudo.


