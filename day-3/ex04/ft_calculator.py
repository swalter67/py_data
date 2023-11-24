class calculator:
    """ v1 et v2 idem lenght
    https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Vecteurs_en_Python#:~:text=Addition%20modifier&text=Alors%20pour%20avoir%20la%20somme,d'entrer%20u%2Bv.
    https://pythonforge.com/methodes-de-classes-et-statiques/"""
    
    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]):
        """ dot product of two vectors"""
        dot_prod = 0.0
        for x in v1:
            dot_prod += x * v2[v1.index(x)]
        print(f"Dot product is: {int(dot_prod)}")    

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]):
        """ add two vector"""
        add_v = []
        for x in v1:
            add_v.append(x + v2[v1.index(x)])    
        print(f"Add vector is: {[f'{val:.1f}' for val in add_v]}") 

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors 
        """
        ss_vec = []
        for i in V1: 
            ss_vec.append(i - V2[V1.index(i)])
        print(f"Sous Vector is: {[f'{val:.1f}' for val in ss_vec]}")        