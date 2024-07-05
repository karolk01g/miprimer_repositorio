
trabajadores = []

Lista_cargos = ["CEO", "analista programador","Desarrollador"]

def registrar_trabajador():

    nombreT = str(input("ingrese el nombre del trabajador: "))
    apellidoT = str(input("ingrese el apellido del trabajador: "))
    cargoT = input("ingrese el cargo del trabajador: ")
    sueldoBrutoT = int(input("ingrese el sueldo bruto del trabajador: "))

    desc_salud = sueldoBrutoT*0.07
    desc_afp = sueldoBrutoT*0.12
    liquido_pagar = sueldoBrutoT - desc_salud - desc_afp


    trabajador = {
        "nombre": nombreT,
        "apellido": apellidoT,
        "cargo": cargoT,
        "sueldo_bruto": sueldoBrutoT,
        "desc_salud": desc_salud,
        "desc_afp": desc_afp,
        "liquido_pagar": liquido_pagar
      }
    trabajadores.append(trabajador)
    print("\nTrabajador registrado exitosamente")






def listar_trabajadores():
        for trabajador in trabajadores:
          print(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']} - Sueldo Bruto: {trabajador['sueldo_bruto']} - Descuento Salud: {trabajador['desc_salud']} - Descuento AFP: {trabajador['desc_afp']} - Líquido a Pagar: {trabajador['liquido_pagar']}")
        print()




def imprimir_planilla():

      OpIm = input(f"Escriba un cargo a imprimir\n{Lista_cargos}'todos': ")
      
      if OpIm == "todos":
   
         
        with open('planilla_sueldo.txt', 'w') as archivo:
          for trabajador in trabajadores:
            archivo.write(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']} - Sueldo Bruto: {trabajador['sueldo_bruto']} - Descuento Salud: {trabajador['desc_salud']} - Descuento AFP: {trabajador['desc_afp']} - Líquido a Pagar: {trabajador['liquido_pagar']}")
      else:
        
        selec = [trabajador for trabajador in trabajadores if trabajador['cargo'] == OpIm] 
        
        
          
        with open('planilla_sueldo.txt', 'w') as archivo:
          for trabajador in selec:
            archivo.write(f"{trabajador['nombre']} {trabajador['apellido']} - {trabajador['cargo']} - Sueldo Bruto: {trabajador['sueldo_bruto']} - Descuento Salud: {trabajador['desc_salud']} - Descuento AFP: {trabajador['desc_afp']} - Líquido a Pagar: {trabajador['liquido_pagar']}")
 
 
 
Menu = True
while Menu == True:
  OpUs = input("Eliga una opcion\n1-Registrar un Trabajador\n2-Listar todos los trabajadores\n3-Imprimir planilla de sueldos\n4-salir del programa\n")         
  if OpUs == "1":
    registrar_trabajador()
  elif OpUs == "2":
    listar_trabajadores()
  elif OpUs == "3":
    imprimir_planilla()
  elif OpUs == "4":
    print("Saliendo del programa.")
    break
  else:
            print("Error")
  
      
