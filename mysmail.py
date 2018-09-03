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

{'protected': False,
 'protection_url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/branches/master/protection',
 '_links': {'html': 'https://github.com/ywan170/acrn-hypervisor/tree/master',
            'self': 'https://api.github.com/repos/ywan170/acrn-hypervisor/branches/master'},
 'protection': {'required_status_checks': {'enforcement_level': 'off', 'contexts': []}, 'enabled': False},
 'name': 'master',
 'commit': {'html_url': 'https://github.com/ywan170/acrn-hypervisor/commit/11f4b014cbcbee62fa3feb00418fe6fb858e56c6',
            'committer': {'html_url': 'https://github.com/dbkinder',
                          'following_url': 'https://api.github.com/users/dbkinder/following{/other_user}',
                          'gists_url': 'https://api.github.com/users/dbkinder/gists{/gist_id}',
                          'url': 'https://api.github.com/users/dbkinder', 'id': 11063618,
                          'organizations_url': 'https://api.github.com/users/dbkinder/orgs', 'gravatar_id': '',
                          'node_id': 'MDQ6VXNlcjExMDYzNjE4', 'login': 'dbkinder',
                          'followers_url': 'https://api.github.com/users/dbkinder/followers',
                          'repos_url': 'https://api.github.com/users/dbkinder/repos', 'site_admin': False,
                          'events_url': 'https://api.github.com/users/dbkinder/events{/privacy}', 'type': 'User',
                          'subscriptions_url': 'https://api.github.com/users/dbkinder/subscriptions',
                          'received_events_url': 'https://api.github.com/users/dbkinder/received_events',
                          'starred_url': 'https://api.github.com/users/dbkinder/starred{/owner}{/repo}',
                          'avatar_url': 'https://avatars0.githubusercontent.com/u/11063618?v=4'},
            'url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/commits/11f4b014cbcbee62fa3feb00418fe6fb858e56c6',
            'comments_url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/commits/11f4b014cbcbee62fa3feb00418fe6fb858e56c6/comments',
            'sha': '11f4b014cbcbee62fa3feb00418fe6fb858e56c6', 'author': {'html_url': 'https://github.com/gvancuts',
                                                                          'following_url': 'https://api.github.com/users/gvancuts/following{/other_user}',
                                                                          'gists_url': 'https://api.github.com/users/gvancuts/gists{/gist_id}',
                                                                          'url': 'https://api.github.com/users/gvancuts',
                                                                          'id': 2192801,
                                                                          'organizations_url': 'https://api.github.com/users/gvancuts/orgs',
                                                                          'gravatar_id': '',
                                                                          'node_id': 'MDQ6VXNlcjIxOTI4MDE=',
                                                                          'login': 'gvancuts',
                                                                          'followers_url': 'https://api.github.com/users/gvancuts/followers',
                                                                          'repos_url': 'https://api.github.com/users/gvancuts/repos',
                                                                          'site_admin': False,
                                                                          'events_url': 'https://api.github.com/users/gvancuts/events{/privacy}',
                                                                          'type': 'User',
                                                                          'subscriptions_url': 'https://api.github.com/users/gvancuts/subscriptions',
                                                                          'received_events_url': 'https://api.github.com/users/gvancuts/received_events',
                                                                          'starred_url': 'https://api.github.com/users/gvancuts/starred{/owner}{/repo}',
                                                                          'avatar_url': 'https://avatars1.githubusercontent.com/u/2192801?v=4'},
            'node_id': 'MDY6Q29tbWl0MTM1NjQ5NDU4OjExZjRiMDE0Y2JjYmVlNjJmYTNmZWIwMDQxOGZlNmZiODU4ZTU2YzY=', 'commit': {
         'tree': {'sha': 'ccc73c14e82c14f36f083bf4239a421eb6e1b053',
                  'url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/git/trees/ccc73c14e82c14f36f083bf4239a421eb6e1b053'},
         'committer': {'date': '2018-05-31T18:46:03Z', 'name': 'David Kinder', 'email': 'david.b.kinder@intel.com'},
         'url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/git/commits/11f4b014cbcbee62fa3feb00418fe6fb858e56c6',
         'message': "Documentation: small addition to the 'acrnlog' tool documentation\n\nMake it clear that some commands mentionned in the 'acrnlog' tool\ndocumentation are meant to be run in the hypervisor shell and *not*\nthe Service OS shell (as are the other commands throughout the rest\nof that document).\n\nSigned-off-by: Geoffroy Van Cutsem <geoffroy.vancutsem@intel.com>",
         'author': {'date': '2018-05-31T13:31:56Z', 'name': 'Geoffroy Van Cutsem',
                    'email': 'geoffroy.vancutsem@intel.com'}, 'comment_count': 0,
         'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}}, 'parents': [
         {'html_url': 'https://github.com/ywan170/acrn-hypervisor/commit/8838c94d5bf8553aca90b1f23a4e91e2580d4320',
          'sha': '8838c94d5bf8553aca90b1f23a4e91e2580d4320',
          'url': 'https://api.github.com/repos/ywan170/acrn-hypervisor/commits/8838c94d5bf8553aca90b1f23a4e91e2580d4320'}]}}
