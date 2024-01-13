import base64
import cv2
import numpy as np
from pwn import *
from pyzbar.pyzbar import decode
import time


def connect_to_server():
    host = "ctf.mf.grsu.by"
    port = 9011

    try:
        return remote(host, port)
    except Exception as e:
        log.error(f"Error connecting to the server: {e}")
        return None


def receive_data(conn):
    try:
        data = conn.recv().decode('utf-8')
        return data
    except Exception as e:
        log.error(f"Error receiving data: {e}")
        return None


def send_data(conn, data):
    try:
        print("send data::::", data)
        conn.sendline(data)
    except Exception as e:
        log.error(f"Error sending data: {e}")


def decode_qr_code1(base64_data):
    try:
        image_data = base64.b64decode(base64_data)
        image_np = np.frombuffer(image_data, dtype=np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_GRAYSCALE)

        # Use pyzbar to decode QR code
        decoded_objects = decode(image)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        else:
            return None
    except Exception as e:
        log.error(f"Error decoding QR code: {e}")
        return None


import base64
import io
from pyzbar.pyzbar import decode
from PIL import Image


def decode_qr_code(base64_str):
    try:
        # 解码base64
        image_bytes = base64.b64decode(base64_str)

        # 把字节转换为图像
        _image = Image.open(io.BytesIO(image_bytes))
        image = _image.resize((100, 100))
        # 识别条形码或二维码
        decoded_data = decode(image)

        # 返回解码的信息，如果存在的话
        if decoded_data:
            return decoded_data[0].data.decode('utf-8')
        else:
            #            decode_qr_code(base64_str)
            return "No QR code found in the image."

    except Exception as e:
        return str(e)


def main():
    conn = connect_to_server()

    if conn:
        for round_num in range(1, 5800):
            data = receive_data(conn)
            print(data.split("\n"))
            log.info(data)

            # Extract base64 string
            try:
                img_base64 = data.split("\n")[-3]
            except:
                continue
            # Decode and print QR code data
            qr_code_data = decode_qr_code(img_base64)
            if qr_code_data:
                log.success(f"Decoded QR code: {qr_code_data}")

                # Submit the QR code data to the server
                send_data(conn, qr_code_data)
            else:
                log.error("Error decoding QR code. Skipping round.")

        conn.close()


if __name__ == "__main__":
    main()

