import time
import os 
import threading

# def file():
os.chdir("D:\\Source")
with open ("File1.txt","r") as fr:
    lines=fr.readlines()
    os.chdir("D:\\dest")
    with open ("File2.txt","w") as fw:
        for l in lines:
            fw.write(f"{time.strftime("%H:%M:%S")},{l}")
        fw.close()
    fr.close()
                

# t1=threading.Thread(target=file)
# t1.start()
# t1.join()

print((f"{time.strftime("%H:%M:%S")},{lines}"))