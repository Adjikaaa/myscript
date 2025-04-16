import subprocess
import sys, os, shutil, pathlib

sys.stdout.write("Enter N:\n")
N = input()
sys.stdout.write("Enter loop number:\n")
loops = int(input())
homedir = os.getcwd()
dirname = pathlib.Path(N)
dirname.mkdir(parents=True, exist_ok=True)
shutil.copy('zchaff1000', dirname)
for l in range(loops):
    loop = str(l)
    complete = subprocess.run(["python3", "autogen.py", N, loop], capture_output = False, text = True)
    if complete.returncode == 0:
        os.chdir(dirname)
        satsearch = subprocess.run(["./zchaff1000", f"{N + '_' + loop + '.cnf'}"])
        if satsearch.returncode == 0:
            sys.stdout.write("\n")
            if os.path.isfile('keys.log'):
#                print("Файл существует")
                os.chdir(homedir)
                parsing = subprocess.run(["python3", "parser.py", N, loop], capture_output = False, text = True)
            else:
#                print("Файл не существует, cnf-файл удалён")
                os.remove(f'{N + "_" + loop}.cnf') 
                os.chdir(homedir)
        else:
            sys.stdout.write(f"Process returned errcode: {complete.returncode}")
    else:
        sys.stdout.write(f"Process returned errcode: {complete.returncode}")
os.remove(f"{dirname}/zchaff1000")

finalfile = subprocess.run(["python3", "finalfile.py", N], capture_output = False, text = True)




