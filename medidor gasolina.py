unidad_elegida = False



while unidad_elegida == False:
        unidad =int(input("Presiona 1 para Kilómetros o 2 para Millas: "))

        if unidad == 1:
                kilometraje = input("¿Cuántos kilómetros recorriste desde el último tanque lleno? ")
                unidad_elegida = True
                
        elif unidad == 2:
                millaje = input("¿Cuántas millas recorriste desde el último tanque lleno? ")
                unidad_elegida = True
                
                
        else:
                print("Debes elegir millas o kilómetros")

        if unidad == 1:
                gasolina_litros = input("¿Cuántos litros de combustible colocaste en este momento? ")
                kilometros_litro = float(kilometraje) / float(gasolina_litros)
                print("El promedio de economía de combustible es de " +  str("{0:.2f}".format(kilometros_litro)) + " Kilómetros por Litro.")

        if unidad == 2:
                gasolina_galones = input("¿Cuántos galones de combustible colocaste en este momento? ")
                millas_galon = float(millaje) / float(gasolina_galones)
                print("El promedio de economía de combustible es de " +  str("{0:.2f}".format(millas_galon)) + " Millas por galón.")

        volver = str(input("¿Deseas hacer una nueva medición? S / N): ").upper())

        if volver == "S":
                unidad_elegida = False
        
