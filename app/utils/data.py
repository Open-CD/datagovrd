month_names_dict = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

institutions_dict = {
    "sns": {
        "name": "Servicio Nacional de Salud",
        "abbreviation": "SNS",
        "services": ["Estadisticas institucionales", "Nomina", "Inventario"],
    },
    "dncd": {
        "name": "La Dirección Nacional de Control de Drogas",
        "abbreviation": "DNCD",
        "services": [],
    }
}

institutions_arr =  [
    {"name": info["name"], "abbreviation": info["abbreviation"], "services": info["services"]}
    for _, info in institutions_dict.items()
]
