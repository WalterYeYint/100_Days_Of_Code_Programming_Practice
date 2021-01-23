###########################################################################
# Solution 1

def isValidSubsequence(array, sequence):
	# Write your code here.
	Idx = 0
	for i in array:
		if Idx == len(sequence):
			break
		if sequence[Idx] == i:
			Idx += 1
	return Idx == len(sequence)


###########################################################################
# Solution 2

def isValidSubsequence(array, sequence):
	# Write your code here.
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)
				

