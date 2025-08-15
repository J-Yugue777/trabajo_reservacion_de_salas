print("HOLA BIENVENIDO AL LAS RESERVACIONES DE SALA")
a=int(input("¿cuantas reservas desea hacer hoy?  "))
if a == 1:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
    }
    if a1["hora"]+a1["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    lis=[a1]
    print(f"resumen de las reservaciones {lis}")

if a==2:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a1["hora"]+a1["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a2["hora"]+a2["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    lis=[a1,a2]
    print(f"resumen de las reservaciones {lis}")
if a==3:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a1["hora"]+a1["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a2["hora"]+a2["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a3["hora"]+a3["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    lis=[a1,a2,a3]
    print(f"resumen de las reservaciones {lis}")
if  a ==4:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a1["hora"]+a1["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a2["hora"]+a2["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a3["hora"]+a3["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a4={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a4["hora"]+a4["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a4["hora"] <=8 or a4["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    lis=[a1,a2,a3,a4]
    print(f"resumen de las reservaciones {lis}")
if a ==5:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a1["hora"]+a1["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a2["hora"]+a2["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a3["hora"]+a3["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a4={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a4["hora"]+a4["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a4["hora"] <=8 or a4["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    a5={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    if a5["hora"]+a5["duracion"]>=18:
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a5["hora"] <=8 or a5["hora"] >=18:
        print("Error,en  la hora solicida no estamos en servicio ")
    lis=[a1,a2,a3,a4,a5]
    print(f"resumen de las reservaciones {lis}")
elif a>=6:
    print("Solo se encuentran disponibles maximo 5 salas ")