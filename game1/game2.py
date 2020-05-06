testAns=[
	[3, 4, 4, 1, 2, 0],
	[2, 3, 0, 4, 3, 1],
	[0, 0, 2, 0, 1, 2],
	[4, 2, 1, 3, 4, 3],
	[1, 1, 3, 2, 0, 4]
]
# nation	color	drink	cigr 	pet 	pos
# 0			1		2		3		4		5

# nation	0	eng		1	swiden		2	dmk			3	norway		4	german
# color		0	red		1	white		2 	green		3 	blue		4	yellow
# drink		0 	tea		1	coffee		2	milk		3	beer		4	water
# cigr		0	pall	1	dunh		2	master		3	prince		4	blends
# pet 		0	dog		1	bird		2	cat			3	horse		4	fish
# pos		0-4

# rule 0-9 = {1	2 3 5 6 7 8 9 12 13}

import numpy as np
import game2_fc as fc
n=5 #number of people

ans=[0]*6
ans=[ans]
for i in range(1,5):
	ans.append([i]*6)
ans=np.zeros((5,6))
for i in range(5):
	ans[i]=np.full((1,6),i)

def generate(isp,permute2_over):
	global ans
	global gen_bak
	overflag=False
	u=np.full((5,6),-1)

	if(permute2_over):
		gen,overflag=fc.gen_s1(u)
		if(overflag):
			return ans, permute2_over, overflag
		gen_bak=gen.copy()
		gen=fc.gen_s3(gen)
		ans,permute2_over=fc.gen_s4(ans,gen,not permute2_over)
	else:
		gen=gen_bak.copy()
		ans,permute2_over=fc.gen_s4(ans,gen,not permute2_over)

	return ans, permute2_over, overflag

def judge(ans,flag=0):
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
	if(jr14(ans)==False):
		verdict=14
		return [verdict, isp]
	if(jr15(ans)==False):
		verdict=15
		return [verdict, isp]

	return [verdict, isp]

def jr1(ans):
	p1=find_idx_col(ans, 0, 0)	# 	nat eng
	p2=find_idx_col(ans, 1, 0)	#	house red
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr2(ans):	
	p1=find_idx_col(ans, 0, 1)	# 	nat swiden
	p2=find_idx_col(ans, 4, 0)	#	pet dog
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr3(ans):
	p1=find_idx_col(ans, 0, 2)	# 	nat dmk
	p2=find_idx_col(ans, 2, 0) 	#	drink tea
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr4(ans):
	p1=find_idx_col(ans, 1, 2) 	#	color green
	p2=find_idx_col(ans, 1, 1) 	#	color white
	if(p1==-1 or p2 == -1):
		return False
	if((ans[p1][5]-ans[p2][5])==-1):
		return True
	else:
		return False

def jr5(ans):
	p1=find_idx_col(ans, 1, 2) #	color green
	if(p1==-1):
		return False
	elif(ans[p1][2]==1):
		return True
	else:
		return False

def jr6(ans):
	p1=find_idx_col(ans, 3, 0) 	#	cigr pall
	p2=find_idx_col(ans, 4, 1) 	#	pet bird
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr7(ans):
	p1=find_idx_col(ans, 1, 4) 	#	color yellow
	p2=find_idx_col(ans, 3, 1) 	#	cigr dunh
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr8(ans):
	p1=find_idx_col(ans, 5, 2) 	#	pos middle
	p2=find_idx_col(ans, 2, 2) 	#	milk
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr9(ans):
	p1=find_idx_col(ans, 0, 3)	# 	nat norway
	p2=find_idx_col(ans, 5, 0) 	#	pos 0
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr10(ans):	
	p1=find_idx_col(ans, 3, 4) 	#	cigr blend
	p2=find_idx_col(ans, 4, 2)	#	pet cat
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][5]
	pos2=ans[p2][5]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr11(ans):
	p1=find_idx_col(ans, 4, 3)	#	pet horse
	p2=find_idx_col(ans, 3, 1) 	#	cigr dunh
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][5]
	pos2=ans[p2][5]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr12(ans):	
	p1=find_idx_col(ans, 3, 2) 	#	cigr master
	p2=find_idx_col(ans, 2, 3)	#	drink beer
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

def jr13(ans):	
	p1=find_idx_col(ans, 0, 4) 	#	nat german
	p2=find_idx_col(ans, 3, 3) 	#	cigr prince
	if(p1==-1 or p2 == -1):
		return False
	elif(p1==p2):
		return True
	else:
		return False

# nation	color	drink	cigr 	pet 	pos
# 0			1		2		3		4		5

# nation	0	eng		1	swiden		2	dmk			3	norway		4	german
# color		0	red		1	white		2 	green		3 	blue		4	yellow
# drink		0 	tea		1	coffee		2	milk		3	beer		4	water
# cigr		0	pall	1	dunh		2	master		3	prince		4	blends
# pet 		0	dog		1	bird		2	cat			3	horse		4	fish
# pos		0-4

def jr14(ans):	
	p1=find_idx_col(ans, 0, 3) 	#	nat norway
	p2=find_idx_col(ans, 1, 3) 	#	color blue
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][5]
	pos2=ans[p2][5]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def jr15(ans):	
	p1=find_idx_col(ans, 3, 4) 	#	cigr blends
	p2=find_idx_col(ans, 2, 4) 	#	drink water
	if(p1==-1 or p2 == -1):
		return False
	pos1=ans[p1][5]
	pos2=ans[p2][5]
	pos=pos1-pos2
	if(pos*pos!=1):	#judge
		return False
	else:
		return True

def find_idx_col(ans, col, x):
	i=0
	while(i<5):
		if(ans[i][col]==x):
			return i
		i+=1
	return -1
def power_pos_test(ans):
	for i in ans:
		if(i[5]+i[6]!=4):
			return False
	return True

ans_stack=[]
fc.init()
cnt=0
permute2_over=True
prev_ans_length=0
fc.dbflag=-1
fc.pcnt=[2,4,1,3,2,0,2,0,4,3,0]#db
while(True and fc.pcnt[10]<1):
	ret=judge(ans) #return verdict and some info, to inspire how to generate
	if(ret[0]==0): # success! no rule violated
		ans_stack.append([cnt, fc.gen_s1_while_cnt, fc.permute_cnt, ans])
	ans,permute2_over,overflag=generate(ret[1],permute2_over)

	if(overflag):
		break
	cnt+=1

	if(cnt%1000==0):
		print("Area ",cnt-1000," to ", cnt-1, " completed.", " Spotted answer number: ", len(ans_stack)-prev_ans_length, " pcnt :", fc.pcnt, " pcnt2 :", fc.pcnt2)
		prev_ans_length=len(ans_stack)
	if(cnt>3000):
		fc.dbflag=0
	#print("pcnt",fc.pcnt)
	#print("ans", ans)
	#if(fc.pcnt[0]==4):
		#break



def disp_ans(ans):
	name_str=['English','Swedish','Danes','Norwegian','German']
	name_id=-1
	for i in ans:
		if(i[4]==4):
			name_id=i[4]
	return name_str[name_id]

disp_cnt=0
for item in ans_stack:
	disp_cnt+=1
	print ("Status",disp_cnt, " Search cnt: ", item[0], ", area cnt: ", item[1] , ", spot cnt: ", item[2])
	print("The answer is: ", disp_ans(item[3]), "	Ans. Mat.:")
	for line in item[3]:
		print(line)	
