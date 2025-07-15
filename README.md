# Emily - The AI Virtual Assistant
## Introduction
Emily is a voice-controlled AI virtual assistant built using Python. It can perform various tasks such as providing real-time weather updates, fetching Nobel Prize information, reading top news headlines, and opening popular websites. Emily uses speech recognition for voice input and text-to-speech technology for audio responses, creating an interactive and hands-free experience.

## Features
✅ Voice Command Recognition
Listens for the wake word “Emily” and processes user commands.

✅ Real-Time Weather Report
Provides current weather updates for Faisalabad using Open Meteo API.

✅ Nobel Prize Information
Retrieves and speaks out the details of recent Nobel Prize winners.

✅ News Headlines
Fetches and reads the latest top headlines using the News API.

✅ Website Navigation
Opens popular websites like Google, Facebook, and WhatsApp Web on voice command.

✅ Text-to-Speech Conversion
Responds to user commands with clear audio using gTTS and pygame.

## Workflow
### Initialization
Emily starts by announcing its readiness.

### Wake Word Detection

Continuously listens for the word “Emily”.

### Command Recognition

Once activated, it listens for a command such as:

**"Open Google"**

**"Weather of Faisalabad"**

**"Nobel Prize winners"**

**"News"**

## Task Execution

Executes the requested task:

**🔥Fetch data (e.g., weather, news, Nobel Prize).**

**🔥Open a website.**

**🔥Respond using voice output.**

**🔥Repeat Listening**

**🔥Returns to listening mode for the wake word.**

## Technologies & Libraries Used
✅ Python 3.x – Core programming language.

✅ SpeechRecognition – For converting speech to text.

✅ gTTS (Google Text-to-Speech) – Converts text responses into audio.

✅ pygame – Plays the generated audio.

✅ requests – Handles API calls for weather, news, and Nobel Prize data.

✅ webbrowser – Opens websites in the default browser.

✅ time & datetime – Manages time-based tasks.

✅ os – Handles temporary audio file operations.

## APIs Integrated
**🏅Open Meteo API – Provides real-time weather updates.**

**🏅Nobel Prize API – Fetches Nobel Prize winners' information.**

**🏅News API – Retrieves the latest top headlines.**

## How Emily Works
*Step 1: Emily listens for the wake word "Emily" using the microphone.* 

*Step 2: When detected, it acknowledges and listens for a command.*

*Step 3: Based on the command, it performs one of the predefined tasks:*

Opens websites.

Fetches data from APIs and speaks the response.

*Step 4: Returns to listening mode for the next activation.*

## Key Highlights
 💻 Completely Voice-Based – Hands-free experience.

💻 API-Driven – Real-time information retrieval.

💻 Modular Design – Easy to extend with more commands and features.
