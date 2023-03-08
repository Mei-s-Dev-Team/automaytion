import os
import openai
code_type = "ahk"

#['run', 'chrome.exe ', '']
#{'run': {exeFile, input, flags}}
#avail_options[run] = {exeFile, input, flags}
avail_options = dict()
avail_options['run'] = {'exefile':'', 'input':'', 'flags':''}
def main():
    if code_type == "ahk":
        print(f"code_type: ahk")
        f = open("exec.ahk", "w")
        
        #run, chrome.exe %link% " --new-window "

        f.write('run, ')
        f.write('chrome.exe ')
        f.write('google.com ')
        f.write('" --new-window "')
        #os.system('cmd /k AutoHotKey.exe')
        f. close()
        

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content":\
                  "Tell the world about\
                   the ChatGPT API in the style of a pirate."}]
        )

        print(completion)

if __name__ == '__main__':
    main()