import time
import threading

class RelayController:
    def __init__(self):
        self.green_led = "relay_led_sodimm_133"
        self.red_led = "relay_led_sodimm_135"
        self.yellow_led = "relay_led_sodimm_98"

        self.current_thread = None
        self.stop_flag = False
        self.lock = threading.Lock()

    def set_led(self, led, val):
        try:
            with open(f"/sys/class/leds/{led}/brightness", "w") as f:
                f.write(str(val))
        except Exception as e:
            print(f"LED error: {e}")

    def turn_all_off(self):
        self.set_led(self.green_led, 0)
        self.set_led(self.red_led, 0)
        self.set_led(self.yellow_led, 0)

    def trigger(self, color, duration):
        with self.lock:
            # 🔴 Stop previous thread
            self.stop_flag = True
            if self.current_thread and self.current_thread.is_alive():
                self.current_thread.join()

            # 🔴 Reset stop flag
            self.stop_flag = False

            # 🔴 Start new thread
            self.current_thread = threading.Thread(
                target=self._run, args=(color, duration)
            )
            self.current_thread.start()

    def _run(self, color, duration):
        # 🔥 Select LED
        if color == "green":
            led = self.green_led
        elif color == "red":
            led = self.red_led
        elif color == "yellow":
            led = self.yellow_led
        else:
            return

        # 🔴 Turn OFF all first
        self.turn_all_off()

        # 🔴 Turn ON selected
        self.set_led(led, 1)

        start_time = time.time()

        # 🔴 Controlled sleep (can be interrupted)
        while time.time() - start_time < duration:
            if self.stop_flag:
                break
            time.sleep(0.05)

        # 🔴 Turn OFF after duration
        self.set_led(led, 0)