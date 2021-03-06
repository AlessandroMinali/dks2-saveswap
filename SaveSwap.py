#Created by Alessandro Minali 2014
import msvcrt
import shutil
import os
import datetime

class SaveSwap():
    def __init__(self):
        self.FNAME = "DARKSII0000.sl2"
        self.config()
        [x[0] for x in os.walk("C:\Users\\" + self.USERNAME + "\AppData\Roaming\DarkSoulsII")]
        folder = x[0].split("\\")[-1]
        self.PATH = "C:\Users\\" + self.USERNAME + "\AppData\Roaming\DarkSoulsII\\" + folder + "\\"

    def run(self):
        d = os.path.dirname(self.PATH)
        if not(int(self.setup)):
            print "Intializing save directory"
            print "--------------------------------------"
            self.make_save("original")
            print "Made original copy. DO NOT DELETE THIS"
            print "--------------------------------------"
            f = open("config.txt", "w")
            f.write(self.data[:-1] + str(1))
            f.close()
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
        shutil.copyfile(self.PATH + self.FNAME, self.PATH + name)
        print time + " - completed SAVE of " + name.upper() + " save"

    def load_save(self, name):
        time = str(datetime.datetime.now()).split()[1].split(".")[0]
        shutil.copyfile(self.PATH + name, self.PATH + self.FNAME)
        print time + " - completed LOAD of " + name.upper() + " save"   

    def config(self):
        f = open("config.txt","r")
        data = f.read()
        self.data = data
        self.USERNAME = data.split("[")[-1].split("]")[0]
        self.setup = data.split()[-1]
        f.close()

    def delsaves(self):
        for i in os.listdir(self.PATH):
            if i in ['f1','f2','f3','f4','quick','master']:
                os.remove(self.PATH + i)
                print "Removed save " + i + "..."
            
    def debug():
        pass
    
if __name__ == "__main__":
    ##no guarantee this'll work
    try:
        s = SaveSwap()
        s.run()
    except:
        print "Something went horribly wrong. Try relaunching"
        input()
