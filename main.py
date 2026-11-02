# import formulas as fs 
# import json
# with open("config.json") as f:
#     data = json.load(f)
# L=10
# E=data["materials"][0]["E"]
# I = data["materials"][0]["I"]
# for l in data["loads"]:
#     ss_def = fs.ss(l,L,E,I)
#     cl_def = fs.cl(l,L,E,I)
#     print(f"For load of {l}, the maximum deflection in simply supported beam is {ss_def:.6f}\n")
#     print(f"For load of {l}, the maximum deflection in cantilever beam is {cl_def:.6f}\n")
    
import formulas as fs
import json
import csv

try:
    with open("config.json") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: Config.json doesn't exist")
except json.JSONDecodeError:
    print("Error: Invalid JSON format!")
    
E = data["E"]
I = data["I"]
solution = []
functions = {
    "ss_centre" : fs.ss_centre, 
    "ss_point" : fs.ss_point, 
    "ss_UDL" : fs.ss_UDL, 
    "cl_point" : fs.cl_point, 
    "cl_UDL" : fs.cl_UDL
}
for P in data["loads"]:
    for l in data["spans"]:
        for function in data["beam_cases"]:
            deflection = []
            x=[l/n for n in range(1,101)]
            if function == "ss_point" or function =="cl_point":
                for x in x:
                    deflection.append(functions[function](P, l, data["o_center"]*l, x, E, I))
            else:
                for x in x:
                    deflection.append(functions[function](P, l, x, E, I))
            max_deflection = max(deflection)
            # print(f"for {function}, Load: {P}, span: {l}, the maximum deflection is: {max_deflection}")
            solution.append({"Function" : function, "Load(N)" : P, "Span(m)" : l, "Maximum deflection(mm)" : round(max_deflection*10**3,6)})

try:
    with open("Deflections.csv", "w", newline="") as file:
        fieldnames = ["Function", "Load(N)", "Span(m)", "Maximum deflection(mm)" ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(solution)
        print("CSV file updated successfully.")

except PermissionError:
    print("NO PERMISSION!!")
        
            
            
            