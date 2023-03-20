import os
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write



code_type = "ahk"

#['run', 'chrome.exe ', '']
#{'run': {exeFile, input, flags}}
#avail_options[run] = {exeFile, input, flags}
avail_options = dict()
avail_options['run'] = {'exefile':'', 'input':'', 'flags':''}
load_dotenv()

def voice_commands():
    r = sr.Recognizer()
    # Set the duration of the recording in seconds
    duration = 2
    
        # Set the sample rate of the recording
    sample_rate = 44100

    # Record the audio
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)

    # Wait for the recording to finish
    sd.wait()

    # Save the audio to a WAV file
    sf.write('recording.wav', audio, sample_rate)

    try:
        ret = ""
        input_file = sr.AudioFile('recording.wav')
        with input_file as source:
            input_audio = r.record(source)
            print("Google Speech Recognition thinks you said " + r.recognize_google(input_audio))
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        return ret


def main():

    if code_type == "ahk":
        print(f"code_type: ahk")
        f = open("exec.ps1", "w")
        
        prompt = input('Waiting for prompt: ') + "Do not say anything other than the script itself"

        openai.api_key = os.getenv("OPENAI_KEY")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content":\
                  f"{prompt}"}]
        )

        # print(completion['choices'][0]['message']['content'])
        f.write(completion['choices'][0]['message']['content'])
        f.close()

if __name__ == '__main__':
    main()