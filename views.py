from rest_framework import  viewsets, generics
from registros.models import Objeto, Localizacao 
from registros.serializer import ObjetoSerializer, LocalizacaoSerializer

class ObjetoViewSet (viewsets.ModelViewSet):
    """Exibe os registros dos objetos naufragados"""
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer

class LocalizacaoViewSet (viewsets.ModelViewSet):
    """Exibe a localizacao dos objetos naufragados. 
    O formato para inserção da geometria é SRID=4326;POINT (-43.175552 -22.895738)"""
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer


# class ObjetoLocalizacaoViewSet (viewsets.ModelViewSet):
#     """Exibe as informações dos objetos naufragados, vinculando ao posicionamento geográfico."""
#     queryset = ObjetoLocalizacao.objects.all()
#     serializer_class = ObjetoLocalizacaoSerializer        


# #List API View
# class ListaObjeto (generics.ListAPIView):
#     """Lista os naufrágios por estado da nação"""
#     def get_queryset(self):
#         queryset = ObjetoLocalizacao.objeto.filter (objeto_id = self.Kwargs ['estadoNacao'])
#         return queryset
#     serializer_class = ListaObjetoSerializer
