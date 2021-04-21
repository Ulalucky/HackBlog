from django.core.mail import send_mail


def send_activation_code(email, activation_code, is_password):
    activation_url = f'http://localhost:8000/v1/api/account/activate/{activation_code}'
    if not is_password:
         message = f'Thank you for registration!\nTo activate your account, please, click link here {activation_url}'
    else:
         message = activation_code
    send_mail(
        'HackBlog Activation',
        message,
        'admin@admin.com',
        [email, ],
        fail_silently=False
    )

