import speedtest
import time 
start_time= time.time()
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

data_size = {'PNG': 0.024, 'GIF': 0.056, 'JPG': 0.084, 'DOCX': 0.048, 'PDF': .152, 'Ebook': 24, 'mp3': 28, 'DVD Movie': 32000, 'HD Movie': 52000, 'Blu-Ray Movies': 184000 }

truedownload = round(download/1000000, 2)
trueupload = round(upload/1000000, 2) 
print(f"Download Speed : {truedownload} Mbps \nUpload Speed : {trueupload} Mbps")
print(f"Speed tested in {round(time.time() - start_time)} Seconds") 
for ftype, size in data_size.items():
    if 0.024 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 0.056 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 0.084 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 0.048 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 0.152 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 24 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 28 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 32000 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 52000 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")
    elif 184000 == size:
        print(f"{ftype} would take {round(size/truedownload,3)} seconds")


