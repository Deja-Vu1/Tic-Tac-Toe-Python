import random
# Başlıyoruz bakalım...
class olustur():
	def __init__(self):
		self.bitti = 0
		self.list = {"a1" : "." , "b1" : "." , "c1" : "." , "a2" : "." , "b2" : "." ,"c2" : "." ,"a3" : "." , "b3" : "." ,"c3" : "." }
		self.kazanma = [["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"],["a1","b2","c3"],["c1","b2","a3"],["a1","b1","c1"],["a2","b2","c2"],["a3","b3","c3"]]
		print("""
		#############################
		######[ Tic, Tac, Toe ]######
		#############################
		""")
		self.chk = 0
		self.kontrol = 0
		self.secim()
	def söyle(self,a,b):
		print("""
		############################################
		#####[BİLGİSAYAR """+ a + """ KISMINA OYNADI (""" + b + """)]#####
		############################################
			""")
	def başla(self,a):
		if a == "00":
			self.savunma = 0
			self.atakhamlekontrol = 0
			self.svnmahamlekontrol = 0
			self.savunma = 0
			self.svnmahamle = []
			self.atakhamle = []
			if len(self.x) + len(self.o) != 9:
				for i in range(len(self.kazanma)):
					self.atak = 0
					for j in range(3):
						if str(self.o).find(self.kazanma[i][j]) > -1:
							self.atak += 1
					if self.atak == 2:
						for i in self.kazanma[i]:
							if str(self.o).find(i) == -1:
								if str(self.hepsi).find(i) != -1:
									self.o.append(i)
									self.hepsi.remove(i)
									self.söyle(i,"O")
									try:
										self.table[3].remove(i)
									except:
										pass
									self.tablogoster("11")
									self.atakhamlekontrol = 1
									break;
				if self.atakhamlekontrol != 1:
					for i in range(len(self.kazanma)):
						self.savunma = 0
						for j in range(3):
							if str(self.x).find(self.kazanma[i][j]) > -1:
								self.savunma += 1
						if self.savunma == 2:
							for i in self.kazanma[i]:
								if str(self.x).find(i) == -1:
									if str(self.hepsi).find(i) != -1:
										self.o.append(i)
										self.hepsi.remove(i)
										self.söyle(i,"O")
										try:
											self.table[3].remove(i)
										except:
											pass
										self.tablogoster("11")
										self.svnmahamlekontrol = 1
										break;
					if self.svnmahamlekontrol != 1:
						if str(self.hepsi).find("b2") != -1:
							self.bilgoynama = "b2"
							self.o.append(self.bilgoynama)
							self.hepsi.remove(self.bilgoynama)
							self.söyle(self.bilgoynama,"O")
							try:
								self.table[3].remove(self.bilgoynama)
							except:
								pass
							self.tablogoster("11")
						else:
							if len(self.table[3]) != 0:
								self.bilgoynama = random.choice(self.table[3])
								self.o.append(self.bilgoynama)
								self.hepsi.remove(self.bilgoynama)
								self.söyle(self.bilgoynama,"O")
								try:
									self.table[3].remove(self.bilgoynama)
								except:
									pass
								self.tablogoster("11")
							else:
								self.bilgoynama = random.choice(self.hepsi)
								self.o.append(self.bilgoynama)
								self.hepsi.remove(self.bilgoynama)
								self.söyle(self.bilgoynama,"O")
								try:
									self.table[3].remove(self.bilgoynama)
								except:
									pass
								self.tablogoster("11")
		elif a == "01":
			self.savunma = 0
			self.atakhamlekontrol = 0
			self.svnmahamlekontrol = 0
			self.savunma = 0
			self.svnmahamle = []
			self.atakhamle = []
			if len(self.x) + len(self.o) != 9:
				for i in range(len(self.kazanma)):
					self.atak = 0
					for j in range(3):
						if str(self.x).find(self.kazanma[i][j]) > -1:
							self.atak += 1
					if self.atak == 2:
						for i in self.kazanma[i]:
							if str(self.x).find(i) == -1:
								if str(self.hepsi).find(i) != -1:
									self.x.append(i)
									self.hepsi.remove(i)
									self.söyle(i,"X")
									try:
										self.table[3].remove(i)
									except:
										pass
									self.tablogoster("10")
									self.atakhamlekontrol = 1
									break;
				if self.atakhamlekontrol != 1:
					for i in range(len(self.kazanma)):
						self.savunma = 0
						for j in range(3):
							if str(self.o).find(self.kazanma[i][j]) > -1:
								self.savunma += 1
						if self.savunma == 2:
							for i in self.kazanma[i]:
								if str(self.o).find(i) == -1:
									if str(self.hepsi).find(i) != -1:
										self.x.append(i)
										self.hepsi.remove(i)
										self.söyle(i,"X")
										try:
											self.table[3].remove(i)
										except:
											pass
										self.tablogoster("10")
										self.svnmahamlekontrol = 1
										break;
					if self.svnmahamlekontrol != 1:
						if str(self.hepsi).find("b2") != -1:
							self.bilgoynama = "b2"
							self.x.append(self.bilgoynama)
							self.hepsi.remove(self.bilgoynama)
							self.söyle(self.bilgoynama,"X")
							try:
								self.table[3].remove(self.bilgoynama)
							except:
								pass
							self.tablogoster("10")
						else:
							if len(self.table[3]) != 0:
								self.bilgoynama = random.choice(self.table[3])
								self.x.append(self.bilgoynama)
								self.hepsi.remove(self.bilgoynama)
								self.söyle(self.bilgoynama,"X")
								try:
									self.table[3].remove(self.bilgoynama)
								except:
									pass
								self.tablogoster("10")
							else:
								self.bilgoynama = random.choice(self.hepsi)
								self.x.append(self.bilgoynama)
								self.hepsi.remove(self.bilgoynama)
								self.söyle(self.bilgoynama,"X")
								try:
									self.table[3].remove(self.bilgoynama)
								except:
									pass
								self.tablogoster("10")
		elif a == "11":
			while True:
				self.kontrolet = 0
				self.move = input("""
		Lütfen hareket edeceğiniz yeri seçin,
		sırasıyla satır ve sütun olarak: (örnek: a1) """)
				self.move = self.move.lower()
				if str(self.x).find(self.move) > -1 or  str(self.o).find(self.move) > -1:
					print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
				elif str(self.hepsi).find(self.move) > -1:
					for i in self.hepsi:
						if i == self.move:
							self.kontrolet = 1
							self.x.append(self.move)
							self.hepsi.remove(self.move)
							try:
								self.table[3].remove(self.move)
							except:
								pass
							print("""
		##########################################
		######[SİZ """+ self.move + """ KISMINA OYNADINIZ (X)]######
		##########################################
				""")
							self.tablogoster("00")
							break;
					if self.kontrolet != 1:
						print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
				else:
					print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
		elif a == "10":
			while True:
				self.kontrolet = 0
				self.move = input("""
		Lütfen hareket edeceğiniz yeri seçin,
		sırasıyla satır ve sütun olarak: (örnek: a1) """)
				self.move = self.move.lower()
				if str(self.o).find(self.move) > -1 or  str(self.x).find(self.move) > -1:
					print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
				elif str(self.hepsi).find(self.move) > -1:
					for i in self.hepsi:
						if i == self.move:
							self.o.append(self.move)
							self.hepsi.remove(self.move)
							try:
								self.table[3].remove(self.move)
							except:
								pass
							print("""
		##########################################
		######[SİZ """+ self.move + """ KISMINA OYNADINIZ (O)]######
		##########################################
				""")
							self.kontrolet = 1
							self.tablogoster("01")
							break;
					if self.kontrolet != 1:
							print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
				else:
					print("""
			###########################
			[BURAYA YERLEŞTİREMEZSİNİZ]
			###########################
					""")
	def tablo(self):
		self.hepsi = ["a1","b1","c1","a2","b2","c2","a3","b3","c3"]
		self.table = [["a1","b1","c1",],["a2","b2","c2",],["a3","b3","c3",],["a3","a1","c1","c3"]]
		if self.secim != "X":
			print("""
		############################
		[OYUNA BİLGİSAYAR BAŞLAYACAK]
		############################
					""")
			self.baslama = "01"
			self.check = 0
			self.x = []
			self.o = []
			self.tablogoster("2")
		else:
			print("""
		###########################
		[OYUNA SİZ BAŞLAYACAKSINIZ]
		###########################
					""")
			self.baslama = "11"
			self.check = 0
			self.x = []
			self.o = []
			self.tablogoster("2")
	def secim(self):
		while True:
			self.secim = input("""
		Lütfen hangi karakter
		olarak oyuna başlayacağınızı seçiniz (X veya O) :""")
			self.secim = self.secim.upper()
			if self.secim == "O" or  self.secim == "X":
				break;
			else:
				print("""
			##############
			[YANLIŞ SEÇİM]
			##############
					""")
		self.tablo()
	def tablogoster(self,durum):
		for i in range(len(self.x)):
			y = self.x[i]
			d1 = {y: "X"}
			self.list.update(d1)
		for i in range(len(self.o)):
			y = self.o[i]
			d1 = {y: "O"}
			self.list.update(d1)
		print("""
		#|1_2_3_
		a|""" + self.list["a1"]+ """|""" + self.list["a2"]+ """|""" + self.list["a3"]+ """|
		b|""" + self.list["b1"]+ """|""" + self.list["b2"]+ """|""" + self.list["b3"]+ """|
		c|""" + self.list["c1"]+ """|""" + self.list["c2"]+ """|""" + self.list["c3"]+ """|

			""")
		for i in range(len(self.kazanma)):
			if str(self.x).find(self.kazanma[i][0]) > -1 and str(self.x).find(self.kazanma[i][1]) > -1 and str(self.x).find(self.kazanma[i][2]) > -1:
				print("""
		#################
		##[ X KAZANDI ]##
		#################
			""")
				self.bitti = 1
				quit()
		for i in range(len(self.kazanma)):
			if str(self.o).find(self.kazanma[i][0]) > -1 and str(self.o).find(self.kazanma[i][1]) > -1 and str(self.o).find(self.kazanma[i][2]) > -1:
				print("""
		#################
		##[ O KAZANDI ]##
		#################
			""")
				self.bitti = 1
				quit()
		if len(self.x) + len(self.o) == 9:
			print("""
		################
		##[ BERABERE ]##
		################
			""")
			self.bitti = 1
			quit()
		if self.bitti == 0 and len(self.x) + len(self.o) != 9:
			if durum != "2":
				self.başla(durum)
			else:
				self.başla(self.baslama)
		else:
			exit()
tictactoe = olustur()