import argparse, subprocess, sys, pathlib, os

def parserr(N, loop):
    homedir = os.getcwd()
    dirname = pathlib.Path(N)
    os.chdir(dirname)
    k = (3*int(N)) // 2
    sys.stdout = open(N + '.txt', 'a')
    os.rename('keys.log', f'keys_{N + "_" + loop}.log')
    f = open(f'keys_{N + "_" + loop}.log', "r")
  
    res = []
    m = k
    for line in f:
        lst = (line.strip()).split("  ")
        lst = lst[0].split(" ")
        sub = []
        for l in lst:
            a = int(l)    
            if abs(a) in [m-1, m, m+1, m+2]:
                sub.append(a)
        if sub not in res:
            res.append(sub)
    res.pop(0)
  
    if len(res) > 1:
        sys.stdout.write(f'{len(res)} for {N}_{loop}.cnf\n')
        for i in range(len(res)):
            sys.stdout.write(f'{res[i]}\n')
    else:
        os.remove(f'{N + "_" + loop}.cnf') 
    f.close()
        
    os.remove(f'keys_{N + "_" + loop}.log') 
    os.chdir(homedir)
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Extraction of one file')
    parser.add_argument('N', type = str, help = 'Input "N"')
    parser.add_argument('loop', type = str, help = 'Input "l"')
    args = parser.parse_args()
    parserr(args.N, args.loop)
