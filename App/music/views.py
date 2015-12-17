from django.shortcuts import render


def view_songs(request):
    songname =  Songs.objects.filter(cdid = request.Cd.id)
    return render_to_response(request, 'music/view_cd.html', {'song': song})

def view_cart(request):
	carts = Cart.objects.filter(cdid = request.Cd.id).values('cdid','purdate',)
    cd = Cd.objects.all()
    return render(request, 'music/cart.html', {'cart': cart, 'cd': cd})
