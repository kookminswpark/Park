from logic import numbergame

ng=numbergame()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	ng.newgame(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = int (d.get('guess', [''])[0])
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	msg = ng.guess(guess)
	trials = ng.getguesscount()

	return {'code': 'success', 'msg': msg, 'trials': trials}
