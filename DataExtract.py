import csv

with open('Data_2DMat.csv','w') as f1: #output file
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    f = open("rawdbjson.txt", "r") #input file
    header = ["Formula"] + ["Space Group"] + ["Band Gap"] + ["a"] +["b"] +["c"]
    writer.writerow(header) 
    for x in f:
            form = x.find("formula")+17
            end1 = x.find("\"",form)
            lat = x.find("lattice")
            lata = x.find(":", lat+9)+1
            enda = x.find(",",lata)
            latc = x.find(":",lata)+1
            endc = x.find(",",latc)
            latb = x.find(":",latc)+1
            endb = x.find(",",latb)
            sg = x.find("sg_symbol")+12
            end2 = x.find("\"", sg)
            band = x.find("bandstructure")+26
            end3 = x.find(",",band)
            row =  [x[form:end1]] +[x[sg:end2]]+[x[band:end3]]+[x[lata:enda]]+[x[latb:endb]]+[x[latc:endc]]
            writer.writerow(row)
