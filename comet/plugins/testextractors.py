from test_voevents import DUMMY_VOEVENT_GCN, DUMMY_VOEVENT_INTEGRAL, DUMMY_VOEVENT_CHIME, DUMMY_VOEVENT_LIGO, DUMMY_VOEVENT_LIGO_INITIAL, DUMMY_VOEVENT_LIGO_PRELIMINARY, DUMMY_VOEVENT_GCN_FERMI, DUMMY_VOEVENT_GCN_MAXI
from comet.utility.xml import xml_document
import voeventparse as vp
from gcndataextractor import GncDataExtractor
from chimedataextractor import ChimeDataExtractor
from integraldataextractor import IntegralDataExtractor
from ligodataextractor import LigoDataExtractor


class DummyEvent(object):
    """
    Class containing standard voevent from different networks
    """
    gcn = xml_document(DUMMY_VOEVENT_GCN)
    chime = xml_document(DUMMY_VOEVENT_CHIME)
    integral = xml_document(DUMMY_VOEVENT_INTEGRAL)
    fermi = xml_document(DUMMY_VOEVENT_GCN_FERMI) 
    ligo = xml_document(DUMMY_VOEVENT_LIGO)
    ligo2 = xml_document(DUMMY_VOEVENT_LIGO_PRELIMINARY)
    ligo_initial = xml_document(DUMMY_VOEVENT_LIGO_INITIAL)
    maxi = xml_document(DUMMY_VOEVENT_GCN_MAXI)

if __name__ == "__main__":
    """
    Main used to quick test. It Should not be used as unit test
    """
    
    dummyevents = DummyEvent()
    voe_chime = vp.loads(dummyevents.chime.raw_bytes) #tested
    voe_gcn = vp.loads(dummyevents.gcn.raw_bytes) #tested
    voe_integral = vp.loads(dummyevents.integral.raw_bytes) #tested
    voe_fermi = vp.loads(dummyevents.fermi.raw_bytes) #tested
    voe_ligo = vp.loads(dummyevents.ligo.raw_bytes) #tested
    voe_ligo_2 = vp.loads(dummyevents.ligo2.raw_bytes) #tested
    voe_ligo_init = vp.loads(dummyevents.ligo_initial.raw_bytes) #tested
    voe_maxi = vp.loads(dummyevents.maxi.raw_bytes) #tested
    
    gcn = GncDataExtractor("gcn")
    print(gcn.extract(voe_gcn))
    print(gcn.extract(voe_fermi))
    print(gcn.extract(voe_maxi))

    chime = ChimeDataExtractor("chime")
    print(chime.extract(voe_chime))

    integral = IntegralDataExtractor("integral")
    print(integral.extract(voe_integral))

    ligo = LigoDataExtractor("ligo")
    print(ligo.extract(voe_ligo))
    print(ligo.extract(voe_ligo_2))
    print(ligo.extract(voe_ligo_init))
