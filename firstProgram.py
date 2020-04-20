class Conference:
    is_interesting = True

    def __init__(self, name=None, number_of_participants=0, ticket_price=0.0, location=None, topic=None, date=None,
                 organization=None):
        self.__name = name
        self.__number_of_participants = number_of_participants
        self.__ticket_price = ticket_price
        self.__location = location
        self.__date = date
        self.__topic = topic
        self.__organization = organization

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return

    @staticmethod
    def get_is_interesting():
        return Conference.is_interesting

    def get_name(self):
        return self._name

    def get_number_of_participants(self):
        return self._number_of_participants

    def ticket_price(self):
        return self._ticket_price

    def get_location(self):
        return self._location

    def get_topic(self):
        return self._topic

    def get_date(self):
        return self._date

    def get_organization(self):
        return self._organization

    def set_name(self, name):
        self._name = name

    def set_number_of_participants(self, number_of_participants):
        self._number_of_participants = number_of_participants

    def set_ticket_price(self, ticket_price):
        self._ticket_price = ticket_price

    def set_location(self, location):
        self._location = location

    def set_topic(self, topic):
        self._topic = topic

    def set_date(self, date):
        self._date = date

    def set_organization(self, organization):
        self._organization = organization

    def __str__(self):

        object_string = "Conference"

        if self._name is not None:
            name_string = "\nName: " + self._name
        else:
            name_string = ""
        if self._number_of_participants != 0:
            number_string = "\nNumber of participants: " + str(self._number_of_participants)
        else:
            number_string = ""
        if self._ticket_price != 0.0:
            price_string = "\nTicket price: " + str(self._ticket_price)
        else:
            price_string = ""
        if self._location is not None:
            location_string = "\nLocation: " + self._location
        else:
            location_string = ""
        if self._topic is not None:
            topic_string = "\nTopic: " + self._topic
        else:
            topic_string = ""

        if self._date is not None:
            date_string = "\nDate: " + self._date
        else:
            date_string = ""
        if self._organization is not None:
            organization_string = "\norganization: " + self._organization
        else:
            organization_string = ""

        return object_string + name_string + number_string + price_string + location_string + topic_string + date_string + organization_string + "\n---------------------------------------------------------------------"


if name == '__main__':
    print("---------------------------------------------------------------------")
    firstConference = Conference("Programming", 14, 143, "Washington street, 112")
    print(firstConference)
    secondConference = Conference("Java", 98, 200)
    print(secondConference)
    thirdConference = Conference()
    print(thirdConference)
    conferences = [firstConference, secondConference, thirdConference]

    for count_of_object in conferences:
        print(count_of_object)

