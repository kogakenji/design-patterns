# Padrão Template Method
[English version](README.md)

**Tipo: Comportamental**

Define a estrutura/esqueleto do programa ou algoritmo. Permite redefinir/personalizar determinados passos (específicos) do algoritmo em subclasses. Tira proveito de interfaces - implementações comuns.

---
## Como é usado:

Usado quando vários algoritmos implementam uma lógica semelhante, sendo que a implementação de partes específica possa ser subdividida em subclasses para ajudar a reduzir a duplicação de código.

## Objetivos:

- Definir um esqueleto de um algoritmo com operações primitivas
- Redefinir determinadas operações na subclasse sem alterar a estrutura do algoritmo
- Reutilizar código e evitar esforços duplicados
- Tirar proveito de interfaces ou implementações comuns

## Exemplos:

- Compilador multi-plataforma:

Essencialmente um compilador executa duas tarefas: reúne o código fonte e compila gerando um objeto-alvo. Podemos implementar uma classe abstrata que define o algoritmo do compilador e classes concretas que implementa os métodos abstratos e compila/executa o código.


## Operações gancho (hooks) - operações opcionais

Fornecem um comportamento padrão que subclasses podem estender se necessário. Uma operação gancho frequentemente não executa nada por padrão.

É um método declarado na classe abstrata que recebe uma implementação default. A ideia por trás dos hooks é dar a uma subclasse a capacidade de se pendurar no algoritmo sempre que for necessário. Não é obrigatório que a subclasse utilize os hooks, ela pode ignorá-los.

Em termos de implementação, usamos métodos abstratos quando a subclasse DEVE fornecer a implementação, e o hook (um método com implementação prévia) é usado quando sua implementação na subclasse é opcional.

## Princípio de Hollywood ou inversão de controle

"Não nos chame, nós chamaremos você" [[Sweet85]](https://doi.org/10.1145/17919.806843)

A classe mãe chama as operações de uma subclasse e não o contrário.

A classe abstrata de alto nível que organiza os passos para definir o algoritmo. Com base no algoritmo, as classes de baixo nível são solicitadas a definir a implementação concreta dos passos.

## Comentários sobre o padrão

- Evita duplicação de código
- Reutilização de código usando herança, necessitando de algumas sobrescritas de método
- Permite que subclasses decidam como implementar os passos do algoritmo


Desvantagens:
- Depuração e tratamento de errors pode ser confuso. A documentação e tratamento de erros devem ser feitas rigorosamente pelo desenvolvedor.

- Manutenção difícil. A manutenção do framework de templates pode gerar problemas, pois alterações em qualquer nível podem causar distúrbios na implementação.
