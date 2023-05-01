metadeimpar = 0.0
metadepar = 0.0
print("BEM-VINDO AO SISTEMAS DE NOTAS! VAMOS COMEÇAR?")
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
for x in range(1, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    metadeimpar = nota + metadeimpar
    mediaimpar = metadeimpar/25
print("\nA MÉDIA DOS ALUNOS COM NÚMERO ÍMPARES FORAM {}".format(mediaimpar))
print("\nAGORA, VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
for x in range(2, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    metadepar = nota + metadepar
    mediapar = metadepar/25
print("\nA MÉDIA DOS ALUNOS COM NÚMERO PARES FORAM {}".format(mediapar))

if mediapar > mediaimpar:
    print("\nOS ALUNOS PARES TIVERAM A MAIOR MÉDIA COM {}".format(mediapar))
elif mediaimpar > mediapar:
    print("\nOS ALUNOS ÍMPARES TIVERAM A MAIOR MÉDIA COM {}".format(mediaimpar))
else:
    print("\nOS ALUNOS ÍMPARES E PARES OBTIVERAM A MESMA MÉDIA!")
