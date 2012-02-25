class CArray(list):
    def __getitem__(self, index):
        return list.__getitem__(self, index % len(self))
    def __setitem__(self, index, value):
        return list.__setitem__(self, index % len(self), value)
