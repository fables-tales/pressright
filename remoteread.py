import subprocess


def main():
    p = subprocess.Popen(["iremoted"], stdout=subprocess.PIPE ) 
    while True:
        data = p.stdout.readline().strip()
        if data == "0x18 depressed":
            right = subprocess.Popen(["./right"])
            right.wait()

        if data == "0x19 depressed":
            left = subprocess.Popen(["./left"])
            left.wait()

if __name__ == "__main__":
    main()
