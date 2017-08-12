class Parser(object):
    @classmethod
    def parse(data):
        specdata = {'unlocked': False}
        basedata = {}
        opfile = open(data, 'r')
        filelines = opfile.split('\n')
        for line in filelines:
            spacesplitline = line.split(' ')
            try:
                if spacesplitline[0].lower() == 'unlock' and len(spacesplitline) == 1:
                    specdata['unlocked'] = True
                    continue
            except: pass
            try:
                if spacesplitline[1].lower() == '=' and len(spacesplitline) == 1:
                    basedata[spacesplitline[0]] = spacesplitline[2]
                    continue
            except: pass

        return specdata, basedata
