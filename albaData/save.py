import csv

def save_to_file(infos, file_name):
    file_name = "/mnt/c/Users/ljh23/Desktop/python-workspace/albaData/infos/"+file_name+".csv"
    file = open(file_name, mode="w")
    writer = csv.writer(file)
    writer.writerow(["location","title","time","pay","reg_date"])
    for info in infos:
        writer.writerow(list(info.values()))