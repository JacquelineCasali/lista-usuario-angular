from rest_framework import viewsets
from .models import Menber
from .serializers import MenberSerializer , MenberSimpleSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class MenberViewSet(viewsets.ModelViewSet):
  
    queryset = Menber.objects.all()
    serializer_class = MenberSerializer
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=[IsAuthenticated,]

    
#  definir o metodo listen (listagem )

# padrão do django
    def list(self, request, *args, **kwargs):
    # banco de dados 
    # busca itens do banco
        queryset = Menber.objects.all()
        serializer = MenberSimpleSerializer(queryset, many=True)
        return Response(serializer.data)