# API Test
My attempt at solving a python exercise on exercism.io, trying to put special attention into distributing responsibilities.

## The text of the exercise:
	
~~~~
Implement a RESTful API for tracking IOUs.

Four roommates have a habit of borrowing money from each other frequently, and have trouble remembering who owes whom, and how much.

Your task is to implement a simple RESTful API that receives IOUs as POST requests, and can deliver specified summary information via GET requests.

API Specification
User object
{
  "name": "Adam",
  "owes": {
    "Bob": 12.0,
    "Chuck": 4.0,
    "Dan": 9.5
  },
  "owed_by": {
    "Bob": 6.5,
    "Dan": 2.75,
  },
  "balance": "<(total owed by other users) - (total owed to other users)>"
}
Methods
List of user information	GET /users {"users":["Adam","Bob"]}	
Create user             	POST /add	{"user":<name of new user (unique)>}	
Create IOU              	POST /iou	{"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}	
~~~~



## Instructions:
* Install Docker and launch it to start the host;
* Build docker image and run it with: ``make docker``;
* Interact with the API through localhost or ``http://127.0.0.1/``;

## Instructions to test (requires python ^3.8):
- Install poetry: ``pip install poetry``
- launch tests: ``make tests``
