from pathlib import Path
import json
import os
import sys

def merge_files(inp_files, out, out_prefix, size):
    cnt = 1
    key = ""
    os.makedirs(out, exist_ok=True)
    out_d = {"strikers": []}
    file_size = 0
    file_path = os.path.join(out, out_prefix+str(cnt)+".json")
    fp = open(file_path, "w")
    for i in inp_files:
        
        d = json.load(open(i))
        obj = d["strikers"]
        
        for o in obj:
            
            print(json.dumps(o))
            str_size = len(json.dumps(o).encode('utf-8'))
            
            if file_size + str_size < size:
                out_d["strikers"].append(o)
                file_size = file_size + str_size
            else:
                json.dump(out_d, fp)
                cnt = cnt +1
                file_path = os.path.join(out, out_prefix+str(cnt)+".json")
                fp = open(file_path, "w")
            print(str_size)
    json.dump(out_d,fp)

def process(fpath, inp, out, out_prefix, size):
    
    inp_files = []
    files = os.listdir(fpath)
    for f in files:
        if f.startswith(inp) and f.endswith('.json'):
            inp_files.append(f)

    inp_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    merge_files(inp_files, out, out_prefix, size)


process("./", "data", "out", "merged", 102)
