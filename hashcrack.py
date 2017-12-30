import os, hashlib, random, sys, time
from time import gmtime, strftime
name = "henry"
os.system("cls")
hash_types = ["md5","sha1","sha224","sha256","sha512"]
def bruteforce(hash, args, values):
	if "f" in args and "." in hash:
		files = open(values[args.find("f")])
		for xhsd in files.readlines():
			hash = xhsd.replace("\n", "")
			alphabet = "abcdefghijklmnopqrstuvwxyz"
			alphabet += alphabet.upper() + "0123456789!$%^&*(){}~#][;:'@/?.>,<"
			if "b" in args:
				m = args.find("b")
				m = values[m]
			else:
				m = "0,16"
			start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			l = 0
			print("Cracking...")
			attempts = 0
			while l == 0:
				password = ""
				for x in range(random.randrange(int(m.split(",")[0])+1,int(m.split(",")[1])+1)):
					password += alphabet[random.randrange(0,len(alphabet)-1)]
				num = hash_types[int(values[args.find("t")])]
				htype = "hash2 = hashlib."+num+"(password).hexdigest()"
				exec(htype)
				if hash2 == hash:
					attempts += 1
					output = "[*]Hash: " + hash + "\n[*]Cracked: " + password + "\n[*]Hash type: " + num + "\n[*]Method: Bruteforce\n[*]Start Time: " + str(start_time) + "\n[*]End Time: " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "\n[*]Attempts: " + str(attempts)
					print output
					l = 1
					if "o" in args:
						ofile = values[args.find("o")]
						f = open(ofile, "w")
						f.write("")
						f.close()
						f = open(ofile, "a")
						f.write(hash + ":" + password + "\n")

				if hash != hash2:
					attempts += 1
					if "g" in args:
						if values[args.find("g")] == "true":
							if password != "":
								print("Trying " + str(password))
	else:
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		alphabet += alphabet.upper() + "0123456789!$%^&*(){}~#][;:'@/?.>,<"
		if "b" in args:
			m = args.find("b")
			m = values[m]
		else:
			m = "0,16"
		start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		l = 0
		print("Cracking...")
		attempts = 0
		while l == 0:
			password = ""
			for x in range(random.randrange(int(m.split(",")[0])+1,int(m.split(",")[1])+1)):
				password += alphabet[random.randrange(0,len(alphabet)-1)]
			num = hash_types[int(values[args.find("t")])]
			htype = "hash2 = hashlib."+num+"(password).hexdigest()"
			exec(htype)
			if hash2 == hash:
				attempts += 1
				output = "[*]Hash: " + hash + "\n[*]Cracked: " + password + "\n[*]Hash type: " + num + "\n[*]Method: Bruteforce\n[*]Start Time: " + str(start_time) + "\n[*]End Time: " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "\n[*]Attempts: " + str(attempts)
				print output
				l = 1
				if "o" in args:
					ofile = values[args.find("o")]
					f = open(ofile, "w")
					f.write("")
					f.close()
					f = open(ofile, "a")
					f.write(hash + ":" + password + "\n")
			if hash != hash2:
				attempts += 1
				if "g" in args:
					if values[args.find("g")] == "true":
						if password != "":
							print("Trying " + str(password))
