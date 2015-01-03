#"jalali.py" is convertor to and from Gregorian and Jalali calendars. 

g_days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
j_days_in_month = (31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29)

def div(a,b):
	return a/b

def gregorian_to_jalali(g_y, g_m, g_d): 
	gy = g_y-1600 
	gm = g_m-1 
	gd = g_d-1 

	g_day_no = 365*gy+div(gy+3,4)-div(gy+99,100)+div(gy+399,400) 

	for i in range(gm):
		g_day_no += g_days_in_month[i] 
	if (gm>1 and ((gy%4==0 and gy%100!=0) or (gy%400==0))):
	# leap and after Feb
		g_day_no +=1 
	g_day_no += gd 

	j_day_no = g_day_no-79 

	j_np = div(j_day_no, 12053) # 12053 = 365*33 + 32/4 
	j_day_no = j_day_no % 12053 

	jy = 979+33*j_np+4*div(j_day_no,1461) # 1461 = 365*4 + 4/4 

	j_day_no %= 1461 

	if (j_day_no >= 366):
		jy += div(j_day_no-1, 365) 
		j_day_no = (j_day_no-1)%365 


	for i in range(11):
		if j_day_no < j_days_in_month[i]:
			break
		j_day_no -= j_days_in_month[i] 
	jm = i+1 
	jd = j_day_no+1 

	return (jy, jm, jd) 

def jalali_to_gregorian(j_y, j_m, j_d):
	jy = j_y-979 
	jm = j_m-1 
	jd = j_d-1

	j_day_no = 365*jy + div(jy, 33)*8 + div(jy%33+3, 4)
	for i in range(jm): 
		j_day_no += j_days_in_month[i]

	j_day_no += jd 

	g_day_no = j_day_no+79 

	gy = 1600 + 400*div(g_day_no, 146097) # 146097 = 365*400 + 400/4 - 400/100 + 400/400 
	g_day_no = g_day_no % 146097 

	leap = true 
	if g_day_no >= 36525: # 36525 = 365*100 + 100/4 
		g_day_no -=1 
		gy += 100*div(g_day_no, 36524) # 36524 = 365*100 + 100/4 - 100/100  
		g_day_no = g_day_no % 36524

		if g_day_no >= 365: 
			g_day_no +=1
		else:
			leap = False 

	gy += 4*div(g_day_no, 1461) # 1461 = 365*4 + 4/4  
	g_day_no %= 1461 

	if g_day_no >= 366:
		leap = False
		g_day_no -=1
		gy += div(g_day_no, 365) 
		g_day_no = g_day_no % 365 
 
	i=0
	while (g_day_no >= g_days_in_month[i] + (i == 1 and leap)):
		i += 1
		g_day_no -= g_days_in_month[i] + (i == 1 and leap)
	gm = i+1 
	gd = g_day_no+1 

	return (gy, gm, gd) 

def get_jalali_date( gdate='now' ):
	if gdate == 'now':
		import datetime
		today = datetime.date.today()
		(gyear, gmonth, gday ) = (today.year, today.month, today.day )
	else:
		( gyear, gmonth, gday ) = gdate.split('-') 
	( jyear, jmonth, jday ) = gregorian_to_jalali(gyear, gmonth, gday)
	return str(jyear)+"/ "+str(jmonth)+"/ "+str(jday)
