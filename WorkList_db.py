import sqlite3
import sys
import datetime
import xlwt
import os
import re
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

db_con = "C:\\WorkList\\WorkList.db"  ########################## 경로 수정


class Singleton(type):  # Type을 상속받음
    __instances = {}  # 클래스의 인스턴스를 저장할 속성

    def __call__(cls, *args, **kwargs):  # 클래스로 인스턴스를 만들 때 호출되는 메서드
        if cls not in cls.__instances:  # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args, **kwargs)  # 생성하지 않았으면 인스턴스를 생성하여 해당 클래스 사전에 저장
            # print("인스턴스 생성 확인")
        # print("인스턴스 활용중 ~")
        # print(cls)
        return cls.__instances[cls]  # 클래스로 인스턴스를 생성했으면 인스턴스 반환


class WorkList_db_class(metaclass=Singleton):

    # Info_plrn 테이블에 plrn 데이터 입력
    def Input_plrn_data(self, date, protocol_name, smp_num, plate_type, cap_type, ctrl_seq, pcr_bcd, bcd_list):
        self.date = date
        self.protocol_name = protocol_name
        self.smp_num = smp_num
        self.plate_type = plate_type
        self.cap_type = cap_type
        self.ctrl_seq = ctrl_seq
        self.pcr_bcd = pcr_bcd
        self.bcd_list = bcd_list

        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute('''
                    insert into Info_plrn(Date, Protocol_Name, Smp_Num, Plate_Type, Cap_Type, Ctrl_Seq, PCR_bcd, BarcodeList)
                    values(?, ?, ?, ?, ?, ?, ?, ?)
                    '''
                    , (self.date, self.protocol_name, self.smp_num, self.plate_type, self.cap_type, self.ctrl_seq,
                       self.pcr_bcd, self.bcd_list))
        conn.commit()
        cur.execute("select ID from Info_plrn where Date = (%s)" % ("'" + self.date + "'"))
        id_plrn = cur.fetchall()
        cur.close()
        conn.close()
        return id_plrn[0][0]

    # Info_smp 테이블에 샘플 바코드 정보 입력
    def Input_sample_data(self, smp_bcd, id_plrn):
        self.smp_bcd = smp_bcd
        self.id_plrn = id_plrn

        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        for i in range(len(self.smp_bcd)):
            cur.execute("insert into Info_smp(ID, Smp_bcd) values(?, ?)", (self.id_plrn, str(self.smp_bcd[i])))
            conn.commit()
        conn.commit()
        cur.close()
        conn.close()

    # Info_PCR 테이블에 PCR 바코드 정보 입력
    def PCR_test_count(self, pcr_bcd):
        self.pcr_bcd = pcr_bcd
        if self.pcr_bcd == "Hidden Barcode":
            return str(100)
        else:
            conn = sqlite3.connect(db_con)
            cur = conn.cursor()
            try:
                cur.execute("select Test_count from Info_PCR where PCR_bcd = (%s)" % ("'" + self.pcr_bcd + "'"))
                test_count = cur.fetchall()
                if test_count == []:
                    cur.execute("insert into Info_PCR(PCR_bcd, Test_count) values(?, ?)", (self.pcr_bcd, 100))
                    conn.commit()
                    cur.execute("select Test_count from Info_PCR where PCR_bcd = (%s)" % ("'" + self.pcr_bcd + "'"))
                    test_count = cur.fetchall()
            except:
                pass
            cur.close()
            conn.close()
            return str(test_count[0][0])

    # PCR 시약 사용시 test count 차감
    def Use_PCR(self, pcr_bcd, test_count):
        self.pcr_bcd = pcr_bcd
        self.test_count = str(test_count)
        if self.pcr_bcd == "Hidden Barcode":
            return
        else:
            conn = sqlite3.connect(db_con)
            cur = conn.cursor()
            cur.execute("update Info_PCR set Test_count = Test_count - (%s) where PCR_bcd = (%s)" % (
            "'" + self.test_count + "'", "'" + self.pcr_bcd + "'"))
            conn.commit()
            cur.close()
            conn.close()

    def show_path(self):
        print("show_path ", os.getcwd())
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("SELECT Path_monitor FROM Monitor")
        b_info = cur.fetchall()
        cur.close()
        conn.close()
        return b_info

    def Sel_Bcd(self):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("SELECT Inst_bcd FROM Monitor")
        b_info = cur.fetchall()
        cur.close()
        conn.close()
        return b_info

    def update(self, Barcod_List):
        self.bcd_list = Barcod_List

        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("update Monitor set Inst_bcd = (%s)" % ("'" + self.bcd_list + "'"))
        cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return 1

    # plrn 파일 생성
    def make_plrn(self, id_plrn):
        self.id_plrn = str(id_plrn)
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()

        cur.execute("select * from Info_plrn where ID = (%s)" % ("'" + self.id_plrn + "'"))
        info_plrn = cur.fetchall()
        cur.execute("select Smp_bcd from Info_smp where ID = (%s)" % ("'" + self.id_plrn + "'"))
        info_smp = cur.fetchall()

        date = info_plrn[0][1]
        Protocol_Name = info_plrn[0][2]
        smp_num = info_plrn[0][3]
        plate_type = info_plrn[0][4]
        cap_type = info_plrn[0][5]
        ctrl_seq = info_plrn[0][6]
        pcr_bcd = info_plrn[0][7]
        smp_bcd = []
        for i in range(smp_num):
            smp_bcd.append(info_smp[i][0])
        cur.execute(
            "select Protocol_Path, Light from Info_protocol where Protocol_Name = (%s)" % ("'" + Protocol_Name + "'"))
        info_protocol = cur.fetchall()
        Inst_Name = "PreNATII"
        plateBarcode = ""
        ExtractBarcode = ""
        PatientList = []
        for i in range(smp_num):
            PatientList.append("")
        p_list = "','".join(map(str, PatientList))
        PatientName = "'" + p_list + "'"

        cur.execute("select * from Path_plrn")
        dir_plrn = cur.fetchall()
        dir_plrn_1 = dir_plrn[0][0] + f"\\{Protocol_Name}\\plrn, {Inst_Name}, {date}, {Protocol_Name}.plrn"

        try:
            if not (os.path.isdir(dir_plrn[0][0] + f"/{Protocol_Name}")):
                os.makedirs(os.path.join(dir_plrn[0][0] + f"/{Protocol_Name}"))
        except OSError as e:
            print(e)

        smp = ""
        plt_pos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(smp_num + 2):
            if i < smp_num:
                smp += str(plt_pos[i % 8]) + str((i // 8) + 1).zfill(
                    2) + f",{info_protocol[0][1]},,,Unknown,{smp_bcd[i]},,,,,,1_1_0,,,,,,,,,{Protocol_Name},,,,,," + "\n"
            elif i == smp_num:
                ctrl_1 = str(plt_pos[i % 8]) + str((i // 8) + 1).zfill(2)
            else:
                ctrl_2 = str(plt_pos[i % 8]) + str((i // 8) + 1).zfill(2)
        if ctrl_seq == "NC, PC":
            smp += f"{ctrl_1}" + f",{info_protocol[0][1]},,,Negative Control,NC,,,,,,0_1_0,,,,,,,,,{Protocol_Name},,,,,," + "\n"
            smp += f"{ctrl_2}" + f",{info_protocol[0][1]},,,Positive Control,PC,,,,,,0_1_0,,,,,,,,,{Protocol_Name},,,,,," + "\n"
        elif ctrl_seq == "PC, NC":
            smp += f"{ctrl_1}" + f",{info_protocol[0][1]},,,Positive Control,PC,,,,,,0_1_0,,,,,,,,,{Protocol_Name},,,,,," + "\n"
            smp += f"{ctrl_2}" + f",{info_protocol[0][1]},,,Negative Control,NC,,,,,,0_1_0,,,,,,,,,{Protocol_Name},,,,,," + "\n"

        f = open(dir_plrn_1, 'w')
        f.write(
            f'''Plate Header,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Field,Data,,Instructions,,,,,,,,,,,,,,,,,,,,,,,,,,
Version,1,,Do not modify this field.,,,,,,,,,,,,,,,,,,,,,,,,,,
Plate Size,96,,Do not modify this field.,,,,,,,,,,,,,,,,,,,,,,,,,,
Plate Type,BR White,,Allowed values (BR White BR Clear),,,,,,,,,,,,,,,,,,,,,,,,,,
Scan Mode,All Channels,,Allowed values (SYBR/FAM Only All Channels FRET),,,,,,,,,,,,,,,,,,,,,,,,,,
Units,micromoles,,Allowed values (copy number fold dilution micromoles nanomoles picomoles femtomoles attomoles milligrams micrograms nanograms picograms femtograms attograms percent),,,,,,,,,,,,,,,,,,,,,,,,,,
Run ID,,,Short description or bar code with no new line or commas,,,,,,,,,,,,,,,,,,,,,,,,,,
Run Notes,"'runNoteVersion':('1.1'),'plateBarcode':('{plateBarcode}'),'plateType':('{plate_type}'),'capFilm':('{cap_type}'),'ExtractBarcode':('{ExtractBarcode}'),'PCRBarcodeList':('{pcr_bcd}'),'PatientNameList':({PatientName},'',''),'userId':(''),'userName':(''),'ClotSampleWell':(),'dwpBarcode':('')",,Run description with no new line or commas,,,,,,,,,,,,,,,,,,,,,,,,,,
Run Protocol,{info_protocol[0][0]},,Protocol File Name,,,,,,,,,,,,,,,,,,,,,,,,,,
Data File,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
TBD,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Plate Data,,Do not modify this field.,,,,,,,,,,,,,,,,,,,,,,,,,,,
Well,Ch1 Dye,Ch2 Dye,Ch3 Dye,Ch4 Dye,Ch5 Dye,FRET,Sample Type,Sample Name,Ch1 Target Name,Ch2 Target Name,Ch3 Target Name,Ch4 Target Name,Ch5 Target Name,FRET Target Name,Biological Set Name,Replicate,Ch1 Quantity,Ch2 Quantity,Ch3 Quantity,Ch4 Quantity,Ch5 Quantity,FRET Quantity,Well Note,Ch1 Well Color,Ch2 Well Color,Ch3 Well Color,Ch4 Well Color,Ch5 Well Color,FRET Well Color
{smp}''')
        f.close()

        add_path_2 = dir_plrn[0][1]
        add_path_3 = dir_plrn[0][2]
        if add_path_2 != "":
            add_path_2 = add_path_2.replace("/", "\\") + f"\\{Protocol_Name}"
            try:
                if not (os.path.isdir(add_path_2)):
                    os.makedirs(os.path.join(add_path_2))
            except OSError as e:
                print(e)
            add_path_2 = add_path_2 + f"\\plrn, {Inst_Name}, {date}, {Protocol_Name}.plrn"

            src = dir_plrn_1
            shutil.copy(src, add_path_2)
        if add_path_3 != "":
            add_path_3 = add_path_3.replace("/", "\\") + f"\\{Protocol_Name}"
            try:
                if not (os.path.isdir(add_path_3)):
                    os.makedirs(os.path.join(add_path_3))
            except OSError as e:
                print(e)
            add_path_3 = add_path_3 + f"\\plrn, {Inst_Name}, {date}, {Protocol_Name}.plrn"
            src = dir_plrn_1
            shutil.copy(src, add_path_3)

        cur.execute("update Monitor set (Path_plrn, Use_plrn) = ((%s), (%d))" % ("'" + dir_plrn_1 + "'", 0))
        conn.commit()
        cur.execute("select Path_plrn from Monitor")
        cur.close()
        conn.close()

    # plrn 경로 설정
    def set_dir(self, path, i):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        self.path = path
        if i == 1:
            cur.execute("update Path_plrn set Path_1 = (%s)" % ("'" + self.path + "'"))
        elif i == 2:
            cur.execute("update Path_plrn set Path_2 = (%s)" % ("'" + self.path + "'"))
        elif i == 3:
            cur.execute("update Path_plrn set Path_3 = (%s)" % ("'" + self.path + "'"))
        print(i, self.path)
        conn.commit()
        cur.close()
        conn.close()

    # 생성된 Inst 바코드 파일을 불러오면서 프로토콜 기본 setting값을 Temp 테이블에 저장
    def Inst_bcd_path(self, bcd_path):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("update Monitor set Inst_bcd = (%s)" % ("'" + bcd_path + "'"))
        conn.commit()
        cur.execute("select Inst_bcd from Monitor")
        inst_bcd_path = cur.fetchall()

        temp = inst_bcd_path[0][0].split("\\")
        protocol_name = temp[-2].split("_")

        cur.execute("select Protocol_Name from Temp where Protocol_Name = (%s)" % ("'" + protocol_name[-1] + "'"))
        name = cur.fetchall()
        if name == []:
            cur.execute("insert into Temp(Protocol_Name, Plate_Type, Cap_Type, Control) values(?, ?, ?, ?)",
                        (protocol_name[-1], "Plate", "Cap", "NC, PC"))
            conn.commit()
        cur.close()
        conn.close()

    # Make 클릭시 Temp 테이블에 setting값 저장
    def save_Temp(self, protocol, plate_type, cap_type, ctrl_seq):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute(
            "update Temp set (Plate_Type, Cap_Type, Control) = ((%s), (%s), (%s)) where Protocol_Name = (%s)" % (
            "'" + plate_type + "'", "'" + cap_type + "'", "'" + ctrl_seq + "'", "'" + protocol + "'"))
        conn.commit()
        cur.close()
        conn.close()

    # 프로토콜 기본 setting값 불러오기
    def load_setting(self):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("select Inst_bcd from Monitor")
        inst_bcd_path = cur.fetchall()
        temp = inst_bcd_path[0][0].split("\\")
        protocol_name = temp[-2].split("_")
        cur.execute("select * from Temp where Protocol_Name = (%s)" % ("'" + protocol_name[-1] + "'"))
        setting_data = cur.fetchall()
        cur.execute("select Protocol_Name from Temp")
        protocol_list = cur.fetchall()
        cur.close()
        conn.close()
        return setting_data[0][0], setting_data[0][1], setting_data[0][2], setting_data[0][3], protocol_list

    def display_path(self):
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("select * from Path_plrn")
        path = cur.fetchall()
        cur.close()
        conn.close()
        return path

    def show_PE_path(self):
        print("PE_path ", os.getcwd())
        conn = sqlite3.connect(db_con)
        cur = conn.cursor()
        cur.execute("SELECT PE_path FROM Monitor")
        b_info = cur.fetchall()
        cur.close()
        conn.close()
        return b_info