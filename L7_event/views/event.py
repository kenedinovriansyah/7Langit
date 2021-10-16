from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from database.models import TBEvent
from L7_event.serializer.event import EventSerializer, EventModelSerializer
from L7_event.serializer.category import CategorySerializer
from L7_event.serializer.schedulers import SchedulerSerializer

class EventModelViewSets(ModelViewSet):
    queryset = TBEvent.objects.all()
    serializer_class = EventModelSerializer
    serializer_query = EventSerializer
    serilaizer_q_c = CategorySerializer
    serializer_q_s = SchedulerSerializer
    parser_classes = [JSONParser, MultiPartParser,]

    def get_permissions(self):
        return super().get_permissions()

    def create(self, request):
        message = None
        serial_c = self.serilaizer_q_c(data=request.data)
        serial_c.context['types'] = 'create'
        serial_s = self.serializer_q_s(data=request.data)
        serial_s.context['types'] = 'create'
        if serial_c.is_valid() and serial_s.is_valid():
            serial_c.save()
            serial_s.save()
            data = request.data
            data._mutable = True
            data['category'] = serial_c.context['category'].id
            data['schedulers'] = serial_s.context['schedulers'].id
            serial_m = self.serializer_query(data=data)
            serial_m.context['types'] = 'create'
            if serial_m.is_valid():
                serial_m.save()
                return Response({'message': 'Event has been created'},status=status.HTTP_201_CREATED)

            return Response(serial_m.errors,status=status.HTTP_400_BAD_REQUEST)
        if serial_c.errors:
            message = serial_c.errors
        elif serial_s.errors:
            message = serial_s.errors
        return Response(message,status=status.HTTP_400_BAD_REQUEST)







