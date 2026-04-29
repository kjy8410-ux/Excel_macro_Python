#  pyinstaller -p c:\dll --hidden-import pkg_resources 8.excel_c_20231011.py
# 20221027에서 개선 (ORCAD DATA LIST 추출시, NETS 위쪽 데이터 포함으로 프로그램 구동이 가능하도록 변경)

# -*- coding: utf-8 -*-
# 아래 파일 절대 수정 금지
# DXFTOPCADPAD.py


import tkinter as tk
import tkinter.font
import tkinter.ttk
import tkinter.messagebox as msgbox
from tkinter import simpledialog, messagebox
from tkinter import * # __all__
from tkinter import filedialog
from xlrd import count_records, open_workbook
import os
from win32api import GetSystemMetrics
import pygetwindow as gw
import clipboard
import re
import getmac
import ezdxf
# import ConfigMapingBLOCK

def block():
    test = 1
    # ConfigMapingBLOCK.allmake()


def copyfromup() : # 빈칸 위에 자료를 카피
    output = ""
    data = clipboard.paste()
    datalist = list()
    data2 = data.split("\r\n")
    data2.pop()
    for i in range(0,len(data2)):

        if data2[i] =="":
            output = output + datalist[i-1]  + "\r\n"
            datalist.append(datalist[-1])
        else:
            output = output + data2[i] + "\r\n"
            datalist.append(data2[i])    
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)

def numdivtapaplahs():# 숫자 문자 분리후 앞쪽 숫자 0없애고 탭으로 나누기
    output = ""
    data = clipboard.paste()

    data2 = data.split("\r\n")
    data2.pop()

    for i in data2:
        numbers = re.findall('\d+', i)
        alphas = re.findall('[a-zA-Z]+', i)
        if i == len(data2)-1:
            output = output + str(str(alphas) +"\t"+ str(numbers).lstrip("0")).replace("['","").replace("']","")
        else :
            output = output + str(str(alphas) +"\t"+ str(numbers).lstrip("0") + "\r\n").replace("['","").replace("']","")
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)

def numdivalpha(): # 숫자 문자 분리후 숫자앞자리 하나 없애고 0없애기
    output = ""
    data = clipboard.paste()

    data2 = data.split("\r\n")
    data2.pop()

    for i in data2:
        numbers = re.findall('\d+', i)
        alphas = re.findall('[a-zA-Z]+', i)
        if i == len(data2)-1:
            output = output + str(str(alphas) + str(numbers)[3:].lstrip("0")).replace("['","").replace("']","")
        else :
            output = output + str(str(alphas) + str(numbers)[3:].lstrip("0") + "\r\n").replace("['","").replace("']","")
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)


def numdivalphaszifll(): # 숫자 문자 분리후 자리수 맞추기
    output = ""
    data = clipboard.paste()
    자리수 = int(globals()['frame_et{}'.format(button_list.index(numdivalphaszifll))].get())
    data2 = data.split("\r\n")
    data2.pop()

    for i in data2:
        numbers = re.findall('\d+', i)
        # alphas = re.findall('[a-zA-Z]+', i)
        # if i == len(data2)-1:
        #     # output = output + str(alphas).replace("[","").replace("]","").replace("'","") + str(numbers).replace("[","").replace("]","").replace("'","").zfill(자리수)
        #     print(str(i))
        #     output = output + str(i).replace(numbers,str(numbers).replace("[","").replace("]","").replace("'","").zfill(자리수))

        # else :
            # output = output + str(alphas).replace("[","").replace("]","").replace("'","") + str(numbers).replace("[","").replace("]","").replace("'","").zfill(자리수) + "\r\n"
        # print(str(i))
        # print(numbers)
        if i == "" :
            output = output + "\r\n"
            # print("1")    
        elif len(numbers) == 0 :
            output = output + "\r\n"
            # print("2")
        elif i == numbers :
            output = output + "\r\n"
            # print("3")            
        else:
            changenumbers = str(numbers).replace("[","").replace("]","").replace("'","").zfill(자리수)
            output = output + str(i).replace(numbers[0],changenumbers) + "\r\n"
    print(numbers)

            
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)

def numdivalphasziflltext(): # 숫자 문자 분리후 자리수 맞추기 (특정 텍스트만)
    output = ""
    data = clipboard.paste()
    자리수 = int(globals()['frame_et{}'.format(button_list.index(numdivalphaszifll))].get())
    찾을문자 = globals()['frame_et{}'.format(button_list.index(numdivalphasziflltext))].get()
    data2 = data.split("\r\n")
    data2.pop()

    for i2 in data2:
        data3 = i2.split("\t")
        for i in data3:
            numbers = re.findall('\d+', i)
            if i.find(찾을문자):
                output = output + str(i) + "\t"
            else:
                if i == "" :
                    output = output + "\t"
                    # print("1")    
                elif len(numbers) == 0 :
                    output = output + "\t"
                    # print("2")
                elif i == numbers :
                    output = output + "\t"
                    # print("3")            
                else:
                    changenumbers = str(numbers).replace("[","").replace("]","").replace("'","").zfill(자리수)
                    output = output + str(i).replace(numbers[0],changenumbers) + "\t"
        output = output + "\r\n"            
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)

def concatennate(): # 행 순서대로 합치기
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    출력자료 = ""
    구분기호 = globals()['frame_et{}'.format(button_list.index(concatennate))].get()

    자료합치기 = ""

    for 행자료 in data2:
        행자료리스트 = 행자료.split("\t")

        for 행자료인덱스 in range(0,len(행자료리스트)):
            # if 행자료리스트[행자료인덱스] == "":
            #     출력자료 = 출력자료
            #     # print(행자료리스트[행자료인덱스],"1")
            # else:
            출력자료 = 출력자료 + 행자료리스트[행자료인덱스] + 구분기호
            # print(행자료리스트[행자료인덱스],"3") 
        if 출력자료[-1] == 구분기호:
            출력자료 = 출력자료[0:-1] 
        출력자료 = 출력자료 + "\r\n"



    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)


def datalineaddfromnum():# 일정 간격으로 자료 사이에 line 추가 하기
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    출력자료 = ""
    추가자료숫자 = int(globals()['frame_et{}'.format(button_list.index(datalineaddfromnum))].get())
    다음숫자 = 9999999999

    for i in range(0,len(data2)):
        출력자료 = 출력자료 + data2[i] + "\r\n"
        if i == 추가자료숫자-1:
            출력자료 = 출력자료 + "\r\n"
            다음숫자 = 추가자료숫자 + 추가자료숫자 -1 
            
        if i == 다음숫자 :
            출력자료 = 출력자료 + "\r\n"
            다음숫자 = 다음숫자 + 추가자료숫자
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)

def datalineaddfromnum2():# 일정 라인 갯수 기준으로 자료 나열 하기
    # try:    
        data = clipboard.paste()
        data2 = data.split("\r\n")
        data2.pop()
        출력자료 = ""
        추가자료숫자 = int(globals()['frame_et{}'.format(button_list.index(datalineaddfromnum2))].get())
        초기숫자 = 0
        반복횟수 = int(len(data2)/추가자료숫자)   
        print(추가자료숫자, 반복횟수, len(data2))

        for i in range(0,추가자료숫자):
            for i2 in range(0,반복횟수):
                if 추가자료숫자 == 0:
                    추가자료숫자 == 1
                초기숫자 = ((추가자료숫자-1) * i2 ) 
                if i2 == int(반복횟수-1) :
                    출력자료 = 출력자료 + data2[i2+초기숫자+i] + "\r\n"
                else :
                    출력자료 = 출력자료 + data2[i2+초기숫자+i] + "\t" + "\t" 
    
        msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
        clipboard.copy(출력자료)
    # except:
    #     msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    #     clipboard.copy(출력자료)

def datalineaddfromnum3():# 일정 라인 갯수 기준으로 자료 나열 하기
    # try:    
        data = clipboard.paste()
        data2 = data.split("\r\n")
        data2.pop()
        출력자료 = ""
        추가자료숫자 = int(globals()['frame_et{}'.format(button_list.index(datalineaddfromnum3))].get())
        초기숫자 = 0
        반복횟수 = int(len(data2)/추가자료숫자)   
        print(추가자료숫자, 반복횟수, len(data2))

        for i in range(0,추가자료숫자):
            for i2 in range(0,반복횟수):
                if 추가자료숫자 == 0:
                    추가자료숫자 == 1
                초기숫자 = ((추가자료숫자-1) * i2 ) 
                if i2 == int(반복횟수-1) :
                    출력자료 = 출력자료 + data2[i2+초기숫자+i] + "\r\n"
                else :
                    출력자료 = 출력자료 + data2[i2+초기숫자+i] + "\t" 
    
        msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
        clipboard.copy(출력자료)
    # except:
    #     msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    #     clipboard.copy(출력자료)


def datarote():# 자료를 설정된 숫자만큼 행으로 변경
    data = clipboard.paste()
    data2 = data.replace("\r\n","\t")
    data2 = data2.split("\t")
    data2.pop()
    출력자료 = ""
    변경숫자 = int(globals()['frame_et{}'.format(button_list.index(datarote))].get())
    다음숫자 = 9999999999

    for i in range(0,len(data2)):
        
        if i == 변경숫자-1:
            출력자료 = 출력자료 + data2[i] + "\r\n"
            다음숫자 = 변경숫자 + 변경숫자 -1 
            
        elif i == 다음숫자 :
            출력자료 = 출력자료 + data2[i] + "\r\n"
            다음숫자 = 다음숫자 + 변경숫자

        else:
            출력자료 = 출력자료 + data2[i] + "\t"
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)

