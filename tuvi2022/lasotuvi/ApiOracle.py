import cx_Oracle
file = open("clean_data.txt","r")
datas = file.read().split("\n")
ten_menh = []
ten_menh1 = []
ten_phumau = []
ten_huynhde =[]
ten_phuthe =[]
ten_tutuc =[]
matrix=[]
matrix1=[]
ten_taibach=[]
ten_tatach=[]
ten_thiendi=[]
ten_noboc=[]
ten_quanloc=[]
ten_dientrach=[]
ten_phucduc=[]
ten_phumau=[]
ten_tuhoa=[]
ten_menh2=[]
for data in datas:
	# f= open(str(dem)+".txt","w+")
	# f.close()
	data = data.strip()
	dataC = data.split(",")
	idtuvi = '109008'
	if(dataC[110] == idtuvi):
		phantu =[dataC[0],dataC[8],dataC[9],dataC[10],dataC[11],dataC[12],dataC[13],dataC[14],dataC[15],dataC[16],dataC[17],dataC[18],dataC[19],dataC[20]]
		phantusao=["tu_vi_0","thien_co_8","thai_duong_9","vu_khuc_10","thien_dong_11","liem_trinh_12","thien_phu_13","thai_am_14","tham_lang_15","cu_mon_16","thien_tuong_17","thien_luong_18","that_sat_19","pha_quan_20"]
		
		
		ten_can = int(dataC[122])
		menh = dataC[1]
		for i in range(0,14):
			if(menh == phantu[i]):
				ten_menh.append(phantusao[i])

		tu_vi_0 =["tu_vi_1_7","tu_vi_2_8","tu_vi_3_9","tu_vi_4_10","tu_vi_5_11","tu_vi_6_12","tu_vi_1_7","tu_vi_2_8","tu_vi_3_9","tu_vi_4_10","tu_vi_5_11","tu_vi_6_12"]
		thien_co_8 =["thienco_1_7","thienco_2_8","thienco_3_9","thienco_4_10","thienco_5_11","thienco_6_12","thienco_1_7","thienco_2_8","thienco_3_9","thienco_4_10","thienco_5_11","thienco_6_12"]
		thai_duong_9 = ["thai_duong_1_7","thai_duong_2_8","thai_duong_3_9","thai_duong_4_10","thai_duong_5_11","thai_duong_6_12","thai_duong_1_7","thai_duong_2_8","thai_duong_3_9","thai_duong_4_10","thai_duong_5_11","thai_duong_6_12"]
		vu_khuc_10 =["vu_khuc_1_7","vu_khuc_2_8","vu_khuc_3_9","vu_khuc_4_10","vu_khuc_5_11","vu_khuc_6_12","vu_khuc_1_7","vu_khuc_2_8","vu_khuc_3_9","vu_khuc_4_10","vu_khuc_5_11","vu_khuc_6_12"]
		thien_dong_11 =["thien_dong_1_7","thien_dong_2_8","thien_dong_3_9","thien_dong_4_10","thien_dong_5_11","thien_dong_6_12","thien_dong_1_7","thien_dong_2_8","thien_dong_3_9","thien_dong_4_10","thien_dong_5_11","thien_dong_6_12"]
		liem_trinh_12 =["liem_trinh_1_7","liem_trinh_2_8","liem_trinh_3_9","liem_trinh_4_10","liem_trinh_5_11","liem_trinh_6_12","liem_trinh_1_7","liem_trinh_2_8","liem_trinh_3_9","liem_trinh_4_10","liem_trinh_5_11","liem_trinh_6_12"]
		thien_phu_13 =["thien_phu_1_7","thien_phu_2_8","thien_phu_3_9","thien_phu_4_10","thien_phu_5_11","thien_phu_6_12","thien_phu_1_7","thien_phu_2_8","thien_phu_3_9","thien_phu_4_10","thien_phu_5_11","thien_phu_6_12"]
		thai_am_14 =["thai_am_1_7","thai_am_2_8","thai_am_3_9","thai_am_4_10","thai_am_5_11","thai_am_6_12","thai_am_1_7","thai_am_2_8","thai_am_3_9","thai_am_4_10","thai_am_5_11","thai_am_6_12"]
		tham_lang_15 =["tham_lang_1_7","tham_lang_2_8","tham_lang_3_9","tham_lang_4_10","tham_lang_5_11","tham_lang_6_12","tham_lang_1_7","tham_lang_2_8","tham_lang_3_9","tham_lang_4_10","tham_lang_5_11","tham_lang_6_12"]
		cu_mon_16 =["cu_mon_1_7","cu_mon_2_8","cu_mon_3_9","cu_mon_4_10","cu_mon_5_11","cu_mon_6_12","cu_mon_1_7","cu_mon_2_8","cu_mon_3_9","cu_mon_4_10","cu_mon_5_11","cu_mon_6_12"]
		thien_tuong_17 =["thien_tuong_1_7","thien_tuong_2_8","thien_tuong_3_9","thien_tuong_4_10","thien_tuong_5_11","thien_tuong_6_12","thien_tuong_1_7","thien_tuong_2_8","thien_tuong_3_9","thien_tuong_4_10","thien_tuong_5_11","thien_tuong_6_12"]
		thien_luong_18 =["thien_luong_1_7","thien_luong_2_8","thien_luong_3_9","thien_luong_4_10","thien_luong_5_11","thien_luong_6_12","thien_luong_1_7","thien_luong_2_8","thien_luong_3_9","thien_luong_4_10","thien_luong_5_11","thien_luong_6_12"]
		that_sat_19 =["that_sat_1_7","that_sat_2_8","that_sat_3_9","that_sat_4_10","that_sat_5_11","that_sat_6_12","that_sat_1_7","that_sat_2_8","that_sat_3_9","that_sat_4_10","that_sat_5_11","that_sat_6_12"]
		pha_quan_20 =["pha_quan_1_7","pha_quan_2_8","pha_quan_3_9","pha_quan_4_10","pha_quan_5_11","pha_quan_6_12","pha_quan_1_7","pha_quan_2_8","pha_quan_3_9","pha_quan_4_10","pha_quan_5_11","pha_quan_6_12"]
		matrix.append(tu_vi_0)
		matrix.append(thien_co_8)
		matrix.append(thai_duong_9)
		matrix.append(vu_khuc_10)
		matrix.append(thien_dong_11)
		matrix.append(liem_trinh_12)
		matrix.append(thien_phu_13)
		matrix.append(thai_am_14)
		matrix.append(tham_lang_15)
		matrix.append(cu_mon_16)
		matrix.append(thien_tuong_17)
		matrix.append(thien_luong_18)
		matrix.append(that_sat_19)
		matrix.append(pha_quan_20)
		
		for x in range(0,14):
			if(menh == phantu[x]):
				ten_menh1.append(matrix[x][int(menh)-1])
		print(ten_menh1)


		huynhde = dataC[121]
		for j in range(0,14):
			if(huynhde==phantu[j]):
				ten_huynhde.append(phantusao[j])

		phuthe = dataC[120]
		for j in range(0,14):
			if(phuthe==phantu[j]):
				ten_phuthe.append(phantusao[j])
		print(ten_phuthe)

		tutuc = dataC[119]
		for j in range(0,14):
			if(tutuc==phantu[j]):
				ten_tutuc.append(phantusao[j])
		print(ten_tutuc)

		taibach = dataC[118]
		for j in range(0,14):
			if(taibach==phantu[j]):
				ten_taibach.append(phantusao[j])
		print(ten_taibach)
		
		tatach = dataC[117]
		for j in range(0,14):
			if(tatach==phantu[j]):
				ten_tatach.append(phantusao[j])
		print(ten_tatach)
		
		thiendi = dataC[116]
		for j in range(0,14):
			if(thiendi==phantu[j]):
				ten_thiendi.append(phantusao[j])
		print(ten_thiendi)
		
		noboc = dataC[115]
		for j in range(0,14):
			if(noboc==phantu[j]):
				ten_noboc.append(phantusao[j])
		print(ten_noboc)
		
		quanloc = dataC[114]
		for j in range(0,14):
			if(quanloc==phantu[j]):
				ten_quanloc.append(phantusao[j])
		print(ten_quanloc)
		
		dientrach = dataC[113]
		for j in range(0,14):
			if(dientrach==phantu[j]):
				ten_dientrach.append(phantusao[j])
		print(ten_dientrach)
		
		phucduc = dataC[112]
		for j in range(0,14):
			if(phucduc==phantu[j]):
				ten_phucduc.append(phantusao[j])
		print(ten_phucduc)
		
		phumau = dataC[111]
		for j in range(0,14):
			if(phumau==phantu[j]):
				ten_phumau.append(phantusao[j])
		print(ten_phumau)
		

		phantu1 =[dataC[0],dataC[8],dataC[9],dataC[10],dataC[11],dataC[12],dataC[13],dataC[14],dataC[15],dataC[16],dataC[17],dataC[18],dataC[19],dataC[20],dataC[35],dataC[36]]
		phantusao1=["tu_vi_0","thien_co_8","thai_duong_9","vu_khuc_10","thien_dong_11","liem_trinh_12","thien_phu_13","thai_am_14","tham_lang_15","cu_mon_16","thien_tuong_17","thien_luong_18","that_sat_19","pha_quan_20","van_khuc_35","van_xuong_36"]
		
		# ["hoaloc","hoaquyen","hoakhoa","hoaky"]
		giap = ["liem_trinh_12","pha_quan_20","vu_khuc_10","thai_duong_9"]
		at=["thien_co_8","thien_luong_18","tu_vi_0","thai_am_14"]
		binh=["thien_dong_11","thien_co_8","van_xuong_36","liem_trinh_12"]
		dinh =["thai_am_14","thien_dong_11","thien_co_8","cu_mon_16"]
		mau=["tham_lang_15","thai_am_14","thai_duong_9","thien_co_8"]
		ky=["vu_khuc_10","tham_lang_15","thien_luong_18","van_khuc_35"]
		canh=["thai_duong_9","vu_khuc_10","thien_phu_13","thien_dong_11"]
		tan=["cu_mon_16","vu_khuc_10","van_khuc_35","van_xuong_36"]
		nham=["thien_luong_18","tu_vi_0","thien_phu_13","vu_khuc_10"]
		quy=["pha_quan_20","cu_mon_16","vu_khuc_10","tham_lang_15"]

		
		matrix1.append(giap)
		matrix1.append(at)
		matrix1.append(binh)
		matrix1.append(dinh)
		matrix1.append(mau)
		matrix1.append(ky)
		matrix1.append(canh)
		matrix1.append(tan)
		matrix1.append(nham)
		matrix1.append(quy)

		# for ii in range(0,16):
		# 	if(menh == phantu1[ii]):
		# 		ten_menh2.append(phantusao1[ii])
		
		for y1 in range(1,11):
			if(ten_can == y1):
				for y3 in range(0,4):
					for y4 in range(0,len(ten_menh2)):
						if(matrix1[y1-1][y3]==ten_menh2[y4]):
							ten_tuhoa.append(str(y1)+"_"+str(matrix1[y1-1][y3]))
		print(ten_tuhoa)



