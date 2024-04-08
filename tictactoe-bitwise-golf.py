*O,Q,B=0,0,0,["-"]*9
while"-"in B:
 while(I:=input(f"Key in the position to place(0-8).You are {'OX'[Q]}: "))not in map(str,(0,1,2,3,4,5,6,7,8)):print("invalid placement")
 Q^=1;B[I:=int(I)]="OX"[Q];O[Q]|=1<<I
 for j in 0,3,6:print(*B[j:j+3]);any(i==i&O[Q]for i in map(ord,"ǀ8ĤITđ"))and exit("OX"[Q]+" win")
exit("Tie")