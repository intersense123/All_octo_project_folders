import spidev
import gpiod
import time

#from numba import njit

class SPI:
    def __init__(self, factory_config ):
#         self.label = label
        self.factory_config = factory_config

        # ===== GPIO setup (trigger line on gpiochip6, line 2) =====
        self.chip = gpiod.Chip("gpiochip6")
        self.trigger_line = self.chip.get_line(2)
        self.trigger_line.request(consumer="spi_trigger", type=gpiod.LINE_REQ_DIR_OUT)

        # ===== SPI setup =====
        self.spi = spidev.SpiDev()
        self.spi.open(2, 0)                # /dev/spidev2.0
        self.spi.max_speed_hz = 10_000_000 # 10 MHz
        
        if self.factory_config in ('A'):
            self.spi.mode = 0                  # SpiMode=1 from your WinCE code
            self.spi.bits_per_word = 8        # 16-bit words like PackedMode
        if self.factory_config in ('B' , 'C' , 'D','E'):
            self.spi.mode = 0                 # SpiMode=1 from your WinCE code
            self.spi.bits_per_word = 16        # 16-bit words like PackedMode
        # if self.factory_config in ('E'):
        #     self.spi.mode = 1                 # SpiMode=1 from your WinCE code
        #     self.spi.bits_per_word = 16        # 16-bit words like PackedMode
            
            
        self.spi.lsbfirst = False

        # ===== Data patterns =====
        # Each number here is a 16-bit word
        self.spiData_1_MIC = [0xD414, 0x0001]
        self.spiData_2_MIC = [0xD414, 0x0001]
        self.spiData_3_MIC = [0xD414, 0x0001]
        self.spiData_4_MIC = [0xD414, 0x0001]
        
        self.link_active = True
        self.sum_1 = 0
        self.sum_2 = 0
        self.sum_3 = 0

    def trigger_pulse(self):
        self.trigger_line.set_value(1)
        time.sleep(0.001)  # 0.1 ms high
        self.trigger_line.set_value(0)

    def spi_transfer(self, words):
        tx_bytes = []
        for w in words:
            tx_bytes.append((w >> 8) & 0xFF)
            tx_bytes.append(w & 0xFF)

        rx_bytes = self.spi.xfer2(tx_bytes)

        # convert RX bytes → 16-bit words
        rx_words = []
        for i in range(0, len(rx_bytes), 2):
            rx_word = (rx_bytes[i+1] << 8) | rx_bytes[i]
            rx_words.append(rx_word)

        return rx_words

    def to_signed_16(self, x):
        """Convert unsigned 16-bit to signed short."""
        return x - 0x10000 if x & 0x8000 else x
    

    def spi_value_emitter(self):
        """Original infinite loop method - NOT recommended for UI thread."""
        counter = 0
        try:
            while self.link_active:
                spi_values = []
                
                self.trigger_pulse()
                
                if self.factory_config in ('A'):
                    self.trigger_pulse()
                    rx1 = self.spi_transfer(self.spiData_1_MIC)
                    #print(rx1,'second rx1')
                    self.trigger_pulse()
                    rx2 = self.spi_transfer(self.spiData_2_MIC)
                    self.trigger_pulse()
                    rx3 = self.spi_transfer(self.spiData_3_MIC)
                    self.trigger_pulse()
                    rx4 = self.spi_transfer(self.spiData_4_MIC)
                    
                    #print(rx1[0],rx1[1],'aaa')
                    #print('yes',rx1[0] << 8)

                    spi_1 = (rx1[0] << 8) + rx1[1]
                    spi_values.append(spi_1)
                    
                    spi_2 = (rx2[0] << 8) | rx2[1]
                    spi_values.append(spi_2)
                    
                    spi_3 = (rx3[0] << 8) | rx3[1]
                    spi_values.append(spi_3)
                    
                    spi_4 = (rx4[0] << 8) | rx4[1]
                    spi_values.append(spi_4)
                    
                    
                if self.factory_config in ('B'):
                    self.trigger_pulse()
                    rx1 = self.spi_transfer(self.spiData_1_MIC)
                    spi_1 = self.to_signed_16(rx1[0]) # - 32767
                    #print(f"FINAL:{spi_1}")
                    spi_values.append(spi_1)
                    #sum_1=sum_1+int(spi_1)
                    time.sleep(0.05)
                    
                if self.factory_config in ('C'):
                    self.trigger_pulse()
                    rx1 = self.spi_transfer(self.spiData_1_MIC)
                    rx2 = self.spi_transfer(self.spiData_2_MIC)
                    spi_1 = self.to_signed_16(rx1[0]) #- 32767
                    spi_2 = self.to_signed_16(rx2[0]) #- 32767
                    spi_values.append(spi_1)
                    spi_values.append(spi_2)
                    
                if self.factory_config in ('D'):
                    self.trigger_pulse()
                    rx1 = self.spi_transfer(self.spiData_1_MIC)
                    rx2 = self.spi_transfer(self.spiData_2_MIC)
                    rx3 = self.spi_transfer(self.spiData_3_MIC)
                    spi_1 = self.to_signed_16(rx2[0]) #- 32767
                    spi_2 = self.to_signed_16(rx2[0]) #- 32767
                    spi_3 = self.to_signed_16(rx3[0]) #- 32767
                    spi_values.append(spi_1)
                    spi_values.append(spi_3)
                    spi_values.append(spi_2)
                    
                if self.factory_config in ('E'):
                    self.trigger_pulse()
                    rx1 = self.spi_transfer(self.spiData_1_MIC)
                    rx2 = self.spi_transfer(self.spiData_2_MIC)
                    rx3 = self.spi_transfer(self.spiData_3_MIC)
                    rx4 = self.spi_transfer(self.spiData_4_MIC)
                    spi_1 = self.to_signed_16(rx1[0]) #- 32767
                    spi_2 = self.to_signed_16(rx2[0]) #- 32767
                    spi_3 = self.to_signed_16(rx3[0]) #- 32767
                    spi_4 = self.to_signed_16(rx4[0]) #- 32767
                    spi_values.append(spi_1)
                    spi_values.append(spi_2)
                    spi_values.append(spi_3)
                    spi_values.append(spi_4)
                    time.sleep(0.05)
                
                yield spi_values
        except KeyboardInterrupt:
            print("Error in spi Value emitter")
        finally:
            self.trigger_line.set_value(0)
            self.chip.close()
            self.spi.close()

