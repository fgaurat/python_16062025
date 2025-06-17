import json

def main():
    csv_file = "MOCK_DATA.csv"
    all_data = []
    with open(csv_file) as f:
        data = f.readlines()
        keys = data[0].strip()
        values = [d.strip() for d in data[1:]]
        
        # séparer une chaîne : s.split(',')
        # "value01,value02,value03" => ["value01","value02","value03"]

        list_keys = keys.split(',')# ["id","first_name","last_name","email","gender","ip_address"]
        for value in values:
            print(value)
            list_values = value.split(',') # ["1","Hedwig,Feathersby,hfeathersby0@google.cn,Female,151.145.34.217"]
      
            # ["id","first_name","last_name","email","gender","ip_address"]
            # ["1","Hedwig,Feathersby,hfeathersby0@google.cn,Female,151.145.34.217"]
            d = dict(zip(list_keys,list_values))
            all_data.append(d)


    with open("output.json","w") as f:
        json.dump(all_data,f)
            


if __name__=='__main__':
    main()
    # l =["val01","val02"]
    # ";".join(l) #"val01;val02"
