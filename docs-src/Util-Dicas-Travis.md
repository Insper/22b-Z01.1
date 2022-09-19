# Dicas Actions

## Adicionando teste ao projeto

Edite o arquivo `actions.yml` localizado na pasta .github/workflows/, adicionando o script que deseja testar. Exemplos, para testarmos o projeto B é necessário adicionar a seguinte linha:

```
python3 B-LogicaCombinacional/testeLogicaCombinacional.py 
```

Isso deve ser feito na parte final do arquivo

``` 
        python3 B-LogicaCombinacional/testeLogicaCombinacional.py
        python3 C-UnidadeLogicaAritmetica/testeULA.py
        python3 D-LogicaSequencial/testeLogicaSequencial.py
```

!!! warning
    Você não deve remover os testes antigos
