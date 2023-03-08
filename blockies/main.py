import os

code_type = "ahk"

def main():
    if code_type == "ahk":
        f = open("test.ahk", "w")
        f.wrtie('SetMouseDelay, 10; Global variables for waitUntil(hh, mm, ss,\
             interval)global hhglobal mmglobal ssglobal intervalglobal link; Window Contentgui, add, edit,\
                 r1 vhh w150, Hourgui, add, edit, r1 vmm w150, Minutegui, add, edit, r1 vss w150, Secondsgui,\
                     add, edit, r1 vinterval w150, Refresh Interval (seconds)gui, add, edit, r1 vlink w150,\
                         Linkgui, add, button, default w150, Submit; Window Display PropertiesscaledWidth\
                             := A_ScreenWidth*.5scaledHeight := A_ScreenHeight*.5gui show, xcenter ycenter\
                                 w%scaledWidth% h%scaledHeight%, autoMAYtionreturnButtonSubmit: gui, submit,\
                                     nohideaction()action() {    msgbox %link%run, chrome.exe %link% " --new-window "}\
                                         ; recordwaitUntil(hh, mm, ss, interval) {    loop {\
                                                    if (A_hour == hh && A_Min == mm && A_Sec == ss){return \
                                                               } ; If        sleep 1000*interval    } ; Loop} ; waitUntil')
        #os.system('cmd /k "Your Command Prompt Command"')
        f. close()