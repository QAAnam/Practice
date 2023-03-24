
try:
    with open(f"../Provided/Test_Data/jsonf.json", "r") as f:
        contents = f.read()
        print(contents)
except Exception as  e:
    print("pata nahi")
