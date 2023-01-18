"""
Tekijä: Jimi Niemi

Organizations accesscontrol system
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        """

        self.__id = id
        self.__name = name

        if self.__id in USERCODES:

            self.__codes = USERCODES[self.__id]

        else:

            self.__codes = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        """

        accesscodes = ""

        #No accesscodes
        if self.__codes[0] == "":

            pass

        #Only 1 accesscode
        elif len(self.__codes) == 1:

            pass

        else:
            useless_keys = True

            while useless_keys == True:

                for index1 in range(0, len(self.__codes)):

                    try:

                        if self.__codes[index1] in DOORCODES:

                            for code in DOORCODES[self.__codes[index1]]:

                                if code in self.__codes:

                                    self.__codes.remove(self.__codes[index1])

                                else:
                                    useless_keys = False

                        # Estää ohjelmaa jäämästä ikuiseen looppiin
                        if index1 == len(self.__codes) - 1:
                            useless_keys = False

                    except IndexError:
                        break

        #If "self.__codes" had only an empty string the program would print
        #a comma. This deletes the empty string from the list if the list has
        # other items
        if self.__codes[0] == "" \
            and len(self.__codes) > 1:

            self.__codes.remove(self.__codes[0])

        codes = []
        codes = self.__codes
        codes = sorted(codes)

        for index in range(0, len(codes)):

            if index == len(codes) - 1:

                accesscodes += codes[index]

            else:

                accesscodes += codes[index] + ", "

        print(f"{self.__id}, {self.get_name()}, access: {accesscodes}")
        return

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        return self.__name


    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        """

        #Jos koodi on jo kortilla niin ohjelma ei tee mitään
        if new_access_code in self.__codes:

            return

        else:

            code_type = ""

            if new_access_code in doorcodes():

                if len(DOORCODES[new_access_code]) == 0:

                    code_type = "unique"

                else:

                    code_type = "doorcode"

            else:

                code_type = "areacode"

            if code_type == "unique" or code_type == "areacode":

                self.__codes.append(new_access_code)
                return

            else:

                for areacode in DOORCODES[new_access_code]:

                    if areacode in self.__codes:

                        return


                self.__codes.append(new_access_code)
                return


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        """

        if door in self.__codes:

            return True

        else:

            for areacode in DOORCODES[door]:

                if areacode in self.__codes:

                    return True

            return False


    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        """

        for code in card.__codes:

            self.add_access(code)

def card_id_is_valid(card_id):
    """
    Checks if the card id is valid

    :param card_id: str, id of card
    :return: bool, True if the card is valid
    """

    if card_id in ACCESSCARDS:

        return True

    else:

        return False

def check_door_code(door):
    """
    Checks if the door code is valid

    :param door: str, door code to be checked
    :return: bool, True if the code is valid
    """

    if door in doorcodes():

        return True

    elif door in areacodes():

        return True

    else:

        return False


def print_list():
    """
    Prints out list of all the accesscards using the info method
    """

    list_of_ids = []

    for id in ACCESSCARDS:
        list_of_ids.append(id)

    list_of_ids = sorted(list_of_ids)

    for id in list_of_ids:
        whoami(id).info()

def whoami(card_id):
    """
    Returns the correct object

    :param card_id: str, id of a card
    :return: obj, object that matches the card id
    """

    Person = ACCESSCARDS[card_id]

    return Person


def areacodes():
    """
    Returns a list of all the areacodes

    :return: list, list of areacodes
    """

    areacodes = []

    for code in DOORCODES:

        for index in range(0, len(DOORCODES[code])):

            areacode = DOORCODES[code][index]

            if areacode not in areacodes:

                areacodes.append(areacode)

            else:
                pass

    return areacodes

def doorcodes():
    """
    Returns a list of all the doorcodes

    :return: list, list of doorcodes
    """

    doorcodes = []

    for code in DOORCODES:

        doorcode = code

        if doorcode not in doorcodes:

            doorcodes.append(doorcode)

        else:
            pass

    return doorcodes


ACCESSCARDS = {}
USERCODES = {}


def main():

    # Opens up file and makes an object with the information.
    # Saves the object to dict named ACCESSCARDS and doorcodes to dict USERCODES.
    filename = "accessinfo.txt"

    file = open(filename, mode="r")

    for line in file:

        fields = line.split(";")

        id = fields[0]
        name = fields[1]
        doorcodes = fields[2].rstrip("\n").split(",")

        id_as_str = str(id)

        USERCODES[id_as_str] = doorcodes
        Accesscard(id, name)
        ACCESSCARDS[id_as_str] = Accesscard(id, name)

    file.close()

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            print_list()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]

            if card_id_is_valid(card_id) == True:

                whoami(card_id).info()

            else:
                print(f"Error: unknown id.")

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            if card_id_is_valid(card_id) == True:

                Person = whoami(card_id)

                valid_code = check_door_code(door_id)

                if valid_code == True:

                    access = Person.check_access(door_id)

                    if access == True:

                        print(f"Card {card_id} "
                              f"( {whoami(card_id).get_name()} )"
                              f" has access to door {door_id}")

                    else:
                        print(f"Card {card_id} "
                              f"( {whoami(card_id).get_name()} )"
                              f" has no access to door {door_id}")

                else:
                    print(f"Error: unknown doorcode.")

            else:
                print(f"Error: unknown id.")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            if card_id_is_valid(card_id) == True:

                valid_code = check_door_code(access_code)

                if valid_code == True:

                    whoami(card_id).add_access(access_code)

                else:

                    print(f"Error: unknown accesscode.")

            else:

                print(f"Error: unknown id.")

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]

            if card_id_is_valid(card_id_to) == True \
               and card_id_is_valid(card_id_from) == True:

                whoami(card_id_to).merge(whoami(card_id_from))

            else:

                print(f"Error: unknown id.")

        elif command == "quit":
            print("Bye!")
            return

        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
