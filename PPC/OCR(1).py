from pwn import *
import pytesseract
from PIL import Image
import base64
import time
import io
import pytesseract
from pytesseract import Output

def _BaseToImg(bimg):
    pstring = pytesseract.image_to_string(bimg)


    return pstring


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
    # while True:
    # 连接到服务器
    conn = remote(host, port)

    try:
        for round_num in range(1, 100):
            time.sleep(0.1)
            server_info = conn.recv().decode('utf-8')
            time.sleep(0.1)
            start_byte = str(server_info).split('\n')
            time.sleep(0.1)
            print(start_byte)
            img_base = start_byte[-3]
            time.sleep(0.1)
            img_base64_arr=img_base.split("'")
            # print(img_base64_arr)
            time.sleep(0.1)

            img_base64=img_base64_arr[1]
            # time.sleep(0.1)
            res = BaseToImg(img_base64)
#                otqd=str(otq).replace(" ","")
            conn.sendline(res)
            result = conn.recv().decode().strip()
            print(f'Round {round_num}/{50}:\n    - Your answer: {res}\n    - Result: {result}')
            if "{" in result:
                exit()
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
            # 关闭连接
        conn.close()

if __name__ == '__main__':
    main()

