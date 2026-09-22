import gpiod
import time
from PySide2.QtCore import QThread, Signal

class GpioInputHandler(QThread):
    """
    GPIO Input Handler: Continuously monitors specific GPIO pin.
    - Detects HIGH: triggers specific_task()
    - Waits for LOW: resets procedure
    - Loops continuously
    """
    
    high_detected = Signal()
    low_reset = Signal()
    status_changed = Signal(str)
    
    def __init__(self,main_obj, chip_name="gpiochip3", input_line=16):
        super().__init__()
        self.main_obj = main_obj
        self.chip_name = chip_name  # Configurable: e.g., "gpiochip0"
        self.input_line = input_line  # Configurable GPIO line number
        self.chip = None
        self.input_line_obj = None
        self.running = True
    
    def run(self):
        try:
            self.status_changed.emit("Initializing GPIO...")
            self.chip = gpiod.Chip(self.chip_name)
            self.input_line_obj = self.chip.get_line(self.input_line)
            self.input_line_obj.request(
                consumer="input_handler",
                type=gpiod.LINE_REQ_DIR_IN,
                flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP  # Optional pull-up
            )
            self.status_changed.emit(f"Monitoring {self.chip_name}:{self.input_line} (HIGH -> task -> LOW -> repeat)")
            
            while self.running:

                if self.main_obj.stacked.currentIndex() == 25:
                
                    # Seek HIGH
                    while self.running and self.input_line_obj.get_value() == 0:
                        self.msleep(10)  # Poll efficiently
                    
                    if not self.running:
                        break
                    
                    self.status_changed.emit("HIGH detected - running task")
                    self.high_detected.emit()
                    self.specific_task()
                    
                    # Wait for LOW after task
                    while self.running and self.input_line_obj.get_value() == 1:
                        self.msleep(10)
                    
                    if self.running:
                        self.low_reset.emit()
                        self.status_changed.emit("LOW detected - reset, seeking HIGH again")
        
        except Exception as e:
            self.status_changed.emit(f"Error: {str(e)}")
            print(f"GPIO Handler Error: {e}")
        finally:
            self.cleanup()
    
    def specific_task(self):
        """
        OVERRIDE THIS or connect high_detected signal.
        Specific task when HIGH detected.
        Example: self.parent().some_ui_toggle() or DB save, etc.
        """
        print("GPIO HIGH: Save The Value")

        # self.data.save_probe_unique_settings()
        # self.ui.spi_controller.save_probe_values()

        if self.main_obj.stacked.currentIndex() == 25:
            self.main_obj.button_save.click()
        
        # time.sleep(1)  # Example debounce/duration
        pass
    
    def stop(self):
        self.running = False
        self.wait(1000)
    
    def cleanup(self):
        if self.input_line_obj:
            self.input_line_obj.release()
        if self.chip:
            del self.chip
        self.status_changed.emit("GPIO handler stopped")

# Example usage:
# handler = GpioInputHandler(chip_name="gpiochip6", input_line=3)
# handler.high_detected.connect(lambda: print("Custom task!"))
# handler.start()

