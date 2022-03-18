from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.forms import CharField



class Localizacao (models.Model):
    numeroDeOrdem = models.CharField(max_length= 100, verbose_name= 'Número de Ordem')
    pnt = models.PointField ('geom', srid= 4326, default = 'POINT(-43.175552 -22.895738)', null=False, blank=True)

    def __str__(self):
        return self.numeroDeOrdem


class Objeto (models.Model):
    POSICAO = (
        ('R', 'Reportada'),
        ('E', 'Estimada'),
        ('C', 'Confirmada'),
        ('O', 'Outras')
    )
    LOCALIZACAO = (
        ('M', 'MarAberto'),
        ('R', 'Rio'),
        ('L', 'Lagunar'), 
        ('C', 'Costa'),
        ('A', 'AguasInteriores'),
        ('O', 'Outros')
    )
    ESTADONACAO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal'),
    )

    numeroDeOrdem = models.CharField(max_length= 10, verbose_name= 'Número de Ordem')
    estadoNacao = models.CharField (max_length=  2, choices= ESTADONACAO, blank =False, null=False, default= 'O', verbose_name = ' Estado')
    nome = models.CharField(max_length=30, verbose_name= 'Nome do objeto')
    classe = models.CharField(max_length=30, verbose_name= 'Classe do objeto')
    tipo = models.CharField(max_length= 30, verbose_name= 'Tipo do objeto')
    causa = models.CharField(max_length=50, verbose_name= 'Causa do naufrágio')
    posicao = models.CharField (max_length=  1, choices= POSICAO, blank =False, null=False, default= 'O', verbose_name = 'Posição')
    bandeira = models.CharField (max_length=50)
    dataSinistro = models.DateField(verbose_name= 'Data do sinitro')
    informacoesComplementares = models.CharField (max_length= 500, verbose_name = ' Informações complementares')
    fontes = models.CharField(max_length=50)
    dataRegistro = models.DateTimeField (auto_now_add= True, verbose_name= 'Data interna do registro no DPHDM')
    localizacao = models.CharField (max_length=  1, choices= LOCALIZACAO, blank =False, null=False, default= 'O')
    disponibilidadeInformacao = models.CharField (max_length= 50, verbose_name = 'Disponibilidade da informação')
    interesseHistoricoArqueologico = models.CharField (max_length = 50, verbose_name = 'Interesse histórico e arqueológico')

    def __str__(self):
        return self.numeroDeOrdem

# class ObjetoLocalizacao (models.Model):
    
#     numeroDeOrdem = models.ForeignKey (Localizacao, on_delete = models.CASCADE)
#     estadoNacao = models.ForeignKey (Objeto, on_delete = models.CASCADE)
    
#     def __str__(self):
#         return self.estadoNacao
