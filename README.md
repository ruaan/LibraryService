[![Build Status](http://jenkins.tangentme.com/buildStatus/icon?job=Deploy LibraryService to Staging)](http://jenkins.tangentme.com/view/MicroServices/job/Deploy%20LibraryService%20to%20Staging/)

# LibraryService
A Service for tracking and requesting books for the Tangent Library

## Installation 

**Clone the repo.**

    git clone git@github.com:TangentMicroServices/LibraryService.git

**Create virtualenv**

    virtualenv env
    source env/bin/activate

**Install requirements**

    pip install -r requirements.txt

**Run server**

    python manage.py runserver

## Testing

**Run unit tests**
 
   python manage.py test

**Run integration tests**

   python manage.py test --pattern="*_ITCase.py"
