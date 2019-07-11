"""vistas de papeposts"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from datetime import datetime

# Create your views here.
hora = datetime.now().strftime('%b %d del %Y %H:%M horas')
posts = [
    {
        'title': 'viaje a machupichu',
        'user': {
            'name': 'Lorena Delgado Cadena',
            'picture':'https://scontent.fscl11-1.fna.fbcdn.net/v/t1.0-1/c0.12.160.160a/p160x160/65366789_2331563240232595_1786744311107289088_n.jpg?_nc_cat=105&_nc_oc=AQlxrsFRAD_7IOJwnj84NX4axIBi2Po9nS9kFIlWwc5Jb6zifkffMSykjrSC1wrSoPQ&_nc_ht=scontent.fscl11-1.fna&oh=d447e9c5230fddae548da64dd17d70ce&oe=5DAAF38E'
        },
        'timestamp': hora,
        'photo': 'https://scontent.fscl11-1.fna.fbcdn.net/v/t1.0-9/64460645_2304479666274286_6808865521828626432_n.jpg?_nc_cat=111&_nc_oc=AQmHip7g1lpw2e6ScjmRWnJry_xqJwL8gNcdu9w60b4W6_bDMLmwrIP48_6Q9-UGvSk&_nc_ht=scontent.fscl11-1.fna&oh=7d832501dd67edb8c039353b2db2cd75&oe=5DAB32D1'
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Mangel Mera',
            'picture': 'https://scontent.fscl11-1.fna.fbcdn.net/v/t1.0-1/p160x160/48971463_10218118848665155_393845855343345664_n.jpg?_nc_cat=110&_nc_oc=AQmxI7h4kfjVbHgIFGe2iXKGtmWNo9tJjJauXPtbsoGNC0K0lfnv87UnYKBwRTjit_E&_nc_ht=scontent.fscl11-1.fna&oh=ec0be017c2b1ef6d7f222ed4b88cebd8&oe=5DAB3B82'
        },
        'timestamp': hora,
        'photo': 'https://picsum.photos/800/800/?image=903'
    },
    {
        'title': 'viaje a machupichu',
        'user': {
            'name': 'Lorena Delgado Cadena',
            'picture':'https://scontent.fscl11-1.fna.fbcdn.net/v/t1.0-1/c0.12.160.160a/p160x160/65366789_2331563240232595_1786744311107289088_n.jpg?_nc_cat=105&_nc_oc=AQlxrsFRAD_7IOJwnj84NX4axIBi2Po9nS9kFIlWwc5Jb6zifkffMSykjrSC1wrSoPQ&_nc_ht=scontent.fscl11-1.fna&oh=d447e9c5230fddae548da64dd17d70ce&oe=5DAAF38E'
        },
        'timestamp': hora,
        'photo': 'https://picsum.photos/800/800/?image=903'
    }
]

@login_required
def list_posts(request):
	return render(request,'posts/feed.html',{'posts': posts})
