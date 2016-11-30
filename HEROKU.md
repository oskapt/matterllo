## How to
To install this project using Heroku, you will need:

1. A Heroku account, available for free from [Heroku.com](http://heroku.com)
2. A Heroku CLI, available for free from [Heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

## Deployment to Heroku
    $ cd <path_to_matterllo_repository>
    
    $ heroku login
    
    $ heroku create

    $ git push heroku master

    $ heroku run python manage.py migrate

    # automatically create a default superuser.
    $ heroku run python manage.py loaddata admin

    # set the necessary Trello stuff.
    $ heroku config:set TRELLO_APIKEY=<your_api_key>

    $ heroku config:set TRELLO_TOKEN=<your_token>

    # enjoy
    $ heroku open

## Production ready
### Change your admin password
1. Go to the Admin page
2. Use the default account: `admin`/`admin`
3. Go to the `User` part and change the password through the form

### Change the secret
    $ heroku config:set SECRET=<your_secret>

## Technical overview
* `postgresql` is the default database. `Sqlite` is not persistent under Heroku.
* All database objects can be directly manipulate throught the admin interface.