try:

	con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
	print(con.version)

	# Now execute the sqlquery
	cursor = con.cursor()

	# Creating a table employee
	def output_type_handler(cursor, name, default_type, size, precision, scale):
		if default_type == cx_Oracle.DB_TYPE_CLOB:
			return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
		if default_type == cx_Oracle.DB_TYPE_BLOB:
			return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)
	con.outputtypehandler = output_type_handler

	with open(str(idtuvi)+".txt", "w", encoding="utf8") as f0:
		for aa in range(1,3):
			f0.write("Cung Mệnh\n")
			for u in range(0,len(ten_menh)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang1 where ten_sao_chinh_tinh ='"+str(ten_menh[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")
			for u in range(0,len(ten_menh1)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang2 where ten_sao_chinh_tinh ='"+str(ten_menh1[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_huynhde)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang3 where ten_sao_chinh_tinh ='"+str(ten_huynhde[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_phuthe)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang4 where ten_sao_chinh_tinh ='"+str(ten_phuthe[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_tutuc)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang5 where ten_sao_chinh_tinh ='"+str(ten_tutuc[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_taibach)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang6 where ten_sao_chinh_tinh ='"+str(ten_taibach[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_tatach)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang7 where ten_sao_chinh_tinh ='"+str(ten_tatach[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_thiendi)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang8 where ten_sao_chinh_tinh ='"+str(ten_thiendi[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_noboc)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang9 where ten_sao_chinh_tinh ='"+str(ten_noboc[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_quanloc)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang10 where ten_sao_chinh_tinh ='"+str(ten_quanloc[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_dientrach)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang11 where ten_sao_chinh_tinh ='"+str(ten_dientrach[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_phucduc)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang12 where ten_sao_chinh_tinh ='"+str(ten_phucduc[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

			for u in range(0,len(ten_phumau)):
				cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop"+str(aa)+"_bang13 where ten_sao_chinh_tinh ='"+str(ten_phumau[u])+"'")
				rows = cursor.fetchall()
				for i in range(len(rows)):
					b = str(rows[i])[1:len(rows[i])-3] 
					a = b.split("\\n")
					for j in range(len(a)):			
						# with open("11.txt", "a", encoding="utf8") as f1:
						f0.write(str(a[j])+"\n")
					f0.write("\n")

		for u in range(0,len(ten_tuhoa)):
			cursor.execute("select noi_dung_co_ban_chinh_tinh from tamhop1_bang14 where ten_sao_chinh_tinh ='"+str(ten_tuhoa[u])+"'")
			rows = cursor.fetchall()
			for i in range(len(rows)):
				b = str(rows[i])[1:len(rows[i])-3] 
				a = b.split("\\n")
				for j in range(len(a)):			
					# with open("11.txt", "a", encoding="utf8") as f1:
					f0.write(str(a[j])+"\n")
				f0.write("\n")

		
except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()
