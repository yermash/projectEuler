print((lambda n: (p := [1] + [0] * n, 
    [[p.__setitem__(j, p[j] + p[j - i]) 
      for j in range(i, n + 1)] 
      for i in range(1, n + 1)], p)
      [-1])(100)[100])
