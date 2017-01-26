class Kangroo:
	'''
	
	attributes: pouch_contents
	'''
	
	def __init__(self, pouch_contents):
		l = []
		l.append(pouch_contents)
		self.pouch_contents = l
		
	def put_in_pouch(self,obj):
		self.pouch_contents.append(obj) 
		
		
	def __str__(self):
		return '%s' % (''.join(str(x) for x in self.pouch_contents))
		
if __name__ == '__main__':
	a = Kangroo('kanga')
	b = Kangroo('roo')
	a.put_in_pouch(b)
	print(a)
	print(b)