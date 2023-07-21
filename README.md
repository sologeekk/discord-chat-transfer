
# Discord Servers Chat Transfer Aid Tool

## Description
After exporting your Server Channels Chat Data using this amazing [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) Tool by @Tyrrrz into your local computer in `.json` format, You can proceed to do some further processing and filtering on exported json files and gain simple output in `.txt` format and Simply Copy Paste the contents Separated by Channels to your New Channel. At the Moment, It just extracts Authors + Links from each message and Only works with `.json` format but you can simply customize and modify it based on the following instructions and By getting some Help from Mr. ChatGPT :)

***Attention: Check the Workflow below and Follow Instructions with example to Figure how properly Use this tool***

<br />

## Workflow
![image](https://github.com/sologeekk/discord-chat-transfer/assets/74742927/b8c64c36-f13b-4145-b922-c1f92f6afeff)


<br />

## Example with Instructions
1. I have A Server with such Categories (Hacking and General Text Chatting) and Related channels:

![image](https://github.com/sologeekk/discord-chat-transfer/assets/74742927/82304093-be20-475a-b900-ad7f4298863c)
![image](https://github.com/sologeekk/discord-chat-transfer/assets/74742927/ba1587a5-58b6-4da7-98d3-4ee31bf3b040)


2. Using the [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) Tool by @Tyrrrz, I have **Manually** exported each of the Channels Chat in `json` format by assiginng them names that will start with a `Capital Alphabet of their relevant Category + a dash + The name of the Channel` for example: `"G-Freechat.json"`. Under the related category folder we have:
```powershell
├───General Text Channels
│       G-Freechat.json
│       G-Live Hacking.json
│
└───Hacking
        H-BlueTeam.json
        H-Cryptography.json
        H-Forensics.json
        H-Lateral and Priv Escalation.json
        H-Misc.json
        H-Network.json
        H-OS.json
        H-Osint and Social.json
        H-Pwn and Binary.json
        H-Recon.json
        H-RedTeam.json
        H-Rerverse Engineering.json
        H-Threat Intel.json
        H-VIP.json
        H-Web.json
```

3. Now Should I put the `Discord_Parser.py` file in the path that my Category Directories are and modify every Line that holds information about Categories or Directories in my code:
```python
# Line 4 and 5 - Categories Folder Directories

# Line 14 - The Dictionary that holds the First Alphabet of Your Categories 

# Line 35 to 41 If you want to extract other types of data such as line 37:
> if items["content"]

# Line 54 and 55 - Change the Names of Variables into Your Categories Names
```

4. By running the code you should have such results:
```powershell
│   OutJsonFile.json
│
├───G
│       G-Freechat.txt
│       G-Live Hacking.txt
│
└───H
        H-BlueTeam.txt
        H-Cryptography.txt
        H-Forensics.txt
        H-Lateral and Priv Escalation.txt
        H-Misc.txt
        H-Network.txt
        H-OS.txt
        H-Osint and Social.txt
        H-Pwn and Binary.txt
        H-Recon.txt
        H-RedTeam.txt
        H-Rerverse Engineering.txt
        H-Threat Intel.txt
        H-VIP.txt
        H-Web.txt
```

5. And The contents of `H-Cryptography` for example:
```powershell
IAmTalas:
https://www.youtube.com/watch?v=8COArd_EREw
IAmTalas:
https://github.com/Baptiste-Leterrier/md5-collision-finder
mah0x6b:
https://cryptii.com/
```

6. And from here, you will have multiple files and options that each of them points to the contents of an specific channels, all you have to do is to open the file, `Copy + Paste` the contents of it to the newly Created channel in your second server.

<br />

## To-Dos
- [ ] Add some Extra Automation to automate the process of manually saving each file, naming it with the Capital format of the first char of it's related Category and Automating the process of copy pasting it to new Discord Channels
- [ ] Add support for other File formats such as .html
- [ ] Add options to aid user extract other type of data automatically by selecting in the menu

<br />

## Contributions
This is The very simple version of what I had initally in my mind, Hope find some free time to improve it. But Please feel free to contribute in the project as you like. 
*Also I'm open to any new ideas :3*

## Credits
So Grateful of the amazing [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) Tool by @Tyrrrz. 
