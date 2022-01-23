import datetime, os, pyaudio, wave, sys

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

args = sys.argv

while True:
    hour = datetime.datetime.now().hour
    if hour!="":
        filename = str(hour)
    if len(args)>1:
        if args[1]=="-m":
            if args[2]!="":
                filename = filename + "_" + args[2]
    p = pyaudio.PyAudio()
    wf = wave.open(filename + ".wav", 'rb')
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output=True)
    while datetime.datetime.now().hour==hour:
        clear()
        print(" Life-BGM v0.0.1-1")
        print(" ")
        minutes = datetime.datetime.now().minute
        if len(str(minutes))==1:
            minutes *= 10
        print("Current time: " + str(hour) + ":" + str(minutes))
        print("Current file: " + filename + ".wav")
        wf = wave.open(filename + ".wav", 'rb')
        stream.write(wf.readframes(wf.getnframes()))
stream.close()
