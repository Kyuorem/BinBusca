import struct
import sys
 
if len(sys.argv) != 2:
    print "USO %s [CEP]" % sys.argv[0]
    quit()
 
registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
f = open("cep_ordenado.dat","r")
line=f.read(registroCEP.size)

inicial=0
mid=0
encontrado = False
end =['Endereco','Bairro','Cidade','Estado','Sigla','CEP']

vet=[]
while line!="":
   
    record=registroCEP.unpack(line)
    vet.append(record[5])
    line=f.read(registroCEP.size)

final=len(vet)-1

while encontrado==False:
    mid=int((inicial+final)/2)
    if vet[mid] == sys.argv[1]:
            
            encontrado=True
	    tamanho=(mid+1)*registroCEP.size
	    f.seek(tamanho-registroCEP.size)
	    text=f.readline(registroCEP.size)
            dados=registroCEP.unpack(text)
            for i in range(0,len(dados)-1):
                if(dados[i] != " "):
                    print end[i] + ':' + dados[i].strip() 
                    # aqui os dados sao printados
	  	        
       

    if vet[mid] > sys.argv[1]: 
 
        final=mid-1

    else:

        inicial=mid+1 

    if inicial > final:
	    break
           
    
f.close()
