# PyAuto

This project is a simple voice-activated assistant that can perform tasks such as searching Wikipedia, opening websites, sending emails, and telling the current time. 

The assistant responds to voice commands and uses text-to-speech to communicate with the user.

## Features

- **Greeting and Assistance**: The assistant greets the user based on the time of day and offers help.
- **Voice Recognition**: Listens to voice commands and processes them.
- **Wikipedia Search**: Searches Wikipedia and reads a brief summary aloud.
- **Open Applications**: Can open Notepad, YouTube, and Google in the default web browser.
- **Tell the Time**: Tells the current time.
- **Send Emails**: Sends an email to a specified recipient using Gmail.
- **Personalized Commands**: Responds to specific voice commands like opening your YouTube channel.

## Installation

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Required Python Libraries

Install the required Python libraries using the following command:

```bash
pip install -r requirements.txt
```

### File Structure

- `app.py`: The main Python script containing the voice assistant code.
- `requirements.txt`: List of dependencies required to run the project.

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the `main.py` script using Python.
   ```bash
   python main.py
   ```
4. The assistant will greet you and start listening for your commands.

## Voice Commands

Here are some of the voice commands you can use:

- **"Open Wikipedia [your query]"**: Searches Wikipedia for your query and reads a summary.
- **"Open Notepad"**: Opens Notepad on your computer.
- **"Open YouTube"**: Opens YouTube in your default web browser.
- **"Open Google"**: Opens Google in your default web browser.
- **"Tell me the time"**: Tells the current time.
- **"Email to my friend"**: Prompts you to dictate an email, then sends it to a predefined email address.
- **"Open Resultyst YouTube"**: Opens the Resultyst YouTube channel.
- **"Exit" or "Stop"**: Exits the assistant.

## Configuration

- **Email Settings**: 
  - The assistant uses Gmail to send emails. Update the `sendEmail` function with your own email and password.
  - Ensure your Gmail account allows access from less secure apps or use an app-specific password if 2FA is enabled.

## Notes

- The assistant is designed to work on Windows, and some features like opening Notepad might not work on other operating systems.
- Ensure your microphone is working properly for accurate voice recognition.
- The Google Speech Recognition service requires an active internet connection.

