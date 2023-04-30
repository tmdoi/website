from gtts import gTTS
import os

text = "varav lufih zuduq zujob watid bahuk vagip xetug kilis xatib"
language = 'en'

speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")

os.system("mpg123 output.mp3")
