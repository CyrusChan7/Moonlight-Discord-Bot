# Moonlight Discord Bot 
  
![Unit tests](https://github.com/CyrusChan7/Moonlight-Discord-Bot/actions/workflows/python-app.yml/badge.svg)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/Python-3.6%2B-blue)
[<img src="https://img.shields.io/badge/LinkedIn-Cyrus%20Chan-blueviolet">](https://www.linkedin.com/in/cyruschan123/)  
  
## **Discord bots should be ready the moment you invite them, with no setup required.**
  
  *And we have programmed just that!* Simply invite the Moonlight Discord bot to your server and type `%help` to get started.
    
  https://discord.com/api/oauth2/authorize?client_id=616671744031326243&permissions=120259177472&scope=bot
  
### Command list:
`%avatar`  - Download another Discord user's profile picture.  
  
`%clear` - Remove a specified amount of Discord messages in a channel.
  
`%convert`  - Display real time exchange rates between two real-world currencies.  
    
`%covid` - Display real time COVID-19 statistics of a region.

`%ctf` - Convert from Celsius to Fahrenheit.  
  
`%dice` - Roll a 6-sided fair die.  
  
`%filetype` - Display information about extensions attached to the end of files.

`%ftc` - Convert from Fahrenheit to Celsius.  
  
`%help` - Display an aggregate list of all the commands.  
  
### How to host this Discord bot yourself  
  
1. Create or login to your existing Discord account.  
2. Go to `https://discord.com/developers/applications`, then click `New Application`.  
3. Type in any name of your choice, then click `Create`.  
4. Click `Bot`, then click `Add Bot` under `Build-A-Bot`.  
5. Reveal the token, then copy it.  
6. Open `Environmental Variables` options panel in your Operating System.   
7. Create a new user variable — with the variable name of `BOT_TOKEN_HOST`, and with the token value that you have copied in step 5. Remember to save the changes and restart your IDE in order to load the new env configuration.
8. Install Python3 and the pip library requirements in `requirements.txt`.  
9. Run `main.py`. (As long as the `main.py` file is running, the bot will continue responding to all the commands listed above.) 
10. (Optional) Host these files to a dedicated server if you would like the Discord bot to run without you needing your own PC turned on.
11. You're finished. Congratulations!  
  
### How to run unit tests  
  
Navigate to the root of this repository and type `python -m pytest`. Make sure you have installed the pip library requirements in `requirements.txt` first.
  
### License  
  
Copyright © 2021, [Cyrus Chan](https://github.com/CyrusChan7). Released under [MIT License](https://github.com/CyrusChan7/Moonlight-Discord-Bot/blob/main/LICENSE).
