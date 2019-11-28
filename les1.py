# ! /usr/bin/env python
# -*- coding: utf-8 -*-


# git add название.ру
# git commit -m "название.ру"
# git push




# i = 13
# while i<=350:
# 	print(i)
# 	i+=7

# guess=input()
# password='qwerty'
# count=0
# while guess!=password:
# 	count+=1
# 	print('Не правильный ввод пароля')
# 	guess=input()
# print('Вы потратили ',count,' попыток')


# a=[1,2,3]*5
# print(a)
# while 3 in a:
# 	a.remove(3)
# print(a)



# x=int(input())
# kol=0
# kol_ch=0
# s=0
# pr=1
# maxim=0
# minim=9
# while x>0:
# 	last=x%10
# 	kol=kol+1
# 	if last%2==0:
# 		kol_ch+=1
# 	s+=last
# 	pr*=last
# 	if last>maxim:
# 		maxim=last
# 	if last<minim:
# 		minim=last
# 	x=x//10
# print('Всего цифр:',kol)
# print('Всего четных цифр:',kol_ch)
# print('Сумма всех цифр:',s)
# print('Произведение всех цифр:',pr)
# print('Maximum:',maxim)
# print('Minimum:',minim)




# while True:
# 	a=input()
# 	if a=='exit':
# 		break
# 	print(a, len(a))