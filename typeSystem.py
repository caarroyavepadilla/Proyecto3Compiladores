
DEFAULT_TYPES = {
    'int': 4,
    'boolean': 4,
    'char': 4,
}

class Scope:
    def __init__(self, id=0, name="global", parent=None, type = None):
        self.id = id
        self.type = type
        self.name = name
        self.parent = parent
        self.instantiables = []
        self.symbols = []

    def get_instance(self, name):
        for ins in self.instantiables:
            if ins.name == name:
                return ins

    def get_symbol(self, name):
        for sym in self.symbols:
            if sym.name == name:
                return sym

    def get_sub_att(self, instance_name, sub_name):
        for instance in self.instantiables:
            if instance.name == instance_name:
                for sub in instance.sub_att:
                    if sub.name == sub_name:
                        return sub
        return None

    def get_instance_size(self, ins_name):
        for instance in self.instantiables:
            if instance.name == ins_name:
                return instance.size
        else:
            return self.parent.get_instance_size(ins_name)
    
    def get_subatt_offset(self, ins_name):
        for instance in self.instantiables:
            if instance.name == ins_name:
                return 0
    
    def get_size(self):
        size = 0
        for instance in self.symbols:
            if instance.type in DEFAULT_TYPES:
                size += DEFAULT_TYPES[instance.type] * int(instance.reps)
            else:
                if lsize := self.get_instance(instance.type) != None:
                    size += lsize.size * int(instance.reps)
                else:
                    lsize = self.parent.get_instance(instance.type.replace("struct", ""))
                    size += lsize.size * int(instance.reps)
        return size

    def add_insta(self, id, name, type, ret=None, subs=[], size=0):
        insta = Instantaible(id, name, type, ret, subs, size)
        self.instantiables.append(insta)

    def add_symbol(self, type, name, reps, id = 0, offset =0):
        symbol = Symbol(type,name, reps, id, offset)
        self.symbols.append(symbol)

class Instantaible:
    def __init__(self, id=0, name=None, type=None, ret=None, subs=[], size=0):
        self.id = id
        self.name = name
        if type == "struct":
            self.type = type
            self.size = size
            self.sub_att = subs
        else:
            self.type = type
            self.ret = ret
            self.params = subs

class Symbol:
    def __init__(self, type, name, reps, id=0, offset=0):
        self.id = id
        self.name = name
        self.type = type
        self.offset = offset
        self.reps = reps

class Error:
    def __init__(self, prob, line, column):
        self.prob = prob
        self.line = line
        self.column = column

