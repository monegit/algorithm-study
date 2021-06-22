# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

test1 = "...!@BaT#*..y.abcdefghijklmasdfasdfasdfafa."
test2="z-+.^."
test3="=.="
test4="123_.def"
test5="abcdefghijklmn.p"

moji = "-_.~!@#$%^&*()=+[{]}:?,<>/"

def solution(new_id):	
	answer = str(new_id)
	
	# 1
	answer = answer.lower()
	
	# 2
	answer = ''.join(x for x in answer if x not in "~!@#$%^&*()=+[{]}:?,<>/")
	
	# 3
	answer = re.sub("['.']+",".", answer)
	
	# 4
	answer = re.sub("^\.","",answer)
	answer = re.sub("\.$","",answer)
	
	# 5
	if answer == "":
		answer = "a"
		
	# 6
	answer = re.sub("^\.","",answer[:15])
	answer = re.sub("\.$","",answer[:15])
	
	# 7
	if len(answer) < 3:
		for i in range(len(answer),3):
			answer = answer + answer[-1:]
	
	print(answer)
	
	return answer
	
solution(test5)
