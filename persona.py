class Person(object):
    def _init_(self, id, name, address, phone):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone