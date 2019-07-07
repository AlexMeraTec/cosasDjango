"""vistas de papeposts"""
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
hora = datetime.now().strftime('%b %d del %Y %H:%M horas')
posts = [
	{
		'name':'Lorena',
		'user':'warrion_black',
		'timestamp': hora,
		'picture':'https://scontent.fscl11-1.fna.fbcdn.net/v/t1.0-9/64460645_2304479666274286_6808865521828626432_n.jpg?_nc_cat=111&_nc_oc=AQmHip7g1lpw2e6ScjmRWnJry_xqJwL8gNcdu9w60b4W6_bDMLmwrIP48_6Q9-UGvSk&_nc_ht=scontent.fscl11-1.fna&oh=7d832501dd67edb8c039353b2db2cd75&oe=5DAB32D1',
	},
    {
        'name': 'Via Láctea',
        'user': 'Mangel_mera',
        'timestamp': hora,
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': hora,
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]
def list_posts(request):
	content = []
	for post in posts:
		content.append("""
			<p><strong>{name}</strong></p>
			<p><strong>{user} - <i>{timestamp}</i></strong></p>
			<figure><img width="20%" height="35%" src="{picture}"/></figure>
		""".format(**post))
	return HttpResponse('<br/>'.join(content))
