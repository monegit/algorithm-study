test1 = ["119", "97674223", "1195524421"] # false
test2 = ["123","456","789"] # true
test3 = ["12","123","1235","567","88"] # false

def solution(phone_book):
	phone_book.sort()
	
	for p1, p2 in zip(phone_book, phone_book[1:]):
		if p2.startswith(p1):
			return False
	return True
	
print(solution(test1))
