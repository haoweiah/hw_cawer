# _*_ coding:utf-8 _*_

import smtplib

from email.mime.text import MIMEText

sender = 'weix.hao@intel.com'
receivers = ['jinxiax.li@intel.com', 'wenling.zhang@intel.com']
subject = 'outlooktest'
content = 'code send email test'
msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = sender
msg['TO'] = ','.join(receivers)

try:
    s = smtplib.SMTP('smtp.intel.com')
    s.sendmail(sender, receivers, msg.as_string())
    print('send suess')
except smtplib.SMTPException as err:
    print('Failed to send mail\n{}'.format(err))