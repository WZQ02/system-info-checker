import platform

progv = '2021.8.5'
if platform.system() == 'Windows':#判断当前系统是不是Windows
    import os
    import wmi
    import win32api
    import win32con
    for cps in wmi.WMI().Win32_ComputerSystem():
        #bootst = cps.BootupState
        memcab = cps.TotalPhysicalMemory#内存容量
        memcap = int(int(memcab)/1048576)
        manu = cps.Manufacturer
        model = cps.Model
    for cpu in wmi.WMI().Win32_Processor():
        cpunam = cpu.Name#获取CPU名称
        cores = cpu.NumberOfCores#获取CPU核心数
        ths = cpu.NumberOfLogicalProcessors#CPU线程数
        maxfreq = cpu.MaxClockSpeed
    for disk in wmi.WMI().Win32_DiskDrive():
        disknam = disk.Model#硬盘型号
        if disk.InterfaceType == 'IDE':
            diskint = 'PATA/SATA'
        elif disk.InterfaceType == 'SCSI':
            diskint = 'SCSI/NVMe'
        elif disk.InterfaceType == 'USB':
            diskint = 'USB'
        else:
            diskint = '未知接口'#硬盘接口
    for gpu in wmi.WMI().Win32_VideoController():
        gpunam = gpu.Caption#获取显卡名称
        gemcab = gpu.AdapterRAM#显存容量，似乎在win10上不起作用
        #gemcap = int(int(gemcab)/1048576)
        scr_length = gpu.CurrentHorizontalResolution
        scr_width = gpu.CurrentVerticalResolution
        scr_color = gpu.CurrentBitsPerPixel
        scr_refrate = gpu.CurrentRefreshRate
    for stp in wmi.WMI().Win32_SystemEnclosure():#判断计算机类型
        if 'Virtual' in model or 'VMware' in model:
            systyp = '虚拟机'
        elif 3 in stp.ChassisTypes:
            systyp = '台式机'
        elif 10 in stp.ChassisTypes:
            systyp = '笔记本'
        elif 30 in stp.ChassisTypes:
            systyp = '平板电脑'
        elif 8 in stp.ChassisTypes:
            systyp = '便携式'
        elif 13 in stp.ChassisTypes:
            systyp = '一体机'
        elif 9 in stp.ChassisTypes:
            systyp = '膝上型'
        elif 14 in stp.ChassisTypes:
            systyp = '迷你笔记本'
        elif 6 in stp.ChassisTypes:
            systyp = '迷你塔式机'
        elif 7 in stp.ChassisTypes:
            systyp = '塔式机'
        else:
            systyp = '其他平台类型'
        #print(stp.ChassisTypes)
    for sys in wmi.WMI().Win32_OperatingSystem():
        sku = sys.Caption#Windows的SKU
        fbd = sys.Version#Windows的内部版本号，带前缀
        build = sys.BuildNumber#Windows的内部版本号，不带前缀
        bit = sys.OSArchitecture#系统位数
        winsysdir = sys.WindowsDirectory
        if sys.SystemDrive == 'X:':#根据盘符判断是否为pe系统
            pestate = '是'
        else:
            pestate = '否'
        if '11.0.' in fbd or '10.1' in fbd:
            w_cver = 'Windows 11'
        elif '10.0.' in fbd:#判断消费级的Windows版本
            if int(build) < 21400:
                w_cver = 'Windows 10'
            else:
                w_cver = 'Windows 11'
        elif '6.4.' in fbd:
            w_cver = 'Windows 10'
        elif '6.3.' in fbd:
            w_cver = 'Windows 8.1'
        elif '6.2.' in fbd:
            w_cver = 'Windows 8'
        elif '6.1.' in fbd:
            w_cver = 'Windows 7'
        elif '6.0.' in fbd:
            w_cver = 'Windows Vista'
        elif '5.2.' in fbd:
            w_cver = 'Windows XP x64 Edition'
        elif '5.1.' in fbd:
            w_cver = 'Windows XP'
        elif '5.0.' in fbd:
            w_cver = 'Windows 2000'
        else:
            w_cver = 'Windows NT'
        if '5.' in fbd:#判断是不是NT5
            efiboot = False
        else:
            bcdinfof = os.popen(r'bcdedit', "r")#获取bcd信息
            bcdinfo = bcdinfof.read()
            if 'winload.efi' in bcdinfo:#判断UEFI启动
                efiboot = True
            elif 'winload.exe' in bcdinfo:
                efiboot = False
            else:
                efiboot = 'Unknown'
        if efiboot == True:
            bootst = 'UEFI'
            firmtype = 'UEFI'
        elif efiboot == False:
            bootst = '传统'
            firmtype = '支持 CSM 的 UEFI，或者 BIOS'
        else:
            bootst = '未知'
            firmtype = '未知。请以管理员权限运行本程序。'
        if sys.CSDVersion == None:
            if int(build) >= 10240:#判断是不是Windows10
                if int(build) == 10240:
                    sp = '1507'
                elif int(build) == 10586:
                    sp = '1511'
                elif int(build) == 14393:
                    sp = '1607'
                elif int(build) == 15063:
                    sp = '1703'
                elif int(build) == 16299:
                    sp = '1709'
                elif int(build) == 17134:
                    sp = '1803'
                elif int(build) == 17763:
                    sp = '1809'
                elif int(build) == 18362:
                    sp = '1903'
                elif int(build) == 18363:
                    sp = '1909'
                elif int(build) == 19041:
                    sp = '2004'
                elif int(build) == 19042:
                    sp = '20H2'
                elif int(build) == 19043:
                    sp = '21H1'
                elif int(build) == 19044:
                    sp = '21H2'
                elif int(build) > 19044:
                    sp = 'Dev'
                else:
                    sp = 'Insider Preview'#是Windows10，但又不是目前已发布的正式版本，暂且假定为Insider Preview
            else:
                sp = ''#不是Windows10，但系统又无sp更新
        else:
            sp = sys.CSDVersion#系统为sp更新
    print('程序版本: {}\r\n\r\n操作系统: {}\r\n操作系统内部版本号: {}\r\n对应的消费级 Windows 版本: {} {}\
          \r\n系统位数: {}\r\nWindows 系统目录: {}\r\n是否为 Windows PE: {}\r\n系统启动方式: {}\
          \r\n固件类型: {}\r\n\r\n处理器: {} ({} 核 {} 线程，基准频率: {} MHz)\
          \r\n系统已识别内存容量: {} MB\r\n主硬盘: {} ({})\r\n显卡: {}\
          \r\n当前显示器视频模式: {} x {} 像素，{} 位色彩，{} 赫兹\r\n\r\n计算机类型: {}\r\n制造商: {}\r\n型号: {}\r\n\r\n按回车退出...'\
          .format(progv,sku,fbd,w_cver,sp,bit,winsysdir,pestate,bootst,firmtype,cpunam,cores,ths,maxfreq,memcap,disknam,\
                  diskint,gpunam,scr_length,scr_width,scr_color,scr_refrate,systyp,manu,model))
    input();
