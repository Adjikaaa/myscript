import secrets as rnd
import argparse, subprocess, sys, os, pathlib

def printcnf(F, N, l):
    n = 3*int(N) // 2 + 2
    filename = N + '_' + l + '.cnf'
    dirname = pathlib.Path(N)

    ff = open(f'{dirname}/{filename}', 'w')
    ff.write(f"p cnf {max(n, 120)} {len(F)}\n")
    for cl in F:
        st = ""
        for lit in cl:
            st += str(lit) + " "
        st += "0"
        ff.write(f'{st}\n')
    for var in range(n+1,121):
        ff.write(f'{var} 0\n')
    ff.close()

def gen3reg(n):
    issimple = False
    while not issimple:
        E = []
        A = []
        B = []
        vert = []
        for i in range(3*n):
            vert.append(i+1)
        for i in range(3*n):
            B.append([])
            for j in range(3*n):
                B[i].append(0)
        while len(vert) > 0:
            jj = rnd.randbelow(len(vert) - 1) + 1
            i = vert[0]
            j = vert[jj]
            B[i - 1][j - 1] = 1
            B[j - 1][i - 1] = 1
            vert.remove(i)
            vert.remove(j)
        for i in range(3*n):
            for j in range(3*n):
                if B[i][j] == 1:
                    E.append(j)                
        for i in range(n):
            A.append([])
            for j in range(n):
                A[i].append(0)
        issimple = True
        for i in range(n):
            a = 3*i
            b = 3*i + 1
            c = 3*i + 2
            d = E[a] // 3
            e = E[b] // 3
            f = E[c] // 3
            if d == e or d == f or e == f or d == i or e == i or f == i:
                issimple = False
            A[i][d] = 1
            A[i][e] = 1
            A[i][f] = 1
            A[d][i] = 1
            A[e][i] = 1
            A[f][i] = 1
    return A            

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

def genice(A, N):
    F = []
    n = len(A)
#    l = 3
#    ll = 2
#    lll = 3
    N = int(N)
    l = N // 4
    ll = N // 4
    lll = N // 4
    cnt = 1
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] == 1:
                A[i][j] = cnt
                A[j][i] = cnt
                cnt += 1
    m = 3*n // 2
    firsta = False
    firstb = False
    for i in range(n):
        var = []
        for j in range(n):
            if A[i][j] != 0:
                if A[i][j] == m - 1 and firsta:
                    vari = m + 1
                elif A[i][j] == m and firstb:
                    vari = m + 2
                else:
                    vari = A[i][j]

                var.append(vari)
                if A[i][j] == m - 1:
                    firsta = True
                if A[i][j] == m:
                    firstb = True
        if l > 0:
            l -= 1
            G = majorrity(var)
        elif ll > 0:
            ll -= 1
            G = xor(var)
        elif lll > 0:
            lll -= 1
            G = nae(var)
        else:
            G = onein3(var)
        for cl in G:
            F.append(cl)

    k = 3
    for i in range(k): 
        fixa = rnd.randbelow(m - 2) + 1
        F.append([fixa])
    return F

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Extraction of one file')
    parser.add_argument('N', type = str, help = 'Input "N"')
    parser.add_argument('loop', type = str, help = 'Input "loops"')
    args = parser.parse_args()
    A = gen3reg(int(args.N))
    F = genice(A, args.N)
    printcnf(F,args.N, args.loop)


