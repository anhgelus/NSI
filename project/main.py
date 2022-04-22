# Import des systèmes de chiffrement
from encryption_system.code_de_cesar import CodeDeCesar
from encryption_system.chiffre_de_vigenere import ChiffreDeVigenere
from encryption_system.carre_de_polybe import CarreDePolybe

# Import de la classe qui génère les questions
from question import Question

print("PROJECT WILLIAM HERGES - NSI 2021-2022")


def main():
    """
    Fonction principal
    """

    # Se répète jusqu'à la désactivation manuelle par la fonction 0 (Annuler) via exit()
    while True:
        chiffrage_list = ["Annuler", "ROT13", "Code de César", "Chiffre de Vigenère", "Carré de Polybe"]
        # Quelque chiffrage utilisé
        type_chiffrage = Question(Question.COMPLEX_QUESTION, "\nType de chiffrage: \n\n- ROT13 (1)\n- Code de César (" +
                                  "2)\n- Chiffre de Vigenère (3)\n- Carré de Polybe (4)\n" +
                                  "- Annuler (0)\n" +
                                  "Type de chiffrage ", chiffrage_list).get_answer()
        # print(
        #    "\nType de chiffrage: \n\n- ROT13 (1)\n- Code de César (2)\n- Chiffre de Vigenère (3)\n- Carré de Polybe "
        #    "(4)")

        # Demande confirmation avant de lancer la méthode de children
        validation = Question(Question.BOOL_QUESTION, type_chiffrage).get_answer()

        if validation:
            # Quand la fonction 0 (Annuler) est appelée
            if type_chiffrage == chiffrage_list[0]:
                exit()

            usage_type = {1: "chiffer", 2: "déchiffer"}
            usage = Question(Question.COMPLEX_QUESTION, "Souhaitez-vous chiffrer (1) ou déchiffrer (2) ? ",
                             usage_type).get_answer()

            # Quand la fonction 2 (Code de César) est appelée
            if type_chiffrage == chiffrage_list[2]:
                cesar = CodeDeCesar()  # Initialise la class CodeDeCesar

                # Demande la phrase et le code pour chiffrer/déchiffer la phrase
                try:
                    crypt = str(input("Phrase à " + str(usage) + " avec " + type_chiffrage + " "))
                    pass_code = int(input("Décalage "))
                except KeyboardInterrupt as e:
                    exit(e)
                    return

                # Vérifie la méthode à utiliser (chiffrement (1) ou déchiffrement (2))
                if usage == usage_type.get(1):
                    # Chiffre le message avec le code de césar
                    cesar.encrypt(crypt, pass_code)
                elif usage == usage_type.get(2):
                    # Déchiffre le message avec le code de césar
                    cesar.decrypt(crypt, pass_code)

            # Quand la fonction 1 (ROT13) est appelée
            elif type_chiffrage == chiffrage_list[1]:
                cesar = CodeDeCesar()  # Initialise la class CodeDeCesar
                # Demande la phrase pour chiffrer/déchiffer la phrase
                try:
                    crypt = str(input("Phrase à " + str(usage) + " avec " + type_chiffrage + " "))
                except KeyboardInterrupt as e:
                    exit(e)
                    return

                # Vérifie la méthode à utiliser (chiffrement (1) ou déchiffrement (2))
                if usage == usage_type.get(1):
                    # Chiffre le message avec le code de césar et la décal à 13
                    cesar.encrypt(crypt, 13)
                elif usage == usage_type.get(2):
                    # Déchiffre le message avec le code de césar et la décal à 13
                    cesar.decrypt(crypt, 13)

            # Quand la fonction 3 (Chiffre de Vigenere) est appelée
            elif type_chiffrage == chiffrage_list[3]:
                vigenere = ChiffreDeVigenere()

                # Demande la phrase et le code pour chiffrer/déchiffer la phrase
                try:
                    crypt = str(input("Phrase à " + str(usage) + " avec " + type_chiffrage + " "))
                    passcode = input("Passcode ")
                except KeyboardInterrupt as e:
                    exit(e)
                    return

                    # Vérifie la méthode à utiliser (chiffrement (1) ou déchiffrement (2))
                if usage == usage_type.get(1):
                    # Chiffre le message avec le chiffre de vigenere
                    vigenere.encrypt(crypt, passcode)
                elif usage == usage_type.get(2):
                    # Déchiffre le message avec le chiffre de vigenere
                    vigenere.decrypt(crypt, passcode)

            elif type_chiffrage == chiffrage_list[4]:
                print("/!\\ Dans le Carré de Polybe, le I = J /!\\")
                polybe = CarreDePolybe()

                # Demande la phrase et le code pour chiffrer/déchiffer la phrase
                try:
                    crypt = str(input("Phrase à " + str(usage) + " avec " + type_chiffrage + " "))
                    alphabet = input("Alphabet ")
                except KeyboardInterrupt as e:
                    exit(e)
                    return

                if alphabet == "":
                    alphabet = None

                # Vérifie la méthode à utiliser (chiffrement (1) ou déchiffrement (2))
                if usage == usage_type.get(1):
                    # Chiffre le message avec le carré de polybe
                    polybe.encrypt(crypt, alphabet)
                elif usage == usage_type.get(2):
                    # Déchiffre le message avec le carré de polybe
                    polybe.decrypt(crypt, alphabet)


# Appelle le programme
main()
