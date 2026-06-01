import numpy as np

# Classical Fast Fourier Transform algorithm (unitary)
def fft(f):
    f = np.asarray(f, dtype=complex)
    if len(f) == 1:
        return f

    splice_len = len(f)//2
    even_tf = fft(f[::2])
    odd_tf = fft(f[1::2])

    tf = np.zeros(len(f), dtype=complex)
    for k in range(splice_len):
        phase = np.exp(-2*k*np.pi*1j/len(f))

        tf[k] = 1/np.sqrt(2)*(even_tf[k] + phase*odd_tf[k])
        tf[k+splice_len] = 1/np.sqrt(2)*(even_tf[k] - phase*odd_tf[k])

    return tf

arr = [1/np.sqrt(2)*(1+1j), 1/np.sqrt(2)*(1-1j)]
print(np.fft.fft(arr, norm="ortho"))
print(fft(arr))