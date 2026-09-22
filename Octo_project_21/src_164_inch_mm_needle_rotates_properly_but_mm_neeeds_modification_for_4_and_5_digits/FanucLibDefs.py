import ctypes , os
import socket
import threading
import time
#from pathlib import Path

from PySide2.QtWidgets import QMessageBox

#C:\\Users\\Lenovo\\Documents\\Received Files\\GE Fanus Focas Lib 2.5\\fwlib-master\\
#libpath = ("D:\\PreciGoFanuc\\Run_For_Exe_6\\Fwlib32.dll")
#libpath = ("C:\\Program Files\\PreciGo\\dll\\Fwlib32.dll")
# libpath = "D:\PreciGoFanuc\Run_For_Exe_7\Fwlib32.dll"

current_file_path = os.path.abspath(__file__)
# print(current_file_path)

a = current_file_path.split('/')
a.pop(-1)
path = '/'.join(a)
path = '/home/torizon/app/data'
#/home/pi/Desktop/Project/2/Auto correction FANUC/intersense/pages/
libpath = "/home/torizon/app/data/libfwlib32-linux-armv7.so.1.0.5"
# libpath = "Fwlib32.dll"
# # print(libpath,12121212121212121212112121212121212121212121212)

class ODBTOFS(ctypes.Structure):
    _fields_ = [("datano", ctypes.c_short),
                ("type", ctypes.c_short),
                ("data", ctypes.c_long)]
    
    def __repr__(self):
        return f'Point({self.datano},{self.type},{self.data})'

    def clearSelf(self):
        del self
        
class FANUCDEFS:
    def __init__(self,ip,port):
        try:
            self.ip = ip
            self.port = port
            
            self.focas = ctypes.cdll.LoadLibrary(libpath)
        
            self.focas.cnc_allclibhndl3.restype = ctypes.c_short
            self.focas.cnc_freelibhndl.restype = ctypes.c_short
            self.focas.cnc_rdcncid.restype = ctypes.c_short
            
            self.focas.cnc_rdtofs.argtypes = ctypes.c_ushort,ctypes.c_short,ctypes.c_short,ctypes.c_short,ctypes.POINTER(ODBTOFS)
            self.focas.cnc_rdtofs.restype = ctypes.c_short
            
            self.focas.cnc_setpath.argtypes = ctypes.c_ushort,ctypes.c_short
            self.focas.cnc_setpath.restype = ctypes.c_short

            self.ip = ip
            self.port = port
            self.timeout = 3
            self.libh =  ctypes.c_ushort(0)
    #         
            self.tofs = ODBTOFS()
        except Exception as e:
            print(f"Error Fanucdefs --init-- -> {e}")
    def connectFanuc(self):
        ret = int()
        
        try:
            ret = self.focas.cnc_allclibhndl3(
                                      self.ip.encode(),
                                      self.port,
                                      self.timeout,
                                      ctypes.byref(self.libh)
                                      )
        except:
            print('Error in Connecting FANUC')
            return 'error'
          # Wait 30 seconds after power-on

        if ret != 0:
            print(ret)
            #raise Exception(f"Error in Connecting with Error Code({ret})")
            return 'error'
        else:
            print('Connected to FANUC')

    
            
    def isActive(self):
        try:
            result = self.readFanuc()
#             print(result,'zzzzzzzzzzzzzzzz')
            return result
        except:
            return 'None'
        
    def checkAlive(self):
        try:
            instance = FANUCDEFS(self.ip,self.port)

            ret = instance.focas.cnc_startupprocess(0, "focas.log")
            if ret != 0:
                raise Exception(f"Failed to create required log file! ({ret})")
            instance.connectFanuc()
            
            result = instance.readFanuc()
            instance.disconnectMachine()
            del instance
            #print('result',result)
            #self.instance.freeLibh()
            return result
        except:
            return 'None'
                
    def readFanuc(self):
        machine_id = ''
        #ret = int(0)
        
        try:
            cnc_ids = (ctypes.c_uint32 * 4)()
            ret = self.focas.cnc_rdcncid(self.libh, cnc_ids)
            print(ret,'ret')
            if ret != 0:
                #raise Exception(f"Failed to Link FANUC with Error ({ret})")
                return 'None'
            else:
                machine_id = "-".join([f"{cnc_ids[i]:08x}" for i in range(4)])
