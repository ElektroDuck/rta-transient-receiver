class Voeventdata(object):
    def __init__(self, datasource, is_ste, instrument_id, trigger_id,
                    packet_type, time, network_id, l, b, position_error,
                    notice, configuration, url, contour, ligo_attributes,
                    name, seqNum, tstart, tstop, last) -> None:
        self.datasource = datasource
        self.is_ste = is_ste
        self.instrument_id = instrument_id
        self.trigger_id = trigger_id
        self.packet_type = packet_type
        self.time = time
        self.network_id = network_id
        self.l = l
        self.b = b
        self.position_error = position_error
        self.notice = notice
        self.configuration = configuration
        self.url = url
        self.contour = contour
        self.ligo_attributes = ligo_attributes
        self.name = name
        self.seqNum = seqNum
        self.tstart = tstart
        self.tstop = tstop
        self.last = last

    def __str__(self):
        return f"Voevent\nIntrumentID: {self.instrument_id}, name:{self.name}, seqNum {self.seqNum}, triggerid: {self.trigger_id}, packetType: {self.packet_type},time: {self.time}, l: {self.l}, b: {self.b}, contour: {self.contour}, url: {self.url}"