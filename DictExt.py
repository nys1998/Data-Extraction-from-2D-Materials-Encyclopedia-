import json
import csv


with open('Data_2DMat.csv','w') as f1: #output file
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    g = open("2DMatjson.txt")
    data = json.load(g)
    header = ["Formula"] + ["No. of Elements"] + ["Discovery Process"] + ["Space Group"] + ["Point Group"] +["Crystal System"]+ ["Band Gap"] +["Is Gap Direct?"]+ ["a"] +["b"] +["c"]
    writer.writerow(header)
    for line in data:
            form = line["formula_pretty"]
            nelement = line["nelements"]
            discproc = line["discovery_process"]
            sgroup = line["spacegroup"]["symbol"]
            pgroup = line["spacegroup"]["point_group"]
            crysys = line["spacegroup"]["crystal_system"]
            bandgp = line["bandstructure"]["bandgap"]
            diregp = line["bandstructure"]["is_gap_direct"]
            lata = line["structure"]["lattice"]["a"]
            latb = line["structure"]["lattice"]["b"]
            latc = line["structure"]["lattice"]["c"]
            row = [form] +[nelement] + [discproc] + [sgroup] + [pgroup] + [crysys] + [bandgp] + [diregp] + [lata] +[latb] + [latc]
            writer.writerow(row)
