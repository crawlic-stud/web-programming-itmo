from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from django.contrib.auth import get_user_model


def send_message(name: str, email: str, message: str):
    text = get_template("message.html")
    html = get_template("message.html")
    context = {"name": name, "email": email, "message": message}
    subject = "Сообщение от пользователя"
    from_email = "from@example.com"
    text_content = text.render(context)
    html_content = html.render(context)
    
    User = get_user_model()
    all_admins = [user.email for user in User.objects.all()]
    print(all_admins)
    msg = EmailMultiAlternatives(subject, text_content, from_email, all_admins)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
