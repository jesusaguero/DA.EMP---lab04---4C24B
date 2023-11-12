from django.shortcuts import redirect, render


def login(request):
    return render(request, 'login.html')

def calculo(request):
    if request.method == 'POST':
        return redirect('resultado')

    return render(request, 'calculo.html')


def verificar_login(request):
    if request.method == 'POST':
        apellido = request.POST.get('apellido')
        contrasena = request.POST.get('contrasena')

        if apellido == "aguero" and contrasena == "123":
            return redirect('calculo')
        else:
            return redirect('login')

    return render(request, 'login.html')

def resultado(request):
    return render(request, 'resultado.html')