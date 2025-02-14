export const BASE_URL = "http://localhost:8000"
// export const BASE_URL = "http://144.91.86.137:3502"
export const BASE_GEOSERVER_URL = "http://localhost:8080/geoserver/wms"
export const AUTH_URL = BASE_URL + "/token"
export const PREDICTION_URL = BASE_URL + "/predict"
export const baseData = {
    "crops":[
        "Alfalfa",
        "Barley",
        "Beans",
        "Bermudagrass",
        "Birdsfoot Trefoil",
        "Bromegrass",
        "Chickpeas",
        "Clover",
        "Fava Beans",
        "Fescue",
        "Field Peas",
        "Lentils",
        "Lespedeza",
        "Lupins",
        "Millet",
        "Mung Beans",
        "Oats",
        "Orchard Grass",
        "Pearl Millet",
        "Peas",
        "Rye",
        "Rye (Cereal Rye)",
        "Sorghum",
        "Sorghum-Sudangrass Hybrid",
        "Soybeans",
        "Sunn Hemp",
        "Timothy Grass",
        "Triticale",
        "Vetch",
        "Wheat",
    ],
    "common_pests":{
        "Insects":[
            "Colorado Potato Beetle",
            "Potato Tuber Moth",
            "Wireworms",
            "Aphids",
            "Leafhoppers",
            "Flea Beetles",
            "Cutworms",
            "White Grubs",
            "Armyworms",
            "Blister Beetles",
            "Psyllids",
            "Stink Bugs",
            "Thrips"
        ],
        "Nematodes":[
            "Potato Cyst Nematodes",
            "Root Knot Nematodes",
            "Lesion Nematodes",
            "Stubby Root Nematodes"
        ],
        "Mites":[
            "Two-Spotted Spider Mite",
            "Broad Mites",
            "Russet Mites"
        ],
        "Rodents":[
            "Voles",
            "Gophers",
            "Field Mice"
        ]
    }
}