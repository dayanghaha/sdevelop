import asyncio

"""def fib(n):
    a,b,num=0,1,0
    while True:
        if(num>n):
            return
        yield a
        a,b=b,a+b
        num+=1
f=fib(5)


def a(**kwargs):
    print(kwargs)
q=a(2,4)"""

#冒泡排序
"""def mp(l):
    len1=len(l)
    for i in range(len1-1):
        for j in range(i+1,len1):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l
list=[1,54,6,32,67,-3]
a=mp(list)
print(a)"""

#快排
"""def quick(list,start,end):
    if start<end:
        l,r=start,end
        mid=list[l]

        while l<r:
            while (l < r and list[r] > mid):
                r-=1
            list[l] = list[r]
            while(l<r and list[l]<=mid):
                l+=1
            list[r]=list[l]

        list[l]=mid
        quick(list,start,l-1)
        quick(list,r+1,end)
    return list


list1=[1,54,6,32,464,0,213,64,23]
print(quick(list1,0,8))"""



"""def aaa(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
nums = [1,32,5454,2,312,354,66,7,11,15]
target = 9
print(aaa(nums,target))"""

"""with open("C:/Users/user/Desktop/aaa.log") as f:
    a=f.read()
b=a.split("\n")
d={}
for i in b:
    c=i.split(" ")
    if c[2] not in d.keys():
        d[c[2]]=1
    else:
        d[c[2]]=d[c[2]]+1"""

"""a=(1,2,3)
b=hash(a)
print(b)
q=["1","4,5,6",1]
print(" ".join(q))
w={123:2,'q':'dsf'}
print(w[123])"""


"""[1,8,3,9,5,2]
num=10
[[1,9],[2,8]...]


'aaaabbcfaabbz'
'a4b2c1f1a2b2z1'
'a6b4'
for"""

"""a={'a':'dd','sed':'ssa'}
print(type(eval(a)))"""


"""#两链表是否相交
def aa(head1, head2):
  node = head1.next
  while node.next:
    node = node.next
  node.next = head2

  slow = head1
  fast = head1
  while slow.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

#链表中倒数k个数是什么
def bb(head, k):
  n = 0
  node = head
  while node:
    n += 1
    node = node.next

  node=head
  for _ in range(n - k):
    node = node.next
  return node"""

"""url='http://10.16.32.93:443/aiplatform_web/application/ability/1'
import requests
import json
a=requests.get(url)
b=json.dumps(a)
print(b)"""

"""#数组反转，不允许开辟新空间
a=[1,2,3]
for i in range(len(a)-1,-1,-1):
    a.append(a[i])
    a.pop(i)
print(a)"""


"""a=[1,2,3,4,5,6,7]
 
def aaa(l):
    b=[]
    i=0
    j=4
    while j<=len(a):
        if j>len(a):
            j=len(a)
        c=a[i:j]
        c.reverse()
        b=b+c
        i+=4
        j+=4
    c=a[j-4:len(a)]
    c.reverse()
    b=b+c
    return b
print(aaa(a))"""




a=["abca","abc","abca","abc","abcc","aa"]
a.sort(reverse=True)
print(a)

print('这在尝试git哈哈哈hhhhhhhhhhhhhhhhhfgfggdgdfgfgh')

