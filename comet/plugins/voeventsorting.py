
class VoeventSorting(object):
    def __init__(self) -> None:
        pass

    def sort(self, voevent) -> None:
        if "gcn" in voevent.attrib['ivorn']:
            print("gcn")
        elif "gwnet" in voevent.attrib['ivorn']:
            print("ligo")
        elif "chimenet" in voevent.attrib['ivorn']:
            print("chime")
        elif "INTEGRAL" in voevent.attrib['ivorn']:
            print("integral")
        elif "AGILE" in voevent.attrib['ivorn']:
            print("agile")
        else:
            raise Exception(f"Notice not supported  ivorn is {self.voevent.attrib['ivorn']}")
