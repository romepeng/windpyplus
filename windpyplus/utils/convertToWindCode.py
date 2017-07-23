def convertCode(stocklists):
	windCodes= []
	for s in stocklists:
		#print(s)
		if s.startswith('6'):
			windCodes.append(s + '.SH')
		else:
			windCodes.append(s + '.SZ')
	return windCodes

def convertBQCode(bqstocks):
	windCodes= []
	for s in bqstocks:
		s = s.replace('A', '')
		windCodes.append(s)
		
	return windCodes

def main():
	stocklists = ['600690', '000623', '000333','601318']
	bqstocks = ['300418.SZA', '300426.SZA', '300429.SZA',  '600000.SHA', '600004.SHA',
          '600007.SHA',  '600009.SHA',]
	print(convertCode(stocklists))
	print(convertBQCode(bqstocks))


if __name__ == '__main__':
	main()
