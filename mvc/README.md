# Model-View-Controller pattern

[Portuguese (pt-br) version](README.pt-br.md)

**Type: Composite pattern**

# What are composite patterns:

Composite patterns combine two or more patterns in a solution to solve a generic recurring problem.

It is not a set of patterns that works jointly, but a more general solution to a problem.

# MVC

Software pattern to implement user interfaces (UI) and an architecture that can be easily modified and maintained. Splits the application in: model, view and controller. These parts are interconnected and help separate the way the information is represented in how it is presented.

It has the following terminology:

- Model: class to store and manipulate data
- View: class to construct UI and present data
- Controller: class that connects model and view
- User: class that request results based on actions


---
## Uses cases:

- when there is a need to change presentation without changing the business logic
- when many controllers can be used with many views to change the presentation in the UI
- model can be modified without changes in view, because they can be change interchangeably

## Objectives:

- keep separated data and presentation
- facilitate class implementation and maintenance
- flexibility to change how data is stored and presented; both can be independent and, thus, they have more flebility to change independently

## MVC components

### - Model - the data:

Provide data requested by the client. Generally represented by the tables in a database that store and return information. The model has state and methods to change its state.

### - View - the presentation:

Representation of the UI. Can be developed independently, but must not contain complex logic. The logic must be kept in the controller or model.

The views need to be flexible and appropriate to different platforms such as: desktop, mobile, tablets, etc.

The views must not interact directly with databases and must call models to get data if needed.

### - Controller - the glue:

Controls the UI interation. When the user clicks in an UI element, the controller makes a call to the model that will create, update or delete data.

The controllers provides data to the view, that renders the information so that users can visualize in the UI.

They must not call database directly and also not be involved in the data presentation. It has to act as an intermediate between the model and view and be lightweigh.

## Exemples:

- Marketing services:
Application development that provides information about marketing services offered by a company that is in the cloud, including resources such as e-mail, SMS e voice. In the model, we define the services offered by the product (e-mail, SMS, voice) with their specified prices. These represent the service data.

The view class holds methods to present data, such as list_services and list_pricing. The first presents all the services and the second presents the service with their prices.

The controller class specified methods such as get_services and get_pricing. Each of them queries the model to get data that are handled to the view for presentation.


## Comments about the pattern

- Allows separation of the application in three different parts: model, view e controller. This simplifies maintenance, assures loose coupling and reduce complexity
- Allows changes in front-end independently of backend and vice-versa
- The controller can be changed without impact in the front-end or backend 
- Helps in the hiring process of specialized people in platform (backend) or UI (front-end)
