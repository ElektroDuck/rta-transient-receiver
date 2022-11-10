from gcn_kafka import Consumer
import voeventparse as vp
from comet.plugins.voeventhandler import VoeventHandler


#this is used to access old voevents from the kafka stream
#if deleted from the consumer it will only get incoming voevents in real time

"""
connection for testing whith old voevents

config = {'group.id': '',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(config=config,
                    client_id='3vk7sbr0ra6ci9vj7ts25f00tg',
                    client_secret='h1hmi71behgud8u0o195vfi1pcc1jdsrhighmqr10c1jvnqjm0p')

"""
#normal connection

"""
consumer = Consumer(client_id='3vk7sbr0ra6ci9vj7ts25f00tg',
                    client_secret='h1hmi71behgud8u0o195vfi1pcc1jdsrhighmqr10c1jvnqjm0p')

"""

consumer = Consumer(client_id='1bhh120087sgv8s9ctb5lvfpi8',
                    client_secret='d3m68h5mra18litkb1lkh6t93ic16ral36j7gr32kvna4hp5cqh',
                    domain='gcn.nasa.gov')


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
#consumer.subscribe(subscribeSet)
consumer.subscribe(subscribeSet)

#class used to perform action when a voevent is recived
voeventhandle = VoeventHandler()
"""
print('kafka on')
while True:
    for message in consumer.consume():
        value = message.value()
        try:
            voeventhandle.printVoevent(vp.loads(value))
        except Exception as e:
            print(value)
            print(e)
"""