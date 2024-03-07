# Hackatón Judicial

Participé en la Hackatón Judicial organizada por [ACIJ](https://acij.org.ar/) (Asociación Civil por la Igualdad y la Justicia). Durante charlamos algunos retos y problematicas relacionadas a lo trabajoso de extraer manualmente datos de PDFs y las dificultades para automatizar estas tareas. En este repositorio dejo algunas pruebas que hicimos intentando usar herramientas novedosas como [chatGPT](https://chat.openai.com/) y [textract](https://aws.amazon.com/es/textract/) para encarar estos inconvenientes.

## Herramientas

Resumen de herramientas
- [textract](https://aws.amazon.com/es/textract/)
- [openAI Assistant](https://platform.openai.com/playground)
- [chatGPT](https://chat.openai.com/)

## Pruebas hechas

Estan adjuntas en las carpetas correspondientes a cada caso los archivos usados para permitir replicabilidad.

### Caso 1

#### Objetivo

Extraer la tabla encontrada en las últimas 2 páginas de `original.pdf`

#### Procedimiendo

Se sacó un screenshot del PDF en la región de la tabla y se utilizó [textract](https://aws.amazon.com/es/textract/) para extraer la tabla, dando como resultado `tabla-textract.csv`.

#### Resultados y conclusiones

No la revise tanto la tabla pero parece haber dado buenos resultados.  

### Caso 2

#### Objetivo

Convertir el pdf `original.pdf` en un excel

#### Procedimiento

Se convirtieron las páginas del PDF en varias imagenes (una por cada página) y luego como test se intentó digitalizar la primera página usando [textract](https://aws.amazon.com/es/textract/).

#### Resultados y conclusiones

Esto dió buenos resultados, se tendría que repetir este proceso para cada página (o automatizarlo haciendo un pequeño script que realice estos pasos automaticamente).

### Caso 3

#### Objetivo

Averiguar el total de ingresos de causas mencionado en el PDF "Informe_Estadistico-DGDI-julio_diciembre_ok.pdf"

#### Procedimiento

Se usó [openAI assistant](https://platform.openai.com/playground) con los siguientes parámetros.

    Config
        Name 
            PDF judicial extractor

        Instructions
            "Check the attached PDF and answer questions based on the info you get from it. Always specify the page/s you used to answer."

        Model
            gpt-4-turbo-preview

        tools
            Code interpreter OFF
            Retrieval ON

        Files attached
            Informe_Estadistico-DGDI-julio_diciembre_ok.pdf

**Conversación**

- User: _¿Cual es el total de ingresos de causas?_

- Bot: _El total de ingresos de causas es de 141,845._

- User: _de donde sacaste ese dato?_

- Bot: _El dato sobre el total de ingresos de causas, 141,845, fue obtenido de la página 27 del documento ._

#### Resultados y conclusiones

Se logró que conteste el dato correcto sin mayores complicaciones.

### Caso 4

#### Objetivo
De una lista de varios PDFs se quiere calcular la cantidad total de juicios y el promedio de duración de los mismos.

#### Procedimiento
No registre las respuestas pero hice basicamente lo mismo que en el caso 3, use el openAI Assistant y le consulté por los juicios totales y el promedio de duración de los mismos.

#### Resultados y conclusiones
No anduvo bien con openai playground pidiendole que calcule cosas que requieran consultar en varios pdfs y hacer calculos. Charlamos que en esos casos es mejor migrar las tablas a excel, usando por ejemplo textract y despues hacer los calculos en excel. Y en todo caso ahi se le puede pedir ayuda a chatgpt para armar las formulas de excel.

### Caso 5

#### Objetivo
Extraer los siguientes valores de los PDFs del 2023 para "Goce de haberes" de esta pagina de licencias: https://www.csjn.gov.ar/transparencia/personal-judicial/licencias

    Resolucion:	Número de la resolución
    Fecha_res:	Fecha de pedido de la resolución
    Nombre:	Nombre de la persona solicitante de la licencia con goce de haberes
    Cargo:	Cargo de la persona solicitante de la licencia con goce de haberes
    Tribunal:	Nombre del Tribunal, Juzgado o Cámara donde trabaja la persona solicitante
    Fecha_inicio:	Fecha de inicio de la licencia
    Fecha_fin:	Fecha de fin de la licencia
    Motivo:	Razón por la que solicita la licencia
    Comentarios:	Comentarios relevantes sobre el pedido de licencia
    Efecto:	Si queda sin efecto por otra resolución
    Link:	Link a la resolución

#### Método
Esto se arrancó a hacer manualmente, y los resultados estan [acá](https://docs.google.com/spreadsheets/d/1wdHlpvseUHPSc3zL7825aIMNXCcvbQkz19sIYGBcBhI/edit#gid=1415951092). Después en la solapa "chatGPT ejemplo" de ese mismo documento dejé los resultados obtenidos con chatGPT Pro (la versión paga de chatGPT) al pedirle que analice los PDFs, [acá](https://chat.openai.com/share/ce4f7025-88b7-41b2-bfcc-21ce745b40ec) está el detalle de la conversación. Fui consultando uno por uno los PDFs, parecido a lo que se mencionó en el caso 2, se podría automatizar facilmente haciendo un pequeño programa que ejecute esos pasos.

#### Resultados y conclusiones

Me pareció que anduvo bastante bien aunque me aclararon que, por ejemplo, el documento 852 debería decir "Sin efecto" en la columna "Efecto", hablamos que se podría intentar solucionar ese problema si se le aclara al chat las reglas para decidir si algo tiene o no efecto.

# Conclusión General

Mi conclusión es que con un presupuesto de 50 dolares mensuales o menos dedicado a herramientas como textract, chatGPT pro o openAI playground y algo de asistencia tecnica varias tareas de trabajo manual pesado deberían poder automatizarse o reducirse en gran parte.

Páginas con detalles de precios de los servicios

- https://help.openai.com/en/articles/8550641-assistants-api
- https://openai.com/pricing
- https://aws.amazon.com/es/textract/pricing/
- https://openai.com/chatgpt/pricing

# Apéndice

## Links de la hackaton

- [Listado bases de datos](https://docs.google.com/document/d/1Ykj-_d85wV5NB-ClQt_7Jd_oujhOfjlLzzlGcuORjp0/edit)
- [Hackaton judicial](https://docs.google.com/document/d/1kHjrZrUsPVyvL-ewl_P-oZslbMsDRyY2I71N-81tdpw/edit)
- [Documento de trabajo- preguntas disparadoras](https://docs.google.com/document/d/1l5lj-mGs4DRbJSuYkIccv40g1psWaY1H0gA3eoNVoH8/edit)
- [Miro de la Hackaton](https://miro.com/app/board/uXjVNkQbeYA=/)

## Comandos útiles
Ignorar esto si no tenes linux

Convertir PDF a imagenes (una por página)
    `pdftoppm -jpeg 364.pdf output`

Convetir Imagenes a PDF (una por página)
    `img2pdf output*.jpg -o mydoc.pdf`

    Para instalarlo: `sudo apt install img2pdf`