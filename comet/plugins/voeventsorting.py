from comet.plugins.extractors.agiledataextractor import AgileDataExtractor
from comet.plugins.extractors.chimedataextractor import ChimeDataExtractor
from comet.plugins.extractors.gcndataextractor import GncDataExtractor
from comet.plugins.extractors.integraldataextractor import IntegralDataExtractor
from comet.plugins.extractors.ligodataextractor import LigoDataExtractor

class VoeventSorting(object):
    def __init__(self) -> None:
        self.agile = AgileDataExtractor()
        self.chime = ChimeDataExtractor()
        self.gcn = GncDataExtractor()
        self.integral = IntegralDataExtractor()
        self.ligo = LigoDataExtractor()

    def sort(self, voevent) -> None:
        if "gcn" in voevent.attrib['ivorn']:
            print(self.agile.extract(voevent))
        elif "gwnet" in voevent.attrib['ivorn']:
            print(self.ligo.extract(voevent))
        elif "chimenet" in voevent.attrib['ivorn']:
            print(self.chime.extract(voevent))
        elif "INTEGRAL" in voevent.attrib['ivorn']:
            print(self.integral.extract(voevent))
        elif "AGILE" in voevent.attrib['ivorn']:
            print(self.agile.extract(voevent))
        else:
            raise Exception(f"Notice not supported  ivorn is {self.voevent.attrib['ivorn']}")