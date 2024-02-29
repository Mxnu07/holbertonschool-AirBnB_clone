# AirBnB Clone Project

This project is an implementation of a simplified version of the AirBnB website, including a command-line interface (CLI) to interact with the implemented functionalities.

## Command Interpreter

### Starting the Command Interpreter

To start the command interpreter, run the console.py file from the terminal using Python:

```bash
holbertonschool-AirBnB_clone % ./console.py
```

## How to Use the Command Interpreter

Once the command interpreter is running, you can enter various commands to interact with the AirBnB functionalities. Here are some examples of commands you can use:

### Creating an Instance:

To create a new instance of a class, use the `create` command followed by the name of the class. For example, to create a new instance of the BaseModel class:
```bash
(hbnb) create BaseModel
```
### Showing an Instance:

To display the details of an existing instance, use the `show` command followed by the name of the class and the instance ID. For example, to display the details of an instance of the BaseModel class with ID 1234-5678:
```bash
(hbnb) show BaseModel 1234-5678
```
### Destroying an Instance:

To delete an existing instance, use the `destroy` command followed by the name of the class and the instance ID. For example, to delete an instance of the BaseModel class with ID 1234-5678:
```bash
(hbnb) destroy BaseModel 1234-5678
```
### Updating an Instance:

To update the attributes of an existing instance, use the `update` command followed by the name of the class, the instance ID, the attribute name, and the new attribute value. For example, to update the email attribute of an instance of the User class with ID 1234-5678:
```bash
(hbnb) update User 1234-5678 email "newemail@example.com"
```
### Listing all Instances:

To display a list of all instances of a specific class or all classes, use the `all` command followed by the name of the class (optional). For example, to list all instances of the BaseModel class:
```bash
(hbnb) all BaseModel
```
---

## Examples

Here are some examples of how to use the command interpreter:

- ### Creating a new instance of BaseModel:
```bash
(hbnb) create BaseModel
```
- ### Showing details of an instance of BaseModel:
```bash
(hbnb) show BaseModel 1234-5678
```
- ### Destroying an instance of BaseModel:
```bash
(hbnb) destroy BaseModel 1234-5678
```
- ### Updating an instance of User:
```
(hbnb) update User 1234-5678 email "newemail@example.com"
```
- ### Listing all instances of BaseModel:
```bash
(hbnb) all BaseModel
```
### Enjoy using the AirBnB Clone Command Interpreter!
---
## Authors
- Lesty Carrion
- Manuel Morales
