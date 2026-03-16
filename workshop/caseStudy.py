def calculate_grade(f):
    try:
        with open(f,"r") as file:
            lines = file.readlines()
            header = lines[0].strip().split("\t")
            print("Header:", header)
            finalgrade={}
            for line in lines[1:]:
                data = line.strip().split("\t")

                name = data[0]
                a1 = float(data[1])
                a2 = float(data[2])
                a3 = float(data[3])
                finalgrade[name] =(round(0.3*a1)+round(0.3* a2)+round(0.4* a3))
                print(name, a1, a2, a3)
            for i in finalgrade.keys():
                print(i,finalgrade[i])

    except FileNotFoundError:
        print("Oops file not found")
    
calculate_grade("/Users/sandeepkatta77/Downloads/week1-case.txt")