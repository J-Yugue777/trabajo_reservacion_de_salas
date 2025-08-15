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
        print("Error reserva 1 con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error solicitud 1,en  la hora solicida no estamos en servicio ")
    lis=[a1]
    print(f"resumen de las reservaciones {lis}")

elif a==2:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    lis=[a1,a2]
    if a1["hora"]+a1["duracion"]>=18:
        lis.remove(a1)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error solicitud 1,en  la hora solicida no estamos en servicio ")
    if a2["hora"]+a2["duracion"]>=18:
        lis.remove(a2)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error solicitud 2,en  la hora solicida no estamos en servicio ")
    print(f"resumen de las reservaciones {lis}")
elif a==3:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    lis=[a1,a2,a3]
    if a1["hora"]+a1["duracion"]>=18:
        lis.remove(a1)
        print("Error reserva 1 con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error solicitud 1,en  la hora solicida no estamos en servicio ")

    if a2["hora"]+a2["duracion"]>=18:
        lis.remove(a2)
        print("Error reserva 2 con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error solicitud 2,en  la hora solicida no estamos en servicio ")

    if a3["hora"]+a3["duracion"]>=18:
        lis.remove(a3)
        print("Error reserva 3 con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error solicitud 3,en  la hora solicida no estamos en servicio ")
    print(f"resumen de las reservaciones {lis}")
elif  a ==4:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a4={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    lis=[a1,a2,a3,a4]
    if a1["hora"]+a1["duracion"]>=18:
        lis.remove(a1)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error solicitud 1,en  la hora solicida no estamos en servicio ")

    if a2["hora"]+a2["duracion"]>=18:
        lis.remove(a2)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error solicitud 2,en  la hora solicida no estamos en servicio ")

    if a3["hora"]+a3["duracion"]>=18:
        lis.remove(a3)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error solicitud 3,en  la hora solicida no estamos en servicio ")

    if a4["hora"]+a4["duracion"]>=18:
        lis.remove(a4)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a4["hora"] <=8 or a4["hora"] >=18:
        print("Error solicitud 4,en  la hora solicida no estamos en servicio ")
    print(f"resumen de las reservaciones {lis}")
elif a ==5:
    a1={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a2={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a3={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a4={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    a5={
        "solicitante":input("ingrese su nombre porfavor :"),
        "Dia":input("Dia de la semana en la que va ha hacer la reservacion : "),
        "hora":int(input("ingrese la hora del dia para hacer la reservacion (8 am - 18 pm )  ")),
        "duracion":int(input("ingrese la duracion de la reunion : "))
     }
    lis=[a1,a2,a3,a4,a5]
    if a1["hora"]+a1["duracion"]>=18:
        lis.remove(a1)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a1["hora"] <=8 or a1["hora"] >=18:
        print("Error solicitud 1,en  la hora solicida no estamos en servicio ")

    if a2["hora"]+a2["duracion"]>=18:
        lis.remove(a2)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a2["hora"] <=8 or a2["hora"] >=18:
        print("Error solicitud 2,en  la hora solicida no estamos en servicio ")

    if a3["hora"]+a3["duracion"]>=18:
        lis.remove(a3)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a3["hora"] <=8 or a3["hora"] >=18:
        print("Error solicitud 3,en  la hora solicida no estamos en servicio ")

    if a4["hora"]+a4["duracion"]>=18:
        lis.remove(a4)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a4["hora"] <=8 or a4["hora"] >=18:
        print("Error solicitud 4,en  la hora solicida no estamos en servicio ")

    if a5["hora"]+a5["duracion"]>=18:
        lis.remove(a5)
        print("Error con la duracion y hora agendada , porfavor sea cooerente ")
    if a5["hora"] <=8 or a5["hora"] >=18:
        print("Error solicitud 5,en  la hora solicida no estamos en servicio ")

    print(f"resumen de las reservaciones {lis}")
else:
    print("Solo se encuentran disponibles maximo 5 salas ")