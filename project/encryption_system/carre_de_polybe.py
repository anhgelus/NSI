class CarreDePolybe:
    """
    Ensemble de méthode pour utiliser le Carré de Polybe
    """
    __alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']  # pas de J car J = I

    def encrypt(self, text: str, key: str = None):
        """
        Chiffre un message avec une alphabet
        :param text: Texte à chiffrer
        :param key: Phrase qui permet de chiffrer
        :return: Message chiffré
        """
        if key is None:
            key = self.__alpha
        else:
            key = self.__create_key(key)

        crypted = ""
        text = text.upper()  # Transforme le texte en majuscule (ne supporte pas le majuscule/minuscule)
        for letter in text:
            if letter == " ":
                crypted += letter
            if letter in key:
                line = key.index(letter) // 5 + 1  # récupère la ligne
                col = key.index(letter) % 5 + 1  # récupère la colonne
                crypted += str(line) + str(col)  # mets les deux à la suite pour chiffrer
            elif letter == "J":  # comme I = J, J n'est pas dans l'alphabet basique, on le traite donc comme si
                # c'était I
                line = key.index("I") // 5 + 1
                col = key.index("I") % 5 + 1
                crypted += str(line) + str(col)

        # On affiche le résultat
        print("Texte entrée : " + text)
        print("Clef : " + self.__key_to_str(key))
        print("Résultat : " + crypted)

        return crypted

    def decrypt(self, text: str, key: str = None):
        """
        Déchiffre un message avec une alphabet
        :param text: Texte à chiffrer
        :param key: Phrase qui permet de chiffrer
        :return: Message chiffré
        """
        if key is None:
            key = self.__alpha
        else:
            key = self.__create_key(key)

        decrypted = ""
        n = 0  # compteur de caractère
        char = ""  # chaîne temporaire
        chars = []  # liste des caractères

        for c in text:  # On réunit les deux chiffres entre eux
            n += 1  # On incrément le nbr de caractère à chaque passage
            char += c  # On ajoute le charactère à la chaîne temporaire
            if char == " ":  # S'il s'agit d'un espace
                chars.append(char)  # On ajoute l'espace à la liste
                char = ""  # On reset la chaîne temporaire
                n = 0  # On reset le compteur de caractère
            elif n == 2:  # Si on a 2 charactères
                chars.append(char)  # On ajoute la chaîne temporaire à la liste
                char = ""  # On reset la chaîne temporaire
                n = 0  # On reset le compteur de caractère

        for i in chars:  # On déchiffre le duo de caractère ou l'espace
            if i == " ":  # S'il s'agit d'un espace, on skip
                decrypted += i
            else:
                cs = list(i)  # On divise le caractère actuel
                ligne = int(cs[0])  # On récupère la première partie (ligne)
                col = int(cs[1])  # On récupère la deuxième partie (colonne)
                lettre = key[((ligne - 1) * 5 + col) - 1]  # On inverse le chiffrement et on récupère la lettre
                decrypted += lettre

        # On affiche le résultat
        print("Tous les J ont été transformés en I à cause de cette méthode de chiffrement\n")
        print("Texte entrée : " + text)
        print("Clef : " + self.__key_to_str(key))
        print("Résultat : " + decrypted)

        return decrypted

    def __create_key(self, text: str):
        """
        Génère une clef à partir d'un texte
        :param text: Texte servant de clef
        :return: Clef généré à partir du texte
        """
        text = text.upper()  # Transforme la clef en majuscule (ne supporte pas le majuscule/minuscule)
        clef_valide = ""
        for ch in text:
            if ch not in clef_valide:
                if ch != "J":
                    clef_valide += ch
        if len(clef_valide) < 25:
            for ch in self.__alpha:
                if ch not in clef_valide:
                    clef_valide += ch
        return clef_valide

    @staticmethod
    def __key_to_str(key: list):
        """
        Transforme une liste en string
        :param key: Liste
        :return: Liste en string
        """
        alphabet = ""
        for i in key:
            alphabet += i
        return alphabet
