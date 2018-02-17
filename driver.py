from pizza import grid,slice



#create table
table = grid()

#get how many slice to place
slice_count_to_place = table.getSliceCountToPlace()

#place first slice
grid.placeFirstSlice()
slice_count_to_place -= 1

#place rest of slices
for i in range(slice_count_to_place):
	table.placeNewSlice()


any_move_taken = False
any_slice_removed = False
any_slice_added = False

while True:
	any_move_taken = False
	any_slice_removed = False
	any_slice_added = False
	#ASSUMPTION: one move per slice per iteration
	for s in table.getOrderedSliceArray():
		legal_move_tuple = s.getLegalMoves()
		if(legal_move_tuple != (0,0,0,0) ): #decide on the format of legal_move_tuple 0,0,0,0 or [u,p,l]
			direction_to_go = s.getDirection(legal_move_tuple)
			s.move(direction_to_go)
			any_move_taken = True

	if (any_move_taken==False and table.getCurrentSliceCount()-1 > table.getMinSliceCount() ):
		table.removeSlice()
		any_slice_removed=True
	
	#remove slicedan sonra, hemen add mi yapsın, yoksa iterasyonda devam edip
	# removelayamadığında mı add yapsın???
	#
	#su an ikincisini sectik
	
	if(any_slice_removed==False and table.getCurrentSliceCount()+1 < table.getMaxSliceCount()):
		table.addSlice()
		any_slice_added = True




	if (any_move_taken or any_slice_removed or any_slice_added) == False:
		break



#now output the final values













if __name__ == "__main__":
	main()



