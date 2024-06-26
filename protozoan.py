

class Protozoan:

    NUMBER_OF_GENES = 10
    GENE_MIN_VALUE = 0
    GENE_MAX_VALUE = 5

    def __init__(self,given_name,genelist):
        self.__name = given_name
        if self.check(genelist)== True:
            self.__genes = []+genelist
        else:
            self.__genes = [0,0,0,0,0,0,0,0,0,0]



    def check(self,genelist):
        if len(genelist) !=Protozoan.NUMBER_OF_GENES:
            return False
        for geeni in genelist:
            if Protozoan.GENE_MIN_VALUE > geeni or geeni > Protozoan.GENE_MAX_VALUE:
                return False
        return True


    def get_name(self):
        return self.__name

    def get_genes(self):
        return self.__genes

    def mutation(self,gene_no,new_gene):
        if 0 <= gene_no <= 9 and 0 <= new_gene <= 5:
            self.__genes[gene_no] = new_gene
            return True
        else:
            return False

    def clone(self,clone_name):
        olio = Protozoan(clone_name,self.__genes)
        return olio

    def mate(self,another_protozoan,descendant_name):
        lista = [0,0,0,0,0,0,0,0,0,0]
        i = 0
        while i < len(lista):
            if i!=1 and i!=3 and i!=5 and i!=7 and i!=9:
                geeni = another_protozoan.__genes[i]
                lista[i] = geeni
                i+=1
            else:
                geeni = self.__genes[i]
                lista[i] = geeni
                i+=1
        olio_2 = Protozoan(descendant_name,lista)
        return olio_2

    def __str__(self):
        string = "Name: "+self.__name+", genes: "+str(self.__genes)+""
        return string
