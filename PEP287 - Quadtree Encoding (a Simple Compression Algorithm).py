def black_or_white(x,y,N,powers):
    return (x - powers[N - 1])**2 + (y - powers[N - 1])**2 <= powers[2*N - 2]

def min_seq_len(x,y,d,N,powers):
    b = black_or_white(x,y,N,powers)
    if b == black_or_white(x + d,y + d,N,powers) and d != powers[N] - 1:
        if b == black_or_white(x + d,y,N,powers):
            if b == black_or_white(x,y + d,N,powers):
                return 2
    e = d // 2
    return 1 + min_seq_len(x,y,e,N,powers) + min_seq_len(x + e + 1,y + e + 1,e,N,powers) + min_seq_len(x,y + e + 1,e,N,powers) + min_seq_len(x + e + 1,y,e,N,powers)

powers = [1]
for i in range(60):
    powers.append(powers[-1]*2)

N = 24
print(min_seq_len(0,0,2**N - 1,N,powers))

#answer = 313135496
#זמן הרצה - חמש דקות