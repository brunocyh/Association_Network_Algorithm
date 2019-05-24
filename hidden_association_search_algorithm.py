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


class NetworkModel():
    """
    A Network model that represents all the connections and people inside the network.
    Undirected graph.
    """

    def __init__(self):
        self.graph = None
        self.registered_names = {}  # {'Peter': [1,1], 'Sam': [1,2]}

    def add_vertex(self, name, connection_weight):
        pass

    def remove_vertex(self, name):
        pass

    def add_edge(self, object1, object2):
        pass

    def remove_edge(self, object1, object2):
        pass


class FacebookApplication():
    """
    Application 1: Facebook network
    """

    def __init__(self):
        self.network = NetworkModel()
        self.NEW_FRIEND_WEIGHT = 1
        # self.CLOSE_FRIEND_WEIGHT = 1

    def create_account(self, user_name):
        self.network.add_vertex(user_name, self.NEW_FRIEND_WEIGHT)

    def add_friend(self, user1, user2):
        assert user1 in self.network.registered_names
        assert user2 in self.network.registered_names
        self.network.add_edge(user1, user2)

    def remove_friend(self, user1, user2):
        assert user1 in self.network.registered_names
        assert user2 in self.network.registered_names
        self.network.remove_edge(user1, user2)

    def remove_account(self, user_name):
        self.network.remove_vertex(user_name)


def demo():
    # Case 1
    facebook = FacebookApplication()
    facebook.create_account('Peter')
    facebook.create_account('John')
    facebook.create_account('Sam')

    facebook.add_friend('Peter', 'John')
    facebook.add_friend('John', 'Sam')

    finder = HiddenAssociationFinder(facebook)
    finder.validate()
    print(finder.getAssociationsAll(focusedObject='Peter'))
    print(finder.getAssociationsAll(focusedObject='Sam'))
    print(finder.getAssociationsAll(focusedObject='John'))


    # demo_netword = {"a": ['c', 'e', 'GA', 'GB'],
    #                 "b": ['d', 'e', 'GB'],
    #                 "c": ['a', 'd', 'f', 'GA'],
    #                 "d": ['b', 'c', 'e', 'f', 'g', 'GA'],
    #                 "e": ['a', 'b', 'd', 'g', 'GA'],
    #                 "f": ['c', 'd'],
    #                 "g": ['d', 'e'],
    #                 "GA": ['a', 'c', 'd', 'e'],
    #                 "GB": ['a', 'b']}


demo()
