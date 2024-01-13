import time

from pwn import *

# 文件类型与其开始字节的映射
file_types = {
    '60 EA': 'ARJ',
    '42 4D': 'BMP',
    '5F 27 A8 8': 'JAR',
    'FF D8 FF E0': 'JFIF',
    'FF D8 FF E1': 'JPG',
    'FF D8 FF E8': 'JPG',
    '46 57 53': 'SWF',
    '5A 57 53': 'SWF',
    '49 20 49': 'TIF',
    '50 4B':'ZIP',
    '47 49 46 38 3': 'GIF',
    '52 61 72 21 1':'RAR',
    '89 50 4E 47 0': 'PNG'
}

def get_file_type(start_bytes):
    for bytes, file_type in file_types.items():
        if start_bytes.startswith(bytes):
            return file_type
    return 'Unknown'

def main():
    # 连接到服务器
    while True:
        conn = remote('ctf.mf.grsu.by', 9010)
        for e in range(1,52):
            server_info = conn.recv().decode('utf-8')
            # print (server_info.split('\n'))
            start_bytes = str(server_info).split('\n')
            start_byte=start_bytes[-3]
            # print(start_byte)
            file_type = get_file_type(start_byte)
            conn.sendline(file_type)
            time.sleep(0.1)
            # req=conn.recv().decode('utf-8')
            # print(req)
            if '{' in server_info:
                print (start_bytes[1])
                exit()
        conn.recvall().decode('utf-8')

if __name__ == '__main__':
    main()