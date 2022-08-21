# ⚗️ Flask starter

Simple demo of a containerised Flask API

## To run

```sh
docker compose --env-file .env.dev up -d --build server
```

This will set up the app using the host and port specified in `.env.dev`
(by default this is `0.0.0.0` and `9876`, respectively)

## Endpoints

Only one endpoint is defined currently:

`GET /api/v1/status`
