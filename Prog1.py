# your code goes here

f=open('input.txt','r')
f1=open('output.txt','w')


count=0
t=0
f1.write("Nandith Malapati\n")
f1.write("UIN : 01066678\n")
for lines in f:
	flag=0
	t+=1
	a=lines[:-1]
	f1.write(a)
	f1.write("\n")
	a= a.split(".")
	if len(a)!=4:
		flag=1
	else:
		p=a[-1]
		a.remove(p)
		p=p.split(":")
		if len(p)!=2:
			flag=1
		else:
			a.append(p[0])
			a.append(p[1])
	if flag!=1:
		for j in a:
			if j.isdigit() == False:
				flag=1
				break;
			else:
				if int(j)<0:
					flag=1
	if flag==1:
		#print "Error in Line"
		f1.write("Error in line")
		f1.write("\n")
		
		count+=1
	else:
		temp= "Address: "+a[0]+"."+a[1]+"."+a[2]+"."+a[3]+", Port: "+ a[4]
		f1.write(temp)
		f1.write("\n")


		
f1.write("\n\nSummary")
f1.write("\n")
f1.write( "Lines Read: "+ str(t))
f1.write("\n")
f1.write("Number of Errors: "+str(count))

f.close()
f1.close()
	
