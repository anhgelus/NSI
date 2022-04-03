class CodeDeCesar:
    """
    Ensemble de méthode pour utiliser le Code de César
    """
    def encrypt(self, text: str, decal: int):
        """
        Chiffre un message
        :param text: Message à chiffrer
        :param decal: Décalage à effectuer
        :return: Message chiffré
        """
        if decal < 0:
            print("Il n'est pas possible de chiffrer avec un chiffre négatif")
            return

        crypted = self.__crypt(text, decal)

        print("Texte entrée : " + text)
        print("Décalage : " + str(decal))
        print("Résultat : " + crypted)

        return crypted

    def decrypt(self, text: str, decal: int):
        """
        Déchiffre un message
        :param text: Message à déchiffrer
        :param decal: Décalage
        :return: Message déchiffré
        """
        if decal < 0:
            print("Il n'est pas possible de chiffrer avec un chiffre négatif")
            return

        decal_de = 26 - decal  # Inverse le décalage pour déchiffrer le message

        print("Texte entrée : " + text)
        print("Décalage : " + str(decal))
        print("Résultat : " + self.__crypt(text, decal_de))

    def __crypt(self, text: str, decal: int):
        """
        Permet de retourner le résultat du chiffrement
        :param text: Text original
        :param decal: Décalage
        :return: Chiffrement
        """
        result = ""

        dico_down = self.__get_dico(decal, "down")  # Génère le dictionnaire pour les minuscules
        dico_up = self.__get_dico(decal, "up")  # Génère le dictionnaire pour les majuscules

        for i in range(len(text)):  # Pour chaque caractère
            if text[i].islower():  # S'il est minuscule
                result += dico_down.get(text[i], " ")  # Ajout du caractère chiffrer ; si le caractère est inconnu,
                # il sera remplacé par un espace
            else:  # S'il n'est pas minuscule
                result += dico_up.get(text[i], " ")  # Ajout du caractère chiffrer ; si le caractère est inconnu,
                # il sera remplacé par un espace

        return result

    @staticmethod
    def __get_dico(decal: str, type: str):
        """
        Permet de récupérer le dictionnaire chiffrer
        :param decal: Décalage à effectuer
        :param type: Si le dictionnaire doit être majuscule (up) ou minuscule (down)
        :return: Le dictionnaire chiffré
        """
        letters_down = "abcdefghijklmnopqrstuvwxyz"  # Alphabet latin minuscule
        letters_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alphabet latin majuscule
        dico = {}  # Initialise le dictionnaire
        lenm = len(letters_down)  # Récupère la longueur de l'alphabet
        decal = int(decal)  # Transforme le décalage en entier si ce n'est le cas

        for i in range(lenm):  # Pour chaque lettre dans l'alphabet
            if type == "up":  # Si le type est up
                if i + decal >= lenm:  # Si la somme de i + decal dépasse la longueur de l'alphabet, alors on recompte à
                    # partir de 0
                    dico[letters_up[i]] = letters_up[i + decal - 26]  # Ajout de la lettre dans le dictionnaire
                else:
                    dico[letters_up[i]] = letters_up[i + decal]  # Ajout de la lettre dans le dictionnaire
            elif type == "down":  # Si le type est down
                if i + decal >= lenm:  # Si la somme de i + decal dépasse la longueur de l'alphabet, alors on recompte à
                    # partir de 0
                    dico[letters_down[i]] = letters_down[i + decal - 26]  # Ajout de la lettre dans le dictionnaire
                else:
                    dico[letters_down[i]] = letters_down[i + decal]  # Ajout de la lettre dans le dictionnaire
        return dico
