import subprocess
import sys

sys.stdout.write("Enter N:\n")
N = input()
sys.stdout.write("Enter k:\n")
k = input()
sys.stdout.write("Enter loop number:\n")
loops = int(input())
for _ in range(loops):
    complete = subprocess.run(["python3", "autogen.py", N], capture_output = False, text = True)
    if complete.returncode == 111:
        sys.stdout.write("Smth wrong!\n")
    elif complete.returncode == 0:
        satsearch = subprocess.run(["./zchaff1000", "tst.cnf"])
        if satsearch.returncode == 111:
            sys.stdout.write("Smth wrong!\n")
        elif satsearch.returncode == 0:
            sys.stdout.write("\n")
            parsing = subprocess.run(["python3", "parser.py", N, k], capture_output = False, text = True)
            if parsing.returncode == 111:      
                sys.stdout.write(f"Smth wrong!\n")
        else:
            sys.stdout.write(f"Process returned errcode: {complete.returncode}")
    else:
        sys.stdout.write(f"Process returned errcode: {complete.returncode}")
#finalfile = subprocess.run(["python3", "finalfile.py", N], capture_output = False, text = True)




