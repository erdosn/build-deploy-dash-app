# What we're doing
* Learning how to build a dash app
* Learning how to deploy that app on Heroku using their github deployment tool

# Day 1
## Things you should do
(All in terminal)
* install virtualenv `pip install virtualenv`
* create virtualenv for project `virtualenv venv`
* activate the virtual env in terminal`activate venv/bin/activate`

(After you create and activate venv)
* install dash `pip install dash`
* install dash-bootstrap-components `pip install dash-bootstrap-components`
* we'll install libraries as we need them

### Build App! 

# Day 2
## Things you should do 
* setup directory with necessary heroku files and libraries
    * These are already here so we'll just go over them 
* Setup heroku account (free)
* Create requirements.txt with `pip freeze >> requirements.txt`
* Push all changes to github and check its' up to date and working
* Deploy on heroku


## What did we learn?
* how to create a virtual environment using virtualenv
    * create `virtual envname`
    * activate `source envname/bin/activate`
    * deactivate `deactivate`
* the libraries to build a dash app
* writing app callbacks in dash
    * what triggers a callback? Input
    * state grabs the current state of attributes of components
    * output is where the return value is placed
* using pip freeze to create a requirements.txt file
    * `pip freeze >> requirements.txt`