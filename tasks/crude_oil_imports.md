# Crude Oil Imports Menu task

Using the API specification in `docs/EIA APIv2.postman_collection.json`, the examples of other menus implemented in `openbb_energy` and the OpenBB Platform documentation in related to adding new extensions in the following URLs:

- https://docs.openbb.co/platform/developer_guide/architecture_overview
- https://docs.openbb.co/platform/developer_guide/data_provider
- https://docs.openbb.co/platform/developer_guide/extensions

Implement the `crude-oil-imports` section of the EIA API in a designated menu.

---

Task context:

Get responses from the EIA API:

```json
{
  "response": {
    "id": "crude-oil-imports",
    "name": "Crude Oil Imports",
    "description": "Crude oil imports by country to destination, \r\n        includes type, grade, quantity.  Source: EIA-814  Interactive data \r\n        product:  www.eia.gov/petroleum/imports/companylevel/",
    "frequency": [
      {
        "id": "monthly",
        "description": "One data point for each month.",
        "query": "M",
        "format": "YYYY-MM"
      },
      {
        "id": "annual",
        "description": "One data point for each calendar year.",
        "query": "A",
        "format": "YYYY"
      }
    ],
    "facets": [
      {
        "id": "originId",
        "description": "Origin Id"
      },
      {
        "id": "originType",
        "description": "Origin Type"
      },
      {
        "id": "destinationId",
        "description": "Destination Id"
      },
      {
        "id": "destinationType",
        "description": "Destination Type"
      },
      {
        "id": "gradeId",
        "description": "Grade Id"
      }
    ],
    "data": {
      "quantity": {
        "units": "thousand barrels"
      }
    },
    "startPeriod": "2009-01",
    "endPeriod": "2025-04",
    "defaultDateFormat": "YYYY-MM",
    "defaultFrequency": "monthly"
  },
  "request": {
    "command": "/v2/crude-oil-imports/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
  "response": {
    "totalFacetOptions": 5,
    "facetOptions": [
      "originId",
      "originType",
      "destinationId",
      "destinationType",
      "gradeId"
    ]
  },
  "request": {
    "command": "/v2/crude-oil-imports/facet/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
  "response": {
    "totalFacets": 71,
    "facets": [
      {
        "id": "CTY_CA",
        "name": "Canada"
      },
      {
        "id": "CTY_BL",
        "name": "Bolivia"
      },
      {
        "id": "CTY_NI",
        "name": "Nigeria"
      },
      {
        "id": "CTY_SY",
        "name": "Syria"
      },
      {
        "id": "CTY_TH",
        "name": "Thailand"
      },
      {
        "id": "CTY_KZ",
        "name": "Kazakhstan"
      },
      {
        "id": "REG_ME",
        "name": "Middle East"
      },
      {
        "id": "CTY_PM",
        "name": "Panama"
      },
      {
        "id": "CTY_CO",
        "name": "Colombia"
      },
      {
        "id": "CTY_EK",
        "name": "Equatorial Guinea"
      },
      {
        "id": "CTY_AG",
        "name": "Algeria"
      },
      {
        "id": "CTY_AR",
        "name": "Argentina"
      },
      {
        "id": "CTY_VM",
        "name": "Vietnam"
      },
      {
        "id": "CTY_CG",
        "name": "Congo-Kinshasa"
      },
      {
        "id": "CTY_GH",
        "name": "Ghana"
      },
      {
        "id": "CTY_IR",
        "name": "Iran"
      },
      {
        "id": "CTY_GT",
        "name": "Guatemala"
      },
      {
        "id": "CTY_IZ",
        "name": "Iraq"
      },
      {
        "id": "CTY_AS",
        "name": "Australia"
      },
      {
        "id": "CTY_VE",
        "name": "Venezuela"
      },
      {
        "id": "CTY_MU",
        "name": "Oman"
      },
      {
        "id": "CTY_IV",
        "name": "Cote d'Ivoire"
      },
      {
        "id": "CTY_AL",
        "name": "Albania"
      },
      {
        "id": "CTY_DA",
        "name": "Denmark"
      },
      {
        "id": "CTY_TS",
        "name": "Tunisia"
      },
      {
        "id": "CTY_BB",
        "name": "Barbados"
      },
      {
        "id": "CTY_CF",
        "name": "Congo-Brazzaville"
      },
      {
        "id": "CTY_EG",
        "name": "Egypt"
      },
      {
        "id": "CTY_KU",
        "name": "Kuwait"
      },
      {
        "id": "CTY_YM",
        "name": "Yemen"
      },
      {
        "id": "REG_EU",
        "name": "Europe"
      },
      {
        "id": "OPN_Y",
        "name": "OPEC"
      },
      {
        "id": "CTY_AE",
        "name": "United Arab Emirates"
      },
      {
        "id": "CTY_LY",
        "name": "Libya"
      },
      {
        "id": "CTY_NO",
        "name": "Norway"
      },
      {
        "id": "CTY_MR",
        "name": "Mauritania"
      },
      {
        "id": "CTY_NL",
        "name": "Netherlands"
      },
      {
        "id": "REG_OA",
        "name": "Other Americas"
      },
      {
        "id": "REG_AF",
        "name": "Africa"
      },
      {
        "id": "OPN_N",
        "name": "Non-OPEC"
      },
      {
        "id": "CTY_SP",
        "name": "Spain"
      },
      {
        "id": "CTY_OD",
        "name": "South Sudan"
      },
      {
        "id": "CTY_PP",
        "name": "Papua New Guinea"
      },
      {
        "id": "CTY_CH",
        "name": "China"
      },
      {
        "id": "CTY_GB",
        "name": "Gabon"
      },
      {
        "id": "CTY_AJ",
        "name": "Azerbaijan"
      },
      {
        "id": "CTY_AO",
        "name": "Angola"
      },
      {
        "id": "CTY_BH",
        "name": "Belize"
      },
      {
        "id": "CTY_BR",
        "name": "Brazil"
      },
      {
        "id": "CTY_MX",
        "name": "Mexico"
      },
      {
        "id": "CTY_RS",
        "name": "Russia"
      },
      {
        "id": "CTY_SA",
        "name": "Saudi Arabia"
      },
      {
        "id": "CTY_ID",
        "name": "Indonesia"
      },
      {
        "id": "REG_CA",
        "name": "Canada (Region)"
      },
      {
        "id": "CTY_CD",
        "name": "Chad"
      },
      {
        "id": "CTY_EC",
        "name": "Ecuador"
      },
      {
        "id": "CTY_CM",
        "name": "Cameroon"
      },
      {
        "id": "CTY_TD",
        "name": "Trinidad and Tobago"
      },
      {
        "id": "CTY_UK",
        "name": "United Kingdom"
      },
      {
        "id": "CTY_BX",
        "name": "Brunei"
      },
      {
        "id": "REG_AP",
        "name": "Asia-Pacific"
      },
      {
        "id": "CTY_GY",
        "name": "Guyana"
      },
      {
        "id": "CTY_MY",
        "name": "Malaysia"
      },
      {
        "id": "CTY_PE",
        "name": "Peru"
      },
      {
        "id": "CTY_QA",
        "name": "Qatar"
      },
      {
        "id": "CTY_IT",
        "name": "Italy"
      },
      {
        "id": "CTY_SF",
        "name": "South Africa"
      },
      {
        "id": "REG_EA",
        "name": "Eurasia"
      },
      {
        "id": "WORLD",
        "name": "World"
      },
      {
        "id": "CTY_BF",
        "name": "The Bahamas"
      },
      {
        "id": "CTY_SG",
        "name": "Senegal"
      }
    ]
  },
  "request": {
    "command": "/v2/crude-oil-imports/facet/originId/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
  "response": {
    "totalFacets": 4,
    "facets": [
      {
        "id": "REG",
        "name": "Region"
      },
      {
        "id": "CTY",
        "name": "Country"
      },
      {
        "id": "OPN",
        "name": "OPEC/non-OPEC"
      },
      {
        "id": "WORLD",
        "name": "World"
      }
    ]
  },
  "request": {
    "command": "/v2/crude-oil-imports/facet/originType/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
  "response": {
    "totalFacets": 508,
    "facets": [
      {
        "id": "RF_394",
        "name": "PHILLIPS 66 / PONCA CITY / OK"
      },
      {
        "id": "RF_528",
        "name": "MARATHON PETROLEUM CO LP / DETROIT / MI"
      },
      {
        "id": "RF_530",
        "name": "MARATHON PETROLEUM CO LP / GARYVILLE / LA"
      },
      {
        "id": "RF_2403",
        "name": "UNKNOWN PROCESSOR-WY / UNKNOWN PROCESSOR-WY / WY"
      },
      {
        "id": "RF_310",
        "name": "SUNOCO INC / MARCUS HOOK / PA"
      },
      {
        "id": "RF_148",
        "name": "PASADENA REFINING SYSTEMS INC / PASADENA / TX"
      },
      {
        "id": "RF_506",
        "name": "DELAWARE CITY REFINING CO LLC / DELAWARE CITY / DE"
      },
      {
        "id": "RF_83",
        "name": "TOTAL PETROCHEMICALS USA INC / PORT ARTHUR / TX"
      },
      {
        "id": "RF_98",
        "name": "BP PRODUCTS NORTH AMERICA / CHERRY POINT REFINERY / WA"
      },
      {
        "id": "RF_289",
        "name": "PHILLIPS 66 / ALLIANCE / LA"
      },
      {
        "id": "RF_92",
        "name": "ST PAUL PARK REFINING CO LLC / ST PAUL PARK REFINING CO LLC / MN"
      },
      {
        "id": "RF_3114",
        "name": "TEPPCO CRUDE PL / CUSHING / OK"
      },
      {
        "id": "RF_3828",
        "name": "L & L OIL & GAS INC / MORGAN CITY 31 / LA"
      },
      {
        "id": "RF_339",
        "name": "VALERO REFINING CO OKLAHOMA / ARDMORE / OK"
      },
      {
        "id": "RF_4832",
        "name": "LBC TERMINALS / SUNSHINE / LA"
      },
      {
        "id": "RF_4870",
        "name": "DELTA TRADING LP - PALOMA / BAKERSFIELD / CA"
      },
      {
        "id": "RF_363",
        "name": "PAR HAWAII REFINING LLC / KAPOLEI / HI"
      },
      {
        "id": "RF_4509",
        "name": "KINDER MORGAN LIQ TERMLS LLC / PERTH AMBOY / NJ"
      },
      {
        "id": "RF_4831",
        "name": "NUSTAR ENERGY LP / ST JAMES / LA"
      },
      {
        "id": "RF_4913",
        "name": "TIDAL ENERGY MARKETING INC / CUSHING / OK"
      },
      {
        "id": "RF_2396",
        "name": "UNKNOWN PROCESSOR-MS / UNKNOWN PROCESSOR-MS / MS"
      },
      {
        "id": "RF_3587",
        "name": "KINDER MORGAN LIQ TERMLS LLC / PHILADELPHIA / PA"
      },
      {
        "id": "RF_290",
        "name": "CONTINENTAL REFINING CO LLC / CONTINENTAL REFINING CO LLC / KY"
      },
      {
        "id": "RF_3862",
        "name": "NUSTAR ENERGY LP / BALTIMORE / MD"
      },
      {
        "id": "RF_4347",
        "name": "BUCKEYE TERMINALS LLC / WOODHAVEN TERMINAL / MI"
      },
      {
        "id": "RF_2677",
        "name": "MARATHON PETROLEUM CO LLC / LIMA / OH"
      },
      {
        "id": "RF_4879",
        "name": "BUCKEYE TERMINALS LLC / PERTH AMBOY / NJ"
      },
      {
        "id": "RF_4076",
        "name": "CROSSTEX PROCESSING SVCS LLC / RIVERSIDE FRACTIONATION PLANT / LA"
      },
      {
        "id": "RF_3594",
        "name": "VALERO MARKETING & SUPPLY CO / ST JAMES / LA"
      },
      {
        "id": "RF_2394",
        "name": "UNKNOWN PROCESSOR-AR / UNKNOWN PROCESSOR-AR / AR"
      },
      {
        "id": "RS_MN",
        "name": "Minnesota"
      },
      {
        "id": "RS_AR",
        "name": "Arkansas"
      },
      {
        "id": "RS_ID",
        "name": "Idaho"
      },
      {
        "id": "RS_MO",
        "name": "Missouri"
      },
      {
        "id": "RS_FL",
        "name": "Florida"
      },
      {
        "id": "RP_5",
        "name": "PADD5 (West Coast)"
      },
      {
        "id": "PT_1003",
        "name": "Newark, NJ"
      },
      {
        "id": "PT_2001",
        "name": "Morgan City, LA"
      },
      {
        "id": "PT_5104",
        "name": "Christianstd, VI"
      },
      {
        "id": "PT_5311",
        "name": "Freeport, TX"
      },
      {
        "id": "PT_5310",
        "name": "Galveston, TX"
      },
      {
        "id": "PT_0901",
        "name": "Buff-Niag Fl, NY"
      },
      {
        "id": "PT_3002",
        "name": "Tacoma, WA"
      },
      {
        "id": "PT_3303",
        "name": "Salt Lk Cty, UT"
      },
      {
        "id": "PT_3382",
        "name": "Natrona Aprt, WY"
      },
      {
        "id": "PT_3402",
        "name": "Noyes, MN"
      },
      {
        "id": "PS_LA",
        "name": "Louisiana"
      },
      {
        "id": "PS_WY",
        "name": "Wyoming"
      },
      {
        "id": "PT_2901",
        "name": "Astoria, OR"
      },
      {
        "id": "PP_3",
        "name": "PADD3 (Gulf Coast)"
      },
      {
        "id": "RF_3004",
        "name": "PHILLIPS 66 CARRIER LLC / PASADENA / TX"
      },
      {
        "id": "RF_3021",
        "name": "SUNOCO LOGISTICS / WESTVILLE / NJ"
      },
      {
        "id": "PT_2802",
        "name": "Eureka, CA"
      },
      {
        "id": "RF_5032",
        "name": "SUNOCO PARTNERS NGL FACILITIES LLC / NEDERLAND NGLS / TX"
      },
      {
        "id": "PT_2801",
        "name": "San Fran Int Ap, CA"
      },
      {
        "id": "RF_2367",
        "name": "UNKNOWN PROCESSOR-MA / UNKNOWN PROCESSOR-MA / MA"
      },
      {
        "id": "RF_282",
        "name": "EQUILON ENTERPRISES LLC / DES PLAINES TERMINAL / IL"
      },
      {
        "id": "PS_IA",
        "name": "Iowa"
      },
      {
        "id": "RF_2407",
        "name": "UNKNOWN PROCESSOR-HI / UNKNOWN PROCESSOR-HI / HI"
      },
      {
        "id": "PT_3701",
        "name": "Milwaukee, WI"
      },
      {
        "id": "RF_3694",
        "name": "PAR HAWAII REFINING LLC / SAND ISLAND / HI"
      },
      {
        "id": "PT_2713",
        "name": "Port Hueneme, CA"
      },
      {
        "id": "RF_4301",
        "name": "MAGELLAN PIPELINE CO LP / EAST HOUSTON / TX"
      },
      {
        "id": "RF_203",
        "name": "FLINT HILLS RESOURCES LP / PINE BEND REFINERY / MN"
      },
      {
        "id": "RF_278",
        "name": "TESORO REFINING & MARKETING / ANACORTES / WA"
      },
      {
        "id": "RF_526",
        "name": "PDV MIDWEST REFINING LLC / CITGO LEMONT / IL"
      },
      {
        "id": "RF_2379",
        "name": "UNKNOWN PROCESSOR-IN / UNKNOWN PROCESSOR-IN / IN"
      },
      {
        "id": "RF_2398",
        "name": "UNKNOWN PROCESSOR-TX / UNKNOWN PROCESSOR-TX / TX"
      },
      {
        "id": "RF_139",
        "name": "SUNOCO INC / EAGLE POINT / NJ"
      },
      {
        "id": "RF_121",
        "name": "ISLAND ENERGY SVCS DOWNSTREAM / KAPOLEI / HI"
      },
      {
        "id": "RF_80",
        "name": "LIMETREE BAY REFINING LLC / LIMETREE BAY / VI"
      },
      {
        "id": "RF_3124",
        "name": "OIL TANKING PL INC / HOUSTON (GULF) / TX"
      },
      {
        "id": "RF_385",
        "name": "DEER PARK REFINING LP / DEER PARK / TX"
      },
      {
        "id": "RF_401",
        "name": "SHELL OIL PRODUCTS US / ST ROSE / LA"
      },
      {
        "id": "RF_2395",
        "name": "UNKNOWN PROCESSOR-LA / UNKNOWN PROCESSOR-LA / LA"
      },
      {
        "id": "RF_303",
        "name": "WESTERN REFINING YORKTOWN INC / YORKTOWN / VA"
      },
      {
        "id": "RF_479",
        "name": "AXEON SPECIALTY PRODUCTS LLC / PAULSBORO / NJ"
      },
      {
        "id": "RF_529",
        "name": "MARATHON PETROLEUM CO LP / TEXAS CITY / TX"
      },
      {
        "id": "RF_2703",
        "name": "MARATHON PETROLEUM CO LLC / CANTON / OH"
      },
      {
        "id": "RF_87",
        "name": "MARATHON PETROLEUM CO LP / CATLETTSBURG / KY"
      },
      {
        "id": "RF_159",
        "name": "ERGON REFINING INC / VICKSBURG / MS"
      },
      {
        "id": "RF_2402",
        "name": "UNKNOWN PROCESSOR-UT / UNKNOWN PROCESSOR-UT / UT"
      },
      {
        "id": "RF_2372",
        "name": "UNKNOWN PROCESSOR-PA E / UNKNOWN PROCESSOR-PA / PA"
      },
      {
        "id": "RF_2388",
        "name": "UNKNOWN PROCESSOR-OH / UNKNOWN PROCESSOR-OH / OH"
      },
      {
        "id": "RF_209",
        "name": "ULTRAMAR INC / WILMINGTON REFINERY / CA"
      },
      {
        "id": "RF_3292",
        "name": "TRANSMONTAIGNE PRODT SVCS INC / PORT EVERGLADES SOUTH / FL"
      },
      {
        "id": "RF_3895",
        "name": "NUSTAR ENERGY LP / TEXAS CITY T-76-TX-2814 / TX"
      },
      {
        "id": "RF_2404",
        "name": "UNKNOWN PROCESSOR-AK / UNKNOWN PROCESSOR-AK / AK"
      },
      {
        "id": "RF_3965",
        "name": "PHILLIPS 66 CO / HARTFORD / IL"
      },
      {
        "id": "RF_3821",
        "name": "L & L OIL & GAS INC / FOURCHON 15 / LA"
      },
      {
        "id": "RS_LA",
        "name": "Louisiana"
      },
      {
        "id": "RS_MT",
        "name": "Montana"
      },
      {
        "id": "RS_WY",
        "name": "Wyoming"
      },
      {
        "id": "RS_NY",
        "name": "New York"
      },
      {
        "id": "RS_MD",
        "name": "Maryland"
      },
      {
        "id": "RP_6",
        "name": "PADD6 (Territories)"
      },
      {
        "id": "PT_2004",
        "name": "Baton Rouge, LA"
      },
      {
        "id": "PT_2002",
        "name": "New Orleans, LA"
      },
      {
        "id": "PT_2809",
        "name": "Sanfrancisco, CA"
      },
      {
        "id": "PT_3005",
        "name": "Bellingham, WA"
      },
      {
        "id": "PT_1402",
        "name": "Newport News, VA"
      },
      {
        "id": "PT_3304",
        "name": "Great Falls, MT"
      },
      {
        "id": "PT_3601",
        "name": "Duluth, MN"
      },
      {
        "id": "PT_3322",
        "name": "Del Bonita, MT"
      },
      {
        "id": "PT_3403",
        "name": "Portal, ND"
      },
      {
        "id": "PT_1001",
        "name": "New York, NY"
      },
      {
        "id": "PS_PA",
        "name": "Pennsylvania"
      },
      {
        "id": "PS_TX",
        "name": "Texas"
      },
      {
        "id": "PS_NJ",
        "name": "New Jersey"
      },
      {
        "id": "PT_1104",
        "name": "Pittsburgh, PA"
      },
      {
        "id": "PS_MN",
        "name": "Minnesota"
      },
      {
        "id": "PS_ND",
        "name": "North Dakota"
      },
      {
        "id": "PT_3308",
        "name": "Porthill, ID"
      },
      {
        "id": "PS_OR",
        "name": "Oregon"
      },
      {
        "id": "PP_6",
        "name": "PADD6 (Territories)"
      },
      {
        "id": "PP_1",
        "name": "PADD1 (East Coast)"
      },
      {
        "id": "US",
        "name": "United States"
      },
      {
        "id": "PT_2909",
        "name": "Kalama, WA"
      },
      {
        "id": "PT_3007",
        "name": "Port Angeles, WA"
      },
      {
        "id": "PT_3905",
        "name": "Gary, IN"
      },
      {
        "id": "PT_3205",
        "name": "Honolulu Int Ap, HI"
      },
      {
        "id": "RF_3070",
        "name": "ADJ CO-IL / IMPUTE ADJ - IL / IL"
      },
      {
        "id": "PT_4501",
        "name": "Kansas City, MO"
      },
      {
        "id": "RF_3592",
        "name": "VALERO MARKETING & SUPPLY CO / CORPUS CHRISTI / TX"
      },
      {
        "id": "RF_3135",
        "name": "PAR HAWAII REFINING LLC / MAUI / HI"
      },
      {
        "id": "RF_4085",
        "name": "ENTERPRISE GC LLC / HO NGL-ALMEDA TERMINAL 1 / TX"
      },
      {
        "id": "PT_5502",
        "name": "Amarillo, TX"
      },
      {
        "id": "PT_2103",
        "name": "Orange, TX"
      },
      {
        "id": "RF_223",
        "name": "PAULSBORO REFINING CO LLC / PAULSBORO / NJ"
      },
      {
        "id": "RF_308",
        "name": "TOLEDO REFINING CO LLC / TOLEDO / OH"
      },
      {
        "id": "RF_523",
        "name": "UNITED REFINING CO / WARREN / PA"
      },
      {
        "id": "RF_531",
        "name": "MARATHON PETROLEUM CO LP / ROBINSON / IL"
      },
      {
        "id": "RF_2359",
        "name": "EXXON CHEMICAL TRADING INC / HOUSTON / TX"
      },
      {
        "id": "RF_4690",
        "name": "SUNCOR ENERGY INC / GUERNSEY / WY"
      },
      {
        "id": "RF_125",
        "name": "CHEVRON USA / PASCAGOULA / MS"
      },
      {
        "id": "RF_434",
        "name": "PREMCOR REFINING GROUP INC / PORT ARTHUR / TX"
      },
      {
        "id": "RF_119",
        "name": "CHEVRON USA INC / EL SEGUNDO / CA"
      },
      {
        "id": "RF_288",
        "name": "LIMA REFINING CO / LIMA / OH"
      },
      {
        "id": "RF_2406",
        "name": "UNKNOWN PROCESSOR-CA / UNKNOWN PROCESSOR-CA / CA"
      },
      {
        "id": "RF_187",
        "name": "CALUMET MONTANA REFINING LLC / GREAT FALLS / MT"
      },
      {
        "id": "RF_228",
        "name": "CHALMETTE REFINING LLC / CHALMETTE / LA"
      },
      {
        "id": "RF_505",
        "name": "SHELL OIL PRODUCTS US / CONVENT / LA"
      },
      {
        "id": "RF_150",
        "name": "SILVER EAGLE REFINING INC / WOODS CROSS / UT"
      },
      {
        "id": "RF_276",
        "name": "SHELL OIL PRODUCTS US / NORCO / LA"
      },
      {
        "id": "RF_2387",
        "name": "UNKNOWN PROCESSOR-ND / UNKNOWN PROCESSOR-ND / ND"
      },
      {
        "id": "RF_4619",
        "name": "PLAINS LPG SERVICES / TULSA TERMINAL / OK"
      },
      {
        "id": "RF_3575",
        "name": "SUNOCO LOGISTICS / NEDERLAND TERMINAL / TX"
      },
      {
        "id": "RF_4953",
        "name": "VOPAK TERMINALS NORTH AMER INC / SAVANNAH / GA"
      },
      {
        "id": "RF_3251",
        "name": "GLOBAL CO LLC / ALBANY / NY"
      },
      {
        "id": "RF_2350",
        "name": "MOBIL OIL CORP / CHICAGO (EAST) / IL"
      },
      {
        "id": "RS_TX",
        "name": "Texas"
      },
      {
        "id": "RS_IL",
        "name": "Illinois"
      },
      {
        "id": "RS_IN",
        "name": "Indiana"
      },
      {
        "id": "RP_1",
        "name": "PADD1 (East Coast)"
      },
      {
        "id": "PT_3902",
        "name": "Peoria, IL"
      },
      {
        "id": "PT_4105",
        "name": "Toledo-Sandusky, OH"
      },
      {
        "id": "PT_1118",
        "name": "Marcus Hook, PA"
      },
      {
        "id": "PT_1101",
        "name": "Philadelphia, PA"
      },
      {
        "id": "PT_1903",
        "name": "Pascagoula, MS"
      },
      {
        "id": "PT_2101",
        "name": "Port Arthur, TX"
      },
      {
        "id": "PT_5312",
        "name": "Corpus Chris, TX"
      },
      {
        "id": "PT_2820",
        "name": "Martinez, CA"
      },
      {
        "id": "PT_3201",
        "name": "Honolu/Pearl, HI"
      },
      {
        "id": "PT_1103",
        "name": "Wilmington, DE"
      },
      {
        "id": "PT_3009",
        "name": "Sumas, WA"
      },
      {
        "id": "PT_3803",
        "name": "Sault St-Mar, MI"
      },
      {
        "id": "PT_3501",
        "name": "Minneapolis, MN"
      },
      {
        "id": "PT_1703",
        "name": "Savannah, GA"
      },
      {
        "id": "PT_3425",
        "name": "Pinecreek, MN"
      },
      {
        "id": "PT_3604",
        "name": "Inter. Falls, MN"
      },
      {
        "id": "PT_3414",
        "name": "Sherwood, ND"
      },
      {
        "id": "PT_5504",
        "name": "Oklahoma Cty, OK"
      },
      {
        "id": "PS_MT",
        "name": "Montana"
      },
      {
        "id": "PS_NY",
        "name": "New York"
      },
      {
        "id": "PS_VI",
        "name": "Virgin Islands"
      },
      {
        "id": "PS_GA",
        "name": "Georgia"
      },
      {
        "id": "PS_MD",
        "name": "Maryland"
      },
      {
        "id": "RF_4647",
        "name": "EXXON MOBIL REFG & SPLY COMP / BEAUMONT / TX"
      },
      {
        "id": "RF_3569",
        "name": "ENT BEAUMONT MARINE WEST LP / BEAUMONT RP WEST TERMINAL / TX"
      },
      {
        "id": "RF_3921",
        "name": "BUCKEYE TERMINALS LLC / RARITAN BAY / NJ"
      },
      {
        "id": "PT_0206",
        "name": "Beecherfalls, VT"
      },
      {
        "id": "PT_2102",
        "name": "Sabine, TX"
      },
      {
        "id": "PT_3906",
        "name": "O'Hare Int Ap, IL"
      },
      {
        "id": "PT_3808",
        "name": "Escanaba, MI"
      },
      {
        "id": "PT_4102",
        "name": "Cinci-Lawrnburg, OH"
      },
      {
        "id": "RF_3056",
        "name": "MONROE ENERGY LLC / PHILADELPHIA / PA"
      },
      {
        "id": "RF_2631",
        "name": "MARATHON PIPELINE LLC / HARTFORD / IL"
      },
      {
        "id": "RF_4830",
        "name": "MUSKET CORP / FORT WORTH ETHANOL TERMINAL / TX"
      },
      {
        "id": "RF_4547",
        "name": "CITGO PETROLEUM CORP / OAK PARK AVE TRUCK RACK / TX"
      },
      {
        "id": "RF_5161",
        "name": "FLINT HILLS RESOURCES LP / UMORE / MN"
      },
      {
        "id": "RF_329",
        "name": "US OIL & REFINING CO / TACOMA / WA"
      },
      {
        "id": "RF_2386",
        "name": "UNKNOWN PROCESSOR-NE / UNKNOWN PROCESSOR-NE / NE"
      },
      {
        "id": "RF_2389",
        "name": "UNKNOWN PROCESSOR-OK / UNKNOWN PROCESSOR-OK / OK"
      },
      {
        "id": "RF_163",
        "name": "EXXONMOBIL REFINING & SPLY CO / BAYTOWN / TX"
      },
      {
        "id": "RF_164",
        "name": "VALERO REFINING CO CALIFORNIA / BENICIA / CA"
      },
      {
        "id": "RF_2393",
        "name": "UNKNOWN PROCESSOR-AL / UNKNOWN PROCESSOR-AL / AL"
      },
      {
        "id": "RF_124",
        "name": "CHEVRON USA / SALT LAKE CITY / UT"
      },
      {
        "id": "RF_392",
        "name": "PHILLIPS 66 / LAKE CHARLES / LA"
      },
      {
        "id": "RF_480",
        "name": "NUSTAR ASPHALT REFINING LLC / SAVANNAH / GA"
      },
      {
        "id": "RF_517",
        "name": "VALERO REFG NEW ORLEANS LLC / SAINT CHARLES / LA"
      },
      {
        "id": "RF_314",
        "name": "TESORO ALASKA LLC / KENAI REFINERY / AK"
      },
      {
        "id": "RF_442",
        "name": "LION OIL CO / EL DORADO / AR"
      },
      {
        "id": "RF_2344",
        "name": "CHEVRON USA INC / BELLE CHASSE / LA"
      },
      {
        "id": "RF_497",
        "name": "HOLLY REFG & MKTG CO - TULSA LLC / TULSA / OK"
      },
      {
        "id": "RF_2380",
        "name": "UNKNOWN PROCESSOR-IA / UNKNOWN PROCESSOR-IA / IA"
      },
      {
        "id": "RF_97",
        "name": "TESORO REFINING & MARKETING / CARSON/WILMINGTON / CA"
      },
      {
        "id": "RF_538",
        "name": "HUNT SOUTHLAND REFINING CO LLC / ROGERSLACY / MS"
      },
      {
        "id": "RF_4784",
        "name": "EQUILON ENTERPRISES LLC / ST JAMES/SUGARLAND / LA"
      },
      {
        "id": "RF_78",
        "name": "HESS CORP / SEWAREN / NJ"
      },
      {
        "id": "RF_2661",
        "name": "BP PRODUCTS NORTH AMERICA / SEATTLE / WA"
      },
      {
        "id": "RF_2381",
        "name": "UNKNOWN PROCESSOR-KS / UNKNOWN PROCESSOR-KS / KS"
      },
      {
        "id": "RF_3959",
        "name": "PHILLIPS 66 CO / WESTLAKE / LA"
      },
      {
        "id": "RF_3571",
        "name": "VOPAK TERMINALS NORTH AMER INC / GP WEST CHEMICAL / TX"
      },
      {
        "id": "RF_230",
        "name": "EXXONMOBIL / HAMMOND TERMINAL / IN"
      },
      {
        "id": "RS_PA",
        "name": "Pennsylvania"
      },
      {
        "id": "RS_DE",
        "name": "Delaware"
      },
      {
        "id": "RS_MI",
        "name": "Michigan"
      },
      {
        "id": "PT_2010",
        "name": "Gramercy, LA"
      },
      {
        "id": "PT_5306",
        "name": "Texas City, TX"
      },
      {
        "id": "PT_2013",
        "name": "St Rose, LA"
      },
      {
        "id": "PT_1102",
        "name": "Chester, PA"
      },
      {
        "id": "PT_3401",
        "name": "Pembina, ND"
      },
      {
        "id": "PT_1108",
        "name": "Phil., PA"
      },
      {
        "id": "PT_3903",
        "name": "Omaha, NE"
      },
      {
        "id": "PT_3316",
        "name": "Piegan, MT"
      },
      {
        "id": "PS_VA",
        "name": "Virginia"
      },
      {
        "id": "PS_IL",
        "name": "Illinois"
      },
      {
        "id": "PS_OH",
        "name": "Ohio"
      },
      {
        "id": "PS_WI",
        "name": "Wisconsin"
      },
      {
        "id": "PS_HI",
        "name": "Hawaii"
      },
      {
        "id": "PT_5506",
        "name": "Austin, TX"
      },
      {
        "id": "PS_ID",
        "name": "Idaho"
      },
      {
        "id": "RF_4825",
        "name": "SUNOCO LOGISTICS / EAGLE POINT TANK FARM EPTF / NJ"
      },
      {
        "id": "PT_3820",
        "name": "Mackinac Isl, MI"
      },
      {
        "id": "RF_4960",
        "name": "ZENITH ENERGY TERMINALS HOLDINGS LLC / WILLBRIDGE / OR"
      },
      {
        "id": "RF_2924",
        "name": "PETRO-DIAMOND TERMINAL CO / LONG BEACH / CA"
      },
      {
        "id": "RF_4110",
        "name": "MOTIVA ENTERPRISES LLC / BEAUMONT BLENDING TERMINAL / TX"
      },
      {
        "id": "RF_386",
        "name": "DIAMOND SHAMROCK REFG CO LP / MCKEE REFINERY / TX"
      },
      {
        "id": "RS_MA",
        "name": "Massachusetts"
      },
      {
        "id": "RF_3962",
        "name": "PHILLIPS 66 CO - BILLINGS / BILLINGS MT / MT"
      },
      {
        "id": "RF_3237",
        "name": "ENTRPRS REFINED PRODTS CO LLC / NORTH HOUSTON RP TRUCK TERML / TX"
      },
      {
        "id": "RF_3770",
        "name": "CITGO PETROLEUM CORP / VICTORIA / TX"
      },
      {
        "id": "PT_2803",
        "name": "Fresno, CA"
      },
      {
        "id": "RF_3325",
        "name": "PAR HAWAII INC / KAMUELA / HI"
      },
      {
        "id": "PT_0715",
        "name": "Trout River, NY"
      },
      {
        "id": "RF_2665",
        "name": "TORRANCE LOGISTICS CO LLC / VERNON / CA"
      },
      {
        "id": "RF_2580",
        "name": "BUCKEYE TERMINALS LLC / LOUISVILLE / KY"
      },
      {
        "id": "RF_4015",
        "name": "ENERGY TRANSFER GC NGLS LLS / MONT BELVIEU / TX"
      },
      {
        "id": "RF_317",
        "name": "FRONTIER EL DORADO REFG LLC / EL DORADO / KS"
      },
      {
        "id": "RF_322",
        "name": "HOLLYFRONTIER PUGET SOUND REFNG LLC / PUGET SOUND / WA"
      },
      {
        "id": "RF_332",
        "name": "TESORO REFINING & MARKETING / GOLDEN EAGLE / CA"
      },
      {
        "id": "RF_307",
        "name": "PHILADELPHIA ENERGY SOLUTIONS / PHILADELPHIA / PA"
      },
      {
        "id": "RF_256",
        "name": "PHILLIPS 66 / SWEENY / TX"
      },
      {
        "id": "RF_115",
        "name": "CHS MCPHERSON REFINERY INC / MCPHERSON / KS"
      },
      {
        "id": "RF_502",
        "name": "VALERO REFINING CO TEXAS LP / HOUSTON REFINERY / TX"
      },
      {
        "id": "RF_503",
        "name": "VALERO REFINING CO TEXAS LP / TEXAS CITY / TX"
      },
      {
        "id": "RF_3238",
        "name": "LOOP LLC / METAIRIE / LA"
      },
      {
        "id": "RF_507",
        "name": "MOTIVA ENTERPRISES LLC / PORT ARTHUR / TX"
      },
      {
        "id": "RF_217",
        "name": "PREMCOR REFINING GROUP INC / MEMPHIS / TN"
      },
      {
        "id": "RF_257",
        "name": "HOLLYFRONTIER REFINING MKTG / WOODS CROSS / UT"
      },
      {
        "id": "RF_2383",
        "name": "UNKNOWN PROCESSOR-MI / UNKNOWN PROCESSOR-MI / MI"
      },
      {
        "id": "RF_2357",
        "name": "STRATEGIC PETROLEUM RESERVE / FREEPORT / TX"
      },
      {
        "id": "RF_2369",
        "name": "UNKNOWN PROCESSOR-NJ / UNKNOWN PROCESSOR-NJ / NJ"
      },
      {
        "id": "RF_202",
        "name": "KERN OIL & REFINING / BAKERSFIELD / CA"
      },
      {
        "id": "RF_501",
        "name": "ALON REFINING KROTZ SPGS INC / KROTZ SPRINGS / LA"
      },
      {
        "id": "RF_2521",
        "name": "OMEGA PARTNERS III LLC / HARTFORD / IL"
      },
      {
        "id": "RF_4967",
        "name": "GENESIS ENERGY LP / NATCHEZ / MS"
      },
      {
        "id": "RF_4291",
        "name": "UNITED REFINING CO / VULCAN / AL"
      },
      {
        "id": "RS_MS",
        "name": "Mississippi"
      },
      {
        "id": "RS_ND",
        "name": "North Dakota"
      },
      {
        "id": "RS_OH",
        "name": "Ohio"
      },
      {
        "id": "RS_OK",
        "name": "Oklahoma"
      },
      {
        "id": "RS_VI",
        "name": "Virgin Islands"
      },
      {
        "id": "RS_GA",
        "name": "Georgia"
      },
      {
        "id": "RS_VA",
        "name": "Virginia"
      },
      {
        "id": "RS_IA",
        "name": "Iowa"
      },
      {
        "id": "PT_4503",
        "name": "St Louis, MO"
      },
      {
        "id": "PT_5301",
        "name": "Houston, TX"
      },
      {
        "id": "PT_5505",
        "name": "Tulsa, OK"
      },
      {
        "id": "PT_2812",
        "name": "Richmond, CA"
      },
      {
        "id": "PT_3010",
        "name": "Anacortes, WA"
      },
      {
        "id": "PT_2104",
        "name": "Beaumont, TX"
      },
      {
        "id": "PT_1105",
        "name": "Paulsboro, NJ"
      },
      {
        "id": "PT_3307",
        "name": "Denver, CO"
      },
      {
        "id": "PT_5203",
        "name": "Pt Everglade, FL"
      },
      {
        "id": "PT_3417",
        "name": "Fortuna, ND"
      },
      {
        "id": "PS_DE",
        "name": "Delaware"
      },
      {
        "id": "PS_UT",
        "name": "Utah"
      },
      {
        "id": "PS_AZ",
        "name": "Arizona"
      },
      {
        "id": "PS_AR",
        "name": "Arkansas"
      },
      {
        "id": "PP_2",
        "name": "PADD2 (Midwest)"
      },
      {
        "id": "RF_2423",
        "name": "EXXONMOBIL PIPELINE CO / LOCKPORT TERMINAL / IL"
      },
      {
        "id": "RF_3024",
        "name": "BUCKEYE TERMINALS LLC / BALTIMORE / MD"
      },
      {
        "id": "RF_3953",
        "name": "UNITED REFINING CO / RIVERHEAD / NY"
      },
      {
        "id": "RF_99",
        "name": "CONOCOPHILLIPS CO / KUPARUK / AK"
      },
      {
        "id": "RF_408",
        "name": "KINDER MORGAN / CARTERET / NJ"
      },
      {
        "id": "PS_IN",
        "name": "Indiana"
      },
      {
        "id": "RF_4499",
        "name": "HOLLY ENERGY PARTNERS / CASPER / WY"
      },
      {
        "id": "RF_3593",
        "name": "VALERO MARKETING & SUPPLY CO / HOUSTON / TX"
      },
      {
        "id": "RF_2700",
        "name": "ANDEAVOR LOGISTICS LP / WILMINGTON / CA"
      },
      {
        "id": "RF_3304",
        "name": "BUCKEYE TERMINALS LLC / NAPOLEON / MI"
      },
      {
        "id": "RF_5258",
        "name": "EXXONMOBIL PIPELINE CO / SORRENTO DOME / LA"
      },
      {
        "id": "RF_2980",
        "name": "CHEVRON USA INC FORT WORTH / FORT WORTH TERMINAL / TX"
      },
      {
        "id": "RF_2392",
        "name": "UNKNOWN PROCESSOR-WI / UNKNOWN PROCESSOR-WI / WI"
      },
      {
        "id": "RF_3109",
        "name": "EXCEL PARALUBES / WESTLAKE / LA"
      },
      {
        "id": "RF_4414",
        "name": "MARATHON PETROLEUM CO LLC / GARYVILLE - ASPHALT / LA"
      },
      {
        "id": "RF_2560",
        "name": "MAGELLAN PIPELINE CO LP / DONIPHAN / NE"
      },
      {
        "id": "RF_4021",
        "name": "DEER PARK REFINING LP / DEER PARK / TX"
      },
      {
        "id": "PT_3001",
        "name": "Seattle, WA"
      },
      {
        "id": "RF_255",
        "name": "WRB REFINING LP / BORGER / TX"
      },
      {
        "id": "RF_333",
        "name": "PHILLIPS 66 CO / FERNDALE / WA"
      },
      {
        "id": "RF_335",
        "name": "PHILLIPS 66 CO / BAYWAY / NJ"
      },
      {
        "id": "RF_387",
        "name": "VALERO ENERGY CORP / THREE RIVERS / TX"
      },
      {
        "id": "RF_391",
        "name": "SUNCOR ENERGY USA INC / COMMERCE CITY REFY - WEST PLNT / CO"
      },
      {
        "id": "RF_444",
        "name": "HOUSTON REFINING LP / HOUSTON / TX"
      },
      {
        "id": "RF_323",
        "name": "TESORO REFINING & MARKETING / WILMINGTON - LOS ANGELES / CA"
      },
      {
        "id": "RF_465",
        "name": "CITGO PETROLEUM CORP / LAKE CHARLES REFINERY / LA"
      },
      {
        "id": "RF_89",
        "name": "MARATHON PETROLEUM CO LP / CANTON / OH"
      },
      {
        "id": "RF_162",
        "name": "PAR MONTANA LLC / BILLINGS REFINERY / MT"
      },
      {
        "id": "RF_168",
        "name": "CVR REFINING CVL LLC / COFFEYVILLE / KS"
      },
      {
        "id": "RF_206",
        "name": "SHELL CHEMICAL LP / MOBILE / AL"
      },
      {
        "id": "RF_2385",
        "name": "UNKNOWN PROCESSOR-MO / UNKNOWN PROCESSOR-MO / MO"
      },
      {
        "id": "RF_2401",
        "name": "UNKNOWN PROCESSOR-MT / UNKNOWN PROCESSOR-MT / MT"
      },
      {
        "id": "RF_458",
        "name": "PARAMOUNT PETROLEUM CORP / PARAMOUNT / CA"
      },
      {
        "id": "RF_4622",
        "name": "STRATEGIC PETROLEUM RESERVE / LAKE CHARLES METER STATION / LA"
      },
      {
        "id": "RF_185",
        "name": "NAVAJO REFINING CO / ARTESIA / NM"
      },
      {
        "id": "RF_342",
        "name": "PHILLIPS 66 CO / SAN FRANCISCO / CA"
      },
      {
        "id": "RF_2349",
        "name": "KOCH REFINING CO / KOCH / LA"
      },
      {
        "id": "RF_3854",
        "name": "TARGA SOUND TERMINAL / SOUND / WA"
      },
      {
        "id": "RF_2541",
        "name": "BP PLC / CUSHING / OK"
      },
      {
        "id": "RF_2391",
        "name": "UNKNOWN PROCESSOR-TN / UNKNOWN PROCESSOR-TN / TN"
      },
      {
        "id": "RF_3780",
        "name": "NATIONAL COOP REFINERY ASSOC / NCRA / IA"
      },
      {
        "id": "RF_4952",
        "name": "VOPAK TERMINALS NORTH AMER INC / GALENA PARK / TX"
      },
      {
        "id": "RS_CA",
        "name": "California"
      },
      {
        "id": "RS_NM",
        "name": "New Mexico"
      },
      {
        "id": "RS_WI",
        "name": "Wisconsin"
      },
      {
        "id": "RS_CO",
        "name": "Colorado"
      },
      {
        "id": "RP_2",
        "name": "PADD2 (Midwest)"
      },
      {
        "id": "RP_4",
        "name": "PADD4 (Rocky Mountain)"
      },
      {
        "id": "PT_2704",
        "name": "Los Angeles, CA"
      },
      {
        "id": "PT_3901",
        "name": "Chicago, IL"
      },
      {
        "id": "PT_1004",
        "name": "Perth Amboy, NJ"
      },
      {
        "id": "PS_CA",
        "name": "California"
      },
      {
        "id": "PS_MS",
        "name": "Mississippi"
      },
      {
        "id": "PS_WA",
        "name": "Washington"
      },
      {
        "id": "PS_MI",
        "name": "Michigan"
      },
      {
        "id": "PS_FL",
        "name": "Florida"
      },
      {
        "id": "PT_1816",
        "name": "Pt Canaveral, FL"
      },
      {
        "id": "RF_4867",
        "name": "BUCKEYE TEXAS HUB LLC / CORPUS CHRISTI / TX"
      },
      {
        "id": "RF_3894",
        "name": "NUSTAR ENERGY LP / TEXAS CITY T-76-TX-2796 / TX"
      },
      {
        "id": "PS_MA",
        "name": "Massachusetts"
      },
      {
        "id": "RF_3851",
        "name": "KINDER MORGAN LIQ TERMLS LLC / STATEN ISLAND / NY"
      },
      {
        "id": "RF_262",
        "name": "PLACID REFINING CO LLC / PORT ALLEN / LA"
      },
      {
        "id": "RF_4998",
        "name": "KINDER MORGAN CRUDE & CONDENSATE / GALENA PARK / TX"
      },
      {
        "id": "PS_VT",
        "name": "Vermont"
      },
      {
        "id": "RF_3215",
        "name": "EQUISTAR CHEMICALS LP / EQUISTAR CVO NORTH PLANT / TX"
      },
      {
        "id": "RF_4663",
        "name": "SUNOCO LOGISTICS / HEBERT / TX"
      },
      {
        "id": "RF_3043",
        "name": "PBF LOGISTICS PRODUCTS TERMINALS LLC / PAULSBORO / NJ"
      },
      {
        "id": "RF_3071",
        "name": "ADJ CO-LA GULF / IMPUTE ADJ - LA GULF / LA"
      },
      {
        "id": "RF_4907",
        "name": "SUNOCO LOGISTICS / MARCUS HOOK / PA"
      },
      {
        "id": "RF_4834",
        "name": "ZENITH ENERGY TERMINALS HOLDINGS LLC / CHICKASAW / AL"
      },
      {
        "id": "RF_205",
        "name": "FLINT HILLS RESOURCES LP / EAST PLANT / TX"
      },
      {
        "id": "RF_2660",
        "name": "ANDEAVOR LOGISTICS LP / CARSON / CA"
      },
      {
        "id": "RF_240",
        "name": "NUSTAR ENERGY LP / NORTHVILLE LINDEN / NJ"
      },
      {
        "id": "RF_3766",
        "name": "ERGON REFINING INC / VICKSBURG / MS"
      },
      {
        "id": "RF_4033",
        "name": "PAR MONTANA LLC / BILLINGS / MT"
      },
      {
        "id": "RF_4011",
        "name": "CHEVRON USA INC PASCAGOULA / PASCAGOULA MS / MS"
      },
      {
        "id": "RF_4304",
        "name": "BUCKEYE TERMINALS LLC / PORT WILMINGTON / DE"
      },
      {
        "id": "RF_2772",
        "name": "CHEVRON USA INC RICHMOND / RICHMOND CA TERMINAL / CA"
      },
      {
        "id": "RF_4408",
        "name": "MARATHON PETROLEUM CO LLC / DETROIT - ASPHALT / MI"
      },
      {
        "id": "RF_382",
        "name": "CROSS OIL REFINING & MKTG INC / CROSS OIL REFINING & MKTG INC / AR"
      },
      {
        "id": "RF_227",
        "name": "EXXONMOBIL REFINING & SPLY CO / JOLIET / IL"
      },
      {
        "id": "RF_275",
        "name": "WRB REFINING LLC / WOOD RIVER / IL"
      },
      {
        "id": "RF_287",
        "name": "OHIO REFINING CO LLC / TOLEDO / OH"
      },
      {
        "id": "RF_297",
        "name": "BP PRODUCTS NORTH AMERICA / WHITING REFINERY / IN"
      },
      {
        "id": "RF_302",
        "name": "TESORO REFINING & MARKETING / SALT LAKE CITY / UT"
      },
      {
        "id": "RF_403",
        "name": "FRONTIER REFINING LLC / CHEYENNE / WY"
      },
      {
        "id": "RF_2540",
        "name": "SUN TERMINAL / SUN / TX"
      },
      {
        "id": "RF_4643",
        "name": "SHELL OIL PRODUCTS US / LOCKPORT / IL"
      },
      {
        "id": "RF_161",
        "name": "EXXONMOBIL REFINING & SUPPLY / BATON ROUGE REFINERY / LA"
      },
      {
        "id": "RF_191",
        "name": "VALERO REFINING CO CALIFORNIA / WILMINGTON ASPHALT PLANT / CA"
      },
      {
        "id": "RF_301",
        "name": "MARATHON PETROLEUM CO LP / GALVESTON BAY / TX"
      },
      {
        "id": "RF_204",
        "name": "FLINT HILLS RESOURCES LP / WEST / TX"
      },
      {
        "id": "RF_4538",
        "name": "TEPPCO TERMINAL & MKTG CO LLC / HOUSTON / TX"
      },
      {
        "id": "RF_4624",
        "name": "STRATEGIC PETROLEUM RESERVE / SUNTMNL / TX"
      },
      {
        "id": "RF_4548",
        "name": "SEMCRUDE LP / CUSHING / OK"
      },
      {
        "id": "RF_190",
        "name": "HUNT REFINING CO / TUSCALOOSA / AL"
      },
      {
        "id": "RF_237",
        "name": "VALERO REFINING - MERAUX LLC / MERAUX REFINERY / LA"
      },
      {
        "id": "RF_2410",
        "name": "UNKNOWN PROCESSOR-WA / UNKNOWN PROCESSOR-WA / WA"
      },
      {
        "id": "RF_2351",
        "name": "SHELL OIL CO / DEER PARK / TX"
      },
      {
        "id": "RF_2399",
        "name": "UNKNOWN PROCESSOR-CO / UNKNOWN PROCESSOR-CO / CO"
      },
      {
        "id": "RF_4072",
        "name": "PHILLIPS 66 GULF COAST PROPERTIES LL / BEAUMONT TERMINAL / TX"
      },
      {
        "id": "RF_2927",
        "name": "MOTIVA ENTERPRISES LLC / SEWAREN BLENDING TERMINAL / NJ"
      },
      {
        "id": "RF_3138",
        "name": "IMTT / ST ROSE / LA"
      },
      {
        "id": "RF_3265",
        "name": "MURPHY OIL USA INC / SUPERIOR / WI"
      },
      {
        "id": "RF_340",
        "name": "SUNCOR ENERGY USA INC / COMMERCE CITY EAST / CO"
      },
      {
        "id": "RF_4835",
        "name": "ARC TERMINALS HOLDINGS LLC / BLAKELEY / AL"
      },
      {
        "id": "RF_3596",
        "name": "INTL MATEX TANK TERMINALS / ST ROSE / LA"
      },
      {
        "id": "RF_4546",
        "name": "CITGO PETROLEUM CORP / PORT AVE TRUCK RACK / TX"
      },
      {
        "id": "RF_2363",
        "name": "UNKNOWN PROCESSOR-FL / UNKNOWN PROCESSOR-FL / FL"
      },
      {
        "id": "RF_153",
        "name": "NUSTAR REFINING LLC / SAN ANTONIO / TX"
      },
      {
        "id": "RF_2370",
        "name": "UNKNOWN PROCESSOR-NY / UNKNOWN PROCESSOR-NY / NY"
      },
      {
        "id": "RF_4966",
        "name": "MERCURIA ENERGY TRADING / GREEN PORT / TX"
      },
      {
        "id": "RF_2409",
        "name": "UNKNOWN PROCESSOR-OR / UNKNOWN PROCESSOR-OR / OR"
      },
      {
        "id": "RF_438",
        "name": "IMTT / BAYONNE / NJ"
      },
      {
        "id": "RF_4971",
        "name": "NUSTAR ENERGY LP / TEXAS CITY / TX"
      },
      {
        "id": "RF_2599",
        "name": "BP PRODUCTS NORTH AMERICA / WHITING / IN"
      },
      {
        "id": "RS_NJ",
        "name": "New Jersey"
      },
      {
        "id": "RS_WA",
        "name": "Washington"
      },
      {
        "id": "RS_AL",
        "name": "Alabama"
      },
      {
        "id": "RS_KS",
        "name": "Kansas"
      },
      {
        "id": "RS_AK",
        "name": "Alaska"
      },
      {
        "id": "PT_2830",
        "name": "Carquinez St, CA"
      },
      {
        "id": "PT_1901",
        "name": "Mobile, AL"
      },
      {
        "id": "PT_2709",
        "name": "Long Beach, CA"
      },
      {
        "id": "PT_3126",
        "name": "Anchorage, AK"
      },
      {
        "id": "PT_3310",
        "name": "Sweetgrass, MT"
      },
      {
        "id": "PT_3608",
        "name": "Superior, WI"
      },
      {
        "id": "PT_2305",
        "name": "Hidalgo, TX"
      },
      {
        "id": "PT_3301",
        "name": "Raymond, MT"
      },
      {
        "id": "PT_3004",
        "name": "Blaine, WA"
      },
      {
        "id": "PT_2604",
        "name": "Nogales, AZ"
      },
      {
        "id": "PT_3006",
        "name": "Everett, WA"
      },
      {
        "id": "PS_CO",
        "name": "Colorado"
      },
      {
        "id": "PT_2003",
        "name": "Little Rock, AR"
      },
      {
        "id": "PS_AK",
        "name": "Alaska"
      },
      {
        "id": "PT_3309",
        "name": "Scobey, MT"
      },
      {
        "id": "PT_3306",
        "name": "Turner, MT"
      },
      {
        "id": "PS_MO",
        "name": "Missouri"
      },
      {
        "id": "PS_KY",
        "name": "Kentucky"
      },
      {
        "id": "PS_NE",
        "name": "Nebraska"
      },
      {
        "id": "PP_4",
        "name": "PADD4 (Rocky Mountain)"
      },
      {
        "id": "RF_4963",
        "name": "GATEWAY TERMINALS LLC / SAUGET / IL"
      },
      {
        "id": "RF_4933",
        "name": "BUCKEYE TERMINALS LLC / PORT READING / NJ"
      },
      {
        "id": "RF_4008",
        "name": "CHEVRON USA INC ARCADIA / ARCADIA TERMINAL / LA"
      },
      {
        "id": "PT_3904",
        "name": "East Chicago, IN"
      },
      {
        "id": "PT_3410",
        "name": "Ambrose, ND"
      },
      {
        "id": "RF_5107",
        "name": "CPI OPERATIONS LLC / CPI OPERATIONS LLC / NJ"
      },
      {
        "id": "RF_4790",
        "name": "ENTRPRS REFINED PRODTS CO LLC / PORT ARTHUR RP STORAGE TERML / TX"
      },
      {
        "id": "PT_3003",
        "name": "Aberdn-Hoqua, WA"
      },
      {
        "id": "PT_3101",
        "name": "Juneau, AK"
      },
      {
        "id": "PT_2712",
        "name": "Ventura, CA"
      },
      {
        "id": "RF_2990",
        "name": "EXXONMOBIL CORP / NORTH HOUSTON / TX"
      },
      {
        "id": "RF_499",
        "name": "SINCLAIR CASPER REFINING CO / CASPER / WY"
      },
      {
        "id": "RF_3688",
        "name": "PLAINS LPG SERVICES LP / RANCHO SAN PEDRO TERMINAL / CA"
      },
      {
        "id": "RF_225",
        "name": "EXXONMOBIL REFINING & SPLY CO / BEAUMONT / TX"
      },
      {
        "id": "RF_238",
        "name": "SUPERIOR REFINING CO LLC / SUPERIOR / WI"
      },
      {
        "id": "RF_336",
        "name": "MONROE ENERGY LLC / TRAINER / PA"
      },
      {
        "id": "RF_393",
        "name": "PHILLIPS 66 / BILLINGS REFINERY / MT"
      },
      {
        "id": "RF_478",
        "name": "CITGO REFINING & CHEMICAL INC / CORPUS CHRISTI / TX"
      },
      {
        "id": "RF_496",
        "name": "SINCLAIR WYOMING REFINING CO / RAWLINS / WY"
      },
      {
        "id": "RF_2378",
        "name": "UNKNOWN PROCESSOR-IL / UNKNOWN PROCESSOR-IL / IL"
      },
      {
        "id": "RF_279",
        "name": "MARTINEZ REFINING CO LLC / MARTINEZ / CA"
      },
      {
        "id": "RF_343",
        "name": "PHILLIPS 66 / LOS ANGELES / CA"
      },
      {
        "id": "RF_120",
        "name": "CHEVRON USA / RICHMOND / CA"
      },
      {
        "id": "RF_351",
        "name": "VALERO REFINING CO TEXAS LP / CORPUS CHRISTI / TX"
      },
      {
        "id": "RF_116",
        "name": "CHS INC / LAUREL / MT"
      },
      {
        "id": "RF_454",
        "name": "BTB REFINING LLC / CORPUS CHRISTI / TX"
      },
      {
        "id": "RF_2384",
        "name": "UNKNOWN PROCESSOR-MN / UNKNOWN PROCESSOR-MN / MN"
      },
      {
        "id": "RF_2400",
        "name": "UNKNOWN PROCESSOR-ID / UNKNOWN PROCESSOR-ID / ID"
      },
      {
        "id": "RF_226",
        "name": "TORRANCE REFINING CO LLC / TORRANCE REFINERY / CA"
      },
      {
        "id": "RF_309",
        "name": "HOLLYFRONTIER TULSA REFINERY LLC TWP / TULSA WEST PLANT / OK"
      },
      {
        "id": "RF_2366",
        "name": "UNKNOWN PROCESSOR-MD / UNKNOWN PROCESSOR-MD / MD"
      },
      {
        "id": "RF_3969",
        "name": "ENT HOUSTON SHIP CHANNEL LP / HSC REFINED TERMINAL / TX"
      },
      {
        "id": "RF_3279",
        "name": "PHILLIPS 66 CO / KAY / OK"
      },
      {
        "id": "RF_2361",
        "name": "UNKNOWN PROCESSOR-DE / UNKNOWN PROCESSOR-DE / DE"
      },
      {
        "id": "RF_3723",
        "name": "HOUSTON FUEL OIL TERMINAL CO / HOUSTON / TX"
      },
      {
        "id": "RF_4500",
        "name": "INTERCONTINENTAL TERMINALS CO / DEER PARK / TX"
      },
      {
        "id": "RS_HI",
        "name": "Hawaii"
      },
      {
        "id": "RS_KY",
        "name": "Kentucky"
      },
      {
        "id": "RS_UT",
        "name": "Utah"
      },
      {
        "id": "RS_NE",
        "name": "Nebraska"
      },
      {
        "id": "RS_TN",
        "name": "Tennessee"
      },
      {
        "id": "RS_OR",
        "name": "Oregon"
      },
      {
        "id": "RP_3",
        "name": "PADD3 (Gulf Coast)"
      },
      {
        "id": "PT_2017",
        "name": "Lake Charles, LA"
      },
      {
        "id": "PT_2711",
        "name": "El Segundo, CA"
      },
      {
        "id": "PT_3404",
        "name": "Neche, ND"
      },
      {
        "id": "PT_3802",
        "name": "Port Huron, MI"
      },
      {
        "id": "PT_1303",
        "name": "Baltimore, MD"
      },
      {
        "id": "PT_3302",
        "name": "Eastport, ID"
      },
      {
        "id": "PT_0712",
        "name": "Champl-Rs Pt, NY"
      },
      {
        "id": "PT_1002",
        "name": "Albany, NY"
      },
      {
        "id": "PS_AL",
        "name": "Alabama"
      },
      {
        "id": "PT_4116",
        "name": "Port Of Entry-Owensboro, KY"
      },
      {
        "id": "PT_2014",
        "name": "Good Hope, LA"
      },
      {
        "id": "PT_2015",
        "name": "Vicksburg, MS"
      },
      {
        "id": "PT_3801",
        "name": "Detroit, MI"
      },
      {
        "id": "PS_OK",
        "name": "Oklahoma"
      },
      {
        "id": "PP_5",
        "name": "PADD5 (West Coast)"
      },
      {
        "id": "RF_3876",
        "name": "NUSTAR ENERGY LP / LINDEN / NJ"
      },
      {
        "id": "RF_498",
        "name": "SINCLAIR OIL CORP / DENVER / CO"
      },
      {
        "id": "RF_2341",
        "name": "AMERADA HESS CORP / NEW YORK / NY"
      },
      {
        "id": "PT_0401",
        "name": "Boston, MA"
      },
      {
        "id": "RF_2983",
        "name": "NUSTAR ENERGY LP / PAULSBORO / NJ"
      },
      {
        "id": "RF_353",
        "name": "AMERICAN REFINING GROUP INC / BRADFORD / PA"
      },
      {
        "id": "RF_4917",
        "name": "WESTERN REFINING SOUTHWEST INC / BLOOMFIELD / NM"
      },
      {
        "id": "RF_3915",
        "name": "BUCKEYE TERMINALS LLC / BAYONNE / NJ"
      },
      {
        "id": "RF_2989",
        "name": "EXXONMOBIL PL CO / SOUTH HOUSTON / TX"
      },
      {
        "id": "RF_5126",
        "name": "DELAWARE RIVER PARTNERS LLC / REPAUNO PORT & RAIL TERMINAL / NJ"
      },
      {
        "id": "RF_5125",
        "name": "JEFFERSON GULF COAST ENERGY PARTNERS / JEFFERSON ENERGY TERMINAL / TX"
      },
      {
        "id": "RF_4666",
        "name": "SINCLAIR OIL CORP / SINCLAIR / WY"
      },
      {
        "id": "RF_5083",
        "name": "ENTRPRS REFINED PRODTS CO LLC / BEAUMONT MARINE RP EAST TERML / TX"
      },
      {
        "id": "PT_3907",
        "name": "Des Moines, IA"
      },
      {
        "id": "PT_2811",
        "name": "Oakland, CA"
      },
      {
        "id": "RF_3756",
        "name": "FLINT HILL RESOURCES LP / ST PAUL / MN"
      },
      {
        "id": "RF_5354",
        "name": "OCEAN POINT TERMINAL / KINGSHILL / VI"
      },
      {
        "id": "RF_4005",
        "name": "CHEVRON USA INC EL SEGUNDO / EL SEGUNDO CA / CA"
      }
    ]
  },
  "request": {
    "command": "/v2/crude-oil-imports/facet/destinationId/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
  "response": {
    "totalFacets": 7,
    "facets": [
      {
        "id": "PS",
        "name": "Port State"
      },
      {
        "id": "US",
        "name": "United States"
      },
      {
        "id": "RP",
        "name": "Refinery PADD"
      },
      {
        "id": "PP",
        "name": "Port PADD"
      },
      {
        "id": "RS",
        "name": "Refinery State"
      },
      {
        "id": "PT",
        "name": "Port"
      },
      {
        "id": "RF",
        "name": "Refinery"
      }
    ]
  },
  "request": {
    "command": "/v2/crude-oil-imports/facet/destinationType/",
    "params": {
      "api_key": "MOCK_API_KEY"
    }
  },
  "apiVersion": "2.1.8",
  "ExcelAddInVersion": "2.1.0"
}
```

```json
{
    "response": {
        "totalFacets": 5,
        "facets": [
            {
                "id": "HSW",
                "name": "Heavy Sweet"
            },
            {
                "id": "MED",
                "name": "Medium"
            },
            {
                "id": "HSO",
                "name": "Heavy Sour"
            },
            {
                "id": "LSO",
                "name": "Light Sour"
            },
            {
                "id": "LSW",
                "name": "Light Sweet"
            }
        ]
    },
    "request": {
        "command": "/v2/crude-oil-imports/facet/gradeId/",
        "params": {
            "api_key": "MOCK_API_KEY"
        }
    },
    "apiVersion": "2.1.8",
    "ExcelAddInVersion": "2.1.0"
}
```
