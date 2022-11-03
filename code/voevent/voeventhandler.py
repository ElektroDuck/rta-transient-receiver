from voeventdata.voeventdata import Voeventdata
from voeventsorting.voeventsorting import VoeventSorting

class voeventHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def elaborate_voevent(voevent) -> None:
        try:
            voeventdata = VoeventSorting.sort(voevent)
        except Exception as e:
            print(e)
            return None