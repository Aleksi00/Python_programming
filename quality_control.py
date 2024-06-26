def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        product_file = open(filename,'r')
        total = 0.0
        count = 0
        optimaaliset = 0
        sallitut = 0
        virheelliset = 0
        for line in product_file:
            line = line.rstrip()
            if 4.52<=float(line)<=4.58:
                optimaaliset+=1
            elif 4.50<=float(line)<=4.60:
                sallitut+=1
            if float(line)<4.50 or float(line)>4.60:
                virheelliset+=1
            measure = float(line)
            total += measure
            count += 1


        print("File read succesfully.")

        print("The batch contained:")

        print("{} optimal ({:.1f}%)".format(optimaaliset,(optimaaliset/count)*100))
        print("{} allowed ({:.1f}%)".format(sallitut,(sallitut/count)*100))
        print("{} faulty ({:.1f}%)".format(virheelliset,(virheelliset/count)*100))
        
        if (virheelliset/count)*100 > 3:
            print("The batch didn't pass the quality inspection.")
        else:
            print("The batch passed the quality inspection.")
        product_file.close()

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except ValueError:
        print("Incorrect number in the file '{:s}'. Program ends.".format(filename))

main()
