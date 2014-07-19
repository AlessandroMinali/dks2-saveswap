#Created by Alessandro Minali 2014
#contact at: alessandro.minali@gmail.com
#Visit me at: alessandrom.me
import msvcrt
import shutil
import os
import datetime

class SaveSwap():
    def __init__(self):
        self.FNAME = "DARKSII0000.sl2"
        self.config()
        self.PATH = "C:\Users\\" + self.USERNAME + "\AppData\Roaming\DarkSoulsII\\0110000102050552\\"
        self.SPATH = "C:\Users\\" + self.USERNAME + "\AppData\Roaming\DarkSoulsII\\0110000102050552\save\\"

    def run(self):
        d = os.path.dirname(self.SPATH)
        if not os.path.exists(d):
            print "Intializing save directory @ " + self.SPATH
            os.mkdir(d)
            print "--------------------------------------"
            self.make_save("original")
            print "Made original copy. DO NOT DELETE THIS"
            print "--------------------------------------"
        print "Directory found, making master save record for this session ..."
        self.make_save("master")
        print "--------------------------------------"
        while True:
            x = msvcrt.getwch()
            fn = ord(x)
            if not(fn):
                y = msvcrt.getwch()
                if y == ";":
                    self.make_save("f1")
                elif y == "<":
                    self.make_save("f2")
                elif y == "=":
                    self.make_save("f3")
                elif y == ">":
                    self.make_save("f4")
                elif y == "?":
                    self.load_save("f1")
                elif y == "@":
                    self.load_save("f2")
                elif y == "A":
                    self.load_save("f3")
                elif y == "B":
                    self.load_save("f4")
                elif y == "C":
                    self.make_save("quick")
                elif y == "D":
                    self.load_save("quick")                        

    def make_save(self, name):
        time = str(datetime.datetime.now()).split()[1].split(".")[0]
        shutil.copyfile(self.PATH + self.FNAME, self.SPATH + name)
        print time + " - completed SAVE of " + name.upper() + " save"

    def load_save(self, name):
        time = str(datetime.datetime.now()).split()[1].split(".")[0]
        shutil.copyfile(self.SPATH + name, self.PATH + self.FNAME)
        print time + " - completed LOAD of " + name.upper() + " save"   

    def config(self):
        f = open("config.txt","r")
        data = f.read()
        self.USERNAME = data.split("[")[-1].split("]")[0]
        
    def debug():
        pass

##no guarantee this'll work
try:  
    s = SaveSwap()
    s.run()
except:
    print "Something went horribly wrong. Try relaunching and send me an email about the problem"
    print "alessandro.minali@gmail.com"
    input()
