class Contact:
    name = TextField()
    email = EmailAddressField()


class Person(Contact):
    first_name = TextField()
    last_name = TextField()


class Friend(Person):
    relationship_details = TextField()


class FamilyMember(Person):
    relationship_details = TextField()
    family_members = IntegetField()
