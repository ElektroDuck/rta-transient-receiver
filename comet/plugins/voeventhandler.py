from comet.plugins.voeventdata import Voeventdata
from comet.plugins.voeventsorting import VoeventSorting

class VoeventHandler(object):
    
    def __init__(self):
        pass

    def handleVoevent(self, voevent):
        data = self.__voeventSorter(voevent)
        return data
    
    def __voeventSorter(self, voevent) -> Voeventdata:
        voevent_sorter = VoeventSorting()
        return voevent_sorter.sort(voevent) 
