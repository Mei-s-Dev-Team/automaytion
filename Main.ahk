; Global variables for waitUntil(hh, mm, ss, interval)
global hh
global mm
global ss
global interval
global link

; Window Content
gui, add, edit, r1 vhh w150, Hour
gui, add, edit, r1 vmm w150, Minute
gui, add, edit, r1 vss w150, Seconds
gui, add, edit, r1 vinterval w150, Refresh Interval (seconds)
gui, add, edit, r1 vlink w150, Link
gui, add, button, default w150 grecord, submit

; Window Display Properties
scaledWidth := A_ScreenWidth*.9
scaledHeight := A_ScreenHeight*.9
gui show, w%scaledWidth% h%scaledHeight%, autoMAYtion
SetMouseDelay, 10

return

ButtonSubmit:
gui, submit

record() {
    msgbox %link%
    run, chrome.exe %link% " --new-window "
} ; record

stopRec() {
    send, {F9} ; Stop Record Hotkey
    Exit
} ; StopRec

waitUntil(hh, mm, ss, interval) {
    loop {
        if (A_hour == hh && A_Min == mm && A_Sec == ss){
            return
        } ; If
        sleep 1000*interval
    } ; Loop
} ; waitUntil