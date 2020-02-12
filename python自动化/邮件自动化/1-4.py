import zmail

server = zmail.server('gongzuo7853@163.com', 'pxy1010995752')
mail = server.get_latest()
# zmail.show(mail)
print(mail['subject'])

zmail.save_attachment(mail, target_path=None, overwrite=True)