def datacellonerow():
    rowdata = int(globals()['frame_et{}'.format(button_list.index(datacellonerow))].get())
    data = clipboard.paste()
    data2 = data.split("\r\n")
    출력자료 = ""
    data2.pop()
    for i in range(0,rowdata):
        locals()['rowdata_{}'.format(i)] = list()

    for i2 in range(0,len(data2)):
        indata = i2 % rowdata
        locals()['rowdata_{}'.format(indata)].append(data2[i2])

    for i3 in range(0,rowdata):
        for i4 in locals()['rowdata_{}'.format(i3)]:
            출력자료 = 출력자료 + i4 + "\t"
        출력자료 = 출력자료 + "\r\n"
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)    
    
def datacelloneline(): # 빈셀 없애고 한줄로 만들기
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    출력자료 = ""

    for i in data2:
        i = i.split("\t")
        for i2 in i :
            if not i2 == "" :
                출력자료 = 출력자료 + i2 + "\r\n"
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)

def datarowsort(): # 데이터 행으로 역순 정렬
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    출력자료 = ""
    
    for data2t in data2 :
        data2t = data2t.split("\t")
        for i2 in range(0,len(data2t)):
            if not i2 == len(data2t)-1:
                출력자료 = 출력자료 + data2t[len(data2t)-1-i2] + "\t"
            else : 
                출력자료 = 출력자료 + data2t[len(data2t)-1-i2]
        출력자료 = 출력자료 + "\r\n"
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)

def datacolsort(): # 데이터 열 역순 정렬
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    출력자료 = ""

    for i in range(0,len(data2)):
        출력자료 = 출력자료 + data2[len(data2)-1-i] + "\r\n"
            
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(출력자료)

def numdivalphaszifllfirst(): # 숫자 문자 분리후 뒷 자리수 맞추기
    print("numdivalphaszifllfirst")
    output = ""
    data = clipboard.paste()
    자리수 = int(globals()['frame_et{}'.format(button_list.index(numdivalphaszifllfirst))].get())
    찾을문자 = globals()['frame_et{}'.format(button_list.index(numdivalphasziflltext))].get()
    data2 = data.split("\r\n")
    data2.pop()
    sheetindex = 0

    for i in data2:
        if 찾을문자 in i:
            sheetindex = sheetindex + 1
            numbers = re.findall(r'\d+', i)
            alphas = re.findall(r'[a-zA-Z]+', i)
            if i[0].isalpha():
                if len(alphas) == len(numbers):
                    for i2 in range(0, len(alphas)):
                        if i2 == 0:
                            output = output + alphas[i2] + numbers[i2] + "_"
                        else:
                            output = output + alphas[i2] + "_" + str(int(numbers[i2])).zfill(자리수)
                else:
                    for i2 in range(0, len(alphas)):
                        if len(numbers) == 0:
                            output = output + alphas[i2]
                        else:
                            if i2 == 0:
                                output = output + alphas[i2] + numbers[i2] + "_"
                            elif i2 == (len(alphas) - 1):
                                output = output + alphas[i2]
                            else:
                                output = output + alphas[i2] + "_" + str(int(numbers[i2])).zfill(자리수)
                output = output + "\r\n"
            else:
                if len(alphas) == len(numbers):
                    for i2 in range(0, len(numbers)):
                        if i2 == 0:
                            output = output + numbers[i2] + "_" + alphas[i2]
                        else:
                            output = output + str(int(numbers[i2])).zfill(자리수)  + "_" + alphas[i2]
                else:
                    for i2 in range(0, len(numbers)):
                        if len(alphas) == 0:
                            output = output + numbers[i2] + "_"
                        else:
                            if i2 == 0:
                                output = output + numbers[i2] + "_" + alphas[i2]
                            elif i2 == len(numbers) - 1:
                                output = output + numbers[i2]
                            else:
                                output = output + numbers[i2] + "_" + alphas[i2]
                output = output + "\r\n"
        else:
            output = output + str(i) + "\r\n"

    msgbox.showinfo("붙여넣기 하세요.", "붙여넣기 하세요!")
    clipboard.copy(output)


def numdivalphaszifllfirst2():
    output = ""
    data = clipboard.paste()
    자리수 = int(globals()['frame_et{}'.format(button_list.index(numdivalphaszifllfirst2))].get())
    찾을문자 = globals()['frame_et{}'.format(button_list.index(numdivalphasziflltext))].get()
    data2 = data.split("\r\n")
    data2.pop()
    sheetindex = 0

    for i in data2:
        if 찾을문자 in i:
            sheetindex = sheetindex + 1
            numbers = re.findall(r'\d+', i)
            alphas = re.findall(r'[a-zA-Z]+', i)
            if i[0].isalpha():
                if len(alphas) == len(numbers):
                    for i2 in range(0, len(alphas)):
                        if i2 == 0:
                            output = output + alphas[i2] + str(int(numbers[i2])).zfill(자리수) + "_"
                        else:
                            output = output + alphas[i2] + "_" + numbers[i2]
                else:
                    for i2 in range(0, len(alphas)):
                        if len(numbers) == 0:
                            output = output + alphas[i2]
                        else:
                            if i2 == 0:
                                output = output + alphas[i2] + str(int(numbers[i2])).zfill(자리수) + "_"
                            elif i2 == (len(alphas) - 1):
                                output = output + alphas[i2]
                            else:
                                output = output + alphas[i2] + "_" + numbers[i2]
                output = output + "\r\n"
            else:
                if len(alphas) == len(numbers):
                    for i2 in range(0, len(numbers)):
                        if i2 == 0:
                            output = output + str(int(numbers[i2])).zfill(자리수) + "_" + alphas[i2]
                        else:
                            output = output + numbers[i2] + "_" + alphas[i2]
                else:
                    for i2 in range(0, len(numbers)):
                        if len(alphas) == 0:
                            output = output + numbers[i2] + "_"
                        else:
                            if i2 == 0:
                                output = output + numbers[i2] + "_" + alphas[i2]
                            elif i2 == len(numbers) - 1:
                                output = output + numbers[i2]
                            else:
                                output = output + numbers[i2] + "_" + alphas[i2]
                output = output + "\r\n"
        else:
            output = output + str(i) + "\r\n"

    msgbox.showinfo("붙여넣기 하세요.", "붙여넣기 하세요!")
    clipboard.copy(output)



def meargdata1_2(): # 1열 기준 2열 자료를 취합 해줌
    output = ""
    data = clipboard.paste()
    data2 = data.split("\r\n")
    data2.pop()
    data1list = list()
    data2list = list()
    data3list = list()
    for i in data2 :
        data3 = i.split("\t")
        data1list.append(data3[0])
        data2list.append(data3[1])


    for i in range(0,len(data1list)):
        data1listlist = list()
        if not data1list[i] in data3list:
            data1listlist = [i5 for i5, value in enumerate(data1list) if value == data1list[i]]
            print(data1listlist)
            # print(data1list[i])
            print(len(data1list),"진행",i)
            if i == len(data1list)-1 :
                output = output + data1list[i] + "\t"
                for i2 in data1listlist:
                    if len(data1listlist) == 1:
                        output = output + data2list[i2]
                    elif i2 == data1listlist[-1]:
                        output = output + data2list[i2]
                    else:
                        output = output + data2list[i2] + ","
            else:
                output = output + data1list[i] + "\t"
                for i2 in data1listlist:
                    if len(data1listlist) == 1:
                        output = output + data2list[i2]
                    elif i2 == data1listlist[-1]:
                        output = output + data2list[i2]
                    else:
                        output = output + data2list[i2] + ","
                output = output + "\r\n"

        if not data1list[i] in data3list:
            data3list.append(data1list[i])


    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")
    clipboard.copy(output)


##### 2번째 행 자료들

def coordinates(): # 좌표 정보 변환
    to = clipboard.paste()
    adddata = ""
    datalist = ""
    for i in to:
        adddata = adddata + str(i)
    adddata = str(adddata).replace(" ","\t").split(",")
    for i in adddata:
        i = i.replace("\r\n","\t")
        i2 = i.split("\t")
        for i3 in i2:
            find1 = i3.count("(")
            find2 = i3.count(")")
            find3 = find1 + find2
            if find3 == 2:
                data2 = i2.index(i3)
                datazfill = re.findall("\d+", i2[data2-1])
                originaldata = i2[data2-1].split("-")
                # datazfille = originaldata[0].replace(datazfill[0],datazfill[0].zfill(3)) + "-" + originaldata[1].replace(datazfill[1],datazfill[1].zfill(3))
                
                datalist = datalist + "{1}\t{0}\r\n".format(i2[data2-1],i2[data2].replace("(","").replace(")","").replace(":","\t"))#datazfille)
    clipboard.copy(datalist)
    msgbox.showinfo("데이터 변환 완료", "변환이 완료 되었습니다. 붙여넣기 하세요.")

def p_transdata2():
    to = clipboard.paste()
    alldata = to.split("\r\n")
    pastedata = ""
    columnlinelist = []

    for columnline in range(0,len(alldata)):
        check = alldata[columnline]
        if "§" in check:
            columnlinelist.append(columnline)
            print(columnlinelist)

    for data in range(0,len(columnlinelist)-1):
        startline = columnlinelist[data]
        endline = columnlinelist[data+1]
        startlinedata = alldata[startline].split("\t")
        blockname = startlinedata[0]
 
        # pastedata = pastedata + alldata[startline] + "\r\n"
        for i in range(startline+1,endline):
            linedata = alldata[i].split("\t")
            # pastdata = linedata[0] 
            for i2 in range(1,len(linedata)):
                if linedata[i2] == "":
                    pastedata = pastedata + "\t"
                else:
                    pastedata = pastedata  +blockname + "◇" + startlinedata[i2]  + "◇" + linedata[0] + "◇" + linedata[i2] + "\t"
            pastedata = pastedata + "\r\n" 
        pastedata = pastedata + "\r\n"

    clipboard.copy(pastedata)
    msgbox.showinfo("데이터 변환 완료", "변환이 완료 되었습니다. 붙여넣기 하세요.")

