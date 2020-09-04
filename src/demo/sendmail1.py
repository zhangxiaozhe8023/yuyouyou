#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020-08-10 09:45
# @Author : apple
# @Software: PyCharm
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '980778026@qq.com'  # 发件人邮箱账号
my_pass = 'mymvvlcfrvbubfjf'  # 发件人邮箱密码
my_user = '193148037@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        # msg = MIMEText ( '填写邮件内容', 'plain', 'utf-8' )
        # msg['From'] = formataddr ( ["FromRunoob", my_sender] )  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr ( ["FK", my_user] )  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        msgRoot = MIMEMultipart ( 'related' )
        msgRoot['From'] = formataddr ( ["张晓哲测试", my_sender] )  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msgRoot['From'] = Header ( "这是头部", 'utf-8' )
        msgRoot['To'] = Header ( "测试", 'utf-8' )
        subject = 'Python SMTP 邮件测试'
        msgRoot['Subject'] = Header ( subject, 'utf-8' )

        msgAlternative = MIMEMultipart ( 'alternative' )
        msgRoot.attach ( msgAlternative )

        mail_msg = """
        <p>各位领导</p>
<br>

<p>您好，以下是20190414测试报告，如有任何问题，请与测试部门联系。</p>
<img src='th.jpeg'>
<table border="1" cellpadding="3" cellspacing="0" style='font-size:12px;text-align:left;border-color:#fff;empty-cells: show;' >
    <tr>
        <td bgcolor="#E0EEE0">日期:#billing_date#</td>
        <td></td>
    </tr>
    <tr>

        <td bgcolor="#E0EEE0">账号</td>
        <td>#customer_account#</td>
    </tr>
    <tr>
        <td bgcolor="#E0EEE0">发送数目</td>
        <td>#totalsendnumber#</td>
    </tr>
    <tr>
        <td bgcolor="#E0EEE0">计费数目</td>
        <td>#totalratednumber#</td>
    </tr>
    <tr>
        <td bgcolor="#E0EEE0">费用USD</td>
        <td>#totalcharge#</td>
    </tr>
</table>

</br>
<table border="0" cellpadding="3" cellspacing="2" >
    <tr>
        <td colspan="2" >
            <table class="table table-bordered" border="1" cellpadding="3" cellspacing="0" style='font-size:12px;text-align:left;border-color:#fff'>
                <thead>
                    <tr bgcolor="#E0EEE0">
                        <th width=150> 国家 </th>
                        <th width=150> 发送条数 </th>
                        <th width=150> 计费条数  </th>
                        <th width=150> 单价  </th>
                        <th width=150> 费用USD </th>
                    </tr>
                </thead>
                    <tbody>
                #country_based_detailed_template#
                    </tbody>
                <tfoot>
                    <tr>
                        <th colspan="2">总数</th>
                        <th>#totalsendnumber#</th>
                        <th>#totalratednumber#</th>
                        <th>#totalcharge#</th>

                    </tr>
                </tfoot>
            </table>
        </td>
    </tr>
</table>
</br>
<p>质量是第一生命线!</p>
详细信息请查看<a href="https://testerhome.com/topics/18760">详细信息</a>
<p>测吧质量部</p>
<p><img src="cid:image1"></p>
        """
        msgAlternative.attach ( MIMEText ( mail_msg, 'html', 'utf-8' ) )

        # 指定图片为当前目录
        fp = open ( 'th.jpeg', 'rb' )
        msgImage = MIMEImage ( fp.read () )
        fp.close ()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header ( 'Content-ID', '<image1>' )
        msgRoot.attach ( msgImage )

        server = smtplib.SMTP_SSL ( "smtp.qq.com", 465 )  # 发件人邮箱中的SMTP服务器，端口是25
        server.login ( my_sender, my_pass )  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail ( my_sender, [my_user, ], msgRoot.as_string () )  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit ()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print ( "邮件发送成功" )
else:
    print ( "邮件发送失败" )