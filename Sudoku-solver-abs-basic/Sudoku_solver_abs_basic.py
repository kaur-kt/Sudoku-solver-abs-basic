# Sudoku lahendaja, absull beisik
#
#
# Lahendus põhineb sudoku lahendamisel nn backtracking'u kaudu 
# N määrab ära 2-dimensionaalse N*N maatriksi 
N = 9

# Funktsioon , mis prindib maatriksi välja 

def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end=" ")
		print()

# Funktsioon , mis kontrollib, kas antud numbri võib lisada etteantud ritta/veergu

def isSafe(maatriks, rida, veerg, num):

	# Tsükkel, kus kus kontrollime, kas antud number juba leidub etteantud reas
	# kui jah, siis tagastame - false
	for x in range(9):
		if maatriks[rida][x] == num:
			return False

	# Tsükkel, kus kus kontrollime, kas antud number juba leidub etteantud veerus
	# kui jah, siis tagastame - false
	for x in range(9):
		if maatriks[x][veerg] == num:
			return False

	# Tsükkel, kus kus kontrollime, kas antud number juba leidub konkreetses 3*3 alammaatriksis
	# kui jah, siis tagastame - false
	startrida = rida - rida % 3
	startveerg = veerg - veerg % 3
	for i in range(3):
		for j in range(3):
			if maatriks[i + startrida][j + startveerg] == num:
				return False
	return True


# Funktsioon võtab osaliselt täidetud maatriksi ja püüab määrata kõigi maatriksi seni tühjade väljade väärtused,
# jälgides nõudeid, et poleks korduseid ridades ja veergudes, ega 3*3 alammaatriksites
# Backtracking tähendab, et teostame lahendust rekursiivselt


def solveSudoku(maatriks, rida, veerg):

	# Kontrollime, kas oleme jõudnud 8. ritta ja 9. veeruni
	# kui, siis seega pole mõtet edasist backtrackingut teha ja väljastame - true 
	if (rida == N - 1 and veerg == N):
		return True

	# Kui veeru väärtus on 9, siis alustame uuesti esimesest veerust, st 0
	if veerg == N:
		rida += 1
		veerg = 0

	# Kontrollime, kas antud postsioon juba omab nullist suuremat väärtust
	# kui, siis võtame järgmise veeru
	if maatriks[rida][veerg] > 0:
		return solveSudoku(maatriks, rida, veerg + 1)
	for num in range(1, N + 1, 1):

		# Kontrollime, kas on võimalik lisada 1-9 number antud positsiooni (rida/veerg) maatriksis 
		# Liigume järgmisele veerule
		if isSafe(maatriks, rida, veerg, num):

			# Lisame antud numbri maatriksi antud positsioonile (rida/veerg)
			# ja eeldame et see sobib antud postisioonis 
			maatriks[rida][veerg] = num

			# Kontrollime sama järgmise veerguga 
			if solveSudoku(maatriks, rida, veerg + 1):
				return True

		# Kuna meie eeldus/oletus oli vale ja number ei sobi siia, eemaldame numbri
		# ja läheme uuele katsele juba uue numbriga
		maatriks[rida][veerg] = 0
	return False

# Programmi kood

# 0 tähendab tühjasid pesasid, 
maatriks = [[6, 9, 1, 0, 5, 0, 0, 0, 0],
		[0, 0, 0, 7, 0, 0, 0, 5, 0],
		[0, 0, 8, 9, 0, 4, 0, 1, 0],
		[0, 0, 0, 4, 0, 1, 0, 0, 7],
		[0, 0, 0, 0, 0, 0, 0, 3, 0],
		[0, 8, 0, 0, 6, 7, 0, 0, 0],
		[0, 0, 0, 0, 7, 0, 0, 0, 0],
		[0, 3, 0, 2, 0, 8, 0, 0, 1],
		[0, 5, 7, 0, 0, 0, 9, 0, 0]]

maatriks2 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

# Peale Sudoku töötlemist prindime välja seisud
# kui lahendus, siis maatriksi , kui ei siis teavitame, et lahendus puudub 
if (solveSudoku(maatriks, 0, 0)):
	printing(maatriks)
else:
	print("Noh, puudub lahendus!")





