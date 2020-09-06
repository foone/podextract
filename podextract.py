import sys,struct,os,fnmatch
files=[]
if len(sys.argv)!=3:
	print('Usage: {} <filepattern>'.format(sys.argv[0]))
	print('Example: {} "*.MOD"'.format(sys.argv[0]))
	sys.exit()
else:
	podfile=sys.argv[1]
	pattern=sys.argv[2].upper()
with open(podfile,'rb') as f:
	f.seek(0)
	header=f.read(4)
	if header in ('POD2','POD3'):
		print('This is a {} file: They are not supported!'.format(header))
		sys.exit()
	num_files = struct.unpack('<L',header)[0]
	f.seek(0x54)
	for i in range(num_files):
		parts=struct.unpack('<32sLL',f.read(0x28))
		name,length,offset=parts
		nameparts=name.split('\0',1)
		if len(nameparts)==1:
			main_name=nameparts[0].rstrip('\0')
			sub_name=''
		else:
			main_name,sub_name=nameparts
			sub_name=sub_name.rstrip('\0')
		print(main_name, sub_name, length,offset)
		files.append({
			'name':main_name,
			'sub_name':sub_name,
			'length':length,
			'offset':offset,
		})

	for file in files:
		if fnmatch.fnmatch(file['name'].upper(),pattern):
			f.seek(file['offset'])
			data=f.read(file['length'])
			name = file['name']
			dirpath=os.path.dirname(name)
			if not os.path.exists(dirpath):
				os.makedirs(dirpath)
			with open(name,'wb') as outf:
				outf.write(data)