def 내용추가리스트():
    global 좌우리스트
    리스트추가 = clipboard.paste()
    좌우리스트 = 리스트추가.split("\r\n")
    좌우리스트.pop()
    msgbox.showinfo("데이터 입력완료","리스트 데이터 입력 완료")

def 앞쪽내용추가():
    출력용데이터 = ""
    기존데이터 = clipboard.paste()
    기존데이터 = 기존데이터.split("\r\n")
    for 자료합치기 in 좌우리스트:
        for 행자료 in 기존데이터:
            행자료리스트 = 행자료.split("\t")
            for 자료인덱스 in range(0,len(행자료리스트)) :
                if not 자료인덱스 == len(행자료리스트)-1 :
                    if 행자료리스트[자료인덱스].strip() == "":
                        출력용데이터 = 출력용데이터 +  "\t"
                    else :
                        출력용데이터 = 출력용데이터 + 자료합치기 + 행자료리스트[자료인덱스] + "\t"
                else:
                    if 행자료리스트[자료인덱스].strip() == "":
                        출력용데이터 = 출력용데이터 +  "\r\n"
                    else :
                        출력용데이터 = 출력용데이터 + 자료합치기 + 행자료리스트[자료인덱스] + "\r\n"
    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def 뒤쪽내용추가():
    출력용데이터 = ""
    기존데이터 = clipboard.paste()
    기존데이터 = 기존데이터.split("\r\n")
    for 자료합치기 in 좌우리스트:
        for 행자료 in 기존데이터:
            행자료리스트 = 행자료.split("\t")
            for 자료인덱스 in range(0,len(행자료리스트)) :
                if not 자료인덱스 == len(행자료리스트)-1 :
                    if 행자료리스트[자료인덱스].strip() == "":
                        출력용데이터 = 출력용데이터 +  "\t"
                    else :
                        출력용데이터 = 출력용데이터 +  행자료리스트[자료인덱스] + 자료합치기 + "\t"
                else:
                    if 행자료리스트[자료인덱스].strip() == "":
                        출력용데이터 = 출력용데이터 +  "\r\n"
                    else :
                        출력용데이터 = 출력용데이터 + 행자료리스트[자료인덱스] + 자료합치기+ "\r\n"                        
        
    # print(출력용데이터)
    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def 기준데이터입력(): #기준 데이터 입력
    global 기준데이터
    기준데이터 = clipboard.paste()
    기준데이터 = 기준데이터.split("\r\n")
    기준데이터.pop
    msgbox.showinfo("데이터 입력완료","기준 데이터 입력 완료")
    # return 기준데이터

def 변환용데이터입력(): #변환 데이터 입력
    global 변환용데이터
    변환용데이터인덱스 = list()
    변환용데이터 = clipboard.paste()
    변환용데이터 = 변환용데이터.split("\r\n")
    for 변환용데이터입력 in 변환용데이터 :
        변환용데이터인덱스.append(변환용데이터입력.split("\t"))
    변환용데이터 = 변환용데이터인덱스
    변환용데이터.pop
    msgbox.showinfo("데이터 입력완료","변환 자료 입력 완료")
    # return 변환용데이터

def 데이터변환(): #1열 검색 2열 변환
    global 기준데이터
    global 변환용데이터
    출력용데이터 = ""

    for 기준데이터입력 in 기준데이터 :
        기준데이터행 = 기준데이터입력.split("\t")
        기준데이터행출력 = ""
        for 기준데이터셀자료 in 기준데이터행:            
            for i in range(0,len(변환용데이터)-1):
                입력자료 = 변환용데이터[i][0]
                if 기준데이터셀자료 == 입력자료:
                    기준데이터셀자료 = 변환용데이터[i][1]
                    break
            
            기준데이터행출력 = 기준데이터행출력 + 기준데이터셀자료 + "\t"
    
        출력용데이터 = 출력용데이터 + 기준데이터행출력 + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def 데이터변환삭제(): #1열 검색 2열 변환
    global 기준데이터
    global 변환용데이터
    출력용데이터 = ""

    for 기준데이터입력 in 기준데이터 :
        기준데이터행 = 기준데이터입력.split("\t")
        기준데이터행출력 = ""
        for 기준데이터셀자료 in 기준데이터행:            
            원래데이터 = 기준데이터셀자료
            데이터바뀜 = 0
            for i in range(0,len(변환용데이터)-1):
                입력자료 = 변환용데이터[i][0]
                if 기준데이터셀자료 == 입력자료:
                    기준데이터셀자료 = 변환용데이터[i][1]
                    데이터바뀜 = 1
                    break

            if 원래데이터 == 기준데이터셀자료 :
                if not 데이터바뀜 == 1:
                    기준데이터셀자료 = ""
            if len(기준데이터행) == 1:
                기준데이터행출력 = 기준데이터행출력 + 기준데이터셀자료
            else:
                기준데이터행출력 = 기준데이터행출력 + 기준데이터셀자료 + "\t"
    
        출력용데이터 = 출력용데이터 + 기준데이터행출력 + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def 서브자료저장버튼(): # 양쪽 데이터 합치기
    global 서브자료저장
    서브자료저장 = clipboard.paste()
    서브자료저장 = 서브자료저장.split("\r\n")
    서브자료저장.pop()
    msgbox.showinfo("데이터 입력완료","서브자료 데이터 입력 완료")

def 기준자료에서브자료매칭(): # 기존자료 기준 서브 자료에 있는 데이터를 합쳐줌
    global 서브자료저장
    서브자료열갯수 = 서브자료저장[0].split("\t")

    기존자료 = clipboard.paste()
    기존자료리스트 = 기존자료.split("\r\n")
    기존자료리스트.pop()
    기존자료열갯수 = 기존자료리스트[0].split("\t")

    출력용데이터 = ""
    중간문자 = "§"

    if len(서브자료저장) == len(기존자료리스트) and len(서브자료열갯수) == len(기존자료열갯수):
        for 행자료인덱스 in range(0,len(기존자료리스트)) :
            기존행자료 = 기존자료리스트[행자료인덱스].split("\t")
            서브행자료 = 서브자료저장[행자료인덱스].split("\t")
            for 열자료 in range(0,len(기존행자료)):
                기존셀자료 = 기존행자료[열자료]
                서브셀자료 = 서브행자료[열자료]
                중간문자 = "§"
                if 기존셀자료 == 서브셀자료 :
                    if not 열자료 == len(기존행자료)-1 :
                        if not 기존셀자료.strip() == "":
                            출력용데이터 = 출력용데이터 + 기존셀자료 + "\t"
                        else :
                            출력용데이터 = 출력용데이터 + "\t"
                    else:    
                        if not 기존셀자료.strip() == "":
                            출력용데이터 = 출력용데이터 + 기존셀자료 + "\r\n"
                        else :
                            출력용데이터 = 출력용데이터 + "\r\n"
                else:
                    if not 열자료 == len(기존행자료)-1 :
                        if not 기존셀자료.strip() == "":
                            출력용데이터 = 출력용데이터 + 서브셀자료 + 중간문자 + 기존셀자료 + "\t"
                        else :
                            출력용데이터 = 출력용데이터 + "\t"
                    else:    
                        if not 기존셀자료.strip() == "":
                            출력용데이터 = 출력용데이터 + 서브셀자료 + 중간문자 + 기존셀자료 + "\r\n"
                        else :
                            출력용데이터 = 출력용데이터 + "\r\n"
            



        clipboard.copy(출력용데이터)
        msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

    else:
        msgbox.showinfo("자료가 다릅니다.","기준자료{}행,{}열,서브자료{}행,{}열".format(len(기존자료리스트),len(기존자료열갯수),len(서브자료저장),len(서브자료열갯수)))

def Criteria1_1(): # 기준 데이터
    global criteriadata
    criteriadata = clipboard.paste()
    msgbox.showinfo("데이터 입력완료","기준 데이터 입력 완료")

def Criteria1_2(): # 좌표 데이터    
    global searchdata
    searchdata = clipboard.paste()
    msgbox.showinfo("데이터 입력완료","좌표 데이터 입력 완료")

def marge(): # 좌표 데이터 자료 매칭
    clipboardcopy = ""

    stripsearchdata = searchdata.split("\r\n")
    stripsearchdatalist = []
    for i in stripsearchdata:
        i = i.split("\t")
        index2 = len(i) -1
        data = i[index2]
        stripsearchdatalist.append(data)


    stripcriteria = criteriadata.split("\r\n")

    for i in stripcriteria:
        i2 = i.split("\t")
        index2 = len(i2) -1
        data = i2[index2]
        if data in stripsearchdatalist :
            searchindex = stripsearchdatalist.index(data)
            clipboardcopy = clipboardcopy + i + "\t" + stripsearchdata[searchindex] + "\r\n"
        else:
            clipboardcopy = clipboardcopy + i + "\t" + "X" + "\r\n"

    clipboard.copy(clipboardcopy)
    msgbox.showinfo("데이터 변환 완료", "변환이 완료 되었습니다. 붙여넣기 하세요.")

def Criteria1_1(): # 기준 데이터
    global criteriadata
    criteriadata = clipboard.paste()
    msgbox.showinfo("데이터 입력완료","기준 데이터 입력 완료")

