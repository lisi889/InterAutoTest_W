import smtplib
from email.mime.multipart import MIMEMultipart

#建立数据初始化、
#smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
from email.mime.text import MIMEText


class SendEmail:
    def __init__(self,stmp_addr,username,password,recv,title,content=None,file=None):
        self.stmp_addr = stmp_addr
        self.username =username
        self.password = password
        self.recv= recv
        self.title=title
        self.content = content
        self.file = file

#发送邮件方法
    def send_mail(self):
        #mine
        msg = MIMEMultipart()
        #初始化邮件信息
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.recv
        #邮件附件
        #判断是否附件
        if self.file:
        #Mimetex读取文件
            att = MIMEText(open(self.file).read())
        #设置内容类型
            att["Content-Type"] = 'application/octet-stream'
        #设置附件头
            att["Content-Disposition"] = 'attachement;filename="%s"'% self.file
        #将内容附件到邮件主体中
            msg.attach(att)
        #登录邮件服务器
        self.smtp = smtplib.SMTP(self.stmp_addr,port=25)
        self.smtp.login(self.username,self.password)
    #发送邮件
        self.smtp.sendmail(self.username,self.recv,msg.as_string())

if __name__ == '__main__':
    #初始化类(self,stmp_addr,username,password,recv,title,content,file)
    from config.Conf import ConfigYaml
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr,username,password,recv,"测试")
    email.send_mail()
