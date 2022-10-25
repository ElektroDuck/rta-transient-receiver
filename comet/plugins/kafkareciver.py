from gcn_kafka import Consumer
from Voevent import Voevent
import voeventparse as vp

# Connect as a consumer.
# Warning: don't share the client secret with others.
"""
consumer = Consumer(client_id='3vk7sbr0ra6ci9vj7ts25f00tg',
                    client_secret='h1hmi71behgud8u0o195vfi1pcc1jdsrhighmqr10c1jvnqjm0p')
"""
config = {'group.id': '',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(config=config,
                    client_id='3vk7sbr0ra6ci9vj7ts25f00tg',
                    client_secret='h1hmi71behgud8u0o195vfi1pcc1jdsrhighmqr10c1jvnqjm0p')


subscribeSet = ['gcn.classic.voevent.AGILE_MCAL_ALERT',
                    'gcn.classic.voevent.AMON_ICECUBE_EHE',
                    'gcn.classic.voevent.AMON_ICECUBE_HESE',
                    'gcn.classic.voevent.FERMI_GBM_FLT_POS',
                    'gcn.classic.voevent.FERMI_LAT_MONITOR',
                    'gcn.classic.voevent.FERMI_LAT_OFFLINE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD',
                    'gcn.classic.voevent.INTEGRAL_OFFLINE',
                    'gcn.classic.voevent.INTEGRAL_REFINED',
                    'gcn.classic.voevent.INTEGRAL_WAKEUP',
                    'gcn.classic.voevent.LVC_EARLY_WARNING',
                    'gcn.classic.voevent.LVC_INITIAL',
                    'gcn.classic.voevent.LVC_PRELIMINARY',
                    'gcn.classic.voevent.LVC_UPDATE',
                    'gcn.classic.voevent.MAXI_KNOWN',
                    'gcn.classic.voevent.MAXI_UNKNOWN',
                    'gcn.classic.voevent.SWIFT_BAT_QL_POS',
                    'gcn.classic.voevent.KONUS_LC']



# Subscribe to topics and receive alerts
consumer.subscribe(subscribeSet)

i = 0

while i < 20:
    i = i + 1
    for message in consumer.consume():

        value = message.value()
        try:
            test = Voevent(vp.loads(value))
            print("------------")
            print(test)
            print("-----------")    
        except:
            print(value)
