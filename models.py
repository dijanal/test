# from flask_table import Table, Col

class Comment(object):
	def __init__(self,text,date):
		self.text=text
		self.date=date

	def __repr__(self):
		return '{},{}'.format(self.text,self.date)

print 'eeee'




COMMENTS = [
    Comment("hello", "2018-01-01"),
    Comment("world", "2018-01-02"),
    Comment("test", "2018-01-03"),]


class Table(object):
    text = Col('Text')
    date = Col('Date')
# texts = ['a','b','c']
# dates = ['12-12-12']

# for index in xrange(0,3):
# 	c = Comment(texts[index], dates[index])
# 	COMMENTS.append(c)








