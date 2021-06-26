import hashlib

class DECRYPTHASH(object):

	def Crack(self,filename,stdin):
		self.filename,self.stdin=filename,stdin

		def Sha256(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.sha256(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED!! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')

		def Md5(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.md5(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED !! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')

		def Sha384(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.sha384(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED!! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')

		def Sha1(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.sha1(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED!! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')

		def Sha224(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.sha224(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED!! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')

		def Sha512(filename,stdin):
			wordlist=open(filename,'r').read().split()

			for i in range(len(wordlist)):
				hashed=hashlib.sha512(wordlist[i].encode()).hexdigest()

				if hashed==stdin:
					print(f'CRACKED!! {wordlist[i]}')
					break
				else:
					print('INVALID VALUE')


		size=len(stdin)

		if size==64:
			Sha256(filename,stdin)
		elif size==40:
			Sha1(filename,stdin)
		elif size==32:
			Md5(filename,stdin)
		elif size==128:
			Sha512(filename,stdin)
		elif size==96:
			Sha384(filename,stdin)

	def CrackSha256(self,filename,stdin):
		self.filename,self.stdin=filename,stdin
		wordlist=open(filename,'r').read().split()

		for i in range(len(wordlist)):
			hashed=hashlib.sha256(wordlist[i].encode()).hexdigest()

			if hashed==stdin:
				print(f'CRACKED!!! {wordlist[i]}')
				break
			else:
				print('INVALID VALUE')

	def CrackSha384(self,filename,stdin):
		self.filename,self.stdin=filename,stdin
		wordlist=open(filename,'r').read().split()

		for i in range(len(wordlist)):
			hashed=hashlib.sha384(wordlist[i].encode()).hexdigest()

			if hashed==stdin:
				print(f'CRACKED!! {wordlist[i]}')
				break
			else:
				print('INVALID VALUE')

	def CrackSha1(self,filename,stdin):
		self.filename,self.stdin=filename,stdin
		wordlist=open(filename,'r').read().split()

		for i in range(len(wordlist)):
			hashed=hashlib.sha1(wordlist[i].encode()).hexdigest()

			if hashed==stdin:
				print(f'CRACKED!! {wordlist[i]}')
				break
			else:
				print('INVALID VALUE')

	def Md5(self,filename,stdin):
		self.filename,self.stdin=filename,stdin
		wordlist=open(filename,'r').read().split()

		for i in range(len(wordlist)):
			hashed=hashlib.md5(wordlist[i].encode()).hexdigest()

			if hashed==stdin:
				print(f'CRACKED!! {wordlist[i]}')
				break
			else:
				print('INVALID VALUE')

	def Sha224(self,filename,stdin):
		self.filename,self.stdin=filename,stdin
		wordlist=open(filename,'r').read().split()

		for i in range(len(wordlist)):
			hashed=hashlib.sha224(wordlist[i].encode()).hexdigest()

			if hashed==stdin:
				print(f'CRACKED!! {wordlist[i]}')
				break
			else:
				print('INVALID VALUE')



class QUICKHASH(object):
	def Sha256(self,plain):
		self.plain=plain
		plain=plain.encode()

		hashed=hashlib.sha256(plain).hexdigest()

		return hashed


	def Md5(self,plain):
		self.plain=plain
		plain=plain.encode()

		hashed=hashlib.md5(plain).hexdigest()

		return hashed
		

	def Sha512(self,plain):

		self.plain=plain 
		plain=plain.encode()

		hashed=hashlib.sha512(plain).hexdigest()

		return hashed

	def Sha384(self,plain):

		self.plain=plain
		plain=plain.encode()

		hashed=hashlib.sha384(plain).hexdigest()

		return hashed

	def Sha224(self,plain):
		self.plain=plain

		hashed=hashlib.sha224(plain.encode()).hexdigest()

		return hashed