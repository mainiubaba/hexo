# -*- coding: utf-8 -*-
try:
    import wmi
    import win32api
except ImportError:
    wmi = None
import sys,platform
import subprocess
import os


def get_system_info(c,sys):
    if sys == "Windows":
        for sys in c.Win32_OperatingSystem():
            print  ("Version :\t%s" % sys.Caption.encode( "GBK"))
            print  ("Vernum :\t%s" % sys.BuildNumber)

def get_memory_info(c,sys):
    if sys == "Windows":
        for mem in c.Win32_MemoryArray():
            print ('\t' + str(mem.Caption)  + '\t' + str(mem.Name))
        cs = c.Win32_ComputerSystem()
        pfu = c.Win32_PageFileUsage()
        MemTotal = int(cs[ 0].TotalPhysicalMemory)/ 1024/1024
        print  ("TotalPhysicalMemory :" + '\t' + str(MemTotal) + "M"  )
        #tmpdict ["MemFree"] = int( sys[0].FreePhysicalMemory)/1024
        SwapTotal = int(pfu[ 0].AllocatedBaseSize)
        print ( "SwapTotal :" + '\t' + str(SwapTotal) + "M"  )
        #tmpdict ["SwapFree"] = int( pfu[0].AllocatedBaseSize - pfu[0].CurrentUsage)

def get_disk_info(c,sys,infolist):
    if sys == "Windows":
        tmpdict = dict()
        tmplist=list()
        for physical_disk in c.Win32_DiskDrive():
            if physical_disk.Size:
                tmpdict[ "disk"]=str(physical_disk.Caption)
                tmpdict["size" ]=str(long(physical_disk.Size)/1024/1024/1024)+"G"
                tmpdict[ "dev"] = str(physical_disk.MediaType)
                tmplist.append(tmpdict)
                print (tmpdict["dev" ]+":\t"+tmpdict["disk"] + ' :\t' + tmpdict["size" ])
        infolist.append(tmplist)

def get_cpu_info(c,sys,infolist):
    if sys == "Windows":
        tmplist=list()
        tmpdict=dict()
        tmpdict[ "CpuCores"] = 0
        for cpu in c.Win32_Processor():
            tmpdict[ "model name"] = cpu.Name
        try:
            tmpdict[ "CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict[ "CpuCores"] += 1
            tmpdict[ "CpuClock"] = cpu.MaxClockSpeed
        print  ('CpuType :\t' + str(tmpdict["model name"]) )
        print  ('CpuCores :\t' + str(tmpdict["CpuCores"]) )
        tmplist.append(tmpdict)
        #infolist.append(tmplist)
        return tmplist


def get_network_info(c,sys,infolist):
    if sys == "Windows":
        tmplist=list()
        for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                tmpdict=dict()
                tmpdict[ "Description"] = interface.Description
                tmpdict[ "IPAddress"] = interface.IPAddress[0 ]
                tmpdict[ "IPSubnet"] = interface.IPSubnet[0 ]
                tmpdict[ "MAC"] = interface.MACAddress
                tmplist.append(tmpdict)
        for i in tmplist:
            print ( i["Description"])
            print   ('\t' + "MAC :" + '\t' + i["MAC" ])
            print  ('\t' + "IPAddress :" + '\t' + i["IPAddress" ])
            print  ( '\t' + "IPSubnet :" + '\t' + i["IPSubnet" ])
        infolist.append(tmplist)
        for interfacePerfTCP in c.Win32_PerfRawData_Tcpip_TCPv4():
                print ( 'TCP Connect :\t' + str(interfacePerfTCP.ConnectionsEstablished))

def get_Proceess_cmd(c,process_name):
    cmd = ""
    for process in c.Win32_Process():
        temp =   unicode(process.CommandLine)
        name = process.Name
        if name.find(process_name) >= 0:
            cmd = temp
    return cmd



def get_info(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell= False)
    return p.communicate()[ 0].split( "\n")[0 ]

if __name__ == "__main__":
    sys = platform.system()
    infolist = list()
    c = wmi.WMI ()