for j in range(3): #outer for. Se va a ejecutar primero, y se queda en este formato hasta que el segundo loop termina. 
    for k in range(2): #inner for, se ejecuta de segundo orden, y normalmente acaba el primer loop para luego dejar que el outer for siga el curso, se repite hasta que toda la secuencia acaba.
        print(f"{j}, {k}")