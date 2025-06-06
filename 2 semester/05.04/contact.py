from __future__ import annotations
from typing import Optional, Protocol


class ContactList(list['Contact']):
    def search(self, name: str, email: str) -> list['Contact']:
        matching_contacts: list[['Contact']] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    __all_contacts: list["Contacts"] = []

    def __init__(self, /, name: str = '', email: str = '', *args) -> None:
        self.name = name
        self.email = email
        super().__init__(*args)
        Contact.__all_contacts.append(self)

    @classmethod
    def getAll(cls):
        return cls.__all_contacts

    # @classmethod
    # def find_name(cls, name):
    #     names = []
    #     for cnt in cls.__all_contacts:
    #         if cnt.name == name:
    #             names.append(cnt)
    #     return 'Not Found' if names == [] else names


    def __repr__(self)  -> str:
        return (
            f'{self.__class__.__name__}('
            f'{self.name!r}, {self.email!r}'
            f')'
        )


class Supplier(Contact):
    def order(self, order: 'Order') -> None:
        print(
            'If this were a real system we would send'
            f'{order!r} order to {self.name!r}'
        )


class Emailable(Protocol):
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f'Sending mail to {self.email}')


class EmailableContact(Contact, MailSender):
    pass


class Nameable(Protocol):
    name: str

class NameableContact(Contact, Nameable):
    pass

class AddressHolder:
    def __init__(self, street: str, city:str, state: str, code:str):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(
            self,
            name: str,
            email: str,
            phone: str,
            street: str,
            city: str,
            state: str,
            code: str
    ) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone

class MyObject(Contact):
    print('1')


c = Contact('bkb', 'tpout')
c1 = Contact('yadol', 'suuu')
c2 = Contact('yae', 'tttttt')
c3 = Contact('yadol', 'tetete')