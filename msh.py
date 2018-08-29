import argparse

from mysql_helper import MysqlHelper
parser = argparse.ArgumentParser()

# Print args
def prase_args():
    # Add argument
    parser.add_argument("-H",'--host', help='mysql host', default="127.0.0.1")
    parser.add_argument("-u",'--user', help='mysql user', default="root")
    parser.add_argument("-p",'--psw', help='mysql psw', default="")
    parser.add_argument("-d",'--database', help='mysql database', default="test")
    parser.add_argument("-P",'--port', type=int, help='mysql port', default=3306)

    # Parse argument
    return parser.parse_args()


def show_tables(args):
    m = MysqlHelper(args.host, args.user, args.psw, args.database, args.port)
    res = m.fetchall("show tables")
    for o in res:
        tab = list(o.values())[0]
        print("-- %s --" % tab)
        res = m.fetchall("show create table %s" % tab)
        create_sql = res[0]['Create Table']
        print(create_sql)
        arr = create_sql.split("\n")

        for i, a in enumerate(arr):
            if i == 0:
                pass
            elif i == len(arr) - 1:
                pass
            else:
                q = '''ALTER TABLE `%s` ADD %s;''' % (tab, a.split(",")[0])
                print(q)
def main():
    args=prase_args()
    print("args",args)
    show_tables(args)
if __name__ == '__main__':
    main()