def Criteria2():
    global searchdata
    global searchdata2

    searchdata = clipboard.paste()
    searchdata2 = list() # 리스트화 시킨 채널 정보
    searchdata3 = list() # 데이터 묶음용 버퍼
    # searchdata = searchdata.replace("-","/") #특수문자 및 스페이스바 제거
    while True :
        cutdatas = searchdata.find(" (")
        if cutdatas > -1 :
            cutdatae = searchdata.find(")")                    
            searchdata = searchdata.replace(searchdata[cutdatas:cutdatae+1],"")
        else :
            break
    searchdata = searchdata.split("\r\n")
    for i in range(0,len(searchdata)):
        if not searchdata[i] == "":
            if not searchdata[i][-1] == ",":
                searchdata[i] = searchdata3 + searchdata[i].replace("        ","").replace(" ","☆").split(",")    
                searchdata2.append(searchdata[i]) #searchdata2 Pcad 데이터
                searchdata3 = []

            else:
                searchdata3 = searchdata3 + searchdata[i][0:-1].replace("        ","").replace(" ","☆").split(",")
    msgbox.showinfo("데이터 입력완료","CAM NET 입력 완료")

def netmarge():
    global criteriadata
    global searchdata2
    clipboardcopy = ""
    stripcriteria = criteriadata.split("\r\n")
    for 기존좌표 in stripcriteria:
        비교데이터 = clipboardcopy
        for 비교자료 in searchdata2:
            if 기존좌표 in 비교자료 :
                # deldata = searchdata2.index(비교자료)
                del비교자료 = 비교자료.index(기존좌표)
                del 비교자료[del비교자료]
                clipboardcopy = clipboardcopy + "{0}\t{1}\r\n".format(비교자료[0],비교자료[1:])
                # del searchdata2[deldata]
                break
        if 비교데이터 == clipboardcopy:
            clipboardcopy = 비교데이터 + "\tX\r\n"            

    clipboard.copy(clipboardcopy)
    msgbox.showinfo("데이터 변환 완료", "변환이 완료 되었습니다. 붙여넣기 하세요.")

def 채널정리(): # 1열 기준 2열 데이터자료중 제일 아래 있는 자료로 데이터 변경
    채널네임 = list()
    채널연결리스트 = list()
    출력용데이터 = ""
    기존채널 = clipboard.paste()
    채널리스트 = 기존채널.split("\r\n")

    for i in 채널리스트[:-1]:
        i = i.split("\t")
        채널네임.append(i[0])
        채널연결리스트.append(i[1])


    for 채널 in range(0,len(채널네임)):
        if 채널네임.count(채널네임[채널]) > 1 :
            res_list = [i for i, value in enumerate(채널네임) if value == 채널네임[채널]]
            출력용데이터 = 출력용데이터 + 채널네임[채널] + "\t"
            출력용데이터 = 출력용데이터 + 채널연결리스트[res_list[len(res_list)-1]] + "\r\n"
        else:
            출력용데이터 = 출력용데이터 + 채널네임[채널] + "\t"
            출력용데이터 = 출력용데이터 + 채널연결리스트[채널] + "\r\n"
        
    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def 멀티플채널검색(): # 동일한 자료가 있으면 해당 자료를 1개씩만 출력
    채널리스트 = clipboard.paste()
    채널리스트 = 채널리스트.split("\r\n")
    출력용데이터 = ""
    멀티플리스트 = list()

    for 채널리스트검색용 in 채널리스트 :
        if 채널리스트.count(채널리스트검색용) > 1:
            if not 채널리스트검색용 in 멀티플리스트 :
                멀티플리스트.append(채널리스트검색용)

    for 출력 in 멀티플리스트:
        출력용데이터 = 출력용데이터 + 출력 + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!") 

def 문자포함자료만찾기():
    입력자료 = clipboard.paste()
    입력자료 = 입력자료.split("\r\n")
    찾을자료 = str(globals()['2frame_et{}'.format(button_list2.index(문자포함자료만찾기))].get())
    찾을자료 = 찾을자료.split(",")
    출력용데이터 = ""
    # print(입력자료,찾을자료)
    for i in 입력자료:
        리스트분해 = i.split(",")
        dataon = 0
        for i2 in range(0,len(리스트분해)):
            for i in 찾을자료:
                if not 리스트분해[i2].find(i) == -1:
                    출력용데이터 = 출력용데이터 + 리스트분해[i2] + ","
                    dataon = 1
                    break
        if dataon == 1:
            출력용데이터 = 출력용데이터[:-1]        
        출력용데이터 = 출력용데이터 + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!") 

def 문자포함자료만제거():
    입력자료 = clipboard.paste()
    입력자료 = 입력자료.split("\r\n")
    찾을자료 = globals()['2frame_et{}'.format(button_list2.index(문자포함자료만찾기))].get()
    출력용데이터 = ""
    # print(입력자료,찾을자료)
    for i in 입력자료:
        리스트분해 = i.split(",")
        dataon = 0
        for i2 in range(0,len(리스트분해)):
            for i in 찾을자료:
                if 리스트분해[i2].find(i) == -1:
                    출력용데이터 = 출력용데이터 + 리스트분해[i2] + ","
                    dataon = 1
                    break
        if dataon == 1:
            출력용데이터 = 출력용데이터[:-1]        
        출력용데이터 = 출력용데이터 + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")


# def DCBA한줄정렬():
#     입력자료 = clipboard.paste()
#     입력자료 = 입력자료.split("\r\n")
#     입력자료.pop()
#     출력용데이터 = ""
#     입력자료열수 = 입력자료[0].split("\t")
#     print(입력자료열수)
#     입력자료열수 = len(입력자료열수)
#     for i2 in range(1,(입력자료열수+1)):
#         for i in range(0,len(입력자료)):
#             출력인덱스 = 입력자료열수 - i2
#             출력자료 = 입력자료[i].split("\t")
#             print(입력자료열수)
#             print(출력인덱스,i2)
#             출력용데이터 = 출력용데이터 + 출력자료[출력인덱스] + "\r\n"

#     clipboard.copy(출력용데이터)
#     msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def DCBA한줄정렬():
    입력자료 = clipboard.paste()
    입력자료 = 입력자료.split("\r\n")
    입력자료.pop()
    출력용데이터 = ""
    입력자료열수 = 입력자료[0].split("\t")
    # print(입력자료열수)
    입력자료열수 = len(입력자료열수)
    배수 = int(입력자료열수/5) + 1
    for i2 in range(1,배수):
        실제위치 = i2 * 5
        for i in range(0,len(입력자료)):
            출력인덱스 = 실제위치 - 1
            출력자료 = 입력자료[i].split("\t")
            # print(입력자료열수)
            # print(출력인덱스,i2)
            출력용데이터 = 출력용데이터 + 출력자료[출력인덱스] + "\r\n"
        for i in range(0,len(입력자료)):
            출력인덱스 = 실제위치 - 2
            출력자료 = 입력자료[i].split("\t")
            # print(입력자료열수)
            # print(출력인덱스,i2)
            출력용데이터 = 출력용데이터 + 출력자료[출력인덱스] + "\r\n"
        for i in range(0,len(입력자료)):
            출력인덱스 = 실제위치 - 3
            출력자료 = 입력자료[i].split("\t")
            # print(입력자료열수)
            # print(출력인덱스,i2)
            출력용데이터 = 출력용데이터 + 출력자료[출력인덱스] + "\r\n"
        for i in range(0,len(입력자료)):
            출력인덱스 = 실제위치 - 4
            출력자료 = 입력자료[i].split("\t")
            # print(입력자료열수)
            # print(출력인덱스,i2)
            출력용데이터 = 출력용데이터 + 출력자료[출력인덱스] + "\r\n"


    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def CHINMIF():
    global CHINMIF_list
    global CHINMIFDATA
    CHINMIF_list = list()
    CHINMIFDATA = clipboard.paste()
    CHINMIFDATA = CHINMIFDATA.split("\r\n")
    CHINMIFDATA.pop()
    for i in CHINMIFDATA:
        CHINMIFi = i.split("\t")
        CHINMIF_list.append(CHINMIFi[0])
    # print(CHINMIF_list)
    msgbox.showinfo("CH_LIST 입력.","입력성공!")    

def CHINMIF_MIF(): 
    global CHINMIF_MIF_list
    global CHINMIF_MIFDATA
    CHINMIF_MIF_list = list()   
    CHINMIF_MIFDATA = clipboard.paste()
    CHINMIF_MIFDATA = CHINMIF_MIFDATA.split("\r\n")
    CHINMIF_MIFDATA.pop()
    for i in CHINMIF_MIFDATA:
        CHINMIFi = i.split("\t")
        CHINMIF_MIF_list.append(CHINMIFi[0])
    # print(CHINMIF_MIF_list)
    msgbox.showinfo("MIF_LIST 입력.","입력성공!")    

def CHINMIF_MERGE():
    global CHINMIF_MIF_list
    global CHINMIF_MIFDATA
    global CHINMIFDATA
    global CHINMIF_list

    출력용데이터 = ""
    
    for i in range(0,len(CHINMIF_MIF_list)):
        datain = 0
        for i2 in range(0,len(CHINMIF_list)):
            if CHINMIF_MIF_list[i] == CHINMIF_list[i2]:
                출력용데이터 = 출력용데이터 + CHINMIF_MIFDATA[i] + "\t" + "\t" + CHINMIFDATA[i2] + "\r\n" 
                datain = 1
                break
        if datain == 0:
            출력용데이터 = 출력용데이터 + CHINMIF_MIFDATA[i] + "\t" + "NONE" + "\r\n"

    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")

def netlistdown():
    출력용데이터 = ""
    netlist = clipboard.paste()
    netlist = netlist.split("\r\n")
    netlist.pop()

    for i in range(0,len(netlist)):
        netlistdata = netlist[i].split("\t")
        netlistindex = netlistdata[-1].split(",")
        if len(netlistindex) > 1 :
            for i in netlistindex :
                for i2 in range(0,len(netlistdata)-1):
                    출력용데이터 = 출력용데이터 + netlistdata[i2] + "\t"
                출력용데이터 = 출력용데이터 + i + "\r\n" 
        else :
            출력용데이터 = 출력용데이터 + netlist[i] + "\r\n"
    clipboard.copy(출력용데이터)
    msgbox.showinfo("붙여넣기 하세요.","붙여넣기 하세요!")


