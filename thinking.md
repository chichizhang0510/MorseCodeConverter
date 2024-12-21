## Morse Code

### 理解规则

Morse Code is a coding system that uses dots (.) and dashes (-) to represent letters, numbers, and symbols.

- Dots (`.`) and dashes (`-`) are the basic elements of Morse Code.
- Each character (letter or number) consists of a group of dots and dashes, ranging in length from 1 to 5 units.
- Different characters are separated by spaces, and different words are separated by longer spaces.
- The length of a dot in Morse Code is one time unit.
- The length of a dash is three time units.
- The interval between symbols within the same character is one time unit.
- The interval between different characters is three time units.
- The interval between different words is seven time units.

#### Common Morse code tables

```
A: .-       B: -...    C: -.-.    D: -..
E: .        F: ..-.    G: --.     H: ....
I: ..       J: .---    K: -.-     L: .-..
M: --       N: -.      O: ---     P: .--.
Q: --.-     R: .-.     S: ...     T: -
U: ..-      V: ...-    W: .--     X: -..-
Y: -.--     Z: --..


0: -----    1: .----    2: ..---    3: ...--
4: ....-    5: .....    6: -....    7: --...
8: ---..    9: ----.


. (点): .-.-.-   , (逗号): --..--   ? (问号): ..--..
' (单引号): .----.   ! (感叹号): -.-.--   / (斜线): -..-.
( ) (括号): -.--.-   & (和): .-...   : (冒号): ---...
; (分号): -.-.-.   = (等号): -...-   + (加号): .-.-.
- (减号): -....-   _ (下划线): ..--.-   " (双引号): .-..-.
$ (美元符): ...-..-   @ (at符号): .--.-.
```



## coding structure building

OOP

Machine:

- message
- rule file

- GetInput
- Encrypt: Converts letters, numbers or symbols in ordinary text into Morse code. Each character in Morse code is separated by a single space. Words are separated by three spaces.
- Decrypt: Converts Morse code back to ordinary characters based on the space interval. The space between single characters is one unit, and the space between words is three units.
- Single Character Encrypt
- Single Character Decrypt
- BreakMessage
- Restart

