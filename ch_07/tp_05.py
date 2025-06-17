import json
import csv

def main():
    all_data = []
    csv_file = "MOCK_DATA.csv"
    with open(csv_file,newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_data.append(row)


    with open("output2.json","w") as f:
        json.dump(all_data,f)
            


if __name__=='__main__':
    main()
    # l =["val01","val02"]
    # ";".join(l) #"val01;val02"
