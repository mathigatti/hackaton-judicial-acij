import pandas as pd

data = [
    {
        "Resolucion": "29/2023",
        "Fecha_res": "14 de febrero de 2023",
        "Nombre": "Dra. Silvia Sawaya de Llobeta",
        "Cargo": "Secretaria de juzgado de la Cámara Federal de Apelaciones de Tucumán",
        "Tribunal": "Cámara Federal de Apelaciones de Tucumán",
        "Fecha_inicio": "20 de septiembre de 2022",
        "Fecha_fin": "7 de diciembre de 2022",
        "Motivo": "Cuidado de su cónyuge internado luego de un trasplante renal",
        "Analista": "chatGPT",
        "Comentarios": "La licencia es extraordinaria con goce de haberes. La agente agotó los días de licencia por atención de familiar enfermo. La licencia se otorga sin objeciones por parte del Presidente de la Cámara.",
        "Efecto": "No especificado"
    },
    {
        "Resolucion": "2105/2023",
        "Fecha_res": "25 de agosto de 2023",
        "Nombre": "Claudio M. Vázquez",
        "Cargo": "Magistrado del Juzgado Federal de Primera Instancia de Río Gallegos",
        "Tribunal": "Juzgado Federal de Primera Instancia de Río Gallegos",
        "Fecha_inicio": "27 de junio de 2023",
        "Fecha_fin": "30 de junio de 2023",
        "Motivo": "Participar del 'Encuentro Federal de Jueces y Secretarios Electorales 2023' en la sede de la Cámara Nacional Electoral en la Ciudad Autónoma de Buenos Aires",
        "Analista": "chatGPT",
        "Comentarios": "La licencia fue aprobada sin objeciones por el Presidente de la Cámara Federal de Apelaciones de Comodoro Rivadavia.",
        "Efecto": "No especificado"
    },
    {
        "Resolucion": "2087/2023",
        "Fecha_res": "25 de agosto de 2023",
        "Nombre": "Alicia Marta Valente",
        "Cargo": "Prosecretaria administrativa del Juzgado Nacional de Menores N° 7",
        "Tribunal": "Juzgado Nacional de Menores N° 7",
        "Fecha_inicio": "2 de julio de 2023",
        "Fecha_fin": "Indeterminado (6 meses o hasta que se otorgue la jubilación si esta se produce antes)",
        "Motivo": "Prórroga del plazo previsto para licencia por afección que padece y situación de jubilación por invalidez",
        "Analista": "chatGPT",
        "Comentarios": "La licencia con goce del 50% de haberes se otorga sin objeciones de la Cámara Nacional de Apelaciones en lo Criminal y Correccional. La agente debe informar periódicamente el estado del trámite jubilatorio.",
        "Efecto": "No especificado"
    },
    {
        "Resolucion": "852/2023",
        "Fecha_res": "28 de abril de 2023",
        "Nombre": "Dr. Sebastián Picasso",
        "Cargo": "Magistrado integrante de la Sala “A” de la Cámara Nacional de Apelaciones en lo Civil",
        "Tribunal": "Cámara Nacional de Apelaciones en lo Civil",
        "Fecha_inicio": "7 de junio de 2023",
        "Fecha_fin": "9 de junio de 2023",
        "Motivo": "Asistir como jurado académico al concurso público n° 211 del Consejo de la Magistratura de la Provincia del Neuquén",
        "Analista": "chatGPT",
        "Comentarios": "La licencia fue aprobada sin objeciones por la Presidencia de la Cámara Nacional de Apelaciones en lo Civil.",
        "Efecto": "No especificado"
    },
    {
        "Resolucion": "1789/2023",
        "Fecha_res": "6 de julio de 2023",
        "Nombre": "Dra. Mariana Inés Catalano",
        "Cargo": "Magistrada integrante de la Cámara Federal de Apelaciones de Salta",
        "Tribunal": "Cámara Federal de Apelaciones de Salta",
        "Fecha_inicio": "9 de junio de 2023",
        "Fecha_fin": "9 de junio de 2023",
        "Motivo": "Licencia con goce de haberes previamente concedida",
        "Comentarios": "Se deja sin efecto parcialmente la resolución n° 681/23 respecto del día 8 de junio de 2023, manteniéndose la licencia solo para el día 9 de junio de 2023.",
        "Efecto": "Parcialmente sin efecto respecto del día 8 de junio de 2023"
      }

]

pd.DataFrame(data).to_csv("data.csv", index=False)