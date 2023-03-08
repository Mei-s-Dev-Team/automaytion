import os

code_type = "ahk"

def main():
    if code_type == "ahk":
        f = open("test.ahk", "w")
        
        os.system('cmd /k Spotify.exe')
        f. close()

if __name__ == '__main__':
    main()