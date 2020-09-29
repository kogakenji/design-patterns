# Padrão Observer (Publish/Subscriber)
[English version](README.md)

**Tipo: Comportamental**

Interação entre objetos para desenvolver funcionalidades

---
## Como é usado:

Usado para monitorar mudanças e publicar notificações para objetos cadastrados/subscritos.

## Objetivos:

- Dependência de um para muitos (1 para n). Uma modificação em um objeto dispara a notificação para n objetos
- Encapsula o objeto sujeito (a fonte de mudança, publicação)

## Exemplos:

- Broadcast de publicações:

Os usuários interessados em uma publicação se cadastram no site. A cada publicação nova, eles são notificados desta nova publicação.

- Sistema de alerta

Os contatos dos operadores do sistema devem estar cadastrados (e.g. telefone). Caso o sistema venha a falhar, uma notificação SMS será enviada para o celular dos interessados sobre a falha.

## Modelos do padrão

- Modelo Push

É o mais comum e o publicador desempenha o papel dominante, já que os interessados já registraram seu interesse na publicação.

O publicador (subject) pode enviar mensagens detalhadas para os interessados.

Há um problema de lentidão caso uma grande quantidade de informação seja enviada para os interessados. Neste caso, somente os dados necessários devem ser enviados para que o desempenho seja melhor.

- Modelo Pull

Os interessados buscam as mudanças do publicador. Este não é um modelo muito eficiente, pois os interessados devem buscar as mudanças que ocorreram.

Isto funciona neste padrão da seguinte forma. O publicador notifica os interessados que houveram mudanças e os interessados buscam a mudança do publicador.

## Comentários sobre o padrão

- Oferece suporte para o princípio de baixo acoplamento entre objetos
- Permite enviar dados a outros objetos de modo eficiente
- Flexibilidade na inclusão/remoção de objetos observers

Desvantagens:
- A interface observer deve ser implementada por ConcreteObserver, o que envolve herança. Não há possibilidade de composição.
- Pode acrescentar complexidade e levar a problemas de desempenho
- Notificações podem não ser confiáveis e resultar em condições de concorrência ou inconsistência.

