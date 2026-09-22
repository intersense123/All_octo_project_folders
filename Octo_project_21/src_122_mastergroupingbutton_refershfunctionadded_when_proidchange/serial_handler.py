import serial
import time

class SerialHandler:
    """
    Class for serial communication handling with comprehensive exception handling.
    """
    def __init__(self, port, baud_rate, parity, stopbits, data_bits):
        """
        Initialize and open serial connection.
        
        :param port: Serial port (e.g., '/dev/ttyUSB0')
        :param baud_rate: Baud rate (e.g., 9600)
        :param parity: Parity ('N', 'E', 'O')
        :param stopbits: Stop bits (1 or 2)
        :param data_bits: Data bits (5, 6, 7, 8)
        """
        # Parameter validation
        if not isinstance(port, str):
            raise TypeError("port must be a string")
        if not isinstance(baud_rate, int) or baud_rate <= 0:
            raise ValueError("baud_rate must be a positive integer")
        
        parity_upper = parity.upper()
        parity_map = {'N': serial.PARITY_NONE, 'E': serial.PARITY_EVEN, 'O': serial.PARITY_ODD}
        if parity_upper not in parity_map:
            raise ValueError("parity must be 'N', 'E', or 'O'")
        self.parity = parity_map[parity_upper]
        
        stopbits_map = {1: serial.STOPBITS_ONE, 2: serial.STOPBITS_TWO}
        if stopbits not in stopbits_map:
            raise ValueError("stopbits must be 1 or 2")
        self.stopbits = stopbits_map[stopbits]
        
        databits_map = {5: serial.FIVEBITS, 6: serial.SIXBITS, 7: serial.SEVENBITS, 8: serial.EIGHTBITS}
        if data_bits not in databits_map:
            raise ValueError("data_bits must be 5, 6, 7, or 8")
        self.data_bits = databits_map[data_bits]
        
        self.port = '/dev/' + port
        self.baud_rate = baud_rate
        
        self.ser = serial.Serial()
        self.ser.port = '/dev/' + port
        self.ser.baudrate = baud_rate
        self.ser.parity = self.parity
        self.ser.stopbits = self.stopbits
        self.ser.bytesize = self.data_bits
        self.ser.timeout = 1
        
        try:
            self.ser.open()
        except (serial.SerialException, OSError) as e:
            self.ser.close()  # Ensure cleanup
            raise RuntimeError(f"Failed to open serial port {port}: {str(e)}") from e
    
    def send_data(self, data: str):
        """
        Send string data over serial.
        
        :param data: String to send
        :raises RuntimeError: If port not open or send fails
        """
        if not self.ser or not self.ser.is_open:
            raise RuntimeError("Serial port not open")
        if not isinstance(data, str):
            raise TypeError("data must be a string")
        try:
            self.ser.write(data.encode('utf-8'))
            self.ser.flush()  # Ensure sent
        except (serial.SerialException, OSError) as e:
            raise RuntimeError(f"Failed to send data: {str(e)}") from e
    
    def __del__(self):
        """Destructor: close serial port safely."""
        if hasattr(self, 'ser') and self.ser and self.ser.is_open:

            try:
                self.ser.close()
            except (serial.SerialException, OSError):
                pass  # Silently ignore errors in destructor
