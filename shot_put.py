def main():
    print("Enter the lengths of the throws (m) separated by commas.")
    heitot = input()
    if heitot =="":
        print("No accepted results.")
    else:
        heitot_erikseen = heitot.split(",")
        heitto_lista=[]
        for i in heitot_erikseen:
            heitto_lukuna = float(i)
            heitto_lista.append(heitto_lukuna)
        res_max = max(float(sub) for sub in heitto_lista)
        print("The best result is {:.2f} m.".format(res_max))


main()