from grid import grid
from slicem import slicem


def drive():
	#create table
	table = grid()

	#get how many slice to place
	slice_count_to_place = table.getSliceCountToPlace()
	print("slice count to place: ",slice_count_to_place)

	#place first slice
	table.placeFirstSlice()
	slice_count_to_place -= 1

	#place rest of slices
	for i in range(slice_count_to_place):
		table.placeNextSlice()

	print("curr slice count: ",len(table.slices))
	print()

	any_move_taken = False
	any_slice_removed = False
	any_slice_added = False

	while True:
		print("an iteration starts")
		any_move_taken = False
		any_slice_removed = False
		any_slice_added = False
		#ASSUMPTION: one move per slice per iteration
		for s in table.getOrderedSliceArray():
			legal_move_tuple = s.setLegalMoves()
			print()
			print("slice: ",s.solust," ",s.sagalt)
			print("this slice's legal moves",legal_move_tuple)
			
			if(legal_move_tuple != (0,0,0,0) ): #decide on the format of legal_move_tuple 0,0,0,0 or [u,p,l]
				direction_to_go = s.getMoveDirection(legal_move_tuple)
				s.move(direction_to_go)
				print("moved to: ",direction_to_go)
				print("new slice: ",s.solust," ",s.sagalt)
				any_move_taken = True

		if (any_move_taken==False and table.getCurrentSliceCount()-1 > table.minSliceCount() ):
			table.removeSlice()
			any_slice_removed=True
		
		#remove slicedan sonra, hemen add mi yapsın, yoksa iterasyonda devam edip
		# removelayamadığında mı add yapsın???
		#
		#su an ikincisini sectik
		
		if(any_slice_removed==False and table.getCurrentSliceCount()+1 < table.maxSliceCount()):
			table.addSlice()
			any_slice_added = True




		if (any_move_taken or any_slice_removed or any_slice_added) == False:
			break

	#now output the final values
	print("finished driver")
	print()
	print(len(table.slices))
	for s in table.slices:
		print(s.solust[0]," ",s.solust[1]," ",s.sagalt[0]," ",s.sagalt[1])



drive()

if __name__ == "__main__":
	drive()



