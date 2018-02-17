from pizza import grid,slice












if __name__ == "__main__":
	
	table = grid()
	#En az kalan eleman 
	minority = "M" if table.remainingM <= table.remainingT else "T"
	firstMinority = None

