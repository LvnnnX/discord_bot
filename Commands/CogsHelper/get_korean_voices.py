from gtts import gTTS
from io import BytesIO
from pygame import mixer
from pathlib import Path

PATH = Path(__file__).parent.parent

text = '안녕하세요 소개합니다 제 이름은 Dito입니다'
language = 'ko'

# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save(f'{DDIR}/PerkenalanDito.mp3')


def speak(text:str,lang:str):
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.write_to_fp(mp3_fp)
    tts.save(f'{PATH}/audio.wav')
    return mp3_fp

def start(text:str):
    print(text)
    mixer.init()
    sound = speak(text,language)
    # sound.seek(0)
    # mixer.music.load(sound, "mp3")
    # return mixer.music.play()
    # time.sleep(5)