#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# i=1:a=1:sum=1
# i=2:a=2:sum=3
# i=3:a=4:sum=7
# i=4:a=8:sum=15
# i=5:a=16:sum=31
# i=6:a=32:sum=63
sum=1
a=1
for i in range(1,31):
    a = a * 2
    sum=sum+a

    print('a=',a,'i=',i)
    print('sum=',sum)
print(sum/100)