def examine2(): # CAM DATA LIST 출력기
    searchdata = clipboard.paste()
    searchdata2 = list() # 리스트화 시킨 채널 정보
    searchdata3 = list() # 데이터 묶음용 버퍼
    # searchdata = searchdata.replace("-","/") #특수문자 및 스페이스바 제거
            # while True :
            #     cutdatas = searchdata.find(" (")
            #     if cutdatas > -1 :
            #         cutdatae = searchdata.find(")")                    
            #         searchdata = searchdata.replace(searchdata[cutdatas:cutdatae+1],"")
            #     else :
            #         break
    searchdata = searchdata[searchdata.find("% SIGNALS\r\n")+11:].split("\r\n")
    
    for i in range(0,len(searchdata)):
        if not searchdata[i] == "":
            if not searchdata[i][-1] == ",":
                searchdata[i] = searchdata3 + searchdata[i].replace(" (","(").replace("        ","").replace(" ","☆").split(",")    
                searchdata2.append(searchdata[i]) #searchdata2 Pcad 데이터
                searchdata3 = []

            else:
                searchdata3 = searchdata3 + searchdata[i][0:-1].replace(" (","(").replace("        ","").replace(" ","☆").split(",")
  
    원본데이터 = searchdata2
    검색용데이터 = criteriadata2

    searchdatalist = []
    countnum = 0
    copydata = ""

    for i in range(0,len(검색용데이터)):
        searchdatalist.append(검색용데이터[i][0])

    for i in range(0,len(원본데이터)):
        # if searchdatalist.count(원본데이터[i][0]) == 1:
        #     searchdatindex = searchdatalist.index(원본데이터[i][0])
        #     for i2 in 원본데이터[i]:
        #         countnum = countnum + 검색용데이터[searchdatindex].count(i2)
        #     # print(countnum,len(원본데이터[i]),len(검색용데이터[searchdatindex]))

        #     if countnum == 검색용데이터[searchdatindex]:
        #         copydata = copydata + str(원본데이터[i]) + "\tO\t{}\r\n".format(len(원본데이터[i]))
        #         countnum = 0
        #     else :
        #         i4 = 0
        #         if len(str(원본데이터[i])) > 30000 :
        #             print(len(str(원본데이터[i])))
        #             for i3 in range(0,len(원본데이터[i])) :
        #                 if i4 >500 :
        #                     copydata = copydata + str(원본데이터[i][i3]) + "\tX\t{}\r\n".format(len(원본데이터[i])) + str(원본데이터[i][0]) + "\t"
        #                     i4 = 0
        #                     print(str(원본데이터[i][i3]),str(원본데이터[i][0]))
        #                 else :
        #                     copydata = copydata + str(원본데이터[i][i3])
        #                     countnum = 0
        #                 i4 = i4 + 1
        #         else :
        #             copydata = copydata + str(원본데이터[i]) + "\tX\t{}\r\n".format(len(원본데이터[i]))
        #             countnum = 0
        # else:
            if len(str(원본데이터[i])) > 30000 :
                print(str(원본데이터[i][0]))
                i4 = 0
                for i3 in range(0,len(원본데이터[i])) :
                    if i4 >500 :
                        copydata = copydata + str(원본데이터[i][i3]) + "\tX\t{}\r\n".format(len(원본데이터[i])) + str(원본데이터[i][0])[:str(원본데이터[i][0]).find("☆")+1].replace("☆","\t")
                        i4 = 0
                        print(str(원본데이터[i][i3]),str(원본데이터[i][0]))
                    else :
                        if i3 == len(원본데이터[i]) -1 :
                            copydata = copydata + str(원본데이터[i][i3]) + "\tX\t{}\r\n".format(len(원본데이터[i]))
                        else :
                            copydata = copydata + str(원본데이터[i][i3]) 
                    i4 = i4 + 1
            else :
                copydata = copydata + str(원본데이터[i]) + "\tX\t{}\r\n".format(len(원본데이터[i]))

    clipboard.copy(copydata.replace("[","").replace("]","").replace("'","").replace("☆","\t").replace(", ",","))

    msgbox.showinfo("net 데이터 출력", "출력 완료 붙여넣기 하세요.")

def ORCADDATALIST():
    global criteriadata
    global searchdata
    global criteriadata2
    global searchdata2


    criteriadata2 = list() # 리스트화 시킨 채널 정보
    criteriadatai3 = list() # 데이터 묶음용 버퍼
    criteriadata = clipboard.paste()
    criteriadatacut = criteriadata.find("NETS\r\n") + 8
    criteriadata = criteriadata[criteriadatacut: ]
    criteriadata = criteriadata.replace(" = ","").replace("            ","").split("\r\n")
    for i in range(0,len(criteriadata)):
        criteriadatai = criteriadata[i].split(" ")
        if criteriadatai[-1] == ";":
            criteriadatai = criteriadatai3 + criteriadatai[0:-1]
            criteriadata2.append(criteriadatai) #criteriadata2 Pcad 데이터
            criteriadatai3 = []
        else:
            criteriadatai3 = criteriadatai3 + criteriadatai
    outdata = ""
    for i2 in criteriadata2:

        # for i3 in range(0,len(i2)) :
        #     if i3 == len(i2)-1 :
        #         outdata = outdata + i2[i3]
        #     elif i3 == 0 :
        #         outdata = outdata + i2[i3] + "\t"
        #         print(i3) 
        #     else: 
        #         outdata = outdata + i2[i3] + ","
        # outdata = outdata + "\t" + str(len(i2)) + "\r\n"

        divnum = 1000
        for i3 in range(0,len(i2)) :
            if divnum == i3:
                divnum = divnum + 1000
                outdata = outdata + "\t" + str(len(i2)) + "\r\n" + i2[0] + "\t"
            if i3 == len(i2)-1 :
                outdata = outdata + i2[i3]
            elif i3 == 0 :
                outdata = outdata + i2[i3] + "\t"
            elif divnum == i3 + 1 :
                outdata = outdata + i2[i3]
            else: 
                outdata = outdata + i2[i3] + ","
                        


        outdata = outdata + "\t" + str(len(i2)) + "\r\n"


    clipboard.copy(outdata)
    msgbox.showinfo("데이터 출력", "출력 완료 붙여넣기 하세요.")


