"""
Simple hangman game

GitHub : @hakiKhuva
"""

import time
import random
import sys
import sqlite3

words = ['hop', 'jog', 'recondite', 'burn', 'rabbits', 'dark', 'robin', 'yard', 'plantation', 'mass', 'pass', 'billowy', 'responsible', 'learn', 'spy', 'different', 'floor', 'innate', 'close', 'bird', 'detail', 'quarter', 'dare', 'teeny', 'defiant', 'rinse', 'invite', 'skirt', 'lip', 'substance', 'launch', 'vanish', 'wholesale', 'tame', 'disturbed', 'limit', 'lame', 'straw', 'paddle', 'realize', 'cold', 'ill-informed', 'pause', 'bedroom', 'laborer', 'instrument', 'servant', 'kind', 'view', 'wet']

class scores:
	@staticmethod
	def create():
		conn = sqlite3.connect('db.sqlite3')
		curs = conn.cursor()
		curs.execute('''CREATE TABLE IF NOT EXISTS hangmanGame (
				indexKey INTEGER PRIMARY KEY NOT NULL,
				tries INTEGER NOT NULL,
				timeTaken TEXT NOT NULL,
				word TEXT NOT NULL
		)''')
		conn.close()

	@staticmethod
	def get_score():
		scores.create()
		conn = sqlite3.connect('db.sqlite3')
		curs = conn.cursor()
		data = curs.execute('SELECT * FROM hangmanGame')
		print ("\nIndex\tTries\tTime\tWord")
		print ("-"*50)
		for index,tri,Time,word in data:
			print(f"{index}\t{tri}\t%.2f\t{word}" %float(Time))
		conn.close()

	@staticmethod
	def add_score(tries,timeTaken,word):
		scores.create()
		conn = sqlite3.connect('db.sqlite3')
		curs = conn.cursor()
		curs.execute(f"INSERT INTO hangmanGame(tries,timeTaken,word) VALUES('{tries}','{timeTaken}','{word}')")
		conn.commit()
		conn.close()


def play():
	word = random.choice(words)
	while " " in word or "-" in word or "_" in word:
		word = random.choice(words)
	word = word.upper()
	nWord = ""
	dashedWord = []
	tri =  0
	leftTries = int(len(word)*1.5)
	for _ in word:
		dashedWord.append("-")

	startTime = time.time()
	while nWord.join(dashedWord) != word and leftTries > 0:
		print ("Current word :",nWord.join(dashedWord))
		print ("Tries left : %d" %(leftTries))
		letter = input("Enter a letter : ")
		letter = letter.upper()

		i = 0 # iteration
		if letter in word:
			for ltr in word:
				if letter == ltr:
					dashedWord[i] = letter
					i += 1
				else:
					i += 1
			tri += 1

		else:
			print ("\nOops, letter you entered is not in the word!")
			tri += 1
			leftTries -= 1
		print ("")

	if nWord.join(dashedWord) != word:
		print ("Oh, you've hanged hangman !")
		print ("Word :",word)
		sys.exit()

	endTime = time.time()

	scores.add_score(tri,endTime-startTime,word)

	print ("Well done, you've saved hangman.")
	print ("You guessed correct word :",word," and you take %.2f seconds." %(endTime-startTime))
	print ("Total tries :",tri)

def main():
	print ("-"*50)
	print ("Hangman Game")
	print ("-"*50)
	print ("[ 1 ] Start game")
	print ("[ 2 ] Score")
	print ("-"*50)
	menu = input("Enter [1|2] : ")
	if menu == "1":
		play()
	elif menu == "2":
		scores.get_score()
	else:
		menu()

if __name__ == "__main__":
	main()
