# ag  st  jo  fo  na  pw  ps
# 0   1   2   3   4   5   6

# style 0	baoli	1	wenjian		2 	aishidi		3 	daqi		4	zhigu
# job   0	kuaiji	1	suanming	2	qishou		3	yisheng		4	chengxuyuan
# food	0 	xiangsu	1	baiqie		2	hongshao	3	kaoquanyang	4	shiwu4 (qiudaoyu)
# name	0	mao		1	gu			2	dou			3	gua			4	gou
# age	0	15		1	21			2	28			3	32			4	55
# rule 0-9 = {1 3 5 6 7 8 9 11 12 15}
# power 0 is most powerful

import numpy as np
import game1_fc as fc
n=5 #number of people

ans=[0]*7
ans=[ans]
for i in range(1,5):
	ans.append([i]*7)
ans=np.zeros((5,7))
for i in range(5):
	ans[i]=np.full((1,7),i)

def generate(isp,permute2_over):
	global ans
	global gen_bak
	u=np.full((5,7),-1)

	if(permute2_over):
		gen=fc.gen_s1(u)
		gen_bak=gen.copy()
		gen=fc.gen_s2(gen)
		gen=fc.gen_s3(gen)
		ans,permute2_over=fc.gen_s4(ans,gen,not permute2_over)
	else:
		gen=gen_bak.copy()
		ans,permute2_over=fc.gen_s4(ans,gen,not permute2_over)
	#print('In generate()')
	for line in gen:
		#print(line)
		continue

	return ans, permute2_over

def judge(ans):
	verdict=0
	isp=ans
	if(jr1(ans)==False):
		verdict=1
		return [verdict, isp]
	if(jr2(ans)==False):
		verdict=2
		return [verdict, isp]
	if(jr3(ans)==False):
		verdict=3
		return [verdict, isp]
	if(jr4(ans)==False):
		verdict=4
		return [verdict, isp]
	if(jr5(ans)==False):
		verdict=5
		return [verdict, isp]
	if(jr6(ans)==False):
		verdict=6
		return [verdict, isp]
	if(jr7(ans)==False):
		verdict=7
		return [verdict, isp]
	if(jr8(ans)==False):
		verdict=8
		return [verdict, isp]
	if(jr9(ans)==False):
		verdict=9
		return [verdict, isp]
	if(jr10(ans)==False):
		verdict=10
		return [verdict, isp]
	if(jr11(ans)==False):
		verdict=11
		return [verdict, isp]
	if(jr12(ans)==False):
		verdict=12
		return [verdict, isp]
	if(jr13(ans)==False):
		verdict=13
		return [verdict, isp]
	return [verdict, isp]

def jr1(ans):
	p1=find_idx_col(ans, 0, 0)	# 	age 15
	p2=find_idx_col(ans, 1, 0)	#	style baoli
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr2(ans):	
	p1=find_idx_col(ans, 3, 0) 	#	xiangsuya
	p2=find_idx_col(ans, 1, 0)	#	baoli
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][6]
	pos2=ans[p2][6]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr3(ans):
	p1=find_idx_col(ans, 4, 0) 	#	name mao
	p2=find_idx_col(ans, 5, 0) 	#	power 0
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr4(ans):
	p1=find_idx_col(ans, 0, 3) 	#	age 32
	p2=find_idx_col(ans, 0, 2) 	#	age 28
	if(p1==-1 or p2 == -1):
		return False
	power1=ans[p1][5]
	power2=ans[p2][5]
	#print('p1',p1,'p2',p2)
	if(power1<power2):
		return True
	else:
		return False

def jr5(ans):
	p1=find_idx_col(ans, 0, 3) 	#	age 32
	p2=find_idx_col(ans, 2, 0) 	#	job kuaiji
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr6(ans):
	p1=find_idx_col(ans, 1, 1) 	#	style wenjian
	p2=find_idx_col(ans, 3, 1) 	#	food baiqiejie
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr7(ans):
	p1=find_idx_col(ans, 4, 1) 	#	name gu
	p2=find_idx_col(ans, 0, 4) 	#	age 55
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr8(ans):
	p1=find_idx_col(ans, 5, 2) 	#	power middle
	p2=find_idx_col(ans, 2, 1) 	#	job suanming
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr9(ans):
	p1=find_idx_col(ans, 4, 2) 	#	name dou
	p2=find_idx_col(ans, 2, 2) 	#	job qishou
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr10(ans):	
	p1=find_idx_col(ans, 1, 2) 	#	style aishidi
	p2=find_idx_col(ans, 3, 2)	#	food hongshao
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][6]
	pos2=ans[p2][6]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr11(ans):
	p1=find_idx_col(ans, 4, 3) 	#	name gua
	p2=find_idx_col(ans, 3, 3) 	#	food kaoquanyang
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr12(ans):	
	p1=find_idx_col(ans, 1, 3) 	#	style daqi
	p2=find_idx_col(ans, 2, 3)	#	job yisheng
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr13(ans):	
	p1=find_idx_col(ans, 1, 2) 	#	style aishidi
	p2=find_idx_col(ans, 2, 4)	#	job chengxuyuan
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][6]
	pos2=ans[p2][6]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr14(ans):	
	p1=find_idx_col(ans, 4, 0) 	#	name mao
	p2=find_idx_col(ans, 0, 1) 	#	age 21
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][6]
	pos2=ans[p2][6]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr15(ans):	
	p1=find_idx_col(ans, 4, 4) 	#	name mao
	p2=find_idx_col(ans, 1, 4) 	#	style aishidi
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def find_idx_col(ans, col, x):
	i=0
	while(i<5):
		if(ans[i][col]==x):
			return i
		i+=1
	return -1

fc.init()
cnt=0
permute2_over=True
while(True):
	ret=judge(ans) #return verdict and some info, to inspire how to generate
	if(ret[0]==0): # success! no rule violated
		break;
	ans,permute2_over=generate(ret[1],permute2_over)
	cnt+=1
	if(cnt%997==0):
		print(cnt)
		print(fc.pcnt)
		print('current ans')
		for line in ans:
			print(line)
	
print ("Search cnt: ", cnt, ", area cnt: ", fc.gen_s1_while_cnt , ", spot cnt: ", fc.permute_cnt)
print("The answer is: ")
for line in ans:
	print(line)