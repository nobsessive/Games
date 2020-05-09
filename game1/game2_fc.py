n=5						# number of people
pcnt=[0]*11				# search cnt, determine which state is generated in gen_s1()
pcnt2=[0]*5				# search2 cnt
gen_s1_while_cnt=0		# area cnt
gen_s2_while_cnt=0		# area2 cnt
permute_cnt=0			# spot cnt
dbflag=-1			# debug flag

def init():
	pcnt[9]=0
	pcnt[8]=0
	pcnt[7]=0

#the first phase of generating a legal state based on pcnt[]
def gen_s1(isq, dbflag=-1):
	global gen_s1_while_cnt
	global pcnt
	global ruleFuncList
	case_over_flag=False
	
	while(True):
		##	debug related section
		if(dbflag>-1):
			print("pcnt",pcnt)
		#	\debug related section

		if(pcnt[10]==1):
			print("gen_s1 completed every case")
			case_over_flag=True
			return isp, case_over_flag

		gen_s1_while_cnt+=1
		isp=isq.copy()

		## new revision using functino pointer
		fcnt=len(ruleFuncList)
		for i in range(fcnt-1):
			ret=ruleFuncList[i](isp)
			if(ret==0):
				ret=raiseCnt(0)
				continue

		ret=ruleFuncList[fcnt-1](isp) #add the last rule
		if(ret==0):
			ret=raiseCnt(9)
			continue
		else:
			ret=raiseCnt(9)
			break
		# \new revision using functino pointer
	return isp, case_over_flag

def gen_s2(gen):
	global dbflag
	isp=[]
	while(True):
		if(dbflag > -1):
			dbflag+=1
			print("dbflag", dbflag)
		isq=gen.copy()
		isq=gen_s1(isq)
		global gen_s2_while_cnt

		resetCnt2() #reset pcnt2
		while(True):
			gen_s2_while_cnt+=1

			if(pcnt2[4]==1): # fail raise pcnt, pcnt2 reset
				raiseCnt(10)
				resetCnt2()
				st2_success=False
				break

			isp=isq.copy()

			ret=add_2rule0()
			if(ret==0):
				raiseCnt2()
				continue

			ret=add_2rule1()
			if(ret==0): 
				raiseCnt2()
				continue

			ret=add_2rule2()
			if(ret==0): 
				raiseCnt2()
				continue

			ret=add_2rule3()
			if(ret==0): 
				raiseCnt2()
				continue
			else:	# succeed, return isp
				raiseCnt2()
				st2_success=True
				break
		if(st2_success==True):
			break
	return isp 

def gen_s3(isp):
	return isp

def gen_s4(last_ans,gen,if_permute):
	global permute_cnt
	flag=True
	if(if_permute==False):
		permute_cnt=0
	for i in range(6):
		permute_cnt+=1
		col_last_ans=get_col(last_ans,i)
		col_gen=get_col(gen,i)
		#print('col_last_ans',col_last_ans,'col_gen',col_gen)
		if(if_permute and flag):
			col, permute2_over=next_col(col_last_ans,col_gen)
			if(not permute2_over and i<5):
				flag=False
		elif(flag==False):
			col=col_last_ans
		else:
			col=min_col(col_gen)
			permute2_over=False
		gen=set_col(gen,i,col)		
	return gen,permute2_over

def get_col(isp,i):
	r=[]
	for j in isp:
		r.append(j[i])
	return r

def set_col(isp,i, col):
	cnt=0
	for j in isp:
		j[i]=col[cnt]
		cnt+=1
	return isp

def next_col(last_ans,gen):
	r=[]
	for i in range(len(gen)):
		if(gen[i]<0 or gen[i]>4):
			r.append(last_ans[i])
	p, overFlag=next_permute(r)
	
	cnt=0
	for j in range(len(gen)):
		if(gen[j]==-1):
			gen[j]=p[cnt]
			cnt+=1
	return gen, overFlag

def min_col(col):
	r=[0]*5
	for i in range(len(col)):
		if(col[i]> -0.5):
			r[col[i]]=1
	t=[]
	for i in range(len(r)):
		if(r[i]==0):
			t.append(i)
	t.sort()
	cnt=0
	for i in range(len(col)):
		if(col[i]<0):
			col[i]=t[cnt]
			cnt+=1
	#print('generated column',col)
	return(col)

def next_permute(r):
	l=len(r)
	pivot=l-1
	flag=False
	while(pivot>0):
		if(r[pivot-1]<r[pivot]):
			flag=True
			break
		pivot-=1
	if(flag==False):
		r.sort()
	else:
		desired_min=pivot
		j=pivot
		pivot-=1
		while(j<l):
			if(r[j]>r[pivot] and r[j]<r[desired_min]):
				desired_min=j
			j+=1
		r[pivot]+=r[desired_min]
		r[desired_min]=r[pivot]-r[desired_min]
		r[pivot]=r[pivot]-r[desired_min]
		r2=r[pivot-l+1:]
		r2.sort()
		r[pivot-l+1:]=r2
	overFlag= not flag
	return r, overFlag

