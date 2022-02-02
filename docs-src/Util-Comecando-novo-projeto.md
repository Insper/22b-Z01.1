# Começando novo projeto

!!! linux
    Usar o Linux fornecido!

!!! warning "Scrum Master"
    O grupo deve escolher um mediador
    
    ==Aconselhável no primeiro projeto o facilitador ser aquele que tem mais facilidade com linux e git.==

Você deve fazer a secção do seu papel: Mediador/ Desenvolvedor

## Antes de começar - Mediador

!!! note "Mediador"
    ==Somente mediador==, mas todos devem acompanhar (uma hora será sua vez).

Antes de começar será necessário atualizar o ==repositório de vocês== com os novos arquivos no repositório oficial da disciplina, e também configurar o Travis para executar os testes nesse novo projeto. 

### upstream

!!! tip "Abrindo terminal no Linux"
    <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>t</kbd>

No terminal:

1. Referenciando repositório original da disciplina

``` bash
$ git remote add upstream https://github.com/insper/Z01.1
```

2. Atualizando repositório do grupo com alterações feitas no repositório da disciplina:

``` bash
$ git fetch upstream
$ git checkout main
$ git merge upstream/main
```

Feito isso deve ter aparecido uma nova pasta dentro do repositório de vocês: `Projetos/B-LogicaCombinacional/`.
<!--
### travis

!!! tip "Arquivos ocultos"
    No linux os arquivos que começam com `.` são ocultos, ou seja, eles não
    aparecem normalmente no gerenciador de arquivos ou no comando `ls`, para ver os arquivos ocultos:
    
    - No gerenciador de arquivos aperte <kbd>crtl</kbd>+<kbd>h</kbd> (*h de hide*)
    - `ls -a` (*onde -a indica all*)

Edite o arquivo `.travis.yml` localizado na raiz do repositório modificando o final do arquivo para ficar como:

``` yml
script:
   - python3 Projetos/A-AmbienteDesenvolvimento/testeAmbienteDesenvolvimento.py
   - python3 Projetos/B-LogicaCombinacional/testeLogicaCombinacional.py 
```

Agora vamos realizar um commit e submeter aos demais colegas do grupo as alterações:

```bash
$ git add .travis.yml
$ git commit -m "configurando travis para novo projeto"
```
-->

### Actions

!!! tip "Arquivos ocultos"
    No linux os arquivos que começam com `.` são ocultos, ou seja, eles não
    aparecem normalmente no gerenciador de arquivos ou no comando `ls`, para ver os arquivos ocultos:
    
    - No gerenciador de arquivos aperte <kbd>crtl</kbd>+<kbd>h</kbd> (*h de hide*)
    - `ls -a` (*onde -a indica all*)

Edite o arquivo `actions.yml` localizado na pasta .github/workflows/ modificando o final do arquivo para ficar como:

``` yml
        python3 Projetos/B-LogicaCombinacional/testeLogicaCombinacional.py
        python3 Projetos/C-UnidadeLogicaAritmetica/testeULA.py
        python3 Projetos/D-LogicaSequencial/testeLogicaSequencial.py
```

Agora vamos realizar um commit e submeter aos demais colegas do grupo as alterações:

```bash
$ git add .github/workflows/actions.yml
$ git commit -m "configurando actions para novo projeto"
```

### `SCRUM_MASTER.json`

O mediador do projeto deve editar o arquivo `SCRUM_MASTER.json` localizado na pasta do projeto (no caso do projeto B: `Projetos/B-LogicaCombinacional/SCRUM_MASTER.json`) com os seus dados.

Após editar esse arquivo deve realizar um commit e fazer o envio para o github:

```bash
$ git commit -am "configurado scrum do projeto"
$ git push origin main
```

!!! note
    Isso é importante pois os professores irão usar esse arquivo para saber quem são os mediadores de cada projeto.

### Atualizar tools

Você deve atualizar os scripts de teste, executando o comando a seguir:

```bash
$ ./updateZ01tools.sh
```

## Antes de começar - Desenvolvedores

!!! note "Desenvolvedores"
    1. Todos desenvolvedores devem fazer essa etapa.
    1. ==Fazer isso somente depois que o mediador fez a parte dele!==

Volte para a branch main:

```
$ git checkout main
```

Agora todos os integrantes do grupo devem atualizar o repositório local:

```
$ git pull origin main
```

## Atualizando Infra

!!! warning
    Todos devem realizar essa etapa: Mediadores e Desenvolvedores

Atualizar a infra da disciplina executando o comando a seguir na pasta raiz ro repositorio:

```bash
$ ./updateZ01tools.sh
```

Isso irá baixar as dependências phython (via pip) e também clonar um repositório chamado `Z01-Tools` na raiz do usuário: `$HOME/Z01-Tools/`.
