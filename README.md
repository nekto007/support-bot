# Support Bots for Telegram and VK

## Overview
This project consists of support bots for VK and Telegram messaging platforms. 
These bots are designed to provide support to users in a group on VK and a channel on Telegram using the Dialogflow natural language understanding platform.



## Prerequisites
Before you can run the support bots, you will need the following tokens and identifiers:

- `SUPPORT_BOT_KEY`: Telegram Bot Token
- `PROJECT_ID`: Google Cloud Project ID
- `VK_TOKEN`: VKontakte Community Token
- `GOOGLE_APPLICATION_CREDENTIALS`: Google Application Credentials JSON file path (for Google Cloud services)

Make sure to obtain these tokens and identifiers from the respective platforms and services.

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/nekto007/support-bot.git
    ```

2. Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Edit the configuration files or environment variables with your tokens and identifiers:

- For VK bot, update `VK_TOKEN` in the VK configuration file.
- For Telegram bot, set `TELEGRAM_TOKEN` in the Telegram configuration file.
- Set `PROJECT_ID` for Dialogflow integration.
- Set `QUESTION_FILE` for path to file with questions. By default using `questions.json`.

## Training bot

1. Question File Format

Your question and answer file should be in the following format:

```json
{
    "display_name": {
        "questions": ["questions1", "questions2"],
        "answer": "ответ"
    }
}
```

## Run

```bash
python api.py
```

## Usage
1. Run the VK support bot:

    ```bash
    python vk_bot.py
    ```

2. Run the Telegram support bot:

    ```bash
    python tg_bot.py
    ```

3. Your bots are now active and ready to provide support in your VK group and Telegram channel.

## Dialogflow Integration
These bots use Dialogflow for natural language understanding and responses. 
Make sure you have configured Dialogflow intents and entities to handle user queries effectively.
