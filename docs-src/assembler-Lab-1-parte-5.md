# parte 5

Implemente o método `initialize` da classe `SymbolTable` utilizando os conceitos visto nos outros labs. 

O initialize utiliza outros métodos dessa classe, edite eles:

```java
    public void addEntry(String symbol, int address) {
        symbolTable.put(symbol, address);
    }
```

```java
  public Boolean contains(String symbol) {
        return symbolTable.containsKey(symbol);
    }
```

```java
 public Integer getAddress(String symbol) {
        return symbolTable.get(symbol);
    }
```

Agora com os demais métodos implementando faça o `initialize`.

!!! tip
    Use os testes para ajudar entender o que o método faz.

Tabela de símbolos? De uma lida na [teoria/Tabela de Símbolos](https://insper.github.io/Z01.1/assembler-Dicas-SymbolTable/)
