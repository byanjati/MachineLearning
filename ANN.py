import random
import math
# input n
jumNeuron = 5
jumOutput = 1
dimPola = 3
lr = 0.1
Epoch = 5000
MaxMSE = 10**-5

def transpose(m,height,width):
	return [[ m[row][col] for row in range(0,height) ] for col in range(0,width) ]

# data tinggal diganti menjadi data ozone
p = [[3,3,2],
	 [3,2,2],
	 [3,2,1],
	 [2,3,2],
	 [2,2,2],
	 [2,2,1],
	 [2,1,1],
	 [1,3,2],
	 [1,2,1],
	 [1,1,2]]

list_p = p

jumData = len(p)

t = [1,1,1,1,0,1,1,1,0,1,0,1]

w1 = [[random.random()*2-1 for j in range(dimPola)] for i in range(jumNeuron)]
w2 = [[random.random()*2-1 for j in range(jumNeuron)] for i in range(jumOutput)]

MSEpoch = MaxMSE + 1
MSE = []
ee = 1

while((ee < Epoch)and(MSEpoch > MaxMSE)):
	MSEpoch = 0
	for i in range(jumData):
		cp = list_p[:][i]
		ct = t[i]

		a1 = []
		v = 0
		for i in range(jumNeuron):
			list_v = [a*b for a,b in zip(cp,w1[:][i])]
			for i in list_v:
				v += i
			math_v = 1/(1+math.exp(-1*v))
			a1.append(math_v)

		v = 0
		for i in range(jumOutput):
			list_v = [p*w for p,w in zip(a1,w2[:][i])]
			for i in list_v:
				v += i
			a2 = 1/(1+math.exp(-1*v))

		Error = ct - a2
		MSEpoch += Error**2

		D2 = a2*(1-a2)*Error

		dw2 = []
		delta2 = []
		for i in range(jumNeuron):
			for j in range(jumOutput):
				delta2.append(lr * D2 * a1[:][j])
			dw2.append(delta2)

		D1 = []
		v = 0
		k = [1]*len(a1)
		list_v = [p-w for p,w in zip(k,a1)]
		for i in range(jumNeuron):
			a_res = [p*w for p,w in zip(a1,k)]
			for j in a_res:
				v +=j
			b_res = D2*w2[0][i]
			D1.append(v*b_res)

		dw1 = []
		for i in range(dimPola):
			for j in range(jumNeuron):
				delta1 = lr * D1[j] * w2[0][j]
			dw1.append(delta1)

		calon_w1 = []
		for i in w1:
			calon_w1.append([p+w for p,w in zip(i,dw1)])

		w1 = calon_w1

		calon_w2 = []
		for i in w2:
			calon_w2.append([p+w for p,w in zip(i,dw2[0])])

		w2 = calon_w2

	MSE.append(MSEpoch/jumData)
	ee += 1

# print(w2)

TestSet = [[3,3,1],
		   [3,1,2],
		   [2,3,1],
		   [2,1,2],
		   [1,3,1],
		   [1,2,2],
		   [1,1,1],]

TestKelas = [0,1,0,1,0,1,0]

jumPola = len(TestSet[:][0])
jumBenar = 0

for i in range(jumPola):
	cp = TestSet[:][i]
	a1 = []
	for j in range(jumNeuron):
		list_v = [a*b for a,b in zip(cp,w1[:][j])]
		v = 0
		for k in list_v:
			v += k
		math_v = 1/(1+math.exp(-1*v))
		a1.append(math_v)

	a2=[]
	for j in range(jumOutput):
		list_v = [a*b for a,b in zip(a1,w2[:][j])]
		v = 0
		for k in list_v:
			v += k
		math_v = 1/(1+math.exp(-1*v))
		a2.append(math_v)

	Kelas = 0 
	for j in range(jumOutput):
		if(a2[:][j] < 0.5):
			Kelas = 0
		else:
			kelas = 1

	if(Kelas==TestKelas[i]):
		jumBenar = jumBenar + 1

hasil = (float(jumBenar)/float(jumPola))*100

print "Akurasi : " + str(hasil) + " %"
