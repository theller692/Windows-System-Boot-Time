from tkinter import * #for window gui
import win32api #for boot tick count
import datetime #to compare time since boot in simple format

#main loop start
master = Tk()




#master window title/resize restrictions
master.wm_title("System Boot Time")
master.resizable(width=FALSE,height=FALSE)
master.option_add("*Font", "Futura")


#Main time getting functions
tickCount = win32api.GetTickCount()
currentTime = datetime.datetime.now()
convertMilliseconds = datetime.timedelta(milliseconds=tickCount)
compareTimes = currentTime-convertMilliseconds

#Master frame (packed at end, to reference what is contained within)
masterFrame = (LabelFrame(master))


#System was booted at 1:1:1 on 5/5/15
bootTime = StringVar()
bootTime.set("System was booted at: {}:{}:{} on {}/{}/{}".format(compareTimes.hour,compareTimes.minute,compareTimes.second,compareTimes.month, compareTimes.day, compareTimes.year))
bootTimeLabel = Label(masterFrame, textvariable=bootTime)
bootTimeLabel.pack(fill=X,padx=5, pady=5)


#string of numbers for milliseconds since boot
bootMilli = StringVar()
bootMilli.set(win32api.GetTickCount())
bootMilliLabel = Label(masterFrame, textvar=bootMilli, padx=5, pady=5)
bootMilliLabel.pack()


timeSinceBoot = StringVar()
timeSinceBoot.set("If this didn't get changed, something went wrong.")

# Loop to update the clock every 50 milliseconds
# 50ms was used instead of 1 to reduce system strain, and should be barely noticeable, if at all
def showLoop():
    if win32api.GetTickCount() > 1:
        global listSize
        global timesList
        bootMilli.set("Total milliseconds running: \n" + str(win32api.GetTickCount()))

        bootTime = datetime.timedelta(milliseconds=win32api.GetTickCount())
        seconds = bootTime.total_seconds()
        timesList = [
                    str(" "),
                    str("Days: "+ str(int(seconds //86400))).center(76),
                    str("Hours: " + str(int(seconds //3600) %24 )).center(76),
                    str("Minutes: " + str(int(seconds //60) %60 )).center(72),
                    str("Seconds: " + str(int(seconds % 60))).center(68),
                    str("Milliseconds: " + str(bootTime.microseconds)[:len(str(bootTime.microseconds))-3:]).center(62),
                    " "
                     ]
        timeSinceBoot.set(timesList)
        listSize = len(timesList)
        #sets loop within tkinter
        master.after(50, showLoop)
showLoop()

timeSinceBootList = Listbox(
masterFrame, listvariable=timeSinceBoot, selectmode=EXTENDED, height=len(timesList),
activestyle="dotbox", background="gray94", selectbackground="gray60", selectforeground="gray99"
)
timeSinceBootList.bind("<space>", timeSinceBootList.selection_clear(1))
timeSinceBootList.pack(fill=X,padx=5, pady=5)


#big close button, just because.
def stopButton():
    exit()
stop = Button(masterFrame, text="Stop", command=stopButton)
stop.pack(ipady=5, padx=10, pady=10)
stop.config(height=3, width=30, bd=3, relief=RAISED, overrelief=SUNKEN)


#end of master frame, at bottom of widgets to show what was contained inside.
masterFrame.pack(fill=BOTH, expand=1, padx=10, pady=10)
masterFrame.config(bd=4)

#end of tkinter window loop
mainloop()
