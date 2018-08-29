# 一个方便的数据结构导出工具

## 参数说明
````
usage: msh.py [-h] [-H HOST] [-u USER] [-p PSW] [-d DATABASE] [-P PORT]

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  mysql host
  -u USER, --user USER  mysql user
  -p PSW, --psw PSW     mysql psw
  -d DATABASE, --database DATABASE
                        mysql database
  -P PORT, --port PORT  mysql port


````

## 示例
````
python3 msh.py -H 127.0.0.1 -P 3306 -u root -p root -d boois-shop

````