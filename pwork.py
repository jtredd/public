import numpy as np 


def to_arr(n: int, shape=None) -> list:
    needed = n.bit_length()
    s = str(n)
    l = len(s)
    L = []
    start, i = 0, 0
    while True:
        L.insert(i, int(s[start+i]))
        i = i + 1
        if i == l:
            if shape is None:
                return L
            shape = needed
            return (L, needed)


def pad(self: list) -> list():
    pad = to_pad(self)
    end = len(self)
    start, i = 0, 0
    L = []
    while True:
        p = pad-len(str(self[start+i]))
        L.insert(i, p * str(0) + str(self[start+i]))
        i = i + 1
        if i == end:
            return L


def to_pad(self: list) -> int:
    return len(str(sorted(self)[-1]))

def _chunk_bs(bs, step=2):
    """chunk by step count"""
    stop = len(bs)
    start = 0
    bs_to_list = []
    for bstep in range(0, stop, step):
        bs_to_list.insert(bstep, bs[start:bstep+step])
        start = start + step
    return bs_to_list

def _from_list(self: list):
    """bytelist to ints"""
    return [int(str(b, 'utf8'), 16) for b in self if b.decode('utf8', errors='ignore').isalpha]

def _bit_length(self: int):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)

def to_bytes(self: list):
    """intlist to bytes"""
    """ why are we using big endian? """
    print('warning, big endian')
    return [b.to_bytes(1, byteorder='big') for b in _from_list(self)]


def to_bin(self: str):
    for b in _from_list(_chunk_bs(self)):
        return bin(b)

def magic1(n: int):
    l = (2047, 121, 781, 17, 5)
    new = []
    start, step = 0, 0
    sieve = np.ones(int(n//3) + (n%6 == 2), dtype=np.bool_)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-1*k-2*k*(i&1))//3::2*k] = False

    uh_oh = np.r_[1, 1, 3, ((3*np.nonzero(sieve)[0]+1)|1)][2:]
    pp = [int(x) for x in pad(uh_oh)]
    while step < len(pp):
        if pp[start+step] % 5 == 0:
            pp.pop(start+step)
        if step < len(pp):
            new.insert(pp[start+step], pp[start+step])
            step = step + 1
    return pp

def primes(L: list) -> list:
    start, step = 0, 0 
    while step < len(L):
        if L[start+step] % 121 == 0:
            print(L[start+step])
            L.pop(start+step)
        if step < len(L):
            step = step + 1
    start, step = 0, 0
    while step < len(L):
        if L[start+step] % 781 == 0:
            print(L[start+step])
            L.pop(start+step)
        if step < len(L):
            step = step + 1
    start, step = 0, 0
    while step < len(L):
        if L[start+step] % 2047 == 0:
            print(L[start+step])
            L.pop(start+step)
        if step < len(L):
            step = step + 1
    start, step = 0, 0
    return L

def test_prime(L: list) -> list:
    """ attempt to iterate list and perform action per iteration """
    pp = L.copy()
    good = []
    for i in L:
        if i in pp:
            if i % 5 == 0:
                pp.pop(pp.index(i))
                #pp.remove(i)
            good.insert(i, i)
        if i % 121 == 0:
            if i % 5:
                pass
            pp.pop(pp.index(i))
        good.insert(i, i)
#   for i in L:
#       if i in pp:
#           if i % 121 == 0:
#               pp.pop(pp.index(i))
#           good.insert(i, i)
#   for i in L:
#       if i in pp:
#           if i % 781 == 0:
#               pp.pop(pp.index(i))
#           good.insert(i, i)
#   for i in L:
#       if i in pp:
#           if i % 2047 == 0:
#               pp.pop(pp.index(i))
#           good.insert(i, i)
    return pp



def subset(list, size):
    if size == 0 or not list:             # order matters here
        return [list[:0]]
    else:
        result = []

    for i in range(len(list)):
        pick = list[i:i+1:]                 # sequence slice
        rest = list[:i] + list[i+1:]        # keep [:i] part
    for x in subset(rest, size-1):
        result.append(pick + x)
    return result

def get_stride(stop, ndim=5):
    if stop % 2 == 0:
        stop = stop - 1
    for i in range(1, stop):
        if stop % i == 0:
            if stop /i <= stop:
                if stop / i == ndim*2:
                    print(i)
                if stop / i == ndim:
                    return i



def main(n: int) -> bool():
    start, i =  0, 0
    if not isinstance(n, int):
        return -1
    
    primes = magic1(n)
    return primes


if __name__ == '__main__':
    import numpy as np
    import sys
    n = int(sys.argv[1]) + 1
    primes = main(n)
    if n - 1 in primes:
        print('True')
