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
    wf = wave.open(filename + ".wav", 'rb')
    clear()
    print(" Life-BGM v0.0.1")
    print(" ")
    print("Current time: " + str(hour))
    print("Current file: " + filename + ".wav")
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output=True)
    try:
        data = wf.readframes(1024)
        while data!='' and datetime.datetime.now().hour==hour:
            stream.write(data)
            data = wf.readframes(1024)
    except KeyboardInterrupt:
        break
