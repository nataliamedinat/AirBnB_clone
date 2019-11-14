# AirBnB Clone - The console
In this project, we will be developing the console for our airbnb project. In this part we wrote a command interpreter to manage our AirBnB objects.

### AirBnB Folder

Files | Description
---- | ----
Authors | Authors who contributed
Readme | Readme file
console.py | Console for the AirBnB

### Models Folder
Files | Description
---- | ---- 
amenity.py | File containing class Amenity
base_model.py | File containing class base_model
city.py | File containing class City
place.py | File containing class Place
review.py | File containing class Review
state.py | File containing class State
user.py | File containing class User

### Engine Folder
Files | Description
---- | ----
file_storage | Json

## :arrows_counterclockwise: Command Interpreter

```
We are able to manage:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
```
To run the command interpreter:
```
$ ./console.py
```

## :pushpin: Examples
Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## :alien: Authors :dancers:
- [Bárbara Calle] (https://github.com/dabrabgellak)
- [Natalia Medina] (https://github.com/nataliamedinat)
