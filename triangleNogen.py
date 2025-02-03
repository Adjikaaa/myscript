import argparse, subprocess, sys
import secrets as rnd
'''
def printsample(F):
    n = 6
    original_stdout = sys.stdout   
    sys.stdout = open('sample.cnf', 'w')
    print("p cnf", max(n, 120), len(F))
    for cl in F:
        st = ""
        for lit in cl:
            st += str(lit) + " "
        st += "0"
        print(st)
    for var in range(n+1,121):
        print(var, " 0")

    sys.stdout = open('keys.log', 'w')
    print(100000)

    sys.stdout = original_stdout
'''
def printcnf(F, n):
    n = 3*n // 2 + 2
    original_stdout = sys.stdout   
    sys.stdout = open('tst.cnf', 'w')
    print("p cnf", max(n, 120), len(F))
    for cl in F:
        st = ""
        for lit in cl:
            st += str(lit) + " "
        st += "0"
        print(st)
    for var in range(n+1,121):
        print(var, " 0")

    sys.stdout = open('keys.log', 'w')
    print(100000)

    sys.stdout = original_stdout

def xor(var):
    F = []
    lit = []
    for v in var:
        s = 1 - 2*rnd.randbelow(2)
        lit.append(s*v)
    
    F.append([lit[0],lit[1],lit[2]])
    F.append([-lit[0],-lit[1],lit[2]])
    F.append([lit[0],-lit[1],-lit[2]])
    F.append([-lit[0],lit[1],-lit[2]])
    return F

def onein3(var):
    F = []
    lit = []
    clp = []
    cln = []
    for v in var:
        s = 1 - 2*rnd.randbelow(2)
        lit.append(s*v)
    
    for v in lit:
        clp.append(v)
    for i in range(len(lit)):
        for j in range(i+1, len(lit)):
            cln = [-lit[i]]    
            cln.append(-lit[j])
            F.append(cln)
    F.append(clp)
    return F

def nae(var):
    F = []
    clp = []
    cln = []
    for v in var:
        s = 1 - 2*rnd.randbelow(2)
        clp.append(s*v)
        cln.append(-s*v)
    F.append(clp)
    F.append(cln)
    
    return F

def majorrity(var):
    F = []
    lit = []
    for v in var:
        s = 1 - 2*rnd.randbelow(2)
        lit.append(s*v)

    F.append([lit[0], lit[1], lit[2]])
    F.append([lit[0], lit[1], -lit[2]])
    F.append([-lit[0], lit[1], lit[2]])
    F.append([lit[0], -lit[1], lit[2]])
    return F

def sample():
    F = []
    var = [1,2,4]
    G = xor(var)
    for cl in G:
        F.append(cl)
    var = [2,3,5]
    G = majorrity(var)
    for cl in G:
        F.append(cl)
    var = [1,3,6]
    G = xor(var)
    for cl in G:
        F.append(cl)
    return F

#N = 4
F = sample()
printsample(F)
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Extraction of one file')
    parser.add_argument('n', type = int, help = 'Input "n"')
   
    args = parser.parse_args()
'''