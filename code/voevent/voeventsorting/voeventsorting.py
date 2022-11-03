from code.voevent.extractors.agiledataextractor import AgileDataExtractor
from code.voevent.extractors.integraldataextractor import IntegralDataExtractor
from code.voevent.extractors.ligodataextractor import LigoDataExtractor
from code.voevent.extractors.gcndataextractor import GncDataExtractor
from code.voevent.extractors.chimedataextractor import ChimeDataExtractor

class VoeventSorting(object):
    def __init__(self) -> None:
        self.agile = AgileDataExtractor()
        self.chime = ChimeDataExtractor()
        self.gcn = GncDataExtractor()
        self.integral = IntegralDataExtractor()
        self.ligo = LigoDataExtractor()

    def sort(self, voevent) -> None:
        if "gcn" in voevent.attrib['ivorn']:
            return self.agile.extract(voevent)
        elif "gwnet" in voevent.attrib['ivorn']:
            return self.ligo.extract(voevent)
        elif "chimenet" in voevent.attrib['ivorn']:
            return self.chime.extract(voevent)
        elif "INTEGRAL" in voevent.attrib['ivorn']:
            return self.integral.extract(voevent)
        elif "AGILE" in voevent.attrib['ivorn']:
            return self.agile.extract(voevent)
        else:
            raise Exception(f"Notice not supported  ivorn is {self.voevent.attrib['ivorn']}")
