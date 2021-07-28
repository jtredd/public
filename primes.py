import numpy as np
from time import time
text = 'Theorem 3 ("Well Known"): Let n = (h*(q**k)+1) with q prime and qk > h.   If there is an integer a such that a**(n-1) ≡ 1 (mod n), and gcd(a**((n-1)/q-1),n) = 1, then n is prime.'

def primal(start: int, well_known: int, k: int, a: int) -> bool:
    """ attempt to generate well known primes. """ 
    Z = [x for x in primes_sieve2(well_known+1)]
    Z.append(start+1)
    if well_known in Z:
        if well_known**k > start:
            n = (start*(well_known**k)+1)
            print(n)
            if np.power(a, (n-1)) % n == 1:
                qq = a**((n-1)/well_known-1)
                print(f'{qq}, {n}, {well_known}')
                if np.gcd(int(qq), n) == 1: 
                    return True
                print(f'false: {qq}, {n}, {well_known}')
    return -1
def timeit(func, arg):
    now = time()
    func(arg)
    stop = time() - now
    return stop

def pad(self: list) -> list():
    """ needed this to convert 64bit ints to standard (longlong) """
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
    """ because you don't know """
    return len(str(sorted(self)[-1]))

def primes_sieve2(limit):
    """ The only one """
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def unique(iterable, key=lambda x: x):
    seen = set()
    for elem, ekey in ((e, key(e)) for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)

def magic1(n: int):
    """ No longer works. """
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

def primes_missed(L: list) -> list:
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

def chunk_bs(bs, step=2):
    """chunk by step count"""
    stop = len(bs)
    start = 0
    bs_to_list = []
    for bstep in range(0, stop, step):
        bs_to_list.insert(bstep, bs[start:bstep+step])
        start = start + step
    return bs_to_list

def from_list(self: list):
    """bytelist to ints"""
    return [int(str(b, 'utf8'), 16) for b in self if b.decode('utf8', errors='ignore').isalpha]

def _bit_length(self: int):
    """ why is this not standard library? """
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
