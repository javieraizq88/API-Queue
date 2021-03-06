# FIFO = # First In - First Out (Primer en Entrar - Primero en Salir)
# Debo eliminar siempre el primero de la lista

# LIFO = # Last In - First Out (Ultimo en Entrar - Primero en Salir)
# Debo eliminar siempre el ultimo de la lista
from twilio.rest import Client

class Queue:
    def __init__(self): # el init es el constructor de JS
        self.account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # lo saque de la pag de twilio
        self.auth_token = 'your_auth_token' # lo saque de la pag de twilio
        self.client = Client(self.account_sid, self.auth_token) # son los elementos q pide twilio
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item): # a quien estoy agregando a la fila
        # POST append dequeue (item)
        self._queue.append(item) # agrega la persona (item) a la lista
        # recibe los atributos de client
        message = self.client.messages.create (
            body="fuiste agregado a la lista de espera",
            to="123",
            from_='+123'
        )
        #message.sid # mensaje en codigo y twilio te dice si lo recibio o no
        # print(message.sid) para saber si esta agregando el elemento
        # print(self.queue)

    def get_queue(self): # muestra todo la lista
        self._queue()

    def size(self): 
        return len(self._queue)

    def dequeue(self): # lo elimino de la lista
        if self._node == "FIFO":
            self._queue.pop(item)
            # recibe los atributos de client
            message = self.client.messages.create (
            body="ya fuiste atendido, adios!",
            to="234",
            from_='+234'
            )
        elif self._node == "LIFO":
            self._queue.shift(item)
            message = self.client.messages.create (
            body="ya fuiste atendido, adios!",
            to="234",
            from_='+234'
            )

'''
message = client.messages.create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         to='+15558675310'
     )

print(message)


{
  "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "api_version": "2010-04-01",
  "body": "Join Earth's mightiest heroes. Like Kevin Bacon.",
  "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
  "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
  "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "+14155552345",
  "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "status": "sent",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
  },
  "to": "+15558675310",
  "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
}

'''