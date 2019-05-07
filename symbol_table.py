class SymbolTable():
    def __init__(self):
        self.table = {}

    def getter(self, variable_name):
        if variable_name in self.table.keys():
            return self.table[variable_name]

        else:
            raise ValueError("Symbol Table Error: Variable {} does not exist".format(variable_name))

    def setter(self, variable_name, variable_value):
        self.table[variable_name] = variable_value