#                 print(f"machine_id={machine_id}")
#                 return machine_id
            
        #except:
        #    return 'None'
        
        finally:
            return machine_id
        
    def FanucVarToRealVar(self,flt):
        try:
           val = format(float(flt/1000), '.3f')
        except:
           val = format('0.000')
        
        return val
    
    def refreshStructure(self):
        self.tofs.datano = 0
        self.tofs.type = 0
        self.tofs.data = 0

    def readValue(self,row,column,bits_length):
        #ret = int()
        try:
            ret = self.focas.cnc_rdtofs(self.libh,row,column,bits_length,ctypes.byref(self.tofs))
        except:
            print('Error in Value Evaluation from FANUC')
            return 'error'
            
        if ret != 0:
            print(ret)
            #QMessageBox.about(self, "Error in reading", "Read Issues!!!")
            #raise Exception(f"Error in Value Evaluation with Error Code ({ret})")
            return 'error'
        else:
            print('Got Value from FANUC')
            return self.tofs.data
    
    def read(self,row,column,bits_length):
        self.refreshStructure()
        val = self.readValue(row,column,bits_length)
        try:
            float(val)
            val = self.FanucVarToRealVar(val)
            return val
        except:
            return val
            #print('Write here for read values')

    def setpath(self,set_path_value):
        ret = int()
        try:
            ret = self.focas.cnc_setpath(self.libh,set_path_value)
            print(ret)
        except:
            print('Error in Setting Path of FANUC')
            return 'error'
        
    def writeValue(self,row,column,bits_length,value):
        ret = int()

        try:
            value = int(1000 * value)
            print(row,column,bits_length,value)
            #value = 12
            ret = self.focas.cnc_wrtofs(self.libh,row,column,bits_length,value)
        except:
            print('Error in Writing Value to FANUC')
            return 'error'
            
        if ret != 0:
            print(ret)
            #raise Exception(f"Error in Writing Value with Error Code ({ret})")
            return 'error'
        else:
            print('Sent Value from FANUC')
            return 0
                
    def write(self,row,column,bits_length,value):
        print(row,column,bits_length,int(value))
        ret_val = self.writeValue(row,column,bits_length,value)
        
        if(ret_val == 'error'):
            return 'error'
        
        self.refreshStructure()
        val = self.read(row,column,bits_length)
        
        # print('Write here for write values')
        return val
        
    def freeLibh(self):
        ret = int()

        try:
            ret = self.focas.cnc_freelibhndl(self.libh)
        except:
            print('Error in Clearing to Library Handle')
            
        if ret != 0:
            pass
#             QMessageBox.about(self, "Error", "Error in Clearing to Library Handle!!!")
            #raise Exception(f"Error in Clearing to Library Handle with Error Code ({ret})")
        else:
            print('Library Handle Got Free')
            
    def disconnectMachine(self):
        self.freeLibh()
        del self

# machine_one = FANUCDEFS('192.168.225.158',8193)
# ret = machine_one.focas.cnc_startupprocess(0, "focas.log")
# if ret != 0:
#     raise Exception(f"Failed to create required log file! ({ret})")
# machine_one.connectFanuc()


# # while True:
# print(machine_one.readFanuc())
# machine_one.disconnectMachine()

# print(machine_one.readFanuc())

# machine_one.write(11,0,8,0.02)
# print(machine_one.read(11,0,8))
#print(machine_one.tofs.data,'val')