def straight(hash, args, values):
	if "f" in args and "." in hash:
		wordlist=values[args.find("w")]
		print(str(sum(1 for line in open(wordlist)))*2 + " passwords loaded.")
		time.sleep(2)
		files = open(values[args.find("f")])
		for xhsd in files.readlines():
			start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			print("Cracking...")
			attempts = 0
			hash = xhsd.replace("\n", "")
			sfs = open(wordlist, "r")
			l=0
			if "p" in args:
				number = int(value[args.find("p")])
			for p in sfs.readlines():
				tmp = 0
				if l == 0:
					p = p.replace("\n", "")
					num = hash_types[int(values[args.find("t")])]
					htype = "hash1 = hashlib."+num+"(p).hexdigest()"
					exec(htype)
					if hash1 == hash:
						attempts += 1
						output = "[*]Hash: " + hash + "\n[*]Cracked: " + p + "\n[*]Hash type: " + num + "\n[*]Method: Bruteforce\n[*]Start Time: " + str(start_time) + "\n[*]End Time: " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "\n[*]Attempts: " + str(attempts)
						print output
						if "o" in args:
							ofile = values[args.find("o")]
							f = open(ofile, "w")
							f.write("")
							f.close()
							f = open(ofile, "a")
							f.write(hash + ":" + p + "\n")
							l += 1
							time.sleep(2)
					else:
						attempts += 1
						if "g" in args:
							if values[args.find("g")] == "true":
								print("Trying " + str(p))
		argline1()
		
	else:
		for x in range(1): # Just a placeholder
			start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			wordlist=values[args.find("w")]
			print(str(sum(1 for line in open(wordlist))) + " passwords loaded.")
			print("Cracking...")
			attempts = 0
			hash = hash.replace("\n", "")
			sfs = open(wordlist, "r")
			l=0
			tmp = 0
			arr = []
			for p in sfs.readlines():
				p = p.replace("\n", "")
				for hsg in range(len(p)):
					yy = 0
					if l == 0:
						for x in list("0123456789"):
							if x in p:
								yy += 1
						print yy
						if yy == 0:
							p = list(p)
							stringg = ""
							for ig in range(len(p)):
								if ig==hsg:
									p[hsg]=p[hsg].upper()
							for ltd in p:
								stringg += ltd
							p = stringg
						num = hash_types[int(values[args.find("t")])]
						htype = "hash1 = hashlib."+num+"(p).hexdigest()"
						exec(htype)
						if hash1 == hash:
							attempts += 1
							output = "[*]Hash: " + hash + "\n[*]Cracked: " + p + "\n[*]Hash type: " + num + "\n[*]Method: Bruteforce\n[*]Start Time: " + str(start_time) + "\n[*]End Time: " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + "\n[*]Attempts: " + str(attempts)
							print output
							if "o" in args:
								ofile = values[args.find("o")]
								f = open(ofile, "w")
								f.write("")
								f.close()
								f = open(ofile, "a")
								f.write(hash + ":" + p + "\n")
								l += 1
							argline()
						else:
							attempts += 1
							if "g" in args:
								if values[args.find("g")] == "true":
									print("Trying " + str(p))
				
			argline1()
	
								
def eval(hash, args, bw):
	r = args.find("a")
	if str(bw[r]) == "0":
		bruteforce(hash, args, bw)
	if str(bw[r]) == "1":
		straight(hash, args, bw)
def argline1():
	argline = raw_input("> ").lower()
	if "-" not in argline:
		print("Invalid usage! --help")
		argline1()
	if argline == "--help" or argline == "--h":
		f = open("help.md", "r")
		print(f.read())
		argline1()
	else:
		args = argline.split(" ")
		u = []
		n=[]
		b=[]
		for x in range(len(args)):
			if x % 2 == 0:
				u.append(args[x]  + " " + args[x + 1])
		for x in u:
			if x[1] == "-" and x[0] == "-":
				n.append(x[2])
			if x[0] == "-" and x[1] != "-":
				n.append(x[1])
			else:
				print("False")
			b.append(x.split(" ")[1])
		stri=""
		for x in range(len(n)):
			stri += n[x]
		if "h" in stri:
			num = stri.find("h")
		else:
			num = stri.find("f")
		required = ["h", "a", "t"]
		recommended = ["o"]
		if b[stri.find("a")] == "0":
			required.append("b")
		else:
			required.append("w")
		error = []
		for yt in required:
			if yt not in stri:
				error.append(yt)
		if len(error) > 0:
			print("Missing parameters or invalid options. --help")
		else:
			eval(b[num], stri, b)	
argline1()
