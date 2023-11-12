import os

domains = ['example.com']


def ping(ip):
    for i in ip:
        os.system('ping' + ' -c 5 ' + str(i))


ping(domains)
