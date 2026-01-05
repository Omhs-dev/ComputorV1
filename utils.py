def is_X_only(i_str):
	for ch in i_str:
		if ch.isalpha() and ch != "X":
			return False
	return True