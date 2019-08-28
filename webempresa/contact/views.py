from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    #verificar si el metodo es post
    if request.method == "POST":   
        #aqui devuelve los datos que estaen el formulario 
        contact_form = ContactForm(data=request.POST)
        # aqui a cada variable le damos el valor de cada campo segun el diccionario
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto ",
                "De {} <{}>\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["abiel1999@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #si todo ha ido bien 
                return redirect(reverse('contact')+ '?ok')
            except:
                # algo o ha ido bien redireccionamos a FAIL
                return redirect(reverse('contact')+ '?fail')
            

    return render(request, "contact/contact.html" , {'form': contact_form })   