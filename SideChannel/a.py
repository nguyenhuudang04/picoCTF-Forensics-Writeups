import subprocess
import time

def run_checker(pin):
    start = time.perf_counter()
    proc = subprocess.run(['./pin_checker'], input=(pin + '\n').encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = time.perf_counter()
    duration = end - start
    return duration, proc.stdout.decode()

def find_pin():
    pin = ""
    for i in range(8): 
        timings = {}
        for d in "0123456789":
            guess = pin + d + "0" * (7 - i)  
            times = []
            for _ in range(3): 
                t, _ = run_checker(guess)
                times.append(t)
            avg = sum(times) / len(times)
            timings[d] = avg
            print(f"Trying {guess} | avg time: {avg:.5f}s")
        best_digit = max(timings, key=timings.get)
        pin += best_digit
        print(f"[+] Found digit {i+1}: {best_digit} -> PIN so far: {pin}")
    return pin
pin = find_pin()
print(f"[!] Guessed PIN: {pin}")
