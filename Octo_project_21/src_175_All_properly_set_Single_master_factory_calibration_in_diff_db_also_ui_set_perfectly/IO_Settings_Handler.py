import time
import threading
import gpiod

class RelayController:
    def __init__(self):
        try:
            # ✅ Replace LED paths with GPIO mapping
            self.green_led = ("gpiochip1", 26)   # SODIMM_133
            self.red_led = ("gpiochip0", 2)      # SODIMM_135
            self.yellow_led = ("gpiochip4", 11)  # SODIMM_98

            self.lines = {}
            self._init_gpio()

            self.current_thread = None
            self.lock = threading.Lock()
            self._generation = 0
            self._stop_event = None
        except Exception as e:
            print(f"Error initializing RelayController: {e}")

    def _init_gpio(self):
        try:
            # Initialize all GPIO lines
            for name, (chip_name, line_no) in {
                "green": self.green_led,
                "red": self.red_led,
                "yellow": self.yellow_led
            }.items():
                try:
                    chip = gpiod.Chip(chip_name)
                    line = chip.get_line(line_no)

                    line.request(
                        consumer=f"relay_{name}",
                        type=gpiod.LINE_REQ_DIR_OUT,
                        default_vals=[0]
                    )

                    self.lines[name] = line

                except Exception as e:
                    print(f"GPIO init error ({name}): {e}")
        except Exception as e:
            print(f"Error initializing GPIO lines: {e}")

    def set_led(self, led, val):
        try:
            # 🔥 led is now ("gpiochipX", line)
            for name, gpio in {
                "green": self.green_led,
                "red": self.red_led,
                "yellow": self.yellow_led
            }.items():
                if led == gpio:
                    self.lines[name].set_value(1 if val else 0)
        except Exception as e:
            print(f"GPIO error: {e}")

    def turn_all_off(self):
        try:
            # Turn off every configured LED line safely
            self.set_led(self.green_led, 0)
            self.set_led(self.red_led, 0)
            self.set_led(self.yellow_led, 0)
        except Exception as e:
            print(f"Error turning all LEDs off: {e}")

    def trigger(self, color, duration):
        try:
            with self.lock:
                # Never join from the GUI thread: joining here can freeze the
                # dial for the previous relay duration. A generation protects a
                # newer relay output from an older worker's cleanup.
                if self._stop_event is not None:
                    self._stop_event.set()

                self._generation += 1
                generation = self._generation
                stop_event = threading.Event()
                self._stop_event = stop_event
                self.current_thread = threading.Thread(
                    target=self._run, args=(color, duration, generation, stop_event),
                    daemon=True
                )
                self.current_thread.start()
        except Exception as e:
            print(f"Error triggering relay: {e}")
    def _run(self, color, duration, generation, stop_event):
        try:
            # 🔥 Select GPIO instead of LED path
            if color == "green":
                led = self.green_led
            elif color == "red":
                led = self.red_led
            elif color == "yellow":
                led = self.yellow_led
            else:
                return

            with self.lock:
                if stop_event.is_set() or generation != self._generation:
                    return
                self.turn_all_off()
                self.set_led(led, 1)

            start_time = time.time()

            # 🔴 Controlled sleep (can be interrupted)
            stop_event.wait(max(0.0, duration))

            with self.lock:
                if generation == self._generation:
                    self.set_led(led, 0)
        except Exception as e:
            print(f"Error running relay thread: {e}")

    def cleanup(self):
        # Optional but recommended
        for line in self.lines.values():
            try:
                line.set_value(0)
                line.release()
            except Exception as e:
                print(f"Error cleaning up GPIO line: {e}")
