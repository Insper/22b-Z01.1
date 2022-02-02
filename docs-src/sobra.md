## Configurando Travis


- Criando um project no github

![Project](figs/C-LogiComb/C-2-project.gif)

- Adicionando issues

![Issues](figs/C-LogiComb/C-3-issues.gif)

Os issues devem ser [todos os módulos](https://github.com/Insper/Z01.1/wiki/C-Logica-Combinacional-Projeto#o-que-deve-ser-feito-) a serem implementados do projeto.


## Referenciando a raiz

Para começar será necessário atualizar o fork do repositório que vocês criaram, com novos dados que serão colocados no repositório da disciplina. Uma vez clonado o repositório, você deve entrar na pasta via o terminal:

``` bash
$ cd Z01.1-NomeDoGrupo
```

Estando na pasta do repositório precisamos agora indicar para o repositório original na qual o repositório que deu origem a esse fork, para isso devemos executar a seguinte linha de código: 

``` bash
$ git remote add upstream https://github.com/insper/Z01.1
```

Para verificar se deu certo, execute:

``` bash
$ git remote -v
```

E deve aparecer além do link para o repositório de vocês a referência ao repositório original:

``` bash
upstream	https://github.com/insper/Z01.1 (fetch)
upstream	https://github.com/insper/Z01.1 (push)
```

!!! tip 
    Dúvidas?
    
    - https://gist.github.com/CristinaSolana/1885435
    - https://help.github.com/articles/syncing-a-fork/

## Sincronizando com upstream

!!! warning "Apenas mediador"
    Essa etapa deve ser realizada apenas pelo mediador do projeto!

Para atualizar o repositório do grupo de vocês com as novas atualizações inseridas no repositório da disciplina basta executar:

``` bash
$ git fetch upstream
```

Agora precisamos realizar um merge desse branch (que contém as atualizações do repositório da disciplina) com o master:

``` bash
$ git checkout master
$ git merge upstream/master
```

Precisamos submeter essa atualização para o repositório remoto a fim de todos do grupo terem acesso a versão mais nova.

``` bash
$ git push origin master
```



!!! note "Dicas VHDL"
    Existem diversos locais onde podem tirar dúvida de `VHDL`, por exemplo : 

    - :+1: http://esd.cs.ucr.edu/labs/tutorial/
    - https://courseware.ee.calpoly.edu/cpe-169/Misc_stuff/cheat_sheet.pdf
    - https://www.ics.uci.edu/~jmoorkan/vhdlref/vhdl_golden_reference_guide.pdf
