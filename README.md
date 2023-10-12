AirBnB Clone - Command Line Interpreter
Description
The AirBnB Clone Command Line Interpreter is a Python-based tool that serves as an interactive interface for managing data objects within the AirBnB Clone project. It enables users to create, manipulate, and manage instances of various classes, such as User, Place, City, State, Amenity, and Review. This command-line tool is part of a larger project that simulates the basic functionality of the AirBnB website.

Command Interpreter
The Command Line Interpreter (CLI) allows users to interact with and manage instances of the different classes defined in the project. These classes are subclasses of a BaseModel class and represent various objects in the AirBnB ecosystem. The CLI provides commands for creating, showing, updating, and deleting instances, as well as listing all instances of a particular class.

How to Start
1- Clone the AirBnB Clone repository to your local machine:
git clone https://github.com/alghurabi0/AirBnB_clone.git
2- Change your working directory to the project folder:
cd AirBnB_clone
3- Run the command interpreter using the following command:
./console.py

How to Use
The command interpreter provides the following commands:

create <class_name>: Create a new instance of the specified class and display its unique identifier.
show <class_name> <id>: Show the string representation of an instance based on the class name and ID.
destroy <class_name> <id>: Delete an instance based on the class name and ID.
all [class_name]: Display all string representations of instances based on the optional class name filter.
update <class_name> <id> <attribute_name> "<attribute_value>": Update an instance's attributes based on the class name and ID.
quit or EOF: Exit the command interpreter.

Examples

Create a User instance:
(hbnb) create User

Show the User instance with a specific ID:
(hbnb) show User 12345

Destroy the User instance with a specific ID:
(hbnb) destroy User 12345

List all User instances:
(hbnb) all User

Update a User instance's attribute:
(hbnb) update User 12345 first_name "John"
