from django.forms import ModelForm, fields
from .models import Productos

class ProductForm(ModelForm):
    class Meta:

        model = Productos

        # fields = ('cod_product','description','category','price','stock')
        fields = '__all__'