elif platform.system() == 'Linux':#判断当前系统是不是Linux
    import os
    #os-release_r = os.open("/etc/os-release",os.O_RDWR)
    release = os.popen(r'cat /etc/os-release', 'r').readline()
    sku = release[6:-2]
    kernel_ver = os.popen(r'uname -r', 'r').readline()
    kernel_time = os.popen(r'uname -v', 'r').readline()
    archti = os.popen(r'uname -m', 'r').readline()
    if "x86_64" in archti:
        bit = "64 位 x86 架构"
    elif "i386" in archti or "i686" in archti:
        bit = "32 位 x86 架构"
    else:
        bit = archti
    if os.path.exists("/sys/firmware/efi/efivars"):
        bootst = 'UEFI'
        firmtype = 'UEFI'
    elif os.path.exists("/sys/firmware/coreboot"):
        bootst = 'CoreBoot'
        firmtype = 'CoreBoot'
    elif 'x86' in bit:
        bootst = '传统'
        firmtype = '支持 CSM 的 UEFI，或者 BIOS'
    else:
        bootst = '未知'
        firmtype = '未知固件类型'
    cpuinfo = os.popen(r'cat /proc/cpuinfo | grep "model name" | uniq ', 'r').readline()
    cpunam = cpuinfo[13:-1]
    cpucount = eval(os.popen(r'cat /proc/cpuinfo | grep "physical id" | uniq | wc -l', 'r').readline())
    cores = eval(os.popen(r'cat /proc/cpuinfo | grep "cpu cores" | uniq', 'r').readline()[12:])
    ths = eval(os.popen(r'cat /proc/cpuinfo | grep "processor" | wc -l', 'r').readline())
    meminfo = os.popen(r'cat /proc/meminfo', 'r').readlines()
    memcab = eval(meminfo[0][9:-4])
    memcap = int(int(memcab)/1024)
    memreb = eval(meminfo[2][13:-4])
    memrem = int(int(memreb)/1024)
    gpunam = os.popen(r'lspci | grep VGA', 'r').readline()[35:]
    print('程序版本: {}\r\n\r\n操作系统: {}\r\n系统内核版本: {}内核信息和编译时间: {}系统针对的 CPU 架构: {}\r\n系统启动方式: {}\r\n固件类型: {}\r\n\r\n处理器: {} ({} 个, {} 核 {} 线程)\r\n系统已识别内存容量: {} MiB ({} MiB 可用)\r\n显卡: {}\r\n按回车退出...'.format(progv,sku,kernel_ver,kernel_time,bit,bootst,firmtype,cpunam,cpucount,cores,ths,memcap,memrem,gpunam))
    input();
else:
    print('本程序目前仅支持 Windows 和 GNU/Linux 系统。按回车键退出。')
    input();
