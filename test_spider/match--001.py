import re
#print(re.match(r'\dcomm','2comming.3come').group())
#print(re.match('com','Comwww.runcomoob',re.).group())
#print(re.match(r'comm','commingCome').group())
#print(re.search(r'comm','commingCome').group())
#print(re.search('\dcom','www.4comrunoob.5com').group())
#print(re.search(r'comm','commingCome').start())
#print(re.search(r'commi','commingCome').span())
#print(re.search(r'comm','commingCome').end())
a = "123abDc456a"
#print(re.search("([0-9]*)",a).group(0))
#print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))
#print(re.match('([a-z]*)','abcD').group())  #匹配字母开头的
#print(re.search("([0-9]*)([a-zA-Z]*)([0-9]*)",a).group(0))
#p = re.compile(r'[a-z]')
#print(p.findall('1-2-3-0-6-a'))
#print(re.split('\d+','a1b3c3'))
#print(re.split('[a-zA-Z]',a)) 分割字符串
msg= "Lilei is a handsome boy"
#print(re.sub('\S+','-',msg))  注意\s  与 \S的区别
print(re.sub(r'\s+', '-->', msg))
print(re.sub('\s+','-',msg))