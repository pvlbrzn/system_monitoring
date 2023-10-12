import psutil


def cpu_info():
    res = {}
    data1 = psutil.cpu_times()
    data2 = psutil.cpu_freq()
    res.update(user_time=data1.user, 
               sys_time=data1.system, 
               idle_time=data1.idle, 
               guest_time=data1.guest,
               current=data2.current)
    
    return res

def memory_info():
    res = {}
    data = psutil.virtual_memory()
    res.update(total=data.total,
               avail=data.available,
               percent=data.percent,
               free=data.free)
    return res

def net_info():
    res = {}
    data = psutil.net_io_counters()
    res.update(sent=data.bytes_sent,
               recv=data.bytes_recv,
               p_sent=data.packets_sent,
               p_recv=data.packets_recv,
               errin=data.errin,
               errout=data.errout)
    return res

def battary_power_left():
    battery = psutil.sensors_battery()
    power_left = battery.percent
    return power_left

def battary_secsleft():
    battery = psutil.sensors_battery()
    secsleft = battery.secsleft
    return secsleft

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def battary_power():
    battery = psutil.sensors_battery()
    bat_power = battery.power_plugged
    return bat_power


def show(cpu=None, memory=None, net=None, secs=None, charge=None, bpower=None):
    cpu_title = ("{:^80}").format("CPU information")
    cpu_sample = ("|{:*^16}"*4 + "|{:*^16}|").format("user_time", 
                                                     "system_time",
                                                     "idle_time",
                                                     "guest_time",
                                                     "current") 
    cpu_tamplate = "|{user_time:_^16}|{sys_time:_^16}|{idle_time:_^16}|{guest_time:_^16}|{current:_^16.3}|"  
    
    memory_title = ("{:^80}").format("Memory information")
    memory_sample = ("|{:*^20}"*3 + "|{:*^20}|").format("total_memory",
                                                        "available_memory",
                                                        "percentage_usage",
                                                        "free_memory") 
    memory_tamplate = "|{total:_^20}|{avail:_^20}|{percent:_^20}|{free:_^20}|"   
    
    net_title = ("{:^84}").format("System-wide network In/Out statistics")
    net_sample = ("|{:*^14}"*5 + "|{:*^14}|").format("bytes_sent", 
                                                     "bytes_recv",
                                                     "packets_sent",
                                                     "packets_recv",
                                                     "error_In",
                                                     "error_Out") 
    net_tamplate = "|{sent:_^14}|{recv:_^14}|{p_sent:_^14}|{p_recv:_^14}|{errin:_^14}|{errout:_^14}|" 

    battary_title = ("{:^54}").format("Battery status information")
    bat_par = (("|{:<25}"+"{:>25}|").format(charge, secs))
    electricity = (("|{:<53}|".format(bpower)))
    processes_title = ("{:^53}").format("All system processes")
    print("\n\n")
    print(cpu_title)
    print(cpu_sample)
    print(cpu_tamplate.format(**cpu))
    print("\n")
    print(memory_title)
    print(memory_sample)
    print(memory_tamplate.format(**memory))
    print("\n")
    print(net_title)
    print(net_sample)
    print(net_tamplate.format(**net))
    print("\n")
    print(battary_title)
    print(bat_par)
    print(electricity)
    print("\n")
    print(processes_title)
    for proc in psutil.process_iter():
        name = proc.name()
        print(name)
        if name == "program.exe":
            pass

def main():
    cpu_data = cpu_info()
    memory_data = memory_info()
    net_data = net_info()
    bat_power_left = battary_power_left()
    battery_charge = "Battery power left = |{}%|".format(bat_power_left)
    bat_sec = battary_secsleft()
    battery_secs = "Time left = |{}|".format(secs2hours(bat_sec))
    batpow1 = battary_power()
    batpow = "Power - |{}|".format(batpow1)
    show(cpu=cpu_data, 
         memory=memory_data, 
         net=net_data, 
         charge=battery_charge, 
         secs=battery_secs, 
         bpower=batpow)


if __name__ == "__main__":
    main()