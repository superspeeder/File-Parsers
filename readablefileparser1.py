class Parser(object):
    @classmethod
    def parse(cls, file):
        data = {}
        opfile = open(file, 'r')
        for x in opfile.read().split('\n'):
            splitdata = x.split(' = ')
            data[splitdata[0]] = splitdata[1]

        return data