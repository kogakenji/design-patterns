# Padrão Modelo-Visão-Controlador (MVC)
[English version](README.md)

**Tipo: Padrões Compostos**

# O que são padrões compostos:

Padrão composto combina dois ou mais padrões em uma solução que resolve um problema recorrente genérico.

Não é um conjunto de padrões que trabalha em conjunto, mas uma solução geral para um problema.

# MVC

Padrão de software para implementação de interfaces de usuário e um arquitetura que pode ser facilmente modificada e mantida. Separa a aplicação em: modelo, visão, controlador. Estas partes estão interconectadas e ajudam a separar os modos como a informação é representada da forma como é apresentada.

Trabalha com os seguintes termos:

- Modelo: classe para armazenar e manipular dados
- Visão: classe para construir interfaces de usuário e exibir dados
- Controlador: classe que conecta o modelo e a visão
- Usuário: classe que solicita determinados resultados com base em ações

---
## Como é usado:

- quando há necessidade de mudar a apresentação sem alterações na lógica de negócio
- quando vários controladores podem ser usados para trabalhar com várias visões para mudar a representação na interface do usuário
- o modelo pode ser modificado sem alterações na visão, pois eles podem trabalhar de forma independente

## Objetivos:

- manter os dados e apresentação separados
- facilitar a manutenção da classe e sua implementação
- flexibilidade para mudar o modo como os dados são armazenados e exibidos; ambos são independentes e, portanto, tem flexibilidade para mudar

## Detalhes dos componentes MVC

### - Modelo - os dados:

Fornece os dados solicitados pelo cliente. Geralmente representado pelas tabelas do banco de dados que armazenam e devolvem as informações. O modelo tem estados e métodos para alterar esses estados.

### - Visão - a aparência:

Representação em interface visual para o cliente. Pode ser desenvolvida de forma independente, mas não deve conter nenhuma lógica muito complexa. A lógica deve continuar no controlador ou no modelo.

As visões devem ser flexíveis e apropriadas para diversas plataformas como: desktop, dispositivos móveis, tablets, etc. 

As visões não devem interagir diretamente com os bancos de dados e devem fazer chamadas aos modelos para obter os dados necessários.

### - Controlador - a cola:

Controla a interação do usuário na interface. Quando o usuário clica em algum elemento da interface o controlador fará uma chamada ao modelo que, por sua vez, criará, atualizará ou apagará dados.

Os controladores também passam os dados para a visão, que renderiza a informação de modo que o usuário possa visualizá-la na interface.

Não devem fazer chamadas diretas ao banco de dados e nem se envolver na apresentação dos dados. Ele deve atuar como um intermediário entre o modelo e a visão e ser o mais enxuto possível.

## Exemplos:

- Serviços de Marketing:
Desenvolvimento de uma aplicação que informe os serviços de marketing oferecidos por uma empresa que atue na nuvem, incluindo recursos de e-mail, SMS e voz. No model, definimos os serviços oferecidos pelo produto (e-mail, SMS, voz) com seus preços especificados. Estes representam os dados dos serviços.

A classe view possui métodos para apresentar os dados, como list_services e list_pricing. O primeiro apresenta todos os serviços e a segunda apresenta os serviços com os respectivos preços.

A classe controller, especifica métodos como get_services e get_pricing. Cada um desses métodos consulta o modelo para obter os dados que são passados para a visão para apresentação.

## Comentários sobre o padrão

- Permite separar a aplicação em três partes principais: modelo, visão e controlador. Isso simplifica a manutenção, garante um baixo acoplamento e reduz a complexidade.
- Permite alterações no front-end independentes do backend e vice-versa
- O controlador pode ser também alterado sem qualquer impacto no frontend e backend
- Ajuda na contratação de pessoas especializadas em plataforma (backend) e UI (frontend)
