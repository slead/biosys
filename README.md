# BioSys - Biological Survey Database System #

BioSys is a biological survey database system for Science and
Conservation Division within the Department of Parks and Wildlife.

GitHub:
[BioSys](https://github.com/parksandwildlife/biosys)

## Getting Started

Biosys is built on Django, the Python web framework and also requires a PostgreSQL database server
(9.3+) with the PostGIS extension.

It is recommended that the system is run in a Python virtual environment to allow the dependent
libraries to be installed without possible collisions with other versions of the same libraries.

### Spin-up

- create a `biosys` virtual enviroment
- create a `biosys` postgres db
- run: `pip install -r requirements_DBCA.txt` within the `biosys` venv
- copy `.env.exmaple` to `.env`
- run: `./manage.py migrate`
- run: `./manage.py runserver`


## Requirements

### Supporting Applications / Packages:

- Python 2.7 or 3.6 (Some dependencies fail on 3.7)
- PostgreSQL (>=9.3)
- PostGIS extension (>=2.1)
- GDAL (>=1.10)

### Python Libraries

Python library requirements should be installed using `pip`:

`pip install -r requirements.txt`

## Environment settings

The following environment settings should be defined in a `.env` file
(set at runtime by `django-confy`). Required settings:

    DJANGO_SETTINGS_MODULE="biosys.settings"
    DEBUG=True
    DATABASE_URL="postgis://USER:PASSWORD@HOST:PORT/NAME"
    SECRET_KEY="ThisIsASecretKey"
    CSRF_COOKIE_SECURE=False
    SESSION_COOKIE_SECURE=False

## Running

Start the application on port 8080:

`python manage.py runserver 0.0.0.0:8080`

## Testing

To run unit tests or generate test coverage reports:

    python manage.py test -k -v2
    coverage run --source='.' manage.py test -k -v2
    coverage report -m

## AWS Elastic Beanstalk deployment

This project is set for Elastic Beanstalk deployment through the `.elasticbeanstalk` dir with the `.ebextensions\*` environment configuration.
Note: the deployment is set tu use the 3.6 eb platform.  

You have to install the eb cli:  
`pip install awsebcli`  
Note: It is recommended to install the eb cli in a different virtual env than the project.

You have to have the right credentials set for you AWS account. (~/.aws/credentials)

Example of how to create an environment:

    # create a environment with a load balancer with 2 EC2 + a postgres RDS micro
    eb create --scale 2 -db -db.engine postgres -db.i db.t2.micro
    # same as above with no load balancer (single instance)
    eb create --single -db -db.engine postgres -db.i db.t2.micro
    # example of uat for slug (mksas). One instance but with load balancer
    eb create --scale 1 -db -db.engine postgres -db.i db.t2.micro --profile mksas
    
Check environment
    
    eb status
    
Deploy :
    
        example: deploy on OEH uat. This assume you have an oeh AWS credential profile. 
        eb deploy biosys-uat --profile oeh
 