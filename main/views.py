from django.shortcuts import render,get_object_or_404, redirect
from .models import Project
from .models import Project, Testimonial
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
import os


def home(request):
    if request.method == 'POST':
        # Testimonial form submission
        if request.POST.get('name') and request.POST.get('role') and request.POST.get('comment'):
            Testimonial.objects.create(
                name=request.POST['name'],
                role=request.POST['role'],
                comment=request.POST['comment']
            )
            messages.success(request, 'Thanks for the feedback! 🙌')
            return redirect('home')

        # Contact form submission
        elif request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
            name = request.POST.get('name', 'there')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            subject = "Thank you for contacting me!"
            body = f"""
Hi {name},

Thank you for reaching out! I appreciate your interest and am excited about the opportunity to work together.

Please find attached my resume for your reference. I will get back to you shortly.

Best regards,
Sarveshver Sham
"""

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )

            pdf_path = os.path.join(settings.BASE_DIR, 'main','static', 'SARVESHVER_RESUME.pdf')
            if os.path.exists(pdf_path):
                email_message.attach_file(pdf_path)
            else:
                messages.warning(request, 'Resume file not found!')

            try:
                email_message.send()
                messages.success(request, 'Resume sent! Check your inbox (and maybe spam folder).')
            except Exception as e:
                messages.error(request, f'Sorry, there was an error sending the email: {e}')

            return redirect('home')

    # Load testimonials for display
    testimonials = Testimonial.objects.all().order_by('-created_at')
    top_testimonials = testimonials[:3]
    bottom_testimonials = testimonials[3:6]

    context = {
        'top_testimonials': top_testimonials,
        'bottom_testimonials': bottom_testimonials,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')



def addproject(request):
    return render(request, 'project.html')  

def project_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'project.html', {'project': project})


def send_about_me(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            subject = "Hi from Sarveshver – Let's Connect!"

            body = """
Hey there 👋,

Thank you for your interest in learning more about me!

I'm Sarveshver Sham – a Full Stack Developer & Digital Solutions Architect.
I specialize in building modern web apps, smart IoT projects, and creating meaningful digital experiences.

💬 Let's chat on WhatsApp: https://wa.me/918695299299  

Feel free to reply if you have any questions or ideas you'd like to discuss!

Warm regards,  
Sarveshver Sham  
sarveshversham@gmail.com  
"""

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )

            try:
                email_message.send()
                return render(request, 'about.html', {'success': 'Message sent! Check your inbox.'})
            except:
                return render(request, 'about.html', {'error': 'Could not send email. Please try again.'})
        else:
            return render(request, 'about.html', {'error': 'Please enter a valid email address.'})

    return redirect('about')