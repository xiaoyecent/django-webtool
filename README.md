# django-webtool
django-webtools django实现的在线渗透实用小脚本

-----------------------------------------------
1.ip在线定位

https://bbs.ichunqiu.com/thread-22449-1-1.html

调用了百度的ip普通定位api以及静态地图生成api，用django实现在线ip定位

-----------------------------------------------
2.在线字典生成

调用exrex模块，利用正则生成相关的密码

注意，这个和社会工程学密码不一样，此项目是根据一个由用户提供的url来生成相关口令以及弱口令，可用于爆破

请使用者在使用在线ip定位时，在ak=xxxxxxxxx处（tool/ipapi.py文件中）填入自己的ak，可在百度开发者平台申请

请使用者在使用在线字典生成时在tool/dic_generate.py中注意dic_rule.ini和comm_dic.txt，此处我用了绝对位置，使用者可自行更改，或者添加path以使用相对地址
