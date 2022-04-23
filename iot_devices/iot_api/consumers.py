from channels.generic.websocket import WebsocketConsumer
from .models import numplate_checkin_data
import json
from .serializer import ForCheckin
import time


class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        checkin_data = numplate_checkin_data.objects.all()
        serializer = ForCheckin(checkin_data, many=True)
        temp = serializer.data[-1]
        while True:
            if serializer.data[-1] != temp:
                self.send(json.dumps({'print_it': serializer.data[-1]}))
                temp = serializer.data[-1]
            checkin_data = numplate_checkin_data.objects.all()
            serializer = ForCheckin(checkin_data, many=True)
            time.sleep(5)
        # print(serializer.data[0])
        # print(serializer.data[0])
