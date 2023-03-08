

#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn ; Enable warnings to assist with detecting common errors.
SendMode Input ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.

; This script opens the Google homepage and searches for the word "AutoHotkey"
#SingleInstance force

; Open Google Homepage
Run, www.google.com

; Wait for 2 seconds to let the website load
Sleep, 2000

; Type the word "AutoHotkey" into the search bar
Send, AutoHotkey

; Wait for 1 second
Sleep, 1000

; Press the Enter key to perform the search
Send, {Enter}

; Wait for 3 seconds to let the search results load
Sleep, 3000

; Scroll down the page to view more search results
Send, {PgDn 3}