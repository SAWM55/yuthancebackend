# yuthanceAPI

[![Build Status](https://travis-ci.org/Dave-mash/yuthancebackend.svg?branch=master)](https://travis-ci.org/Dave-mash/yuthancebackend)
[![Coverage Status](https://coveralls.io/repos/github/Dave-mash/yuthancebackend/badge.svg?branch=master)](https://coveralls.io/github/Dave-mash/yuthancebackend?branch=master)

Yuthance backend API

## Features

### User accounts

* [x] A user should be able to create an account.
* [ ] A user should be able to log in to their account.

### Cart

* [ ] A user should be able to add an item to cart.

### Transactions

* [ ] A user should be able to make a payment

## Installation

* Clone this repository and cd into the folder.
`git clone https://github.com/SAWM55/yuthancebackend.git`
`cd yuthancebackend`

* Create a virtual environment
`python3 -m venv env`

* Set the environment variables
`mv .env.example .env`
`source .env`

* Install dependencies
`pip install -r requirements.txt`

* Perform migrations
`python manage.py migrate`

* Create superuser
`python manage.py createsuperuser --email admin@example.com --username admin`

* Run the app
`python manage.py runserver`

* Testing
`pytest`

### Yuthance application endpoints

| Endpoint        | Functionality           | HTTP method  |
| ------------- |:-------------:| -----:|
| `/users/?format=json`      | Register a user | POST |
| `/users/<int:id>`      | view, edit, delete a user | GET, PATCH, DELETE |
| `/auth/login`      | Login a user       |   POST |

### Authors

David Macharia @[Dave-mash](https://github.com/Dave-mash)
