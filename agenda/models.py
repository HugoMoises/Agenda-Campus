from django.db import models

class Local(models.Model):
    nome = models.CharField(unique=True, max_length=200)
    endereco = models.CharField(max_length=250)
    capacidade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "locais"

class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    titulo = models.TextField()
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.Protect)
    categoria = models.ManyToMany(Categoria, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['inicio']

class Atividade(models.Model):
    titulo = models.TextField()
    palestrante = models.CharField(max_length=250)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)