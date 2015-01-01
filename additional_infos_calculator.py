#!/usr/bin/env python

def AddInfo_pitcher(db):
	cur = db.cursor()
	cur.execute("SELECT count(*) FROM pitcher")
	num=cur.fetchone()[0]
	ran=num/30
	pitcher_stats=[0]*num
	index=0
	for i in range(0,ran+1):
		cur.execute("SELECT * FROM pitcher LIMIT %d, %d" %(i*30,30))
		for row in cur:
			pitcher_stats[index]=row
			index=index+1
	pitcher_addinfo={}
	for pitcher_stat in pitcher_stats:
		tbf=pitcher_stat[11]
		ah=pitcher_stat[14]
		abb=pitcher_stat[20]
		ahbp=pitcher_stat[22]
		asf=pitcher_stat[19]
		asac=pitcher_stat[18]
		a2b=pitcher_stat[15]
		a3b=pitcher_stat[16]
		ahr=pitcher_stat[17]
		k=pitcher_stat[23]
		ip=pitcher_stat[13]
		np=pitcher_stat[12]
		pid=pitcher_stat[0]
		g=pitcher_stat[3]
		w=pitcher_stat[6]
		sv=pitcher_stat[8]
		hld=pitcher_stat[9]
		l=pitcher_stat[7]
		ar=pitcher_stat[26]
		aer=pitcher_stat[27]
		bk=pitcher_stat[25]
		wp=pitcher_stat[24]
		sho=pitcher_stat[4]
		cg=pitcher_stat[5]
		bs=pitcher_stat[28]
		qs=pitcher_stat[31]
		a1b=ah-a2b-a3b-ahr
		aab=tbf-asf-asac-ahbp-abb
		if tbf==0:
			aobp=0.0
		else:
			aobp=float(ah+abb+ahbp)/float(tbf)
		if aab==0:
			aslg=0.0
		else:
			aslg=float(a1b*1+a2b*2+a3b*3+ahr*4)/float(aab)
		if ip==0:
			kpi=0.0
			npi=0.0
		else:
			if (ip*10)%10 == 0:
				rip=ip
			elif (ip*10)%10 == 1.0:
				rip=(ip-0.1)+(1.0/3.0)
			elif (ip*10)%10 == 2.0:
				rip=(ip-0.2)+(2.0/3.0)
			kpi=float(k)/float(rip)
			npi=float(np)/float(rip)
		pitcher_FP=w*100+ip*12+k*10+sv*50+hld*40-l*30-ah*7-ahr*10-ahbp*5-abb*5-ar*5-aer*10-bk*5-wp*5+sho*25+cg*50-bs*25+qs*15
		pitcher_addinfo[(pid,g)]=[aab,aobp,aslg,kpi,npi,a1b,pitcher_FP]
	pitcher_addinfo_key=pitcher_addinfo.keys()	
	for i in range(0,len(pitcher_addinfo_key)):
		cpid=pitcher_addinfo_key[i][0]
		cg=pitcher_addinfo_key[i][1]
		print "Updating %d/%d pitcher. player_id : %d, g : %d" % (i, len(pitcher_addinfo_key) - 1, cpid, cg)
		cur.execute("UPDATE pitcher SET aab=%.3f WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][0],cpid,cg))
		cur.execute("UPDATE pitcher SET aobp=%.3f WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][1],cpid,cg))
		cur.execute("UPDATE pitcher SET aslg=%.3f WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][2],cpid,cg))
		cur.execute("UPDATE pitcher SET kpi=%.3f WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][3],cpid,cg))
		cur.execute("UPDATE pitcher SET npi=%.3f WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][4],cpid,cg))
		cur.execute("UPDATE pitcher SET a1b=%d WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][5],cpid,cg))
		cur.execute("UPDATE pitcher SET PitcherFP=%d WHERE player_id=%d and g=%d" %(pitcher_addinfo[(cpid,cg)][6],cpid,cg))
	db.commit()

def AddInfo_batter(db):
	cur = db.cursor()
	cur.execute("SELECT count(*) FROM batter")
	num=cur.fetchone()[0]
	ran=num/30
	batter_stats=[0]*num
	index=0
	for i in range(0,ran+1):
		cur.execute("SELECT * FROM batter LIMIT %d, %d" %(i*30,30))
		for row in cur:
			batter_stats[index]=row
			index=index+1
	batter_addinfo={}
	for batter_stat in batter_stats:
		b_pid=batter_stat[0]
		b_g=batter_stat[3]
		avg=batter_stat[2]
		hit=batter_stat[7]
		b2b=batter_stat[8]
		b3b=batter_stat[9]
		hr=batter_stat[10]
		slg=batter_stat[22]
		obp=batter_stat[23]
		pa=batter_stat[4]
		r=batter_stat[6]
		rbi=batter_stat[12]
		sb=batter_stat[13]
		bb=batter_stat[17]
		hbp=batter_stat[19]
		sf=batter_stat[16]
		sac=batter_stat[15]
		cs=batter_stat[14]
		so=batter_stat[20]
		gdp=batter_stat[21]
		err=batter_stat[24]
		mh=batter_stat[28]
		b1b=hit-b2b-b3b-hr
		isop=float(slg)-float(avg)
		isod=float(obp)-float(avg)
		batter_fp=pa*1+r*5+b1b*10+b2b*20+b3b*30+hr*60+rbi*15+sb*10+bb*5+hbp*5+sf*5+sac*3-cs*5-so*10-gdp*15-err*10+mh*5
		batter_addinfo[(b_pid,b_g)]=[isop,isod,b1b,batter_fp]
	batter_addinfo_key=batter_addinfo.keys()
	for i in range(0,len(batter_addinfo_key)):
		cbpid=batter_addinfo_key[i][0]
		cbg=batter_addinfo_key[i][1]
		print "Updating %d/%d batter. player_id : %d, g : %d" % (i, len(batter_addinfo_key) - 1, cbpid, cbg)
		cur.execute("UPDATE batter SET isop=%.3f WHERE player_id=%d and g=%d" %(batter_addinfo[(cbpid,cbg)][0],cbpid,cbg))
		cur.execute("UPDATE batter SET isod=%.3f WHERE player_id=%d and g=%d" %(batter_addinfo[(cbpid,cbg)][1],cbpid,cbg))
		cur.execute("UPDATE batter SET 1b=%d WHERE player_id=%d and g=%d" %(batter_addinfo[(cbpid,cbg)][2],cbpid,cbg))
		cur.execute("UPDATE batter SET BatterFP=%d WHERE player_id=%d and g=%d" %(batter_addinfo[(cbpid,cbg)][3],cbpid,cbg))
	db.commit()

def CalcAdditionalInfos():
	from MySQLdb import connect
	db = connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
	AddInfo_pitcher(db)
	AddInfo_batter(db)

if __name__ == "__main__":
	CalcAdditionalInfos()
