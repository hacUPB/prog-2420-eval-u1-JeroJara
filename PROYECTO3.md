

### ### Problema 6 (obligatorio): Calcular la edad de una persona a partir de su fecha de nacimiento y la fecha actual

### **Descripción del Problema:**
### Se desea saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento. Además, le gustaría saber si ya ha cumplido años este año o aún no, y si hoy es su cumpleaños para celebrarlo. Cada una de las fechas está conformada por 3 variables: día, mes y año
 
 ```
 Inicio

  
  leer dia_naci
  leer mes_naci
  leer año_naci
  leer mes_actu
  leer año_actu
  leer dia_actu
      leer lectura dia_naci
      leer lectura mes_naci
      leer lectura año_naci
      leer lectura mes_actu
      leer lectura año_actu
      leer lectura dia_actu
      si lecturaaño_actu-lecturaaño_naci == 0 entonces:
            
      
 Fin
 ```


 ### Problema 1: Determinar el promedio de calificaciones de un estudiante y si ha aprobado o no

Ana quiere saber si ha aprobado sus exámenes finales. Tiene una lista de sus calificaciones y necesita calcular el promedio. Para aprobar, debe tener un promedio de al menos 3.0.

```
Inicio
    leer lista_calificaciones
    leer numero_calificaciones
    definir contador= numero_calificaciones
    mientras contador > 0 entonces:
        definir suma = 0
        leer calificacion
        suma = suma + calificacion
        contador = contador - 1
        
    fin mientras
    dividir suma entre numero_calificaciones = promedio 
    imprimir promedio
    si promedio >= 3 entonces:
        imprimir  "APROBASTE c:"
    fin si

    si promedio < 3 entonces:
    imprimir  "NO APROBASTE :c"
    fin si

Fin
```
