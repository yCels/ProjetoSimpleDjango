from rest_framework import serializers
from escola.models import Aluno, Curso , Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome' , 'rg', 'cpf', 'data_nasc']




class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields = '__all__'
        
        

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []#mesma forma de traz3er todos campos