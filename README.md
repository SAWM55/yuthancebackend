# yuthancebackend

[![Build Status](https://travis-ci.org/Dave-mash/yuthancebackend.svg?branch=master)](https://travis-ci.org/Dave-mash/yuthancebackend)
[![Coverage Status](https://coveralls.io/repos/github/Dave-mash/yuthancebackend/badge.svg?branch=master)](https://coveralls.io/github/Dave-mash/yuthancebackend?branch=master)

Yuthance backend API

## Features

[] A user should be able to sign up.
[] A user should be able to log in.
[] A user should be able to log out.
[] A user should be able to add an item to cart.

## Installation

* Clone this repository and cd into the folder.
`git clone https://github.com/SAWM55/yuthancebackend.git`
`cd yuthancebackend`

* Create a virtual environment
`python3 -m venv venv`

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
`pytest --cov=app`
