from django.contrib import admin
from .models import Cattleya
from .models import Dendrobium
from .models import Chiloschista
from .models import Vanda

# Register your models here.
admin.site.register(Cattleya)
admin.site.register(Dendrobium)
admin.site.register(Chiloschista)
admin.site.register(Vanda)
