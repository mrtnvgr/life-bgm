import datetime, os, pyaudio, wave, sys, threading

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def wait():
    if os.name=="nt":
        os.system("pause")
    else:
        os.system('read -n1 -r -p "Press any key to continue..."')

args = sys.argv
wavfolder = "<default>" # default is current directory

title = " Life-BGM v0.0.2"

def info_thread():
    global minutes
    while True:
        if datetime.datetime.now().minute!=minutes:
            minutes = datetime.datetime.now().minute
            if len(str(minutes))==1:
                minutes *= 10
            clear()
            print()
            print(title + " (--help)")
            print("Time: " + str(hour) + ":" + str(minutes))
            print("File: " + wavfolder + "\\" + filename + ".wav")
            print()
 

thread = threading.Thread(target=info_thread)
while True:
    hour = datetime.datetime.now().hour
    if hour!="":
        filename = str(hour)
    if len(args)>1:
        for i in range(len(args)):
            if args[i]=="--mode" or args[i]=="-m":
                if args[i+1]!="":
                    filename = filename + "_" + args[i+1]
            if args[i]=="--directory" or args[i]=="-d":
                if args[i+1]!="":
                    wavfolder = args[i+1]
                    filename = wavfolder + "\\" + filename
            if args[i]=="--help" or args[i]=="-h":
                print(title)
                print("--help(-h) - help text")
                print("--mode(-m) - file mode (filename_mode)")
                print("--directory(-d) - file directory")
                sys.exit(0)
    p = pyaudio.PyAudio()
    try:
        wf = wave.open(filename + ".wav", 'rb')
    except FileNotFoundError:
        print("File " + filename + ".wav doesn't exist. Use 24-hour format named audio files.")
        wait()
        sys.exit(0)
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output=True)
    minutes = 0
    thread.start()
    while datetime.datetime.now().hour==hour:
        wf = wave.open(filename + ".wav", 'rb')
        stream.write(wf.readframes(wf.getnframes()))
stream.close()
