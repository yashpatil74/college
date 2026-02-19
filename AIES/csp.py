import itertools

def solve():
    
    for perm in itertools.permutations(range(10), 8):
        
        S, E, N, D, M, O, R, Y = perm

        if S == 0 or M == 0:
            continue

        send = 1000*S + 100*E + 10*N + D
        more = 1000*M + 100*O + 10*R + E
        money = 10000*M + 1000*O + 100*N + 10*E + Y

        if send + more == money:
            print(f"  {S}{E}{N}{D}")
            print(f"+ {M}{O}{R}{E}")
            print(f"------")
            print(f" {M}{O}{N}{E}{Y}")
            return

solve()