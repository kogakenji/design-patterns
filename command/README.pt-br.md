# Padrão Command
[English version](README.md)

**Tipo: Comportamental**

Interação entre objetos para desenvolver funcionalidades

---
## Como é usado:

Usado para encapsular informações para executar uma ação posteriormente.

Informações incluem: nome do método, objeto dono do método, valores dos parâmetros.

## Objetivos:

- encapsular requisições como um objeto
- possibilitar parametrização das requisições dos clientes
- permitir salvar requisições em uma fila
- oferece callback OO

## Exemplos:

- Assistente de instalação: 

O assistente possui várias etapas e captura as preferências do usuário.

- Bobina de impressão:

Armazena as configurações da impressão, por exemplo página A4, disposição (retrato/paisagem), agrupado/não agrupado. Quando o usuário mandar imprimir, ele executa o método execute() do Command e a impressão sai com as configurações armazenadas.

- Bolsa de valores:

Um usuário da bolsa de valores compra e vende usualmente através de uma corretora entre ele e a bolsa de valores. Esse agente é responsável por enviar a requisição para a bolsa de valores. Quando o usuário enviar a requisição para a corretora, ela enfileira essa requisição e envia para a bolsa de valores para ser executada quando estiver aberta.

## Comentários sobre o padrão

- Desacopla as classes que invocam a operação do objeto que sabe como executá-la
- Permite criar uma sequência de comandos oferecendo um sistema de fila
- Extensões para adicionar um novo comando são fáceis de implementar, pode ser feito sem alterar o código existente
- Possibilita a implementação de um sistema de rollback

Desvantagens:
- Número elevado de classes e objetos. O desenvolvedor deve tomar cuidado para desenvolver essas classes corretamente
- Todo comando individual é uma classe ConcreteCommand que aumenta o número de classes para implementação e manutenção.