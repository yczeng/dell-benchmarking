def data(file):
	with open('../random information/'+file, 'r') as f:
		output = f.readlines()
	output = [out.strip() for out in output]

	count = 0
	total = 0
	batch = []
	times = []
	for line in output:
		if "Batch" in line:
			batch.append(float(line[7:]))
		if "Average" in line:
			time = float(line[23:-4])
			count += 1
			total += time
		if count == gpu*10:
			times.append(total/(gpu*10))
			count = 0
			total = 0
	print(file)
	print "BATCH:", batch

	print "===========TIMES:============"
	for i in times:
		print(i)
	
	img_per_sec = []
	for i in range(len(batch)):
		img_per_sec.append(1000/times[i] * batch[i])
	print("======IMAGE PER SECOND:======")
	for i in img_per_sec:
		print(i)
	print "\n"

gpu = input("How many GPUs? \n")
data('GoogLeNetData')
data('AlexNetData')