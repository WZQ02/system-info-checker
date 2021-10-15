import cv2
import numpy as np
print("生成黑白条纹图小程序\r\n")
orwid = eval(input("图像宽度："))
orhei = eval(input("图像高度："))
imagetyp = eval(input("指定图像类型，0为横向条纹，1为纵向条纹，2为25%点阵，3为50%点阵，4为75%点阵："))
texwid = eval(input("指定条纹/点阵宽度，值大于等于1，需要同时被图像宽度和高度整除："))
wid = int(orwid / texwid)
hei = int(orhei / texwid)
im = np.zeros((hei,wid),dtype=np.uint8)#生成黑色图像
imlst = list(im)
def img0():#生成横向条纹
    for i in range(0,hei,2):#每隔一行处理
        for j in range(0,wid,1):
            imlst[i][j] = 255
def img1():#生成纵向条纹
    for i in range(0,hei,1):
        for j in range(0,wid,2):#每隔一列处理
            imlst[i][j] = 255
def img2():#生成25%点阵
    for i in range(0,hei,1):
        for j in range(0,wid,1):
            if i%2 != 0:
                imlst[i][j] = 255
            elif j%2 != 0:
                imlst[i][j] = 255
def img3():#生成50%点阵
    for i in range(0,hei,1):
        for j in range(0,wid,1):
            if (i+j)%2 == 0:
                imlst[i][j] = 255
def img4():#生成75%点阵
    for i in range(0,hei,2):
        for j in range(0,wid,2):
            imlst[i][j] = 255
if imagetyp == 0:
    img0()
elif imagetyp == 1:
    img1()
elif imagetyp == 2:
    img2()
elif imagetyp == 3:
    img3()
elif imagetyp == 4:
    img4()
else:
    exit()
im = np.array(imlst)
im = cv2.resize(im,None,fx=texwid,fy=texwid,interpolation = cv2.INTER_NEAREST)
saveto = input("请输入保存图片的位置（完整路径，路径不能有中文）：")
cv2.imwrite(saveto,im)
print("已将图片生成至 {}".format(saveto))
input("按回车退出...")
