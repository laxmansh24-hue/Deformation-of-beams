import formulas as fs 
import json
with open("config.json") as f:
    data = json.load(f)
L=10
# material = {"E":210e9, "I": 0.0002}
# loads = [10,20,30,40]
E=data["materials"][0]["E"]
I = data["materials"][0]["I"]
for l in data["loads"]:
    ss_def = fs.ss(l,L,E,I)
    cl_def = fs.cl(l,L,E,I)
    print(f"For load of {l}, the maximum deflection in simply supported beam is {ss_def:.6f}\n")
    print(f"For load of {l}, the maximum deflection in cantilever beam is {cl_def:.6f}\n")
    
    
