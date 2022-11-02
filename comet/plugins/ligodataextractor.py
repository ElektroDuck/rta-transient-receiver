from templatedataextractor import TemplateDataExtractor
import voeventparse as vp
import requests
import numpy as np
import json
import re
import os
from astropy.coordinates import SkyCoord
from astropy import units as u
import math
from voeventdata import Voeventdata
from datetime import datetime
from ligo.skymap.io.fits import read_sky_map
from ligo.skymap.postprocess.contour import contour as ligo_contour


class LigoDataExtractor(TemplateDataExtractor):
    def __init__(self, datasource) -> None:
        super().__init__(datasource)

    def is_ste(self, voevent):
        return 0

    def get_instrumentID_and_name(self, voevent) -> tuple:
        packet_type = int(voevent.What.Param[0].attrib["value"])
        if packet_type in [53,54,55]: # INTEGRAL FROM GCN
            return 23, "INTEGRAL"
        elif packet_type == 97: #SWIFT 
            return 3, "SWIFT"
        elif packet_type == 111:  #FERMI_GBM 
            return 1, "FERMI_GBM"
        elif packet_type in [125,128]: #FERMI_LAT 
            return 2, "FERMI_LAT"
        elif packet_type == 105: #AGILE_MCAL FROM GCN
            return 5, "AGILE_MCAL"
        elif packet_type in [150, 151, 152, 163]: #LIGO and LIGO_TEST TBD
            if  "test" in voevent.attrib['role']:
                return 19, "LIGO_TEST"
            if  "observation" in voevent.attrib['role']:
                return 7, "LIGO"
        elif packet_type == 158: #ICECUBE_HESE
            return 8, "ICECUBE_HESE"
        elif packet_type == 169: #ICECUBE_EHE
            return 10, "ICECUBE_EHE"
        elif packet_type == 173: #ICECUBE_ASTROTRACK_GOLD
            return 21, "ICECUBE_ASTROTRACK_GOLD"
        elif packet_type == 174: #ICECUBE_ASTROTRACK_BRONZE
            return 22, "ICECUBE_ASTROTRACK_BRONZE"
        elif packet_type == 59: #KONUS
            return 25, "KONUS"
        elif packet_type == 134: #MAXI_UNKNOWN
            return 26, "MAXI_UNKNOWN"
        elif packet_type == 135: #MAXI_KNOWN
            return 27, "MAXI_KNOWN"
        else:
            raise Exception(f"Voevent with packet type {packet_type} not supported")

    def get_triggerID(self, voevent):
        top_params = vp.get_toplevel_params(voevent)
        graceID = top_params["GraceID"]["value"]
        last = str(ord(graceID[-1]) - 96)
        result = re.sub("[^0-9]", "", graceID) + last.zfill(2)
        return result

    def get_packet_type(self, voevent):
        top_params = vp.get_toplevel_params(voevent)
        return top_params["Packet_Type"]["value"]

    def get_networkID(self, voevent):
        return 1

    def get_l_b(self, voevent):
        return 0,0

    def get_position_error(self, voevent):
        return 0

    def get_configuration(self, voevent):
        top_params = vp.get_toplevel_params(voevent)
        return top_params["Instruments"]["value"]

    def get_ligo_attributes(self, voevent):
        """
        tipical LIGO attributes extracted:
        {"bbh": 0, "bns": 0.9999947011562164, "far": 0.00000000000009110699364861295, "nsbh": 0, "has_ns": 1, "grace_id": "MS210208t",
        "mass_gap": 0, "has_remnant": 1, "terrestrial": 0.000005298843783562432}
        """

        top_params = vp.get_toplevel_params(voevent)
        grouped_params = vp.get_grouped_params(voevent)
        attributes = {}
        attributes["bbh"] = grouped_params["Classification"]["BBH"]["value"]
        attributes["bns"] = grouped_params["Classification"]["BNS"]["value"]
        attributes["far"] = top_params["FAR"]["value"]
        attributes["nsbh"] = grouped_params["Classification"]["NSBH"]["value"]
        attributes["has_ns"] = grouped_params["Properties"]["HasNS"]["value"]
        attributes["grace_id"] = top_params["GraceID"]["value"]
        try:
            attributes["mass_gap"] = grouped_params["Classification"]["MassGap"]["value"]
        except:
            attributes["mass_gap"] = 0
        attributes["has_remnant"] = grouped_params["Properties"]["HasRemnant"]["value"]
        attributes["terrestrial"] = grouped_params["Classification"]["Terrestrial"]["value"]

        return str(json.dumps(attributes))

    def get_contour(self, l, b, position, url):
        """
        For LIGO instrument we call contour function from ligo-contour tool
        """
        now = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
        target_path = f'/tmp/skymap_{now}.tar.gz'

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(target_path, 'wb') as f:
                f.write(response.raw.read())

            #Implementing the code from ligo-countour tool, the level [90] is hardcoded

        m, meta = read_sky_map(target_path, nest=True)
        i = np.flipud(np.argsort(m))
        cumsum = np.cumsum(m[i])
        cls = np.empty_like(m)
        cls[i] = cumsum * 100
            

        cont = list(ligo_contour(cls, [90.0], nest=True, degrees=True, simplify=False))
            
        #Conversion to galactic: it computes the position without loops to be more efficient, it uses approx 3 GB RAM
        ra = []
        dec = []
        for level in cont:
            for poligon in level:
                for coord in poligon:
                    ra.append(coord[0])
                    dec.append(coord[1])
            
        c = SkyCoord(ra=ra*u.degree, dec=dec*u.degree)
        contour = ""
        for coords in c.galactic.to_string():
            contour = contour + f"{coords}\n"

        os.remove(target_path)
        return contour

    def get_url(self, voevent):
        grouped_params = vp.get_grouped_params(voevent)
        return  grouped_params["GW_SKYMAP"]["skymap_fits"]["value"]

