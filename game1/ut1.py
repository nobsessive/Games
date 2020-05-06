#import numpy as np
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

r=[0,1,2,4,3]
print(next_permute(r))