# Sudoku lahendaja, absull beisik
#
#
# Lahendus p�hineb sudoku lahendamisel nn backtracking'u kaudu 
# N m��rab �ra 2-dimensionaalse N*N maatriksi 
N = 9

# Funktsioon , mis prindib maatriksi v�lja 

def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end=" ")
		print()

# Funktsioon , mis kontrollib, kas antud numbri v�ib lisada etteantud ritta/veergu

def isSafe(maatriks, rida, veerg, num):

	# Ts�kkel, kus kus kontrollime, kas antud number juba leidub etteantud reas
	# kui jah, siis tagastame - false
	for x in range(9):
		if maatriks[rida][x] == num:
			return False

	# Ts�kkel, kus kus kontrollime, kas antud number juba leidub etteantud veerus
	# kui jah, siis tagastame - false
	for x in range(9):
		if maatriks[x][veerg] == num:
			return False

	# Ts�kkel, kus kus kontrollime, kas antud number juba leidub konkreetses 3*3 alammaatriksis
	# kui jah, siis tagastame - false
	startrida = rida - rida % 3
	startveerg = veerg - veerg % 3
	for i in range(3):
		for j in range(3):
			if maatriks[i + startrida][j + startveerg] == num:
				return False
	return True


# Funktsioon v�tab osaliselt t�idetud maatriksi ja p��ab m��rata k�igi maatriksi seni t�hjade v�ljade v��rtused,
# j�lgides n�udeid, et poleks korduseid ridades ja veergudes, ega 3*3 alammaatriksites
# Backtracking t�hendab, et teostame lahendust rekursiivselt


def solveSudoku(maatriks, rida, veerg):

	# Kontrollime, kas oleme j�udnud 8. ritta ja 9. veeruni
	# kui, siis seega pole m�tet edasist backtrackingut teha ja v�ljastame - true 
	if (rida == N - 1 and veerg == N):
		return True

	# Kui veeru v��rtus on 9, siis alustame uuesti esimesest veerust, st 0
	if veerg == N:
		rida += 1
		veerg = 0

	# Kontrollime, kas antud postsioon juba omab nullist suuremat v��rtust
	# kui, siis v�tame j�rgmise veeru
	if maatriks[rida][veerg] > 0:
		return solveSudoku(maatriks, rida, veerg + 1)
	for num in range(1, N + 1, 1):

		# Kontrollime, kas on v�imalik lisada 1-9 number antud positsiooni (rida/veerg) maatriksis 
		# Liigume j�rgmisele veerule
		if isSafe(maatriks, rida, veerg, num):

			# Lisame antud numbri maatriksi antud positsioonile (rida/veerg)
			# ja eeldame et see sobib antud postisioonis 
			maatriks[rida][veerg] = num

			# Kontrollime sama j�rgmise veerguga 
			if solveSudoku(maatriks, rida, veerg + 1):
				return True

		# Kuna meie eeldus/oletus oli vale ja number ei sobi siia, eemaldame numbri
		# ja l�heme uuele katsele juba uue numbriga
		maatriks[rida][veerg] = 0
	return False

# Programmi kood

# 0 t�hendab t�hjasid pesasid, 
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

# Peale Sudoku t��tlemist prindime v�lja seisud
# kui lahendus, siis maatriksi , kui ei siis teavitame, et lahendus puudub 
if (solveSudoku(maatriks, 0, 0)):
	printing(maatriks)
else:
	print("Noh, puudub lahendus!")





