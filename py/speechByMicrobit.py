from microbit import sleep
import speech

text = "Hello, how are you today? This is a pen."

# Speech synthesis
speech.say(text)

# Sleep to allow the speech to finish
sleep(5000)
