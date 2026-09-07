# 16. Design a Logger System.
#     Create Logger classes supporting INFO, WARNING, and ERROR levels.
#     Implement different output methods such as ConsoleLogger and FileLogg

class Loggersystem:
    def log(self,message):
        pass

class ConsoleLogger(Loggersystem):
    def log(self,message):
        print("console",message)

class FileLogg(Loggersystem):
    def log(self,message):
        file=open("ss.txt","a")
        file.write(message)
        file.close()
        print("file is saved")

aa=ConsoleLogger()
ab=FileLogg()

aa.log("Info")
ab.log("Info")

aa.log("Warning")
ab.log("warning")

aa.log("error level")
ab.log("error level")






