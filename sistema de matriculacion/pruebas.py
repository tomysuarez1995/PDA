from Matriculacion import obt_alum
from Rol import Ingreso
nuevoalumno= Ingreso(nombre= "alfredo sitarroza", CI=5466767, tipoRol= "E", AñoIngreso= 2020)
print(nuevoalumno.guardar_datos())

# from Plan_de_Estudio import UnidadCurricular, Plan_Estudio
# uc1=Plan_Estudio(nombreUC="Electrotecnia", semestreUC= 3, creditosUC= 10, Codigo= "Elect", Previas=["mat2", "fisic2"], Aprobadas=["mat1","Fisic1"])
# print(uc1.ordenar_por_semestre())


print(obt_alum())
