class ChiffreDeVigenere:
    def encrypt(self, text: str, passcode: str):
        """
        Chiffre un message avec une phrase
        :param text: Texte à chiffrer
        :param passcode: Phrase qui permet de chiffrer
        :return: Message chiffré
        """
        crypted = ""  # Résultat à retourner

        dico_down = self.__get_dico("down")  # Génère le dictionnaire pour les minuscules
        dico_up = self.__get_dico("up")  # Génère le dictionnaire pour les majuscules

        passcode_increment = 0  # Numéro du caractère à utiliser pour chiffrer

        for i in range(len(text)):  # Pour chaque caractère
            if passcode_increment == len(passcode):  # Si on a dépassé le dernier charactère de la phrase de pass
                passcode_increment = 0  # On retourne au premier charactère

            if text[i].islower():  # S'il est minuscule
                crypted += self.__crypt_char(text[i], passcode[passcode_increment].lower(),
                                             dico_down)  # Ajout du caractère chiffrer à la chaîne de caractère ; si
                # le caractère est inconnu, il est remplacé par un espace
            else:  # S'il n'est pas minuscule
                crypted += self.__crypt_char(text[i], passcode[passcode_increment].upper(), dico_up)  # Ajout du
                # caractère chiffrer à la chaîne de caractère ; si le caractère est inconnu, il est remplacé par un
                # espace

            passcode_increment += 1  # On passe au caractère suivant

        print("Texte entrée : " + text)
        print("Passcode : " + passcode)
        print("Résultat : " + crypted)

        return crypted

    def decrypt(self, text: str, passcode: str):
        """
        Déchiffre un message avec une phrase
        :param text: Texte chiffré
        :param passcode: Phrase avec laquel le message est chiffré
        :return: Message déchiffré
        """
        decrypted = ""  # Résultat à retourner

        dico_down = self.__get_dico("down")  # Génère le dictionnaire pour les minuscules
        dico_up = self.__get_dico("up")  # Génère le dictionnaire pour les majuscules

        passcode_increment = 0  # Numéro du caractère à utiliser pour chiffrer

        for i in range(len(text)):  # Pour chaque caractère
            if passcode_increment == len(passcode):  # Si on a dépassé le dernier charactère de la phrase de pass
                passcode_increment = 0  # On retourne au premier charactère

            if text[i].islower():  # S'il est minuscule
                decrypted += self.__decrypt_char(text[i], passcode[passcode_increment].lower(),
                                                 dico_down)  # Ajout du caractère chiffrer à la chaîne de caractère ; si
                # le caractère est inconnu, il est remplacé par un espace
            else:  # S'il n'est pas minuscule
                decrypted += self.__decrypt_char(text[i], passcode[passcode_increment].upper(), dico_up)  # Ajout du
                # caractère chiffrer à la chaîne de caractère ; si le caractère est inconnu, il est remplacé par un
                # espace

            passcode_increment += 1  # On passe au caractère suivant

        print("Texte entrée : " + text)
        print("Passcode : " + passcode)
        print("Résultat : " + decrypted)

        return decrypted

    def __crypt_char(self, char: str, passcode_char: str, dico: dict):
        """
        Chiffre un charactère
        :param char: Charactère à chiffrer
        :param passcode_char: Charactère à utiliser pour chiffrer
        :param dico: Dictionnaire à utiliser pour le chiffrement
        :return: Charactère chiffré
        """
        char_value = dico.get(char, " ")
        pass_value = dico.get(passcode_char, " ")

        new_value = char_value + pass_value - 1  # calcule la nouvelle valeur du caractère

        if new_value > 26:  # Si la nouvelle valeur dépasse la taille de l'alphabet
            new_value = new_value - 26

        return self.__invert_dico(dico).get(new_value, " ")  # Récupère le caractère chiffrer ; si le caractère est
        # inconnu il sera remplacé par un espace

    def __decrypt_char(self, char: str, passcode_char: str, dico: dict):
        """
        Déchiffre un charactère
        :param char: Charactère à déchiffrer
        :param passcode_char: Charactère à utiliser pour déchiffrer
        :param dico: Dictionnaire à utiliser pour le déchiffrement
        :return: Charactère déchiffré
        """
        char_value = dico.get(char, " ")
        pass_value = dico.get(passcode_char, " ")

        new_value = char_value - pass_value + 1  # calcule la nouvelle valeur du caractère

        if new_value < 1:  # Si la nouvelle valeur dépasse la taille de l'alphabet
            new_value = new_value + 26

        return self.__invert_dico(dico).get(new_value, " ")  # Récupère le caractère chiffrer ; si le caractère est
        # inconnu il sera remplacé par un espace

    @staticmethod
    def __get_dico(str_type: str, inverted: bool = False):
        """
        Permet de récupérer le dictionnaire chiffrer
        :param str_type: Si le dictionnaire doit être majuscule (up) ou minuscule (down)
        :param inverted: Est-ce que les valeurs sont inversés (retourne la valeur de chaque lettre
        :return: La valeur de chaque lettre
        """

        dico = {}  # dictionnaire à retourner

        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v", "w", "x", "y", "z"]  # Lettres de l'alphabet

        if inverted:  # si on souhaite un dictionnaire inversé
            if str_type == "up":  # si on le souhaite en majuscule
                for i in range(len(letters)):  # pour chaque lettre de l'alphabet
                    dico[i + 1] = letters[i].upper()  # on associe un numéro à une lettre (leur position = numéro - 1)
            if str_type == "down":  # si on le souhaite en minuscule
                for i in range(len(letters)):  # pour chaque lettre de l'alphabet
                    dico[i + 1] = letters[i]  # on associe un numéro à une lettre (leur position = numéro - 1)
        else:  # si on ne souhaite pas un dictionnaire inversé
            if str_type == "up":  # si on le souhaite en majuscule
                for i in range(len(letters)):  # pour chaque lettre de l'alphabet
                    dico[letters[i].upper()] = i + 1  # on associe une lettre à un numéro (position de la lettre + 1)
            if str_type == "down":  # si on le souhaite en majuscule
                for i in range(len(letters)):  # pour chaque lettre de l'alphabet
                    dico[letters[i]] = i + 1  # on associe une lettre à un numéro (position de la lettre + 1)

        return dico

    def __invert_dico(self, dico: dict):
        """
        Inverse le dictionnaire
        :param dico: Dictionnaire à inversé
        :return: Dictionnaire inversé
        """
        value = dico.get("a", False)  # vérifie si le dictionnaire est en minuscule non inversé
        inverted = False
        upper = False

        if not value:  # s'il n'est pas en minuscule non inversé
            value = dico.get("A", False)  # vérifie s'il n'est pas en majuscule non inversé
            if not value:  # vérifie s'il est inversé
                inverted = True
            else:  # indique qu'il est majuscule non inversé
                upper = True

        if inverted:
            value = str(dico.get(1))
            if value.isupper():  # vérifie s'il est en majuscule inversé
                return self.__get_dico("up")  # l'inverse

            return self.__get_dico("down")  # sinon, il est en minuscule inversé -> l'inverse

        if upper:
            return self.__get_dico("up", True)  # vérifie s'il est en majuscule inversé

        return self.__get_dico("down", True)  # sinon, il est en minuscule inversé -> l'inverse
