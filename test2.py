import time
start = time.time()
print("START TIMER")
vExit = "start"
while vExit == "start":
    if time.time() - start < 5:
        x = round(time.time() - start) +1)
        
print("END TIMER")
