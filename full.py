import psutil
import threading

print("Script Start!!!")

def stress_cpu_ram():
    while True:
        while psutil.cpu_percent() < 100:
            pass

        available_memory = psutil.virtual_memory().available

        data = bytearray(available_memory)
        for i in range(len(data)):
            data[i] = 0xFF

cpu_ram_thread = threading.Thread(target=stress_cpu_ram)

cpu_ram_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Programm wurde beendet.")
