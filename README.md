## Digitalocean Template Repos
This repository contains a template for a background worker process suitable for running a Discord bot.

## Deploying the App

Click this button to deploy the app to the DigitalOcean App Platform. If you are not logged in, you will be prompted to log in with your DigitalOcean account.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/digitalocean/template-discord-bot-worker/tree/main)

Using this button disables the ability to automatically re-deploy your app when pushing to a branch or tag in your repository as you are using this repo directly.

## How to setup 
1. Install discord.py
    - Run "pip3 install discord.py"
2. Create and configure a discord bot.
    - Go to the Discord Developer Portal and add a new application. Go to the "Bot" settings and copy the token to use as your 'DISCORD_TOKEN'.
    - Under Bot Permissions, select the Text Permissions that you would like to allow for the bot. Enable "Message Content Intent".
    - Go to OAuth2 settings and select "bot" from the Scopes. Again under Bot Permissions, select the Text Permissions that you would like to allow for the bot.
    - At the bottom, copy the Generated URL and paste it into a new tab. Select the server you want to add the bot to and this will allow the bot to connect to your server.
3. Run the application.
    - Run "python3 discord_bot.py"
