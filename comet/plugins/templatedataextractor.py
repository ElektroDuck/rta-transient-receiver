import os
import re
import json
import math
import requests
import numpy as np
import comet.log as log
import voeventparse as vp
from tokenize import group
from datetime import datetime
from datetime import datetime
from astropy.time import Time
from astropy import units as u
import lxml.etree as ElementTree
from comet.utility import voevent
from astropy.coordinates import SkyCoord
from comet.utility.xml import xml_document
from ligo.skymap.io.fits import read_sky_map
from ligo.skymap.postprocess.contour import contour as ligo_contour
from voeventdata import Voeventdata

class templatedataextractor(object):
    
    
    def __init__(self, datasource) -> None:
        self.datasource = datasource

    def extract(self, voevent):
        is_ste = self.is_ste(self, voevent)
        instrument_id = self.get_instrumentID(self, voevent)
        trigger_id = self.get_triggerID(self, voevent)
        packet_type = self.get_packet_type(self, voevent)
        time = self.get_time_from_voevent(self, voevent)
        network_id = self.get_networkID(self, voevent)
        l, b = self.get_l_b(self, voevent)
        position_error = self.get_position_error(self, voevent)
        notice = vp.prettystr(self.voevent)
        configuration = self.get_configuration(self, voevent)
        url = self.get_url(self, voevent)
        contour = self.get_contour(self, voevent)
        ligo_attributes = self.get_ligo_attributes(self, voevent)
        
        #static fields that probably should be not static 
        name = ""
        seqNum = -1 #to be removed in the future couse should be set by a sql query
        tstart = 0
        tstop = 0
        last = 1

        #here need to be create a new class that store the previusly 
        #extracted data and return it
        return Voeventdata(is_ste, instrument_id, trigger_id,
                            packet_type, time, network_id, l, b, position_error,
                            notice, configuration, url, contour, ligo_attributes,
                            name, seqNum, tstart, tstop, last)

    def is_ste(self, voevent):
        raise NotImplementedError

    def get_instrumentID(self, voevent):
        raise NotImplementedError

    def get_triggerID(self, voevent):
        raise NotImplementedError

    def get_packet_type(args, voevent):
        raise NotImplementedError

    def get_time_from_voevent(self, voevent):
        iso_time = self.voevent.WhereWhen.ObsDataLocation.ObservationLocation.AstroCoords.Time.TimeInstant.ISOTime.text
        t = Time(iso_time, format="fits", scale="utc")
        return np.round(t.unix - 1072915200), t.fits

    def get_networkID(self, voevent):
        raise NotImplementedError

    def get_l_b(self, voevent):
        raise NotImplementedError

    def get_position_error(self, voevent):
        raise NotImplementedError

    def get_configuration(self, voevent):
        raise NotImplementedError

    def get_url(self, voevent):
        raise NotImplementedError

    def get_contour(self, voevent):
        raise NotImplementedError

    def get_ligo_attributes(self, voevent):
        raise NotImplementedError

    def __repr__(self):
        return "class for data extraction from: %s"% (self.datasource)

    def __str__(self):
        return "class for data extraction from: %s"% (self.datasource)