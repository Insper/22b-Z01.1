# Dicas git

## Clonando repositório

```bash
$ git clone URL_DO_SEU_REP
```

## Instalando/Atualizando Z01-tools

```
$ cd SEU_REP
$ ./updateZ01tools.sh
```

O script `updateZ01tools.sh` clona o repositório http://github.com/Insper/z01-tools e o salva em sua pasta $HOME (/home/user/). O script serve para instalar e/ou atualizar a infra da disciplina, deve ser executado sempre que indicado pelo professor.

## Configurando upstream (Z01.1 professor)

Referenciando repositório original da disciplina:

```bash
$ git remote add upstream https://github.com/insper/Z01.1
```

### Atualizando repositório do grupo

Atualizando repositório do grupo com alterações feitas no repositório da disciplina:

```bash
$ git fetch upstream
$ git checkout main
$ git merge upstream/main
$ git push origin main
```