def arc_scr(): # 출력 설정시 /r/n으로 하면 두번 엔터 눌러짐 /n으로 변경
    home_directory = os.getenv('USERPROFILE')

    desktop_path = os.path.join(home_directory,"desktop")

    autocad_t5 = os.path.join(desktop_path,"AUTOCAD_T5")

    txtout = os.path.join(autocad_t5,"t5data.scr")

    if not os.path.isdir(autocad_t5):
        os.mkdir(autocad_t5)

    outdata = ""
    arc_data = clipboard.paste()
    arc_data_list = arc_data.split("\r\n")
    arc_data_list.pop()
    arc_size = globals()['3frame_et{}'.format(button_list3.index(arc_scr))].get()
    for i in arc_data_list :
        outdata = outdata + "circle\n" + i.replace("\t",",") + "\n" + arc_size + "\n"
 
    # clipboard.copy(outdata)
    file = open(txtout, 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(outdata)      # 파일에 문자열 저장
    file.close()
    msgbox.showinfo("데이터 출력", "출력 완료")
    os.startfile(os.path.dirname(txtout))

def text_scr(): # 출력 설정시 /r/n으로 하면 두번 엔터 눌러짐 /n으로 변경

    home_directory = os.getenv('USERPROFILE')

    desktop_path = os.path.join(home_directory,"desktop")

    autocad_t5 = os.path.join(desktop_path,"AUTOCAD_T5")

    txtout = os.path.join(autocad_t5,"t5data.scr")

    if not os.path.isdir(autocad_t5):
        os.mkdir(autocad_t5)

    outdata = ""
    arc_data_list = list()
    text_data_list = list()
    data = clipboard.paste()
    data_list = data.split("\r\n")
    data_list.pop()
    for data in data_list:
        data_list = data.split("\t")
        if len(data_list) == 3:
            arc_data_list.append([data_list[0],data_list[1]])
            text_data_list.append(data_list[2])
        if len(data_list) == 4:
            arc_data_list.append([data_list[0],data_list[1]])
            text_data_list.append(data_list[2]+"\r"+data_list[3])
    # arc_size = globals()['3frame_et{}'.format(button_list3.index(arc_scr))].get()
    test_size = globals()['3frame_et{}'.format(button_list3.index(text_scr))].get()
    # for i in range(0,len(arc_data_list)) :
    #     outdata = outdata + "circle\n" + arc_data_list[i][0] + "," + arc_data_list[i][1] + "\n" + arc_size + "\n" 


    for i in range(0,len(arc_data_list)) :
        arc_data = arc_data_list[i][0] + "," + arc_data_list[i][1]
        outdata = outdata + "-mtext\n" + arc_data + "\n" + "j\nmc\nh\n" + test_size + "\n" + arc_data + "\n"+ text_data_list[i] +"\n\n"


    # clipboard.copy(outdata) 
    file = open(txtout, 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(outdata)      # 파일에 문자열 저장
    file.close()
    msgbox.showinfo("데이터 출력", "출력 완료")
    os.startfile(os.path.dirname(txtout))

def arc_text_scr(): # 출력 설정시 /r/n으로 하면 두번 엔터 눌러짐 /n으로 변경

    home_directory = os.getenv('USERPROFILE')

    desktop_path = os.path.join(home_directory,"desktop")

    autocad_t5 = os.path.join(desktop_path,"AUTOCAD_T5")

    txtout = os.path.join(autocad_t5,"t5data.scr")

    if not os.path.isdir(autocad_t5):
        os.mkdir(autocad_t5)

    outdata = ""
    arc_data_list = list()
    text_data_list = list()
    data = clipboard.paste()
    data_list = data.split("\r\n")
    data_list.pop()
    for data in data_list:
        data_list = data.split("\t")
        if len(data_list) == 3:
            arc_data_list.append([data_list[0],data_list[1]])
            text_data_list.append(data_list[2])
        if len(data_list) == 4:
            arc_data_list.append([data_list[0],data_list[1]])
            text_data_list.append(data_list[2]+"\r"+data_list[3])

    arc_size = globals()['3frame_et{}'.format(button_list3.index(arc_scr))].get()
    test_size = globals()['3frame_et{}'.format(button_list3.index(text_scr))].get()
    for i in range(0,len(arc_data_list)) :
        outdata = outdata + "circle\n" + arc_data_list[i][0] + "," + arc_data_list[i][1] + "\n" + arc_size + "\n" 


    for i in range(0,len(arc_data_list)) :
        arc_data = arc_data_list[i][0] + "," + arc_data_list[i][1]
        outdata = outdata + "-mtext\n" + arc_data + "\n" + "j\nmc\nh\n" + test_size + "\n" + arc_data + "\n"+ text_data_list[i] +"\n\n"


    # clipboard.copy(outdata) 
    file = open(txtout, 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(outdata)      # 파일에 문자열 저장
    file.close()
    msgbox.showinfo("데이터 출력", "출력 완료")
    os.startfile(os.path.dirname(txtout))

    # 글로벌 변수 선언

def uflexddplus():

    home_directory = os.getenv('USERPROFILE')

    desktop_path = os.path.join(home_directory,"desktop")

    UFLEXDDPLUS = os.path.join(desktop_path,"UFLEXDDPLUS")

    txtout = os.path.join(UFLEXDDPLUS,"UFLEXDDPLUSALLDATA.txt")

    if not os.path.isdir(UFLEXDDPLUS):
        os.mkdir(UFLEXDDPLUS)
    os.startfile(os.path.dirname(txtout))
    data = clipboard.paste()
    data = data.split("\r\n")
    data.pop()


    행인덱스list = []
    증가량 = 0
    블럭간격list = [1,93,185,277]
    outputdata = ""

    for i in range(0,32):
        행인덱스list.append(3+i*10)

    for 행인덱스 in 행인덱스list:
        블럭정보 = data[행인덱스].split("\t")
        핀번호 = data[행인덱스+1].split("\t")
        작업데이터A = data[행인덱스+2].split("\t")
        작업데이터B = data[행인덱스+3].split("\t")
        작업데이터C = data[행인덱스+4].split("\t")
        작업데이터D = data[행인덱스+5].split("\t")
        작업데이터E = data[행인덱스+6].split("\t")
        작업데이터F = data[행인덱스+7].split("\t")
        작업데이터G = data[행인덱스+8].split("\t")

        for 블럭간격 in 블럭간격list:
            for 증가량 in range(0,87):
                if not 작업데이터A[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터A[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터A[4+증가량+블럭간격] + "\r"
                if not 작업데이터B[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터B[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터B[4+증가량+블럭간격] + "\r"
                if not 작업데이터C[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터C[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터C[4+증가량+블럭간격] + "\r"
                if not 작업데이터D[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터D[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터D[4+증가량+블럭간격] + "\r"
                if not 작업데이터E[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터E[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터E[4+증가량+블럭간격] + "\r"
                if not 작업데이터F[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터F[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터F[4+증가량+블럭간격] + "\r"
                if not 작업데이터G[4+증가량+블럭간격] == "":
                    outputdata = outputdata + 블럭정보[블럭간격] + "§" + 작업데이터A[2+블럭간격] + "§" + 블럭정보[4+증가량+블럭간격] + "§" + str(작업데이터G[3+블럭간격]) + str(블럭정보[4+증가량+블럭간격][0] + 핀번호[4+증가량+블럭간격]) + "§" + 작업데이터G[4+증가량+블럭간격] + "\r"

    file = open(txtout, 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(outputdata)      # 파일에 문자열 저장
    file.close()    
    msgbox.showinfo("데이터 출력", "출력 완료")

def netlistinput() :
    global netlistdata
    data = clipboard.paste()
    data_list = data.split(";")
    netlistdata = data_list
    msgbox.showinfo("NETLIST 입력", "NETLIST 입력 완료")
    ORCADDATALIST()

def netlistoutput() :
    global netlistdata
    outdata = "" 
    data_list = netlistdata
    data = clipboard.paste()
    listindex = data.split("\r\n")
    listindex.pop()
    irootin = 0
    # print(listindex)
    for i in listindex :
        # print(i)
        irootin = irootin + 1
        lastdata = len(listindex)
        if irootin == lastdata :
            outdata = outdata + data_list[int(i)-1] + ";\r\n"
        else :
            outdata = outdata + data_list[int(i)-1] + ";"
 
    clipboard.copy(outdata)
    msgbox.showinfo("NETLIST 출력 완료 \r붙여넣기 하세요", "완료")

def netdata_pf_net():
    global netinputdata
    netinputdata = clipboard.paste()
    listindex = netinputdata.split("\r\n")
    listindex.pop()

    for i in range(0,len(listindex)):
        if "NET" in listindex[i] :
            netpoint = i 

    

def globalsdata():
    global button_list
    global button_list2
    global 좌우리스트

def text_scrX():
    data = clipboard.paste()
    print(data)
    data = data.replace("\r\n","")
    print(data)
    clipboard.copy(data)

def PCAD_PAD():
    file_path = filedialog.askopenfilename(filetypes=[("DXF files", "*.dxf")])

    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        circles = msp.query('CIRCLE')
        cdata = []
        for circle in circles:
            center = circle.dxf.center
            diameter = round(circle.dxf.radius * 2,4)
            cdata.append([center[0], center[1], diameter])
    else:
        print("No file selected.")


    with open('PCADPAD기본데이터.TXT', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    # clipboard_data = pyperclip.paste()
    # clip_data = [line.split('\t') for line in clipboard_data.split('\n') if line.strip()]
    # result = [[float(x), float(y), float(diameter)] for x, y, diameter in clip_data]
    result = cdata

    # '(PADDATA)' 항목의 인덱스 찾기
    index = data.index('    (PADDATA)')
    for x, y, diameter in result:
        pad_data = (f'    (pad (padNum 0) (padStyleRef "{diameter}") (pt {x} {y}) )')
        data[index+1:index+1] = [pad_data]

    data.remove('    (PADDATA)')

    # '(PADLIST DATA)' 항목의 인덱스 찾기
    index = data.index('  (PADLIST DATA)')

    # '(PADLIST DATA)' 항목 이후에 내가 추가하고자 하는 텍스트 삽입
    diameter_list = list(set([d for _, _, d in result]))
    for diameter in diameter_list:
        pad_list = (f'  (padStyleDef "{diameter}"\n    (holeDiam 0.1)\n    (StartRange 1)\n    (EndRange 2)\n    (padShape (layerNumRef 1) (padShapeType Ellipse) (shapeWidth {diameter}) (shapeHeight {diameter}) )\n    (padShape (layerNumRef 2) (padShapeType Ellipse) (shapeWidth 1.524) (shapeHeight 1.524) )\n    (padShape (layerType Signal) (padShapeType Ellipse) (shapeWidth 1.524) (shapeHeight 1.524) )\n    (padShape (layerType Plane) (padShapeType Thrm4_45) (outsideDiam 2.1336) (insideDiam 1.524) (spokeWidth 0.381) )\n    (padShape (layerType NonSignal) (padShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) )\n  )')
        data[index+1:index+1] = [pad_list]
    data.remove('  (PADLIST DATA)')

    # 사용자 바탕화면 경로 가져오기
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # PCBDXF 폴더 생성
    folder_path = os.path.join(desktop_path, "PCBDXF")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # 파일 경로 생성
    file_path = os.path.join(folder_path, "output.pcb")

    # 폴더 열기
    os.startfile(os.path.dirname(file_path))

    # 파일 저장
    with open(file_path, 'w') as f:
        for item in data:
            f.write("%s\n" % item)

# DXF에서 TEXT 및 MTEXT 데이터 추출
def extract_text_with_coordinates(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    text_entities = msp.query('TEXT')
    mtext_entities = msp.query('MTEXT')
    texts = text_entities + mtext_entities
    data = []
    for text in texts:
        if text.dxftype() == 'TEXT':
            location = text.dxf.insert
            x, y, z = location.x, location.y, location.z
            data.append({'text': text.dxf.text, 'x': x, 'y': y, 'z': z})
        elif text.dxftype() == 'MTEXT':
            location = text.dxf.insert
            x, y, z = location.x, location.y, location.z
            data.append({'text': text.plain_text(), 'x': x, 'y': y, 'z': z})
    return data


def save_text_coordinates_to_file(data, file_path):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(f"{item['x']},{item['y']}")
            f.write(f",{item['text']}\n")

def DXF_TEXT():
    file_path = filedialog.askopenfilename(filetypes=[("DXF files", "*.dxf")])

    if file_path:
        data = extract_text_with_coordinates(file_path)

        # 사용자 바탕화면 경로 가져오기
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # DXFTEXT 폴더 생성
        folder_path = os.path.join(desktop_path, "DXFTEXT")
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # 파일 경로 생성
        file_path = os.path.join(folder_path, "DXFTEXT.TXT")

        # 텍스트와 좌표 저장
        save_text_coordinates_to_file(data, file_path)

        # 폴더 열기
        os.startfile(os.path.dirname(file_path))

        print(f"텍스트와 좌표가 {file_path} 파일에 저장되었습니다.")
    else:
        print("No file selected.")
# DXF에서 TEXT 및 MTEXT 데이터 추출


#변수 선언
좌우리스트 = list()    
기준데이터 = list()
변환용데이터 = list()
서브자료저장 = list()
CHINMIF_list = list()
CHINMIF_MIF_list = list()
CHINMIF_MIFDATA = list()
CHINMIFDATA = list()
criteriadata = ""
searchdata = ""
searchdata2 = ""
criteriadata2 = ""
netinputdata = ""

root = Tk()
root.title("엑셀 & 클립보드 추출 변환기 2")
root.geometry("1200x1000")
root.wm_attributes("-topmost",1)
root.resizable(False, False)

# 첫번째 행 자료들
relyi = list()
relheight_list = list()
columns_list = list()
button_list = list()
entrynot = list()

# 1-1
columns_list.append("빈칸 위에 자료를 자동으로 채우기")
button_list.append(copyfromup)
# entrynot.append(len(columns_list)-1)
# 1-2
columns_list.append("숫자 문자 분리후 앞쪽 숫자 0없애고 탭으로 나누기")
button_list.append(numdivtapaplahs)
# entrynot.append(len(columns_list)-1)
# 1-3
columns_list.append("숫자 문자 분리후 숫자앞자리 하나 없애고 0없애기")
button_list.append(numdivalpha)
# entrynot.append(len(columns_list)-1)
# 1-4
columns_list.append("4.숫자 문자 분리후 자리수 맞추기")
button_list.append(numdivalphaszifll)
entrynot.append(len(columns_list)-1)
# 1-4
columns_list.append("문자 포함 자리수 맞추기\r4,5,6 해당됨")
button_list.append(numdivalphasziflltext)
entrynot.append(len(columns_list)-1)
# 1-14
columns_list.append("5.문자 숫자 조합중 앞부분 숫자를\r 원하는 만큼 자릿수 맞춤")
button_list.append(numdivalphaszifllfirst2)
entrynot.append(len(columns_list)-1)
# 1-15
columns_list.append("6.문자 숫자 조합중 뒷부분 숫자를\r 원하는 만큼 자릿수 맞춤")
button_list.append(numdivalphaszifllfirst)
entrynot.append(len(columns_list)-1)
# 1-5
columns_list.append("행 순서대로 합치기\r구분기호 입력 (Concatenate)")
button_list.append(concatennate)
entrynot.append(len(columns_list)-1)
# 1-13
columns_list.append("마지막 열 기준 ','구분하여 1줄로 만들기")
button_list.append(netlistdown)
# entrynot.append(len(columns_list)-1)
# 1-15
columns_list.append("1열기준 동일 이름이 있으면 2열을 취합해줌")
button_list.append(meargdata1_2)
# entrynot.append(len(columns_list)-1)
# 1-6
columns_list.append("일정 간격으로 자료 사이에 line 추가 하기")
button_list.append(datalineaddfromnum)
entrynot.append(len(columns_list)-1)
# 1-7
columns_list.append("자료를 설정된 숫자 만큼 열에 맞춰 변경")
button_list.append(datarote)
entrynot.append(len(columns_list)-1)
# 1-8
columns_list.append("자료를 설정된 숫자만큼 행에 맞춰 변경")
button_list.append(datacellonerow)
entrynot.append(len(columns_list)-1)
# 1-9
columns_list.append("빈셀 없애고 한줄로 만들기")
button_list.append(datacelloneline)
# entrynot.append(len(columns_list)-1)
# 1-10
columns_list.append("데이터 좌우 뒤집기")
button_list.append(datarowsort)
# entrynot.append(len(columns_list)-1)
# 1-11
columns_list.append("데이터 상하 뒤집기")
button_list.append(datacolsort)
# entrynot.append(len(columns_list)-1)



# columns_list = ["빈칸 위에 자료를 카피","숫자 문자 분리후 앞쪽 숫자 0없애고 탭으로 나누기","숫자 문자 분리후 숫자앞자리 하나 없애고 0없애기","숫자 문자 분리후 자리수 맞추기"
#                  ,"행 순서대로 합치기 (Concatenate)","일정 간격으로 자료 사이에 line 추가 하기","자료를 설정된 숫자 만큼 행으로 변경","자료를 설정된 숫자만큼 열로 변경","빈셀 없애고 한줄로 만들기"
#                  ,"데이터 좌우 뒤집기","데이터 상하 뒤집기","1DCBA 5줄기준 ABCD(번호는삭제됨) 한줄 정렬 (ZIF용)","마지막 열 기준 ','구분하여 1줄로 만들기","문자 숫자 조합중 앞부분 숫자를 원하는 만큼 자릿수 맞춤"
#                  ,"1열기준 동일 이름이 있으면 2열을 취합해줌"]
# button_list = [copyfromup,numdivtapaplahs,numdivalpha,numdivalphaszifll,concatennate,datalineaddfromnum,datarote,datacellonerow,datacelloneline,datarowsort,datacolsort,DCBA한줄정렬,netlistdown,numdivalphaszifllfirst,meargdata1_2]
# entrynot = [3,5,6,7,13]
for i in range(0,len(columns_list)):
    relydiv = (1-0.01)/(len(columns_list))
    i2 = (i * relydiv)+ 0.01
    relyi.append(i2)
    relheight_list.append(relydiv-0.01)

for i in range(0,len(columns_list)):
    globals()['frame_db{}'.format(i)] = tk.LabelFrame(root, padx=5, pady=5, width=12)
    globals()['frame_db{}'.format(i)].place(relx=0.01,rely=relyi[i],relwidth=0.32,relheight=relheight_list[i])
    globals()['frame_lb{}'.format(i)] = tk.Label(globals()['frame_db{}'.format(i)],borderwidth = 3,text=(columns_list[i]))
    globals()['frame_lb{}'.format(i)].place(relx=0.01,rely=0.01,relwidth=0.78,relheight=0.98)
    if i in entrynot :
        globals()['frame_et{}'.format(i)] = Entry(globals()['frame_db{}'.format(i)])
        globals()['frame_et{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['frame_bt{}'.format(i)] = Button(globals()['frame_db{}'.format(i)],text="변환",command=button_list[i])
        globals()['frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.18,relheight=0.48)
    
    else:
        globals()['frame_bt{}'.format(i)] = Button(globals()['frame_db{}'.format(i)],text="변환",command=button_list[i])
        globals()['frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.98)


# 두번째 행 자료들
columns_list2 = list()
button_list2 = list()
button_list2_2 = list()
button_list2_3 = list()
text_list2 =  list()
text_list2_2 = list()
text_list2_3 = list()
entrynot2 = list()
button2 = list()
button3 = list()


# 2-1
columns_list2.append("좌표 변환 POGO 및 PIN (CAM DATA)")
button_list2.append(coordinates)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("변환")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)
# 2-7
columns_list2.append("좌표 데이터 자료 매칭\n좌표 변환자료 바로 이용")
button_list2.append(marge      )
button_list2_2.append(Criteria1_1)
button_list2_3.append(Criteria1_2)
text_list2.append("합치기")
text_list2_2.append("기준")
text_list2_3.append("좌표")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
button3.append(len(columns_list2)-1)
# 2-8
columns_list2.append("CAM NET 자료를 기준 자료에 맞춰 찾기\nNET에 CAM NET 입력")
button_list2.append(netmarge)
button_list2_2.append(Criteria1_1)
button_list2_3.append(Criteria2)
text_list2.append("합치기")
text_list2_2.append("기준")
text_list2_3.append("net")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
button3.append(len(columns_list2)-1)
# 2-14
columns_list2.append("CAM 데이터를 LIST로 출력\r(net버튼으로 입력, NET 부터 복사)")
button_list2.append(examine2)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("출력")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)
# 2-15
columns_list2.append("ORCADDATALIST변환 출력\r(데이터 카피 후 버튼 클릭)")
button_list2.append(ORCADDATALIST)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("출력")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)





# 2-2
columns_list2.append("목차 시작부분 BLOCKNAME§ \r 위 기준사양으로 BLOCKNAME + 행 + 열 + 데이터\r 마지막에 § 표시 꼭 해야함 ")
button_list2.append(p_transdata2)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("변환")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)

# 1-9
columns_list2.append("빈셀 없애고 한줄로 만들기")
button_list2.append(datacelloneline)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("변환")
text_list2_2.append("")
text_list2_3.append("")


# entrynot.append(len(columns_list)-1)


# 2-4
columns_list2.append("변환자료의 1열 기준 검색 2열 데이터로 변경\n기준데이터 1열입력")
button_list2.append(변환용데이터입력)
button_list2_2.append(기준데이터입력  )
button_list2_3.append(데이터변환      )
text_list2.append("변환 자료")
text_list2_2.append("기준")
text_list2_3.append("출력")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
button3.append(len(columns_list2)-1)
# 2-5
columns_list2.append("변환자료의 1열 기준 검색 2열 데이터로 변경\n기준데이터 1열입력 (일치하지 않으면 공백)")
button_list2.append(데이터변환삭제)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("삭제 출력")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)

# 2-10
columns_list2.append("동일한 자료가 있으면 해당 자료를 1개씩만 출력")
button_list2.append(멀티플채널검색)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("정리")
text_list2_2.append("")
text_list2_3.append("")
# entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)
# 2-11
columns_list2.append("해당문자를 포함한 자료만 남기기\r (대/소문자 구분)")
button_list2.append(문자포함자료만찾기)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("찾기")
text_list2_2.append("")
text_list2_3.append("")
entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)
# 2-12
columns_list2.append("해당문자를 포함 하지 않는 자료만 남기기\r(대/소문자 구분)")
button_list2.append(문자포함자료만제거)
button_list2_2.append("")
button_list2_3.append("")
text_list2.append("제거")
text_list2_2.append("")
text_list2_3.append("")
entrynot2.append(len(columns_list2)-1)
# button2.append(len(columns_list2)-1)
# button3.append(len(columns_list2)-1)





# columns_list2 = ["좌표 변환 POGO 및 PIN (CAM DATA)","블럭 이름(입력) + 목차 행 , 열  자료 병합","리스트 만큼 내용 추가 반복 출력","변환자료의 1열 기준 검색 2열 데이터로 변경\n기준데이터 1열입력"
#                  ,"변환자료의 1열 기준 검색 2열 데이터로 변경\n기준데이터 1열입력 (일치하지 않으면 공백)"   
#                  ,"기존자료 기준 서브 자료에 있는 데이터를 합쳐줌","좌표 데이터 자료 매칭\n좌표 변환자료 바로 이용","CAM NET 자료를 기준 자료에 맞춰 찾기\nNET에 CAM NET 입력",
#                  "1열 기준 2열 자료중 제일 아래 있는 자료로 변경","동일한 자료가 있으면 해당 자료를 1개씩만 출력","해당문자를 포함한 자료만 남기기 (대/소문자 구문)","해당문자를 포함 하지 않는 자료만 남기기 (대/소문자 구문)",
#                  "MIF 1열기준 CH 1열에 동일 자료가 있으면\r MIF,CH 연속 출력 - 없으면 NONE","CAM 데이터를 LIST로 출력\r(net버튼으로 입력)"]
# button_list2 =   [coordinates,p_transdata2,내용추가리스트,변환용데이터입력,데이터변환삭제,  서브자료저장버튼    ,marge      ,netmarge,채널정리,멀티플채널검색,문자포함자료만찾기,
#                 문자포함자료만제거,CHINMIF_MERGE,examine2]
# button_list2_2 = ["         ","          ",앞쪽내용추가  ,기준데이터입력  ,"           ",기준자료에서브자료매칭,Criteria1_1,Criteria1_1,"   ","          ","              ",
#                 "   ",CHINMIF]
# button_list2_3 = ["         ","          ",뒤쪽내용추가  ,데이터변환      ,"           ","                  ",Criteria1_2,Criteria2,"     ","          ","              ",
#                 "   ",CHINMIF_MIF,""]

# text_list2 =  ["변환","변환"    ,"리스트 입력","변환 자료","삭제 출력","서브저장"  ,"합치기","합치기","변경","정리","찾기","제거","MERGE","출력"]
# text_list2_2 = [""  ,""        ,"앞"        ,"기준"     ,"   "     ,"자료매칭"  ,"기준","기준","        ","   ","","","CH",""]
# text_list2_3 = [""  ,""        ,"뒤"        ,"출력"     ,"   "     ,""         ,"좌표","net","         ","   ","","","MIF",""]

# entrynot2 = [1,10,11]
# button2 = [5]
# button3 = [2,3,6,7,12]



# 높이 초기화
relyi = list()
relheight_list = list()

for i in range(0,len(columns_list2)):
    relydiv = (1-0.01)/(len(columns_list2))
    i2 = (i * relydiv)+ 0.01
    relyi.append(i2)
    relheight_list.append(relydiv-0.01)



for i in range(0,len(columns_list2)):
    globals()['2frame_db{}'.format(i)] = tk.LabelFrame(root, padx=5, pady=5, width=12)
    globals()['2frame_db{}'.format(i)].place(relx=0.33,rely=relyi[i],relwidth=0.32,relheight=relheight_list[i])
    globals()['2frame_lb{}'.format(i)] = tk.Label(globals()['2frame_db{}'.format(i)],borderwidth = 3,text=(columns_list2[i]))
    globals()['2frame_lb{}'.format(i)].place(relx=0.01,rely=0.01,relwidth=0.78,relheight=0.98)
    
    if i in entrynot2 :
        globals()['2frame_et{}'.format(i)] = Entry(globals()['2frame_db{}'.format(i)])
        globals()['2frame_et{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2[i]),command=button_list2[i])
        globals()['2frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.18,relheight=0.48)
    elif i in button2 :
        globals()['2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2[i]),command=button_list2[i])
        globals()['2frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['2_2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2_2[i]),command=button_list2_2[i])
        globals()['2_2frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.18,relheight=0.48)
        
    elif i in button3 :
        globals()['2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2[i]),command=button_list2[i])
        globals()['2frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['2_2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2_2[i]),command=button_list2_2[i])
        globals()['2_2frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.08,relheight=0.48)
        globals()['2_3frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2_3[i]),command=button_list2_3[i])
        globals()['2_3frame_bt{}'.format(i)].place(relx=0.91,rely=0.51,relwidth=0.08,relheight=0.48)

    else:
        globals()['2frame_bt{}'.format(i)] = Button(globals()['2frame_db{}'.format(i)],text="{}".format(text_list2[i]),command=button_list2[i])
        globals()['2frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.98)

# 세번째 행 자료들
columns_list3 = list()
button_list3 = list()
button_list3_2 = list()
button_list3_3 = list()
text_list3 = list()
text_list3_2 = list()
text_list3_3 = list()
entrynot2 = list()
button2 = list()
button3 = list()


# 3-1
columns_list3.append("cad ARC 작성 !!새문서에서 조작없는 상태로!!\r엑셀의 xy좌표를 입력 바탕화면에 AUTOCAD_T5 폴더\r t5data.scr")
button_list3.append(arc_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("ARC출력")
text_list3_2.append("")
text_list3_3.append("")
entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)

# 3-1
columns_list3.append("cad TEXT 작성 1,X 2,Y 3,TEXT \r위와 동일하게 사용하며 text행을 추가")
button_list3.append(text_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("TEXT출력")
text_list3_2.append("")
text_list3_3.append("")
entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
# 3-1
columns_list3.append("위 두가지를 한번에 진행")
button_list3.append(arc_text_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("ARCTEXT")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("UFLEXDDPLUS한방팩.XLS 파일이용하여\r모든데이터 한번에 1줄로 만들어서 출력")
button_list3.append(uflexddplus)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("MAP변환")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("5.ORCAD NET 아래 부분만 카피하여 가공\rCAM DATA출력후 열에 숫자 입력\r필요한데이터 인덱스로 만들어서 가공")
button_list3.append(netlistinput)
button_list3_2.append(netlistoutput)
button_list3_3.append("")
text_list3.append("NET입력")
text_list3_2.append("INDEX입력")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("5.번이랑 연동, NET기준 위 아래 자료 분리\rPF Profile, NET NET정보 출력")
button_list3.append(text_scrX)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("입력")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("DXF TO PCAD PAD 생성기")
button_list3.append(PCAD_PAD)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("생성")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("DXF 텍스트 추출기\rDXF파일을 선택 Mtext and Text 추출")
button_list3.append(DXF_TEXT)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("추출")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("예비")
button_list3.append(text_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("예비")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("예비")
button_list3.append(text_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("예비")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("예비")
button_list3.append(text_scr)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("예비")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)
columns_list3.append("block")
button_list3.append(block)
button_list3_2.append("")
button_list3_3.append("")
text_list3.append("block")
text_list3_2.append("")
text_list3_3.append("")
# entrynot2.append(len(columns_list3)-1)
# button2.append(len(columns_list3)-1)
# button3.append(len(columns_list3)-1)

# 높이 초기화
relyi = list()
relheight_list = list()

for i in range(0,len(columns_list3)):
    relydiv = (1-0.01)/(len(columns_list3))
    i2 = (i * relydiv)+ 0.01
    relyi.append(i2)
    relheight_list.append(relydiv-0.01)


for i in range(0,len(columns_list3)):
    globals()['3frame_db{}'.format(i)] = tk.LabelFrame(root, padx=5, pady=5, width=12)
    globals()['3frame_db{}'.format(i)].place(relx=0.66,rely=relyi[i],relwidth=0.32,relheight=relheight_list[i])
    globals()['3frame_lb{}'.format(i)] = tk.Label(globals()['3frame_db{}'.format(i)],borderwidth = 3,text=(columns_list3[i]))
    globals()['3frame_lb{}'.format(i)].place(relx=0.01,rely=0.01,relwidth=0.78,relheight=0.98)
    if i in entrynot2 :
        globals()['3frame_et{}'.format(i)] = Entry(globals()['3frame_db{}'.format(i)])
        globals()['3frame_et{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['3frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3[i]),command=button_list3[i])
        globals()['3frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.18,relheight=0.48)
    elif i in button2 :
        globals()['3frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3[i]),command=button_list3[i])
        globals()['3frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['3_2frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3_2[i]),command=button_list3_2[i])
        globals()['3_2frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.18,relheight=0.48)
    elif i in button3 :
        globals()['3frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3[i]),command=button_list3[i])
        globals()['3frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.48)
        globals()['3_2frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3_2[i]),command=button_list3_2[i])
        globals()['3_2frame_bt{}'.format(i)].place(relx=0.81,rely=0.51,relwidth=0.08,relheight=0.48)
        globals()['3_3frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3_3[i]),command=button_list3_3[i])
        globals()['3_3frame_bt{}'.format(i)].place(relx=0.91,rely=0.51,relwidth=0.08,relheight=0.48)

    else:
        globals()['3frame_bt{}'.format(i)] = Button(globals()['3frame_db{}'.format(i)],text="{}".format(text_list3[i]),command=button_list3[i])
        globals()['3frame_bt{}'.format(i)].place(relx=0.81,rely=0.01,relwidth=0.18,relheight=0.98)



root.mainloop()
