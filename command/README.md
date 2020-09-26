# Command Pattern

[Portuguese (pt-br) version](README.pt-br.md)

**Type: Behavioral**

Interaction between objects to develop functionalities

---
## Uses cases:

Used to encapsulate information to execute an action.

Information includes: method name, object owner of the method, parameter values.

## Objectives:

- encapsulate requests as an object
- allows setting parameters for requests from clients 
- allows requests to be saved in a queue
- OO callbacks 

## Exemples:

- Installation wizard: 

The wizard has many steps to capture the users' preference.

- Printer spool:

Store printing settings, for example A4 page, orientation landscape/portrait, grouped/not grouped. When an user print, he/she executes the method execute() from Command and the page is printed with the stored settings.

- Stock market:

An user from stock market usually sell and buy with a broker between the user and the stock market. This agent is responsible to send your request to the stock market. When the user sends a request to the broker, it queue this request and send this for the stock market to execute when it is open.

## Comments about the pattern

- Decouple classes which invokes operations in objects that know how to execute them
- Allow the creation of a queue system with a sequence of commands 
- New commands are easy to implement, which can be made without the need to change existing code
- Allow the implementation of a rollback system

Disadvantages:
- High number of classes and objects. Developers should take care to correctly develop classes
- All individual command is a ConcreteCommand class which increases the number of classes to implement and maintain