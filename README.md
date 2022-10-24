# RentABot
WARNING: PET PROJECT NOT PRODACTION READY

This project let you make your Telegram bot follow some scenarios, you only need to provide token. Many peaple can get they own Telegram bot, with no programming skills.

### How to run
`docker-compose -f docker-compose.dev.yml up -d`

With this setup you can call endpoints, but Telegram webhook (and added bots) will not work. You need domain name and SSL for that. I personaly use SSH reverse tunel and remote server with domain/SSL for development.

Docs:
`0.0.0.0:8000/docs` or `0.0.0.0:8000/redoc`

### How to use
Use Swagger interface on `/docs` to make requests.
- Create user and authenticate using corresponding endpoints in `auth` section
- Create bot using your token from @BotFather. You have to chose one of few scenarios
- If your webhook is configured (see "How to run") everything should work at this point