def raiseCnt(rule_num):
	for i in range(0,11):
		if(pcnt[i]<4):
			rule_num=i
			break
	pcnt[rule_num]+=1
	for i in range (0, rule_num):
		pcnt[i]=0
	return 1

def raiseCnt2():
	for i in range(0,5):
		if(pcnt2[i]<10):
			pcnt2[i]+=1
			return 1

def resetCnt2():
	for i in pcnt2:
		i=0
	return 1


def add_rule0(isp):
	#print('isp f',isp)
	if((isp[pcnt[0]][0]<0 or isp[pcnt[0]][0]==0) and (isp[pcnt[0]][1]<0 or isp[pcnt[0]][1]==0)):
		isp[pcnt[0]][0]=0	#
		isp[pcnt[0]][1]=0	#
	else:
		return 0
	return 1

def add_rule1(isp):
	if((isp[pcnt[1]][0]<0 or isp[pcnt[1]][0]==1) and (isp[pcnt[1]][4]<0 or isp[pcnt[1]][4]==0)):
		isp[pcnt[1]][0]=1 #
		isp[pcnt[1]][4]=0	#
	else:
		return 0
	return 1

def add_rule2(isp):
	if((isp[pcnt[2]][0]<0 or isp[pcnt[2]][0]==2) and (isp[pcnt[2]][2]<0 or isp[pcnt[2]][2]==0) ):
		isp[pcnt[2]][0]=2
		isp[pcnt[2]][2]=0	
	else:
		return 0
	return 1

def add_rule3(isp):
	if((isp[pcnt[3]][1]<0 or isp[pcnt[3]][1]==2) and (isp[pcnt[3]][2]<0 or isp[pcnt[3]][2]==1)):
		isp[pcnt[3]][1]=2#
		isp[pcnt[3]][2]=1#
	else:
		return 0
	return 1

def add_rule4(isp):
	if((isp[pcnt[4]][3]<0 or isp[pcnt[4]][3]==0) and (isp[pcnt[4]][4]<0 or isp[pcnt[4]][4]==1)):
		isp[pcnt[4]][3]=0#
		isp[pcnt[4]][4]=1#
	else:
		return 0
	return 1

def add_rule5(isp):
	if((isp[pcnt[5]][1]<0 or isp[pcnt[5]][1]==4) and (isp[pcnt[5]][3]<0 or isp[pcnt[5]][3]==1)):
		isp[pcnt[5]][1]=4 #
		isp[pcnt[5]][3]=1 #
	else:
		return 0
	return 1

def add_rule6(isp):
	if((isp[pcnt[6]][5]<0 or isp[pcnt[6]][5]==2) and (isp[pcnt[6]][2]<0 or isp[pcnt[6]][2]==2)):
		isp[pcnt[6]][5]=2 #
		isp[pcnt[6]][2]=2 #
	else:
		return 0
	return 1

def add_rule7(isp):
	if((isp[pcnt[7]][0]<0 or isp[pcnt[7]][0]==3) and (isp[pcnt[7]][5]<0 or isp[pcnt[7]][5]==0)):
		isp[pcnt[7]][0]=3#
		isp[pcnt[7]][5]=0 #
	else:
		return 0
	return 1

def add_rule8(isp):
	if((isp[pcnt[8]][3]<0 or isp[pcnt[8]][3]==2) and (isp[pcnt[8]][2]<0 or isp[pcnt[8]][2]==3)):
		isp[pcnt[8]][3]=2
		isp[pcnt[8]][2]=3
	else:
		return 0
	return 1
# nation	color	drink	cigr 	pet 	pos
# 0			1		2		3		4		5

# nation	0	eng		1	swiden		2	dmk			3	norway		4	german
# color		0	red		1	white		2 	green		3 	blue		4	yellow
# drink		0 	tea		1	coffee		2	milk		3	beer		4	water
# cigr		0	pall	1	dunh		2	master		3	prince		4	blends
# pet 		0	dog		1	bird		2	cat			3	horse		4	fish
# pos		0-4

#			  0 1 2 3 4 5 6 7 8  9
# rule 0-9 = {1	2 3 5 6 7 8 9 12 13}
def add_rule9(isp):
	if((isp[pcnt[9]][0]<0 or isp[pcnt[9]][0]==4) and (isp[pcnt[9]][3]<0 or isp[pcnt[9]][3]==3)):
		isp[pcnt[9]][0]=4
		isp[pcnt[9]][3]=3
	else:
		return 0
	return 1

def add_2rule0():
	return 1

def add_2rule1():
	return 1

def add_2rule2():
	return 1

def add_2rule3():
	return 1

ruleFuncList=[add_rule0,add_rule1,add_rule2,add_rule3,add_rule4,\
	add_rule5,add_rule6,add_rule7,add_rule8,add_rule9]