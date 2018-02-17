from pizza import grid,slice












if __name__ == "__main__":
	
	table = grid()
	#En az kalan eleman 
	minority = "M" if table.remainingM <= table.remainingT else "T"
	firstMinority = None
	for i in range(table.r):
		for j in range(table.c):	
			if table[i][j][0] == minority:
				firstMinority = table[i][j]
				break;
		"""____________________________________"""	
		else:
			continue

		break

