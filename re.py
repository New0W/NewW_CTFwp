from Crypto.Util.number import long_to_bytes

a=[0x540a95f0c1ba81ae,0xf8844e52e24a0314,0x9fd988f98143ec9,0x3fc00f01b405ad5e]

for i in range(len(a)):
  for j in range(51):
    for x in range(5):
      if bin(a[i])[-1] == '1':
        m = (a[i] ^ 0x71234EA7D92996F5) >> 1
        n = int('1' + bin(m)[2:].zfill(63), 2)
        a[i] = n
      else:
        a[i] = a[i] >> 1

for i in a:
  print(long_to_bytes(i).decode()[::-1], end='')
#WKCTF{2366064af80f669c2cb9519ab}