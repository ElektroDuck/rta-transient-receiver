from gcn_kafka import Consumer

# Connect as a consumer.
# Warning: don't share the client secret with others.
config = {'group.id': '',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(config=config,
                    client_id='3vk7sbr0ra6ci9vj7ts25f00tg',
                    client_secret='h1hmi71behgud8u0o195vfi1pcc1jdsrhighmqr10c1jvnqjm0p')

topics = [
                    'gcn.classic.voevent.AMON_ICECUBE_EHE',
                    'gcn.classic.voevent.AMON_ICECUBE_HESE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD',
                    'gcn.classic.voevent.MAXI_KNOWN',
                    'gcn.classic.voevent.MAXI_UNKNOWN',
                    'gcn.classic.voevent.SWIFT_BAT_QL_POS',
                    'gcn.classic.voevent.KONUS_LC']

not_working_topic = ['gcn.classic.voevent.AGILE_MCAL_ALERT',
                    'gcn.classic.voevent.FERMI_GBM_FLT_POS',
                    'gcn.classic.voevent.FERMI_LAT_OFFLINE',
                    'gcn.classic.voevent.FERMI_LAT_MONITOR',
                    'gcn.classic.voevent.INTEGRAL_OFFLINE',
                    'gcn.classic.voevent.INTEGRAL_REFINED',
                    'gcn.classic.voevent.INTEGRAL_WAKEUP',
                    'gcn.classic.voevent.LVC_EARLY_WARNING',
                    'gcn.classic.voevent.LVC_INITIAL',
                    'gcn.classic.voevent.LVC_PRELIMINARY',
                    'gcn.classic.voevent.LVC_UPDATE',]




# Subscribe to topics and receive alerts
#consumer.subscribe(['gcn.classic.voevent.AGILE_MCAL_ALERT'])

for topic in not_working_topic:
    consumer.subscribe([not_working_topic])
    print(topic)
    for message in consumer.consume():
        value = message.value()
        print(value)

"""
while True:
    for message in consumer.consume():
        value = message.value()
        print(value)
"""


