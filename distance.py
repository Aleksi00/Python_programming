import math
def calculate_distance_between_points(point1,point2):
    x1=float(point1[0])
    y1= float(point1[1])
    x2= float(point2[0])
    y2=float(point2[1])
    etaisyys = math.sqrt(((x2-x1))**2+((y2-y1)**2))
    return etaisyys
def calculate_total_distance(point_list):
    i = 0
    summa = 0
    while i < len(point_list):
        if point_list[i+1]==point_list[-1]:
            summa += calculate_distance_between_points(point_list[i],point_list[i+1])
            break
        summa+=calculate_distance_between_points(point_list[i],point_list[i+1])
        i+=1
    return summa




def main():
    koordinaatit = input("Enter the coordinates in the format 'x,y'. Stop with an empty line.\n")
    koordinaatit_erikseen = koordinaatit.split(",")
    if koordinaatit != "" and len(koordinaatit_erikseen)!=2:
        while len(koordinaatit_erikseen)!=2:
            print("Enter the coordinates in the format 'x,y'")
            koordinaatit = input("Enter the coordinates:\n")
            koordinaatit_erikseen = koordinaatit.split(",")
    pistelista =[]
    pistelista.append(koordinaatit_erikseen)
    while koordinaatit!="":
        koordinaatit = input("Enter the coordinates:\n")
        koordinaatit_erikseen = koordinaatit.split(",")
        if len(koordinaatit_erikseen)!=2 and koordinaatit!="":
            print("Enter the coordinates in the format 'x,y'.")
        elif len(koordinaatit_erikseen)==2:
            pistelista.append(koordinaatit_erikseen)
    if len(pistelista)<2:
        print("Not enough data.")
    else:
        etaisyys = calculate_distance_between_points(pistelista[0],pistelista[-1])
        kokoetaisyys = calculate_total_distance(pistelista)
        print("The total distance going through all the points is {:.2f} units long.".format(kokoetaisyys))
        print("The straight line from the starting point to the end is {:.2f} units long.".format(etaisyys))



main()