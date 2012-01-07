import subprocess


def main():
    p = subprocess.Popen(["iremoted"], stdout=subprocess.PIPE ) 
    while True:
        data = p.stdout.readline().strip()
        if data == "0x18 depressed":
            right = subprocess.Popen(["./right"])
            right.wait()
if __name__ == "__main__":
    main()
