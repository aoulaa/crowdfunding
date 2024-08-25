# How to run crowdfunding backend


## Create `.env` file

`cp .env.template .env`

And add to this `.env` file all required environment variables.


## Run project with docker compose

Run locally:
```bash
docker-compose -f docker-compose.local.yml up --build
```

Run on server in deamon mode:
```bash
docker-compose up --build -d
```
