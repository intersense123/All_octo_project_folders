import subprocess
from sqlalchemy.orm import *
import ipaddress
import dbus
import socket
import os
from PySide2.QtCore import QTimer, QTime, QDate

from math import *
import re

class Utilities:
    def __init__(self, main_window):
        # self.label_time = label_time
        # self.label_date = label_date
        # self.lineEdit_formulaBar = lineEdit_formulaBar
        self.ui = main_window
        self.timer = None
        
    def validate_formulabar(self):
        def avg(*args):
            total = sum(args)
            count = len(args)
            return total / count if count > 0 else 0
        
        def cosec(x):
            """Return cosecant of x (in radians)"""
            # if sin(x) == 0:
            #     raise ValueError("cosec undefined for this angle (sin(x)=0)")
            return 1 / sin(x)

        def sec(x):
            """Return secant of x (in radians)"""
            # if cos(x) == 0:
            #     raise ValueError("sec undefined for this angle (cos(x)=0)")
            return 1 / cos(x)

        def cot(x):
            """Return cotangent of x (in radians)"""
            # if tan(x) == 0:
            #     raise ValueError("cot undefined for this angle (tan(x)=0)")
            return 1 / tan(x) 
        
        # formula = re.sub(r'P\d+', '2.5', self.lineEdit_formulaBar.text())
        # formula_1 = re.sub(r'D\d+', '2.5', self.lineEdit_formulaBar.text())
        formula = re.sub(r'\b[PD][1-8]\b', '2.5', self.ui.lineEdit_formulaBar.text())

        # print(formula)
        if formula == '' :
            self.ui.lineEdit_formulaBar.setStyleSheet("background-color: red;")
            return
        
        try:
            exec(formula)
            self.ui.lineEdit_formulaBar.setStyleSheet("background-color: green;")
        except:
            self.ui.lineEdit_formulaBar.setStyleSheet("background-color: red;")
    
    def is_raspberry_pi(self) -> bool:
        """Returns True if running on Raspberry Pi"""
        try:
            model_file = "/sys/firmware/devicetree/base/model"
            if os.path.exists(model_file):
                with open(model_file, "r") as f:
                    model = f.read().strip()
                    return "Raspberry Pi" in model
            return False
        except Exception as e:
            print("Error detecting Raspberry Pi:", e)
            return False

    def is_imx7(self) -> bool:
        """Returns True if running on i.MX7"""
        try:
            model_file = "/sys/firmware/devicetree/base/model"
            if os.path.exists(model_file):
                with open(model_file, "r") as f:
                    model = f.read().strip().lower()
                    return "imx7" in model
            return False
        except Exception as e:
            print("Error detecting i.MX7:", e)
            return False

    def set_static_ip(self, ip_address: str, subnet_mask: str, gateway: str):
        """Set static IP on Raspberry Pi"""
        try:
            mask_to_cidr = {
                "255.0.0.0": "8",
                "255.255.0.0": "16",
                "255.255.255.0": "24",
                "255.255.255.128": "25",
                "255.255.255.192": "26",
                "255.255.255.224": "27",
                "255.255.255.240": "28",
                "255.255.255.248": "29",
                "255.255.255.252": "30",
                "255.255.255.254": "31",
                "255.255.255.255": "32",
            }
            cidr = mask_to_cidr.get(subnet_mask.strip())
            if not cidr:
                raise ValueError(f"Invalid subnet mask: {subnet_mask}")

            subprocess.run([
                "sudo", "nmcli", "connection", "modify", "Wired connection 1",
                "ipv4.addresses", f"{ip_address}/{cidr}",
                "ipv4.gateway", gateway,
                "ipv4.method", "manual",
                "ipv4.dns", "8.8.8.8"
            ], check=True)
            subprocess.run(["sudo", "nmcli", "connection", "down", "Wired connection 1"], check=True)
            subprocess.run(["sudo", "nmcli", "connection", "up", "Wired connection 1"], check=True)
            print(f"✅ Static IP {ip_address}/{cidr} set successfully.")
        except Exception as e:
            print("❌ Failed to set static IP:", e)

    def set_static_ip_imx7(self, ip_addr, subnet_mask, gateway, iface='ethernet0'):
        """Set static IP on i.MX7"""
        try:
            bus = dbus.SystemBus()
            cidr = ipaddress.IPv4Network(f"0.0.0.0/{subnet_mask}").prefixlen
            ip_uint = dbus.UInt32(socket.htonl(int(ipaddress.IPv4Address(ip_addr))))
            gateway_uint = dbus.UInt32(socket.htonl(int(ipaddress.IPv4Address(gateway))))
            ip_config = dbus.Array([dbus.Array([ip_uint, dbus.UInt32(cidr), gateway_uint], signature='u')], signature='au')

            settings_obj = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
            settings = dbus.Interface(settings_obj, "org.freedesktop.NetworkManager.Settings")

            conn_obj = None
            for path in settings.ListConnections():
                conn = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager", path),
                                      "org.freedesktop.NetworkManager.Settings.Connection")
                if conn.GetSettings()['connection']['interface-name'] == iface:
                    conn_obj = conn
                    break

            new_settings = {
                'connection': {'id': iface, 'type': '802-3-ethernet', 'interface-name': iface},
                'ipv4': {'method': 'manual', 'addresses': ip_config, 'gateway': gateway,
                         'dns': dbus.Array([dbus.UInt32(socket.htonl(int(ipaddress.IPv4Address('8.8.8.8'))))], signature='u')},
                'ipv6': {'method': 'ignore'}
            }

            if conn_obj is None:
                conn_obj_path = settings.AddConnection(new_settings)
            else:
                conn_obj.Update(new_settings)
                conn_obj_path = conn_obj.object_path

            nm_obj = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
            nm = dbus.Interface(nm_obj, "org.freedesktop.NetworkManager")

            dev_path = None
            for d in nm.GetDevices():
                dev = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager", d), "org.freedesktop.DBus.Properties")
                if str(dev.Get("org.freedesktop.NetworkManager.Device", "Interface")) == iface:
                    dev_path = d
                    break

            if dev_path is None:
                raise RuntimeError(f"Device {iface} not found")

            nm.ActivateConnection(conn_obj_path, dev_path, "/")
            print(f"Permanent IP set: {ip_addr}/{cidr} on {iface}, gateway {gateway}")
        except Exception as e:
            print("❌ Failed to set static IP on i.MX7:", e)

    def apply_static_ip(self, ip: str, subnetmask: str, gateway: str):
        """Apply static IP depending on board type"""
        try:
            if self.is_raspberry_pi():
                print("Detected Raspberry Pi → Applying static IP...")
                self.set_static_ip(ip, subnetmask, gateway)
            elif self.is_imx7():
                print("Detected i.MX7 → Applying static IP...")
                self.set_static_ip_imx7(ip, subnetmask, gateway)
            else:
                raise RuntimeError("❌ Unknown device: Neither Raspberry Pi nor i.MX7 detected.")
        except Exception as e:
            print("Error applying static IP:", e)

    def update_display(self):
        """Update the top labels with current time and date"""
        try:
            current_time = QTime.currentTime()
            self.ui.label_time.setText(current_time.toString('hh:mm:ss'))
            current_date = QDate.currentDate()
            self.ui.label_date.setText(current_date.toString('dd-MM-yyyy'))
        except Exception as e:
            print("Error updating display:", e)

    def set_system_time_raspberyPi(self):
        """Set Raspberry Pi system time"""
        try:
            day = int(self.ui.lineEdit_day.text())
            month = int(self.ui.lineEdit_month.text())
            year = int(self.ui.lineEdit_year.text())
            hour = int(self.ui.lineEdit_hours.text())
            minute = int(self.ui.lineEdit_minutes.text())

            time_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:00"
            os.system(f'sudo date -s "{time_str}"')
            self.update_display()
            print(f"System time set: {time_str}")
        except Exception as e:
            print("❌ Failed to set system time on Raspberry Pi:", e)

    def set_system_time_imx7(self):
        """Set i.MX7 system time"""
        try:
            day = int(self.ui.lineEdit_day.text())
            month = int(self.ui.lineEdit_month.text())
            year = int(self.ui.lineEdit_year.text())
            hour = int(self.ui.lineEdit_hours.text())
            minute = int(self.ui.lineEdit_minutes.text())

            datetimestr = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"
            subprocess.run(["sudo", "date", "-s", datetimestr], check=True)
            subprocess.run(["sudo", "hwclock", "--systohc", "--utc"], check=True)
            self.update_display()
            print("System time and RTC updated successfully.")
        except Exception as e:
            print("❌ Failed to set system time on i.MX7:", e)

    def start_clock_updates(self):
        """Start QTimer to update clock every second"""
        try:
            if not self.timer:
                self.timer = QTimer()
                self.timer.timeout.connect(self.update_display)
                self.timer.start(1000)
                self.update_display()
        except Exception as e:
            print("❌ Failed to start clock updates:", e)

    def Wifi_Settings(self, ssid: str, password: str):
        """Connect Raspberry Pi to WiFi"""
        try:
            ssid = ssid.strip()
            password = password.strip()
            subprocess.run(["sudo", "iwconfig", "wlan0", "essid", ""], check=True)
            network_id = subprocess.run(["wpa_cli", "-i", "wlan0", "add_network"],
                                        capture_output=True, text=True, check=True).stdout.strip()
            subprocess.run(["sudo", "wpa_cli", "-i", "wlan0", "set_network", network_id, "ssid", f'"{ssid}"'], check=True)
            subprocess.run(["sudo", "wpa_cli", "-i", "wlan0", "set_network", network_id, "psk", f'"{password}"'], check=True)
            subprocess.run(["sudo", "wpa_cli", "-i", "wlan0", "enable_network", network_id], check=True)
            subprocess.run(["sudo", "wpa_cli", "-i", "wlan0", "select_network", network_id], check=True)
            subprocess.run(["sudo", "wpa_cli", "-i", "wlan0", "save_config"], check=True)
            subprocess.run(["sudo", "dhclient", "wlan0"], check=True)
            connected_ssid = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True).stdout.strip()
            if connected_ssid == ssid:
                print(f"✅ Connected to WiFi: {ssid}")
            else:
                print(f"❌ Failed to connect. Current SSID: '{connected_ssid}'")
        except Exception as e:
            print("❌ Failed to configure WiFi:", e)

    def shutdown_device(self):
        """Shutdown device based on board type"""
        try:
            if self.is_raspberry_pi():
                print("Shutting down Raspberry Pi...")
                os.system("sudo shutdown -h now")
            elif self.is_imx7():
                print("Shutting down i.MX7...")
                subprocess.run([
                    "dbus-send",
                    "--system",
                    "--print-reply",
                    "--dest=org.freedesktop.login1",
                    "/org/freedesktop/login1",
                    "org.freedesktop.login1.Manager.PowerOff",
                    "boolean:true"
                ], check=True)
            else:
                print("⚠️ Unknown board: Cannot shutdown.")
        except Exception as e:
            print("❌ Failed to shutdown device:", e)

    def restart_device(self):
        """Restart device based on board type"""
        try:
            if self.is_raspberry_pi():
                print("Reboot Raspberry Pi...")
                os.system("sudo reboot")
            elif self.is_imx7():
                print("Reboot i.MX7...")
                subprocess.run([
                    "dbus-send",
                    "--system",
                    "--print-reply",
                    "--dest=org.freedesktop.login1",
                    "/org/freedesktop/login1",
                    "org.freedesktop.login1.Manager.Reboot",
                    "boolean:true"
                ], check=True)
            else:
                print("⚠️ Unknown board: Cannot reboot.")
        except Exception as e:
            print("❌ Failed to restart device:", e)
