# Voice-Assistant
__Voice Assistant - Jarvis Sri__
**Overview**
This is a Python-based voice assistant named "Jarvis Sri" that can perform a variety of tasks based on voice commands. It uses libraries like pyttsx3 for text-to-speech, speech_recognition for voice input, wikipedia for fetching information, and webbrowser for opening websites. The assistant is designed to assist users with daily tasks such as checking the time and date, sending emails, playing music, retrieving weather information, and more.

**Features**
1.__Information Retrieval__
*Searches Wikipedia for information and reads out the summary.
*Retrieves weather information for a specified location.
2.__System Interaction__
*Opens commonly used websites like YouTube, Google, and Stack Overflow.
*Plays music from a predefined directory.
*Checks the current battery percentage.
3.__Communication__
*Sends emails via Gmail with subject and body specified by voice input.
*Greets the user based on the time of day.
4.__Customization__
*Users can add or modify commands for specific tasks as needed.


1__Clone the repository__:
git clone https://github.com/yourusername/voice-assistant-jarvis.git
cd voice-assistant-jarvis

2__Install the required dependencies__:
pip install pyttsx3 datetime speechrecognition wikipedia requests beautifulsoup4 pywikihow psutil smtplib

3.Set up your Gmail credentials for sending emails in the send_email function:

Replace your_email@gmail.com with your Gmail address.
Replace your_password with your Gmail password or app password.

**Libraries Used**
.pyttsx3: Text-to-speech conversion
.speech_recognition: Captures and processes voice input
.wikipedia: Fetches summaries from Wikipedia
.webbrowser: Opens URLs in the web browser
.BeautifulSoup: Parses HTML for web scraping
.psutil: Retrieves system information like battery status
.smtplib: Sends emails using SMTP
