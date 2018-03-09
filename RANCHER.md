## Running under Rancher

Once you have an API key/token and a [Docker container](DOCKER.md) built and stashed in a registry, you're ready to fire this up under Rancher.

## Prep Work
1. Create two secrets
    - `trello_apikey_v1`
    - `trello_token_v1`
1. Create a new stack/service
2. Set the image to your registry image (`monachus/matterllo:latest`)
3. Attach a persistent volume to `/usr/src/app/data`
3. Attach your secrets to the service as:
    - `apikey`
    - `token`
4. Set two environment variables pointing to your secrets locations:
    ```
    TRELLO_APIKEY_FILE=/run/secrets/apikey
    TRELLO_TOKEN_FILE=/run/secrets/token
    ```
5. If you want to map a port directly to the service, do so. If you plan to use a load balancer, skip this step
6. Override the command to be `/bin/bash`
6. Launch your service
7. Connect to the service with a shell and run the following:
    ```
    python manage.py migrate
    python manage.py loaddata admin
    ```
8. Exit the shell

## Production Run
1. Upgrade the container and remove the override to the command
2. Expose the container's port via load balancer, if necessary
3. Wrap the site in TLS via LetsEncrypt





