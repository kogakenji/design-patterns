# Observer pattern

[Portuguese (pt-br) version](README.pt-br.md)

**Type: Behavioral**

Interaction between objects to develop functionalities

---
## Uses cases:

Used to monitor changes and publish notifications to registered/subscribed objects.

## Objectives:

- One to many (1 to n) dependency. A single change in an object triggers the notification to n objects.
- Encapsulate the subject object (source of the change, publish).

## Examples:

- Publication Broadcast:

Interested users register themselves. For each new publication, they get notifications of this new publication.

- Alert system

The system operator contacts should be registered (e.g. phone number). If the system fails, an SMS notification can be sent through the phone to the registered ones about the failure.

## Design pattern models

- Push model

The most common and the publisher plays the dominant role, since the interested already registered their interest in the publication.

The publisher (subject) can send detailed messages for interesteds.

There is a problem of delay when a huge amount of information is sent to the interesteds. In this case, only the necessary data may be sent for the performance to be better.

- Pull model

The interested pulls the changes from the publisher. This is not a very efficient model, because the interested should pull the changes that happened.

This works in this pattern the following way: the publisher notifies the interested that changes happened and the interested pulls the changes from the publisher.

## Comments about the pattern

- Offers support to the loose coupling principle between objects
- Promote the exchange of data between objects efficiently
- Flexibility in add/remove observer objects


Disadvantages:
- The observer interface must be implemented by the ConcreteObserver, which involves inheritance. There is no possibility of composition.
- May add complexity and cause performance issues
- Notifications can be unreliable and result in race conditions or inconsistencies
