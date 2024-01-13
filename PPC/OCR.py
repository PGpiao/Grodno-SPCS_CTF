from pwn import *
import pytesseract
from PIL import Image
import base64
import time
def BaseToImg():
    im = Image.open("1.png")
    pstring = pytesseract.image_to_string(im)
    pas=str(pstring).strip().replace('_','').split("&")
    pstring_a=f"{pas[0]}_&_{pas[1]}_&_{pas[2]}"
    return pstring_a

def main():
    host = 'ctf.mf.grsu.by'
    port = 9007
    # context.log_level = 'DEBUG'
    while True:
    # 连接到服务器
        conn = remote(host, port)
        try:
            for round_num in range(1, 51):
                # time.sleep(0.2)
                server_info = conn.recv().decode('utf-8')
                start_byte = str(server_info).split('\n')
                img_base = start_byte[-3]
                # time.sleep(0.2)
                img_base64_arr=img_base.split("'")
                img_base64=img_base64_arr[1]
                # time.sleep(0.2)
                imgdata=base64.b64decode(img_base64)
                f=open('1.png','wb')
                f.write(imgdata)
                time.sleep(0.1)
                f.close()
                BaseToImg()
                # print(img_base64)
                otq = BaseToImg()
                otqd=str(otq).replace(" ","")
                conn.sendline(otqd)
                # 打印结果
                result = conn.recv().decode().strip()
                print(f'Round {round_num}/{50}:\n    - Your answer: {otqd}\n    - Result: {result}')
                if "{" in result:
                    exit()
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # 关闭连接
            conn.close()

if __name__ == '__main__':
    main()

