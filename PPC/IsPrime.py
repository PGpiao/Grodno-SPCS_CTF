from pwn import *

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    host = 'ctf.mf.grsu.by'
    port = 9000

    # 设置 log_level 为 DEBUG，以输出所有 socket 数据
    context.log_level = 'DEBUG'

    # 连接到服务器
    conn = remote(host, port)

    try:
        # 读取并解析提示
        prompt = conn.recvuntil('Раунд 1/50\n').decode()

        for round_num in range(1, 51):
            # 读取当前轮次的数字
            number = int(conn.recvline().decode().strip())

            # 判断是否为质数
            answer = 'YES' if is_prime(number) else 'NO'

            # 发送答案
            conn.sendline(answer)

            # 打印结果
            result = conn.recvuntil(f'Раунд {round_num + 1}/50\n', drop=True).decode().strip()
            # print(f'Round {round_num}/{50}: {number} - Your answer: {answer} - Result: {result}')
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 关闭连接
        conn.close()

if __name__ == '__main__':
    main()

