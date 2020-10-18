# Template Method pattern

[Portuguese (pt-br) version](README.pt-br.md)

**Type: Behavioral**

Defines the structure of a program or algorithm. Allows redefinition/customisation of specific steps of the algorithm in subclasses. Take advantage of interfaces - common implementations.

---
## Uses cases:

Used to implement a common logic and when specific parts can be subdivided in subclasses to reduce code duplication.

## Objectives:

- Defines an skeleton of an algorithm with primitive operations
- Redefine specific operations in the subclasses without changing the algorithm structure
- Reuse code and avoid duplicated efforts 
- Take advantage of interfaces and common implementations

## Examples:

- Multiplatform compiler:

Essencially a compiler executes two tasks: combine source code and compile generating a target object. We can implement an abstract class that defines a compiler's algorithm and concrete classes that implement abstract methods and compile/execute the code.

## Hook operations (hooks) - optional operations

Provides a standard behaviour which subclasses can extend if necessary. A hook operation frequently doesn't execute anything.

It is a method declared in the abstract class that has a default implementation. The idea is to give a subclass the possibility to hook in the algorithm if necessary. It is not mandatory that the subclass use hooks, the subclass can ignore them.

During implementation, we use abstract methods when the subclass MUST provide the implementation, and a hook (a method with a default implementation) is used when its implemetation in the subclass is optional.

## Hollywood principle or Inversion of Control (IoC)

"Don't call us, we'll call you" [[Sweet85]](https://doi.org/10.1145/17919.806843)

The main class call the operations in the subclass and not the contrary.

The higher level abstract class organizes the steps to define the algorithm. Based on the algorithm, the lower level classes are requested to define the implementation of concrete steps.

## Comments about the pattern

- Avoids code duplication
- Reuse code using inheritance, using some method overwrites 
- Allows that subclass decide how to implement the algorithm steps 

Disadvantages :
- Debugging and exception handling can be hard. Documentation and exception handling must be done extensively by the developer

- Difficult maintenance. The templates framework maintenance can generate problems, because changes in any level can generate disturbances in the implementation