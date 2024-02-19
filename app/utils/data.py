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
