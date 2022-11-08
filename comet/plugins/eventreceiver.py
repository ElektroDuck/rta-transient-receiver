import voeventparse as vp
from comet.icomet import IHandler
from twisted.plugin import IPlugin
from zope.interface import implementer
from comet.plugins.voeventhandler import VoeventHandler

# Event handlers must implement IPlugin and IHandler.
@implementer(IPlugin, IHandler)
class EventReceiver(object):
    
    name = "receive-event"
    print("receive event attivo")       
    

    # When the handler is called, it is passed an instance of
    # comet.utility.xml.xml_document.
    def __call__(self, event):
        
        voevent_handler = VoeventHandler()
        voevent_handler.handleVoevent(vp.loads(event.raw_bytes))
        return True

receive_event = EventReceiver()