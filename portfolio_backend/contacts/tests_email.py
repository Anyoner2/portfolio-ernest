from django.test import TestCase, override_settings
from django.core import mail
from django.core.mail import send_mail


class EmailSendingTests(TestCase):
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_send_mail_puts_message_in_outbox(self):
        sent = send_mail(
            'Test Subject',
            'This is the body of the test message.',
            'sender@example.com',
            ['recipient@example.com'],
        )
        self.assertEqual(sent, 1)
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, 'Test Subject')
        self.assertIn('This is the body', message.body)
        self.assertEqual(message.from_email, 'sender@example.com')
        self.assertEqual(message.to, ['recipient@example.com'])
