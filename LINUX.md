## How to
To install this project, you will need:

1. `pip` package, available with your package manager (e.g. apt-get install python-pip).

## Deployment
    $ cd <path_to_matterllo_repository>

    $ pip install -r requirements_base.txt

    $ python manage.py migrate

    # automatically create a default superuser.
    $ python manage.py loaddata admin

    # set the necessary Trello stuff.
    $ export TRELLO_APIKEY=<your_api_key>

    $ export TRELLO_TOKEN=<your_token>

    $ python manage.py runserver

    # you must public expose the webserver to receive trello callbacks.
    # - use nginx with a proxy pass
    # - use ngrok for test (ngrok http 8000)
    # - etc.. 

## Production ready
### Change your admin password
1. Go to the Admin page
2. Use the default account: `admin`/`admin`
3. Go to the `User` part and change the password through the form

### Change the secret
    $ export SECRET=<your_secret>

## Technical overview
* `sqlite` is the default database.
* All database objects can be directly manipulated through the admin interface.
