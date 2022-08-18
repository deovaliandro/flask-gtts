from flask import Flask, flash, redirect, render_template, request, url_for
from gtts import gTTS
from pydub import AudioSegment

import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = str(request.form.get('name'))
    to = str(request.form.get('to'))

    teks = "Perhatian perhatian, kepada saudara " + name + " diharapkan segera menuju " + to + ", Sekali lagi, kepada saudara " + name + " diharapkan segera menuju " + to + ", Terima kasih."

    file = gTTS(teks, lang='id')
    file.save("hallo.mp3")
    
    sound1 = AudioSegment.from_mp3("bell.mp3")
    sound2 = AudioSegment.from_mp3("hallo.mp3")

    finalsound = sound1 + sound2
    finalsound.export("final.mp3", format="mp3")
    os.system("vlc final.mp3 ")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)