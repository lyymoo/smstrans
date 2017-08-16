# 实现思路
- 使用smtplib和email库，这两个库均包含在python标准函数库中
- smtplib为python下的SMTP (Simple Mail Transport Protcol) 客户端
- email包为python下的邮件消息管理器，专门用来发送各种邮件消息的
- 利用email中email.mime和email.encoder包进行创建新邮件
- MIME: 多用途因特网邮件扩展(Multipurpose Internet Mail Extensions)
- email.mime.base.MIMEBase为MIME-specific子类的基类
- email.mime.multipart.MIMEMultipart为MIMEBase基类的一个子类，用于管理邮件附件
- email.mime.text.MIMEText用于创建基于MIME的邮件文本消息
- email.encoders用于设置邮件传送时（Content-Transfer-Encoding）的编码
# 实现目的
- python有了这些email功能的类库，python的coder可以通过调用这些类库，实现一个具有邮件收发功能的应用程序。
# 实现内容
## 创建一个新邮件

```
mail_me="limeng"+"<"+self.mail_user+"@"+self.mail_postfix+">"
msg = MIMEMultipart()
msg['Subject'] = sub
msg['From'] = mail_me
msg['To'] = ";".join(mail_to)
mail_list = [mail_to]
if mail_cc:
    msg['Cc'] = ";".join(mail_cc)
    mail_list.append(mail_cc)
if mail_bcc:
    msg['Bcc'] = ";".join(mail_bcc)
    mail_list.append(mail_bcc)
msg.attach(MIMEText(content,'html','utf-8'))
for f in files:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(f, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)
```

## 创建一个邮件客户端

```
# SMTP
s = smtplib.SMTP()  
s.connect(self.mail_host)
s.login(self.mail_user+"@"+self.mail_postfix,self.mail_pass)
# 启用了SSL的SMTP
smtp = smtplib.SMTP_SSL(server['name'], server['port'])
s.login(self.mail_user+"@"+self.mail_postfix,self.mail_pass)
```

## 使用邮件客户端发送新邮件

```
try:
    s = smtplib.SMTP()  
    s.connect(self.mail_host)
    s.login(self.mail_user+"@"+self.mail_postfix,self.mail_pass)
    s.sendmail(mail_me, mail_list, msg.as_string())
    s.close()
    return True
except Exception as e:
    print("send mail exception: %s"%(str(e),))
    return False
```

# 参考

- [python官方文档](http://lee.mo.cn/py/library/email.html)
- 借助python的内容email类库，可以轻松实现基于邮件的消息通知
- 国内各种免费的邮箱均提供手机客户端，比如：QQ邮箱客户端、阿里云邮箱客户端、网易邮箱大师
- 手机邮箱客户端结合自动发信应用，在保证实时性的同时可以让消息通知的成本更为低廉
- 典型应用：服务器状态异常告警、自动订羽毛球场地通知……
