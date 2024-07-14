# WKCTF 2024_NewW战队WP

## so_easy

```python
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
```

### 思路

- `>= 0`时，之作`*2`操作，`*2`就是**左移一位**，那么最低位就是`0`，逆向操作就是**右移一位**；

- 左移一位后最低位是`0`，与`5`异或后最低位变成`1`，所以最低位是`1`时，说明原操作数是个**负数**，负数的最高位是`1`，左移时被**舍弃**，逆向右移时需要还原回来，故逆向操作为**先异或，再右移一位，最后将`1`添至最高位**；

- 如此操作`5*51`次；

- 小端存储，故字符串逆序输出。

## signin

### 思路

- 先根据`twinhex`解码，在使用`base64`解码，得到二维码，根据信息发送`WKCTF2024`到**隐雾安全**微信公众号。

- `WKCTF{hello_2024}`