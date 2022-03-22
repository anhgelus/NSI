from encryption_system.code_de_cesar import CodeDeCesar

print("PROJECT WILLIAM HERGES - NSI 2021-2022")


def main():
    """
    Fonction principal
    """
    # Création de l'ensemble des chiffrements possibles
    switch = {
        1: "ROT13",
        2: "Code de César",
        3: "Chiffre de Vigenère",
        4: "Carré de Polybe",
        0: "Annuler"
    }

    enable = True

    cesar = CodeDeCesar()

    # Se répète jusqu'à la désactivation manuelle par la fonction 0 (Annuler)
    while enable:
        # Affiche les informations à propos des chiffrements disponible
        print(
            "\nType de chiffrage: \n\n- ROT13 (1)\n- Code de César (2)\n- Chiffre de Vigenère (3)\n- Carré de Polybe "
            "(4)")
        type = int(input("\n-> (1, 2, 3, 4 ou 0 pour annuler) "))

        is_valid = switch.get(type, "error")  # Récupère le type de chiffrement

        # Vérifie si l'input est valide
        if is_valid == "error":
            print("Type inconnu")
        else:
            # Demande confirmation avant de lancer la méthode de children
            validation_type = {"y": "confirm", "n": "exit"}
            validation = input("Confirmez-vous d'utiliser le " + is_valid + " ? (y/n) ")
            is_validation_valid = validation_type.get(validation, "error")

            if is_validation_valid == "confirm":
                # Quand la fonction 0 (Annuler) est appelée
                if type == 0:
                    enable = False
                # Quand une autre fonction est appelée
                elif type == 1 or type == 2 or type == 3 or type == 4:
                    # Demande s'il s'agit de chiffrer ou de déchiffer
                    encrypt_decrypt_type = {1: "chiffrer", 2: "déchiffrer"}
                    encrypt_decrypt = input("Souhaitez-vous chiffrer (1) ou déchiffrer (2) ? ")
                    is_encrypt_decrypt_valid = encrypt_decrypt_type.get(int(encrypt_decrypt), "error")

                    # Vérifie si l'input est valide
                    if is_encrypt_decrypt_valid == "error":
                        print("Mauvais input")
                    # Quand la fonction 2 (Code de César) est appelée
                    elif type == 2:
                        # Vérifie la méthode à utiliser (chiffrement ou déchiffrement)
                        if is_encrypt_decrypt_valid == "chiffrer":
                            # Demande la phrase et le code pour chiffrer la phrase
                            to_crypt = str(input("Phrase à " + is_encrypt_decrypt_valid + " avec " + is_valid + " "))
                            pass_code = int(input("Décalage "))
                            # Appelle la fonction code de césar
                            cesar.encrypt(to_crypt, pass_code)
                        elif is_encrypt_decrypt_valid == "déchiffrer":
                            # Demande la phrase et le code pour déchiffrer la phrase
                            to_crypt = str(input("Phrase à " + is_encrypt_decrypt_valid + " avec " + is_valid + " "))
                            pass_code = int(input("Décalage "))
                            # Appelle la fonction code de césar
                            cesar.decrypt(to_crypt, pass_code)

                    # Quand la fonction 2 (ROT13) est appelée
                    elif type == 1:
                        # Vérifie la méthode à utiliser (chiffrement ou déchiffrement)
                        if is_encrypt_decrypt_valid == "chiffrer":
                            # Demande la phrase et le code pour chiffrer la phrase
                            to_crypt = str(input("Phrase à " + is_encrypt_decrypt_valid + " avec " + is_valid + " "))
                            # Appelle la fonction code de césar avec comme code "13"
                            cesar.encrypt(to_crypt, 13)
                        elif is_encrypt_decrypt_valid == "déchiffrer":
                            # Demande la phrase et le code pour déchiffrer la phrase
                            to_crypt = str(input("Phrase à " + is_encrypt_decrypt_valid + " avec " + is_valid + " "))
                            # Appelle la fonction code de césar avec comme code "13"
                            cesar.decrypt(to_crypt, 13)

            # Vérifie si l'input lors de la validation est valide
            elif is_validation_valid == "error":
                print("Mauvais input")


# Appelle le programme
main()
