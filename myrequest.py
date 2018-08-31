import requests
import smtplib
from email.mime.text import MIMEText
import logging
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
def send_email(self, subject, content, mail=[]):
    # Send a reminder email
    sender = 'weix.hao@intel.com'
    receivers = ['jinxiax.li@intel.com', 'wenling.zhang@intel.com', 'nanlin.xie@intel.com'] + mail
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['TO'] = ','.join(receivers)
    # print(subject)
    # print(content)
    # print(receivers)
    try:
        s = smtplib.SMTP('smtp.intel.com')
        s.sendmail(sender, receivers, msg.as_string())
        logging.info('send suess')
    except smtplib.SMTPException as err:
        logging.info('Failed to send mail\n{}'.format(err))