# pymongo-tutorial
This is flask and mongodb based simpe user information query api.

## Query

With HTTP request method.

**GET Parameter**
* _id

**List of POST Parameters**
* _id
* name
* surname
* mail
* phone



![Postman Image](postman.png)

## Insert data
Send POST with **insert** parameter: Json text containing *name, surname, mail, phone* data.

>{"mail":"yunus@mail.com","surname":"Agtas","name":"Yunus","phone":"123456"}

After, will return you inserted document id.
