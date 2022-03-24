class Question:
    __answer = ""

    BOOL_QUESTION = "bool"
    COMPLEX_QUESTION = "complex"

    def __init__(self, question_type: str, question: str, reponse=None):
        """
        :param type: bool question ou complex question
        :param question: Question posé
        :param reponse: Réponse possible (uniquement utilisable pour les questions complex et si non spécifié, retourne la valeur donné)
        """
        valid_type = {"bool": 0, "complex": 1}
        used_type = valid_type.get(question_type, "error")

        if used_type == "error":
            return
        elif used_type == 0:
            self.__answer = self.__bool_question_generator(question)
        elif used_type == 1:
            if reponse is None:
                self.__answer = self.__complex_question_generator(question)
            else:
                self.__answer = self.__complex_question_generator(question, reponse)

    def get_answer(self):
        return self.__answer

    def __bool_question_generator(self, question: str):
        """
        Génère une question fermée (oui/non)
        :param question:
        :return: Résultat de la question
        """
        validation_type = {"y": 1, "n": 0}
        answer = input("Confirmez-vous d'utiliser " + question + " ? (y/n) ")
        validation = validation_type.get(answer, "error")

        if validation == "error":
            self.__bool_question_generator(question)
        elif validation == 1:
            return True
        elif validation == 0:
            return False

    def __complex_question_generator(self, question: str, reponses=None):
        """
        Génère une question ouverte
        :param question: Question
        :param reponses: Réponses possibles
        :return: réponse de l'utilisateur
        """
        answer = input(question)

        if reponses is None:
            validation = answer
            return validation

        type_reponse = type(reponses)

        if type_reponse is dict:
            validation = reponses.get(answer, "error")
            if validation == "error":
                try:
                    validation = reponses.get(int(answer), "error")
                except:
                    validation = "error"
        elif type_reponse is tuple:
            validation = reponses.contain(answer)
        elif type_reponse is list:
            try:
                validation = reponses[int(answer)]
            except:
                validation = "error"
        else:
            validation = "error"

        if validation == "error":
            self.__complex_question_generator(question, reponses)

        return validation
