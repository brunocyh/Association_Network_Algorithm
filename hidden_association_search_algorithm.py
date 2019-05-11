import random


class HiddenAssociationFinder(object):
    """
    Prototype version of a facebook friend recommendation system.
    """
    mapping = {}
    flag = False

    def __init__(self, mapping: dict):
        """
        Mapping: {node:array(node)}
        """
        self.mapping = mapping

    def _is_sorted(self, array: list) -> bool:
        """
        Helper method to sort array
        """
        prev_item = ""
        for current_item in array:
            if current_item >= prev_item:
                continue
            else:
                return False

            prev_item = current_item

        return True

    def validate(self):
        """
        In order to perform the calculation, a few things have to be checked        
        """
        for count in range(100):
            node, network = random.choice(list(self.mapping.items()))

            if not self._is_sorted(network):
                raise Exception("Some array not sorted")
        
        self.flag = True
        print('OK')

    def getAssociationsAll(self, focusedObject: str, filtered_boundry: int = 2) -> dict:
        """
        Get hidden associations
        """
        if self.flag == False:
            raise Exception('Data input not validated yet. Please run function validate before any calcualtion.')
        
        hidden_friends = {}
        my_friend_list = self.mapping.get(focusedObject)
        already_friends = set(my_friend_list)
        already_friends.add(focusedObject)

        for friend in my_friend_list:
            friends_friends = self.mapping.get(friend)

            for person in friends_friends:
                if person not in already_friends:
                    response = hidden_friends.get(person)
                    if response == None:
                        hidden_friends.update({person: 1})
                    else:
                        hidden_friends.update({person: response + 1})

        filtered = set()
        for person, count in hidden_friends.items():
            if count < filtered_boundry:
                filtered.add(person)
        for person in filtered:
            hidden_friends.pop(person)

        return hidden_friends

    def getAssociationsLimited(self, limit: int, focusedObject: str):
        pass


def demo():
    demo_netword = {"a": ['c', 'e', 'GA', 'GB'],
                    "b": ['d', 'e', 'GB'],
                    "c": ['a', 'd', 'f', 'GA'],
                    "d": ['b', 'c', 'e', 'f', 'g', 'GA'],
                    "e": ['a', 'b', 'd', 'g', 'GA'],
                    "f": ['c', 'd'],
                    "g": ['d', 'e'],
                    "GA": ['a', 'c', 'd', 'e'],
                    "GB": ['a', 'b']}
    # a prob knows d
    finder = HiddenAssociationFinder(demo_netword)
    finder.validate()
    print(finder.getAssociationsAll(focusedObject='a'))
    print(finder.getAssociationsAll(focusedObject='d'))
    print(finder.getAssociationsAll(focusedObject='g'))
    print(finder.getAssociationsAll(focusedObject='GB'))


demo()
