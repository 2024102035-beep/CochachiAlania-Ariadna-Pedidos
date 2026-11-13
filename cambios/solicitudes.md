# REGISTRO DE SOLICITUDES DE CAMBIO
#Empresa: Comercial NovaTech  
#Responsable: Cochachi Alania Ariadna

## 1. INC-014–Error en el calculo del subtotal

-Descripcion: El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada.
- Tipo de cambio: Correctivo.
- Justificacion: Corregir el calculo para obtener el importe real del pedido.
- Requisito afectado: RN-01.
- Archivos afectados: codigo/pedidos.py.
- Riesgo: Calculo incorrecto de los importes.
- Criterio de aceptacion: Para un precio de S/ 80 y 3 unidades, el subtotal debe ser S/ 240.
- Decision:Aprobado (simulado).

## 2. CR-015–Calculo del costo de envio

- Descripcion: Incorporar el calculo automatico del costo de envio y del total del pedido.
- Tipo de cambio: Perfectivo.
- Justificacion:Mejorar el sistema incorporando el costo de envio segun el subtotal.
- Requisitos afectados:RN-02, RN-03 y RN-04.
- Archivos afectados:codigo/pedidos.py y documentos/requisitos.md.
- Riesgo:Asignacion incorrecta del costo de envio o del total.
- Criterio de aceptacion: Si el subtotal es igual o superior a S/ 300, el envio es gratuito; si es menor, cuesta S/ 20. El total debe sumar subtotal mas envio.
- Decision: Aprobado (simulado).