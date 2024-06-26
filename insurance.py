class Insurance:

    def __init__(self, owner_name, original_premium, given_deductible, cap):
        self.__name = owner_name
        if original_premium < 0.0:
            self.__premium = 0.0
        else:
            self.__premium = original_premium
        if given_deductible < 0.0:
            self.__deductible = 150.0
        else:
            self.__deductible = given_deductible
        self.__total_compensations = 0.0
        if cap <= 0.0:
            self.__total_compensation_cap = 15000.0
        else:
            self.__total_compensation_cap = cap
        self.__valid = True
        self.__bonus = 0.0


    def get_name(self):
        return self.__name

    def get_bonus(self):
        return self.__bonus

    def get_premium(self):
        return self.__premium

    def get_deductible(self):
        return self.__deductible

    def get_total_compensations(self):
        return self.__total_compensations

    def get_total_compensation_cap(self):
        return self.__total_compensation_cap

    def is_valid(self):
        return self.__valid

    def set_premium(self,new_premium):
        if new_premium >= 0.0:
            self.__premium = new_premium

    def set_deductible(self,new_deductible):
        if new_deductible >= 0:
            self.__deductible = new_deductible

    def increase_bonus(self,increase):
        if increase >0.0:
            self.__bonus+=increase
            if self.__bonus > 70.0:
                self.__bonus = 70.0

    def decrease_bonus(self,decrease):
        if decrease > 0.0:
            self.__bonus-=decrease
            if self.__bonus < 0.0:
                self.__bonus = 0.0

    def set_invalid(self):
        self.__valid = False

    def set_valid(self):
        self.__valid = True

    def calculate_real_premium(self):
        return (1-(self.__bonus/100))*self.__premium

    def calculate_compensation(self,damage):
        if self.__valid == True and self.__total_compensations < self.__total_compensation_cap and damage-self.__deductible>0:
            korvaus = damage-self.__deductible
            if damage+self.__total_compensations > self.__total_compensation_cap:
                korvaus = self.__total_compensation_cap - self.__total_compensations
            self.__total_compensations += korvaus
            if korvaus > 0:
                self.decrease_bonus(10)
            return korvaus
        return 0.0

    def __str__(self):
        string = "Owner: "+self.__name+", premium "+str(self.__premium)+" eur / year, bonus "+str(self.__bonus)+" %.\n"
        string = string+ "Deductible "+str(self.__deductible)+" eur, total compensation cap "+str(self.__total_compensation_cap)+" eur.\n"
        string = string+ "Total compensations currently "+str(self.__total_compensations)+" eur.\n"
        if self.__valid == True:
            string+="Insurance policy is valid."
        else:
            string += "Insurance policy is not valid."
        return string












