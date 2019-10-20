#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-17
# source: https://stackoverflow.com/questions/58415096/python-if-else-condition-on-printing-lines/
#=================================================================================
import operator
from functools import reduce

l =  ['TEC,FW,AS.example.111,311496,20180509042152033,20180509042152033,0,480,j8vg3046nhcs2p47ehci3ng6gpgal9hah9dqi1h9hhfaj100,3507b59a19602f0c96792e180d2469d1@10.105.86.9,Cisco-CUCM10.5,sip:+PLT8777447585984834,sip:+440093779379739,sip:+42086081330@example.com,sip:+8777447585984834@10.105.86.51:5060,sip:+441344903000@10.110.70.132:5060,sip:+441499737979@example.com,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,CUST,M79_PL01,mobile,447585984834000,+447585984834,onnet,1001501,1001501', 'TEC,FW,AS.example.111,311497,20180509042152355,20180509042152355,0,480,afc81a7e0aefe660dabb2963acf280,7ee0dd6bb34472945b18c959049f514f@10.105.86.9,NotPresent,sip:+PLT8777447585984834,sip:+440093779379739,sip:+442086081330@example.com,sip:+8777447585984834@example.com:5060,sip:+441344903000@10.105.86.13:5060,sip:+441499737979@example.com,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,CUST,M79_PL01,mobile,447585984834000,+447585984834,onnet,1001501,1001501', 'TEC,FW,AS.example.111,311498,20180509042152828,20180509042152828,0,480,afc81a7e0aefe660dabb2963acf280,5f29e2b4ef5a19c6a489aa53f01c000c@10.105.86.9,NotPresent,sip:+PLT8777447585984834,sip:+440093779379739,sip:+442086081330@example.com,sip:+8777447585984834@example.com:5060,sip:+441344903000@10.105.86.13:5060,sip:+441499737979@example.com,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,CUST,M79_PL01,mobile,447585984834000,+447585984834,onnet,1001501,1001501', 'TEC,IT,AS.example.111,311499,20180509042153373,20180509042202478,9105,normal,afc81a7e0aefe660dabb2963acf280,bc4213fa64c67cbdc8e80c5a437a7677@10.105.86.9,NotPresent,sip:+444441499737979,sip:+441499737979,sip:+442086081330@172.16.90.1,sip:+444441499737979@example.com:5060,sip:+441344903000@10.105.86.17:5080,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,1001501', 'TEC,IT,AS.example.111,311500,20180509042358780,20180509042414784,16004,normal,8deba7200aefe860dabb2b5049eb70,279e60f3eb07aa44c55b8a4b804667bf@10.105.86.9,NotPresent,sip:+744441498738722,sip:+441498738722,sip:+442086081330@172.16.90.1,sip:+444441498738722@example.com:5060,sip:+441344903000@10.105.86.17:5080,CUSTOMER02,GROUP01 - CLUSTER1,pstn,+441498738722,sip:+441498738722@example.com,1000201']
FILTER = ['sip:+420', 'sip:+34', 'sip:+44149']
result = []

for row in l:
    r = row.split(',')
    if r[1] == 'IT':
        if (r[12][:8] in FILTER) or (r[12][:7] in FILTER) or (r[12][:10] in FILTER):
            result.append(row)

    if r[1] == 'FW':
        if (r[13][:8] in FILTER) or (r[13][:7] in FILTER) or (r[13][:10] in FILTER):
            result.append(row)

for row in result:
    print(row)
    print() # jump  line between the output result

# Output
# TEC,FW,AS.example.111,311496,20180509042152033,20180509042152033,0,480,j8vg3046nhcs2p47ehci3ng6gpgal9hah9dqi1h9hhfaj100,3507b59a19602f0c96792e180d2469d1@10.105.86.9,Cisco-CUCM10.5,sip:+PLT8777447585984834,sip:+440093779379739,sip:+42086081330@example.com,sip:+8777447585984834@10.105.86.51:5060,sip:+441344903000@10.110.70.132:5060,sip:+441499737979@example.com,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,CUST,M79_PL01,mobile,447585984834000,+447585984834,onnet,1001501,1001501
# TEC,IT,AS.example.111,311499,20180509042153373,20180509042202478,9105,normal,afc81a7e0aefe660dabb2963acf280,bc4213fa64c67cbdc8e80c5a437a7677@10.105.86.9,NotPresent,sip:+444441499737979,sip:+441499737979,sip:+442086081330@172.16.90.1,sip:+444441499737979@example.com:5060,sip:+441344903000@10.105.86.17:5080,CUST,M79_PL01,pstn,+441499737979,sip:+441499737979@example.com,1001501
# TEC,IT,AS.example.111,311500,20180509042358780,2018050904241478


"""
**Explanations**
#r[12][:8] in FILTER or r[12][:7] in FILTER or r[12][:10]


When the 2nd column is `IT`, you are interested by the 13th column. So `r[12]` gives something like: `sip:+441498738722`.
When the 2nd column is `FW`, you are interested by the 14th column. So, `r[13]` gives something like: `sip:+442086081330@example.com`.

Your filter is: `FILTER = ['sip:+420', 'sip:+34', 'sip:+44149']`. It contains 3 items. The length of the 1st item is **8**.
The length of the 2nd item is **7** and the length of the last item is **10**.

So to know if the `r[12]` (`sip:+441498738722`) or `r[13]` (`sip:+442086081330@example.com`) elements are in the `FILTER`,
you have to take the first 8, 7 and 10 characters and test **if one of them (at least)** is in the `FILTER`.

    if (r[12][:8] in FILTER) or (r[12][:7] in FILTER) or (r[12][:10] in FILTER):
        # code

**For example:** `r[12]` is `sip:+441498738722`. So the first 8 characters are `r[12][:8]` which is `sip:+441`. The first 7
characters are `r[12][:7]` which is `sip:+44`. The first 10 characters are `r[12][:10]` which is `sip:+44149`. Now, you can
see that for this `r[12]` (`sip:+441498738722`), only `r[12][:10]` (`sip:+44149`) is in the `FILTER` variable. So, you can
add this `row` to the `result` list.

It is the same logic, when the 2nd column of the `row` is `FW`.

"""
