# Plex Inviter
Custom plex invitation script with accompanied email using `plexapi`, `flask` and `smtplib`.

All configuration is within `config.yaml`.

## Build Docker image
```
docker image build -t plex_invitation .
```
## Start container
```
docker run -p 5000:5000 -d --name plex_invitation plex_invitation
```

## Web server
Webpage accessible on `localhost:5000`.

## Important note: If you expose this page outside your network, you will need to secure it. E.g. login page.


