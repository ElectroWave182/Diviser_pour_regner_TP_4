def pe (T, A, B, C):
    n = len (T)
    assert 0 <= A <= B <= C < n, "0"
    assert T[A : B] == sorted (T[A : B])
    assert T[B + 1 : C] == sorted T[B + 1 : C]

def ps (T, tab, A, B, C):
    assert sorted (T) == sorted (tab)
    assert tab[A : C] == sorted (tab[A : C])

def fusion (tab, A, B, C)