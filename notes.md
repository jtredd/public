



```
>>> A = np.array([1, 256, 8755], dtype=np.int16)
 |      >>> list(map(hex, A))
 |      ['0x1', '0x100', '0x2233']
 |      >>> A.byteswap(inplace=True)
 |      array([  256,     1, 13090], dtype=int16)
 |      >>> list(map(hex, A))
 |      ['0x100', '0x1', '0x3322']
 ```


```
import numpy as np
import numpy.linalg as lin
B = np.array([[2],[4]])
b = np.array([[4],[4]])

B_linv = lin.solve(B.T.dot(B), B.T)
c = B_linv.dot(b)
print('c\n', c)



c = lin.solve(B.T.dot(B), B.T.dot(b))
print('c\n', c)
```

```
In [15]: B = np.array([[2],[4]])

In [16]: b = np.array([[4],[4]])

In [18]: x,resid,rank,s = np.linalg.lstsq(B,b)

In [19]: x
Out[19]: array([[ 1.2]])
```






