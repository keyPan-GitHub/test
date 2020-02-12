import smtplib
# 加密邮件内容
from smtplib import SMTP_SSL
# 构造邮件的正文
from email.mime.text import MIMEText
# 把邮件的各个部分装在一起
from email.mime.multipart import MIMEMultipart
# 邮件头 会包括邮件标题，收件人等等信息
from email.header import Header

host_server = 'smtp.163.com'  # 163邮箱smtp服务器
sender_163 = 'gongzuo7853@163.com'  # 发件人的邮箱

pwd = 'pxy1010995752'  # pwd为邮箱密码
receiver = 'gongzuo7853@163.com'  # 收件人的邮箱

mail_title = 'Python办公自动化邮件'  # 邮件标题
# 邮件的正文内容
mail_concent = "您好，这是使用python登录163.com邮箱发送邮件的测试：https://www.python.org"

# 初始化邮件主体
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title, 'utf-8')
msg['From'] = sender_163
msg['To'] = Header('测试邮箱', 'utf-8')
# 邮件正文内容
msg.attach(MIMEText(mail_concent, 'plain', 'utf-8'))

smtp = SMTP_SSL(host_server)  # ssl登录
smtp.login(sender_163, pwd)

smtp.sendmail(sender_163, receiver, msg.as_string())
