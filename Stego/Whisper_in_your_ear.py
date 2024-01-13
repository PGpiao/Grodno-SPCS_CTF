import os
import wave
import numpy as np
import matplotlib.pyplot as plt


def solve1():
    file_wave = wave.open("./sample-3sx.wav", "rb")

    params = file_wave.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    str_data = file_wave.readframes(nframes)
    file_wave.close()
    wave_data = np.frombuffer(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    l_channel = wave_data[0]
    r_channel = wave_data[1]
    for i in range(0,len(l_channel)):
        if l_channel[i] != r_channel[i]:
            # print("[d]index:   {0}   l:  {1}    r:    {2}".format(i, l_channel[i], r_channel[i]))
            print("[d]index:   {0}   l:  {1}    r:    {2}     -: {3}".format(i, l_channel[i], r_channel[i], r_channel[i]-l_channel[i]))
    res = ""
    for i in range(0, 272):
        res += str(r_channel[i] - l_channel[i])

    print(res)
    # bin to hex to string


def solve2():
    res1 = ""
    res2 = ""
    file_wave = wave.open("./files/sample-3sxyz.wav", "rb")
    params = file_wave.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    str_data = file_wave.readframes(nframes)
    file_wave.close()
    wave_data = np.frombuffer(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    l_channel = wave_data[0]
    r_channel = wave_data[1]
    for i in range(0, len(l_channel)):
        if l_channel[i] != r_channel[i]:
            print("[d]index:   {0}   l:  {1}    r:    {2}     -: {3}".format(i, l_channel[i], r_channel[i],
                                                                             r_channel[i] - l_channel[i]))
            # res += str(-(r_channel[i]-l_channel[i]))
    for i in range(0, 400):
        res1 += str(abs(r_channel[i]-l_channel[i]))
        res2 += str(abs((abs(r_channel[i]-l_channel[i]))-1))

    res3 = ""
    for i in range(0,400):
        sub = r_channel[i] - l_channel[i]
        if sub > 0:
            res3 += "+"
        if sub == 0:
            res3 += "0"
        if sub < 0:
            res3 += "-"

    print(res1)


    print(res2)
    print(res3)

    fig = plt.figure()
    plt.xlim(xmin=0, xmax=400)
    plt.ylim(ymin=-1, ymax=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    for x in range(0,400):
        y = r_channel[x] - l_channel[x]
        plt.scatter(x, y, color="black", label="data")
        plt.plot(x,y)
        plt.legend()
    path = os.getcwd()  # 获取当前的工作路径
    fileName = "979424151"
    filePath = path + "\\" + fileName + ".png"
    plt.savefig(filePath, dpi=600)  # dpi越大，图像越清晰，当然图像所占的存储也大
    plt.show()

    res4 = ""
    for i in range(0,400):
        sub = r_channel[i] - l_channel[i]
        res4 += str(sub+1)
    print(res4)

    res5_matrix = []
    for i in range(0,400):
        sub = r_channel[i] - l_channel[i]
        res5_matrix.append(sub)
    print(res5_matrix)
solve2()

# 0100011101011000110101101101000001100000010110000110110110010001001110100100000001110111100100110101011010111011011111001000101011011110101001001100001010111010110110011011000101011011010100100110011011000010101110011101000110000100101001010000101000100110101011001110011111101111110000001011000011011010011111100110010100110000010101000010100001110110010110011110000100000111110011001000001110001110
# 1011100010100111001010010010111110011111101001111001001001101110110001011011111110001000011011001010100101000100100000110111010100100001010110110011110101000101001001100100111010100100101011011001100100111101010001100010111001111011010110101111010111011001010100110001100000010000001111110100111100100101100000011001101011001111101010111101011110001001101001100001111011111000001100110111110001110001
# 0-000---0-0-+000+-0+0--0+-0+00000--000000-0+-0000--0-+0-+00-000+00-+-0-00-0000000-+-0---+00-00++0-0+0--0+0-++0+-0-+---00+000+0-0+-0+-++0+0-00-00+-0000-0+0-+-0-0++0-+00-+0-+000+0-0--0--0-0+00+00--00+-0+-0000-0+0-++00-+-0+000++0000+00+0-00-0-0000+0-000-00++0+0+0--00+--00-+++--0----+-000000+0-+0000++0-+0+00--++-+00--00-0-00+-00000-0+0+0000+0-0000---0+-00+0-+00-+--0000-00000+-++-00+-00+00000+++000--+0
# 1011100010102111201210012012111110011111101201111001021021101112110201011011111110201000211011221012100121022120102000112111210120120221210110112011110121020101221021102102111210100100101211211001120120111101210221102012111221111211210110101111210111011221212100112001102220010000201111112102111122102121100220211001101011201111101212111121011110001201121021102001111011111202201120112111112221110021
# [0, -1, 0, 0, 0, -1, -1, -1, 0, -1, 0, -1, 1, 0, 0, 0, 1, -1, 0, 1, 0, -1, -1, 0, 1, -1, 0, 1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 1, -1, 0, 0, 0, 0, -1, -1, 0, -1, 1, 0, -1, 1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 1, -1, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, -1, -1, -1, 1, 0, 0, -1, 0, 0, 1, 1, 0, -1, 0, 1, 0, -1, -1, 0, 1, 0, -1, 1, 1, 0, 1, -1, 0, -1, 1, -1, -1, -1, 0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 1, -1, 0, 1, -1, 1, 1, 0, 1, 0, -1, 0, 0, -1, 0, 0, 1, -1, 0, 0, 0, 0, -1, 0, 1, 0, -1, 1, -1, 0, -1, 0, 1, 1, 0, -1, 1, 0, 0, -1, 1, 0, -1, 1, 0, 0, 0, 1, 0, -1, 0, -1, -1, 0, -1, -1, 0, -1, 0, 1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1, -1, 0, 1, -1, 0, 0, 0, 0, -1, 0, 1, 0, -1, 1, 1, 0, 0, -1, 1, -1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 1, 0, 1, 0, -1, -1, 0, 0, 1, -1, -1, 0, 0, -1, 1, 1, 1, -1, -1, 0, -1, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 1, 0, -1, 1, 0, 0, 0, 0, 1, 1, 0, -1, 1, 0, 1, 0, 0, -1, -1, 1, 1, -1, 1, 0, 0, -1, -1, 0, 0, -1, 0, -1, 0, 0, 1, -1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, -1, -1, -1, 0, 1, -1, 0, 0, 1, 0, -1, 1, 0, 0, -1, 1, -1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, 1, 1, -1, 0, 0, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, 1, 0]