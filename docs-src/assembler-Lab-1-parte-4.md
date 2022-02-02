# parte 4


[Desenvolvimento baseado em testes](https://en.wikipedia.org/wiki/Test-driven_development) é uma técnica que temos utilizado até agora para os nosso projetos, nesse método fragmentando o desenvolvimento em pequenos módulos que são testados de forma individual, por testes unitários. O desenvolvimento é focado em fazer com que os módulos passem nos testes.

Como os testes não são perfeitos e não conseguem cobrir toda a funcionalidade do módulo, é necessário realizarmos o teste de integração, onde juntamos todas as peças e testamos o sistema como um todo.

Utilizaremos o mesmo recurso agora em java, onde cada módulo (método) possui um teste e quando todos os módulos estivem implementados e funcionando realizamos um teste de integração que valida tudo.

Os testes unitários foram feitos com o [JUnit](https://junit.org/junit5/) e estão na pasta do projeto: `G-Assembler/Assembler/test/java/assembler`. Os testes cobrem todas os métodos do projeto.

## Exemplo parser

Os testes são uma guia do que cada método deve fazer, e eles servirão como complemento da documentação do módulo. Iremos seguir o fluxo:

1. Ler descrição do método
1. Abrir teste unitário e entender o que é passado e o que é esperado
1. Desenvolver método
1. Testar
   - Falhou? Volte para 1.

Vamos pegar como exemplo o método `commandType` do `parser`:

```java
/**
 * Retorna o tipo da instrução passada no argumento:
 *  A_COMMAND para leaw, por exemplo leaw $1,%A
 *  L_COMMAND para labels, por exemplo Xyz: , onde Xyz é um símbolo.
 *  C_COMMAND para todos os outros comandos
 * @param  command instrução a ser analisada.
 * @return o tipo da instrução.
 */
 public CommandType commandType(String command) {
   return null;
 }
```

E seu teste unitário:

```java
/**
  * Teste para a instrução commandType
  */
@Test
public void testParser_commandType() {
  try {
      assertTrue("leaw $0,%A",parser.commandType("leaw $0,%A")==Parser.CommandType.A_COMMAND);
      assertTrue("abc:",parser.commandType("abc:")==Parser.CommandType.L_COMMAND);
      assertTrue("movw %A,%D",parser.commandType("movw %A,%D")==Parser.CommandType.C_COMMAND);
      ....
      ....
   }
}
```

Vamos analisar o primeiro teste:

```java
assertTrue("leaw $0,%A",parser.commandType("leaw $0,%A")==Parser.CommandType.A_COMMAND);`
```

- Nesse teste é passado a string `"leaw $0,%A"` para o método `parser.commandType` e esperasse na saída `A_COMMAND`.

Com essa informação complementar conseguimos inciar o desenvolvimento dessa classe.

!!! warning "Antes de continuar"
     1. Implemente a classe `parser.commandType`
     1. Execute o teste unitário do `parser` até que o `comandType` passe nos testes.
     
## Continuando

Siga para a próxima parte.
