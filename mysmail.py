# _*_ coding:utf-8 _*_

import smtplib

from email.mime.text import MIMEText

#
# sender = 'Integration_auto_merge@intel.com'
# receivers = ['weix.hao@intel.com']
# subject = 'outlooktest'
# content = 'code send email test'
# msg = MIMEText(content, 'plain', 'utf-8')
# msg['Subject'] = subject
# msg['From'] = sender
# msg['TO'] = ','.join(receivers)
#
# try:
#     s = smtplib.SMTP('smtp.intel.com')
#     s.sendmail(sender, receivers, msg.as_string())
#     print('send suess')
# except smtplib.SMTPException as err:
#     print('Failed to send mail\n{}'.format(err))
# strh = "https://api.github.com/repos/lyan3/acrn-hypervisor/branches{/branch}".split('{',1)[0]
# print(strh+'/master')
