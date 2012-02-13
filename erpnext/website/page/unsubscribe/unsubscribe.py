import webnotes

@webnotes.whitelist()
def unsubscribe(arg):
	"""unsubscribe from lists"""
	lists = [['Blog Subscriber', 'name']]
	for l in lists:
		webnotes.conn.sql("""delete from `tab%s` where %s=%s""" % (l[0], l[1], '%s'), arg)
		
	webnotes.msgprint('Unsubscribed!')