#histogram
his, bins = np.histogram(a, bins = np,arange(256), density=false)

hcc = np.cumsum(his).astype(float)
hcc = hcc / hcc.max() * 255
hcc = np-uintu(hcc)

b = np.zeros(a.shape, dtype=np.uint8)
b = hcc[a]