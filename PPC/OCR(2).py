from pwn import *
import pytesseract
from PIL import Image
import base64
import time
import io
import re
from pytesseract import Output

def _BaseToImg(bimg):
    pstring = pytesseract.image_to_string(bimg)


    return pstring_a


def BaseToImg(b64img):
    try:
        # decode the base64 string
        image_bytes = base64.b64decode(b64img)
        
        # convert bytes to image
        image = Image.open(io.BytesIO(image_bytes))
        
        # OCR processing on the image
        result = pytesseract.image_to_string(image)

        pas=str(result).strip().replace('_','').split("&")
        res=f"{pas[0]}_&_{pas[1]}_&_{pas[2]}"

        return res.replace(" ","")

    except Exception as e:
        return f"An error occured: {str(e)}"


def main():
    host = 'ctf.mf.grsu.by'
    port = 9007
    # context.log_level = 'DEBUG'
    while True:
    # 连接到服务器
        conn = remote(host, port)
        try:
            for round_num in range(1, 500):
                time.sleep(1)
                # time.sleep(0.2)
                server_info = conn.recv().decode('utf-8')
                start_byte = str(server_info).split('\n')
                rer = re.findall("b'.*?'", str(server_info))
                img_base64 = (rer[0].split("'")[1])
                # time.sleep(0.2)
                res = BaseToImg(img_base64)
                conn.sendline(res)
                # 
                result = conn.recv().decode().strip()
                log.info(str(server_info))
                log.success(f' Your answer: {res}\n    - Result: {result}')
                if "{" in result:
                    exit()
        except Exception as e:
            print(e)

        finally:
            # 关闭连接
            conn.close()

if __name__ == '__main__':
    main()

