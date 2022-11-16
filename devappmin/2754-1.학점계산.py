c=input()
print('0.0'if c=='F'else ord('E')-ord(c[0])+{'+':0.3,'0':0.0,'-':-0.3}[c[1]])
