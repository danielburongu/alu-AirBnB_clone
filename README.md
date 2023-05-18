AirBnB Clone - The console
![Alt text](images/airbnb.png)

<center> <h1>AirBnB - The Console</h1> </center>
<center> <h2>Alu-AirBnB Clone project</h2> </center>

---

The initial phase of this project involves developing a replica of the AirBnB website. The primary objective is to design a program that can convert objects into JSON files, store them persistently, and reload them when the application starts to ensure data continuity across sessions.

The subsequent phase aims to construct a console for managing the stored data. This console allows users to update, delete, and create new instances of any data class. Additionally, it tracks the creation and update timestamps of the objects it manages.
<br>
| Task | Files | Description |
| ----- | ----- | ------ |
| 0: AUTHORS/README File | [AUTHORS](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/AUTHORS) | The authors for the project |
| 1: Pep8 | N/A | All the code in the repository is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/danielburongu/alu-AirBnB_clone/tree/main/tests) | All the unit testing files for the program |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/base_model.py) | The BaseModel class to be inherited by every model class in the project, containing a few useful methods.|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py]()https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/base_model.py | Add functionality to recreate an instance of a class using a dictionary passed with Kwargs |
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/\_ _init_ \_.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/__init__.py) [/models/base_model.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/base_model.py) | Class that handles the JSON serialization and deserialization of a file, and reloads the content of the file to be used within the program through multiple sessions|
| 6. Console 0.0.1 | [console.py]( https://github.com/danielburongu/alu-AirBnB_clone/blob/main/console.py) | Add basic functionality to a console program to quit, handle empty lines, and to handle the console encountering an EOF in the input field |
| 7. Console 0.1 | [console.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/console.py) | Update the console with multiple methods in order to create, destroy, show, and update the contents of individual objects that are stored within the file storage system. |
| 8. Create User class | [console.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/console.py  ) [/models/engine/file_storage.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/user.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/user.py) | Creates a user class and update the console and file storage system to work dynamically work with the user class. |
| 9. More Classes | [/models/user.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/user.py) [/models/place.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/place.py) [/models/city.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/city.py) [/models/amenity.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/amenity.py) [/models/state.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/state.py) [/models/review.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/review.py) | Add more classes to store various information through the file storage system, and to separate similar types |
| 10. Console 1.0 | [console.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/danielburongu/alu-AirBnB_clone/blob/main/models/engine/file_storage.py) | Updates the console to work with all the classes created and update file storage |

---

<center> <h1>General Usage</h1> </center>

---

1. First clone this repository.
2. Once the repository is cloned locate the "console.py" file and run it as follows

```
/AirBnB_clone$ ./console.py
```

3. When this command is run the following prompt should appear:

```
(hbnb)
```

4. This prompt designates you are in the "hbnb" console, there are a variety of commands available once the console program is run.

##### Commands

    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

    - It is possible to call <class_name>.<command>(arguments) as well

---

<center> <h2>Prompts</h2> </center>

---

###### Example 0: Create an object

Usage: create <class_name>

```
(hbnb) create BaseModel
```

```
(hbnb) create BaseModel

(hbnb)
```

###### Example 1: Show an object

Usage: show <class_name> <class_id>

```
(hbnb) show BaseModel 
```

```
(hbnb) show BaseModel 
[BaseModel] 
'updated_at': datetime.datetime
(hbnb)
```

###### Example 2: Destroy an object

Usage: destroy <class_name> <class_id>

```
(hbnb) destroy BaseModel
```

```
(hbnb) destroy BaseModel
(hbnb) show BaseModel 
** no instance found **
(hbnb)
```

###### Example 3: Update an object

Usage: update <class_name> <class_id>

```
(hbnb) update BaseModel first_name "person"
```

```
(hbnb) update BaseModel first_name "person"
(hbnb) show BaseModel 
[BaseModel] 'created_at': datetime.datetime,
'updated_at': datetime.datetime
(hbnb)
```
