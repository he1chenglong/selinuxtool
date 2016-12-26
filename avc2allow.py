#-*-coding:utf-8-*-
import re
import sys
import os

# def writefile(filename = "D:\\uart-log\\zz001\\session-l.log"):
#     with open(filename,'w') as fp:



class analysisrule():
    def __init__(self):
        pass

    def parser(self,filename = "D:\\uart-log\\zz001\\session-l.log"):
        allows = []
        print(filename)
        fp = open(filename,'r')

        for line in fp:
            # 跳过 空行
            if line=='\r\n':
                break
            # print "read: " + line
            avc =  re.findall('avc(.*?)permissive',line)
            if avc:
                # print "read: " + line
                scontext = re.findall('scontext=u:r:(.*?):s0',line)
                # if scontext  :
                #     print scontext[0]

                tcontext = re.findall('tcontext=u:object_r:(.*?):s0',line)

                if tcontext:
                    tcontext = re.findall('tcontext=u:object_r:(.*?):s0',line)
                else:
                    tcontext = re.findall('tcontext=u:r:(.*?):s0',line)
                # if tcontext :
                #     print tcontext[0]

                tclass = re.findall('tclass=(.*?)permissive',line)
               # tclass = re.findall('tclass=(.*?)',line)
                # if tclass :
                #     print tclass[0]

                opra =  re.findall("denied(.*?)for",line)
                # if opra :
                #     print opra[0]

                if scontext and tcontext :
                    if scontext[0] == tcontext[0]:
                        tcontext[0] = 'self'

                all = scontext and  tcontext and tclass and opra
                if all:
                    rule = "allow "+scontext[0]+" "+tcontext[0]+":"+tclass[0]+opra[0].strip()+";"
                    # print rule
                    # 去除 重复的规则
                    if rule not in allows:
                        allows.append(rule)

        fp.close()

        # for info in allows:
        #     print info

        return allows

    def addrule(self,allows,basepath="W:\\temp_zz001_network\\android.host\\"):
        filebasename=basepath+"device\\qcom\\sepolicy\\common"
        sepolicy=basepath+"external\\sepolicy"

        for info in allows:
            print(info)
            # 根据 scontext 找到文件 名字
            namelist = info.split(" ")
            scontextname = namelist[1]
            # print(scontextname)
            tefile = scontextname+".te"
            # print tefile
            devicetefile = os.path.join(filebasename,tefile)
            # print tefileabs
            exttefile = os.path.join(sepolicy,tefile)

            # 搜素的字符串
            searchinfo =namelist[0]+" "+namelist[1]+" "+namelist[2]

            # 搜索下 看下是否有 这个规则了
            isexits = os.path.exists(devicetefile)
            if isexits:
                with open(devicetefile,'ab') as fp:
                    print(devicetefile)
                    # fp.write('\n')
                    # fp.write(info)
                    # fp.write('\n')
            else:
                isexits = os.path.exists(exttefile)
                if isexits:
                    with open(exttefile,'ab') as fp:
                        print(exttefile)
                        # fp.write('\n')
                        # fp.write(info)
                        # fp.write('\n')

            # isexits = os.path.exists(exttefile)
            # if isexits :
            #     with open(exttefile,'r') as dfp:
            #         if  searchinfo in dfp.read():
            #             replace =True
            #             filepath = exttefile
            #         else:
            #             replace = False
            #             filepath = devicetefile
            #
            # isexits = os.path.exists(devicetefile)
            # if isexits :
            #     with open(devicetefile,'r') as dfp:
            #         if  searchinfo in dfp.read():
            #             replace =True
            #             filepath = devicetefile
            #         else:
            #             replace = False
            #             filepath = devicetefile

            # modify(replace,filepath,info)


    def modify(self,replaceflag,filepath,info):
        if replaceflag:
                    # 搜素的字符串
            namelist = info.split(" ")
            searchinfo =namelist[0]+" "+namelist[1]+" "+namelist[2]
            with open(filepath,'r') as fp:
                for line in fp:
                    if searchinfo in line:
                        old = line
                        if  namelist[4] in line:
                            new=old
                            break
                        else:
                            new = line[0:-3] +" "+ namelist[4]+" " +"};"
                            print(new)
                            with open(filepath) as fp:
                                allcontent = fp.read()
                                contents=allcontent.replace(old,new)

            # with open(filepath,"w") as fp:
            #     fp.write(contents)

        else:
            with open(filepath,'a') as fp:
                 fp.write('\n')
                 fp.write(info)

if __name__ == "__main__":
    serules =[]
    if len(sys.argv) > 1 :
        serules=analysisrule.parser(sys.argv[1])
    else:
        serules=analysisrule.parser()

    for info in serules:
        print(info)

    # addrule(serules)
