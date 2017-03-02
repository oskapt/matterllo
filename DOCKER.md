## How to
To install this project, you will need:

1. `docker`package, available with your package manager (e.g. emerge docker)

## Deployment
### Docker

    # retrieve and create the image
    $ docker build -t matterllo .

    # run the container
    $ docker run -d --name matterllo -p 8000:8000 -e TRELLO_APIKEY=<apikey> -e TRELLO_TOKEN=<token> -v data:/usr/src/app/data matterllo

    # apply the migration
    $ docker exec matterllo python manage.py loaddata admin

### Docker compose
```
version: '2'

services:
  bridge:
    build: .
    ports:
      - 8000:8000
    volumes:
      - ./data:/usr/src/app/data
    environment:
      - TRELLO_APIKEY=<APIKEY>
      - TRELLO_TOKEN=<TOKEN>

networks:
  default:
    external:
      name: main
```

## Trello callback
### Premise
* By default, Matterllo take the `django request host` to create the trello callback and receive notifications. Example with a localhost URL:
```
# bad
create trello hook :: callback=http://localhost:8000/callback/1/ :: board=tutorial-board-start-here :: result=False

# good
create trello hook :: callback=http://4308dac9.ngrok.io/callback/2/ :: board=test :: result=<trello[...]>
```

### Solutions
* You could public expose the webserver to receive trello callbacks. (nginx with a proxy pass, ngrok to test...)

* You can override the host address also.
```
$ export MATTERLLO_HOST=matterllo-foo.com
```

## old version
[**Here**](https://hub.docker.com/r/joinville/matterllo/)
