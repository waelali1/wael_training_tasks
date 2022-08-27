import datetime
from odoo import api, fields, models, _


class DateOfBirth(models.Model):
    _inherit = 'res.partner'
    _description = "Res Partner"

    birth_date = fields.Datetime(string='Date Of Birth')

    
    def send_birthday_email(self, contact,name):
        print('===========contact email============',contact.get('email'))
        if not contact.get('email'):
            return False

        today = datetime.datetime.now()
        print('===========today============',today)
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')
        print('===========today_month_day============',today_month_day)
        isYourBirthday = self.env['res.partner'].sudo().search([('birth_date', 'like', today_month_day)]).get()
        print('===========isYourBirthday============',isYourBirthday)
        

        message = _("<p>Dear %s,<br/>Wish you Happy Birthday %s. </p>") % (contact['name'], name)

        mail_values = {
            'subject': _('Receipt %s', name),
            'body_html': message,
            'author_id': self.env.user.partner_id.id,
            'email_from': self.env.company.email or self.env.user.email_formatted,
            'email_to': contact['email'],
        }

        if isYourBirthday:
            print('============iam here========')
            mail = self.env['mail.mail'].sudo().create(mail_values)
            mail.send()

    @api.model
    def _cron_send_birthday_email(self):
        contacts = self.search([('next_run_date', '<=', fields.Date.today())])
        for contact in contacts:
            try:
                contact.action_send()
            except MailDeliveryException as e:
                _logger.warning('MailDeliveryException while sending contact %d. Contact is now scheduled for next cron update.', contact.id)
