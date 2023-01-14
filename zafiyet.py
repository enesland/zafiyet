import os

print("CODED BY ENESLAND")
print("TOOL AMACI ZAFIYET UZERINEDIR")

print("""

1-) NMAP KULLAN
2-) Nikto KULLAN
3-) META KULLAN
4-) IP-TOOL KULLLAN
""")

islemno=input("islem numarasi gir : ")

if islemno=="1":
        hedefip=input("Hedef ip gir : ")

        os.system("nmap "+hedefip)
elif islemno=="2":
        hedefip=input("Nikto kurulum icin enter bas!")

        os.system("git clone https://github.com/sullo/nikto "+hedefip)
elif islemno=="3":
        hedefip=input("Meta kurmak icin enter bas!")

        os.system("git clone https://github.com/rapid7/metasploit-framework "+hedefip)
        print("meta kuruldu calistirmak icin 'msfconsole' yaz")

elif islemno=="4":
        hedefip=input("ip-tool kurmak icin enter bas!")

        os.system("git clone https://github.com/Team0x02/ip-tool "+hedefip)
        print("""calistirmak icin;
                 cd ip-tool
                 python3 ip-tool.py""")
        print("!!!Bilgilendirme!!! ip-tool enesland tarafindan kodlanip buraya eklenmistir")
else:
        print("yanlis tusa bastiniz")
