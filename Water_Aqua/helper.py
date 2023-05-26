from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class Help:
    def mail_functionality(self, email_template, subject, to_email, data):
            # template = get_template(email_template)
            # html = template.render(result_message)
            html_message = render_to_string(email_template, data)
            mail_subject = subject
            message = html_message
            to_email = [to_email]
            # 'sales@amtz.in', 'finance@amtz.in'
            email = EmailMultiAlternatives(
                mail_subject,
                "hello",  # necessary to pass some message here
                settings.EMAIL_HOST_USER, to_email)
            email.attach_alternative(message, "text/html")
            # email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            # receipt_file = BytesIO(pdf)
            return True