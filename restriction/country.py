from .restriction import GeneralRestriction


class Country(GeneralRestriction):
    """Filter result by country"""
    pass


Country.ANY = Country()

# Afghanistan
Country.AF = Country.AFG = Country.Afghanistan = Country('AFG')
# Åland Islands
Country.AX = Country.ALA = Country.AlandIslands = Country('ALA')
# Albania
Country.AL = Country.ALB = Country.Albania = Country('ALB')
# Algeria
Country.DZ = Country.DZA = Country.Algeria = Country('DZA')
# American Samoa
Country.AS = Country.ASM = Country.AmericanSamoa = Country('ASM')
# Andorra
Country.AD = Country.AND = Country.Andorra = Country('AND')
# Angola
Country.AO = Country.AGO = Country.Angola = Country('AGO')
# Anguilla
Country.AI = Country.AIA = Country.Anguilla = Country('AIA')
# Antarctica
Country.AQ = Country.ATA = Country.Antarctica = Country('ATA')
# Antigua and Barbuda
Country.AG = Country.ATG = Country.AntiguaAndBarbuda = Country('ATG')
# Argentina
Country.AR = Country.ARG = Country.Argentina = Country('ARG')
# Armenia
Country.AM = Country.ARM = Country.Armenia = Country('ARM')
# Aruba
Country.AW = Country.ABW = Country.Aruba = Country('ABW')
# Australia
Country.AU = Country.AUS = Country.Australia = Country('AUS')
# Austria
Country.AT = Country.AUT = Country.Austria = Country('AUT')
# Azerbaijan
Country.AZ = Country.AZE = Country.Azerbaijan = Country('AZE')
# Bahamas
Country.BS = Country.BHS = Country.Bahamas = Country('BHS')
# Bahrain
Country.BH = Country.BHR = Country.Bahrain = Country('BHR')
# Bangladesh
Country.BD = Country.BGD = Country.Bangladesh = Country('BGD')
# Barbados
Country.BB = Country.BRB = Country.Barbados = Country('BRB')
# Belarus
Country.BY = Country.BLR = Country.Belarus = Country('BLR')
# Belgium
Country.BE = Country.BEL = Country.Belgium = Country('BEL')
# Belize
Country.BZ = Country.BLZ = Country.Belize = Country('BLZ')
# Benin
Country.BJ = Country.BEN = Country.Benin = Country('BEN')
# Bermuda
Country.BM = Country.BMU = Country.Bermuda = Country('BMU')
# Bhutan
Country.BT = Country.BTN = Country.Bhutan = Country('BTN')
# Bolivia (Plurinational State of)
Country.BO = Country.BOL = Country.BoliviaPlurinationalStateOf = Country('BOL')
# Bonaire, Sint Eustatius and Saba
Country.BQ = Country.BES = Country.BonaireSintEustatiusAndSaba = Country('BES')
# Bosnia and Herzegovina
Country.BA = Country.BIH = Country.BosniaAndHerzegovina = Country('BIH')
# Botswana
Country.BW = Country.BWA = Country.Botswana = Country('BWA')
# Bouvet Island
Country.BV = Country.BVT = Country.BouvetIsland = Country('BVT')
# Brazil
Country.BR = Country.BRA = Country.Brazil = Country('BRA')
# British Indian Ocean Territory
Country.IO = Country.IOT = Country.BritishIndianOceanTerritory = Country('IOT')
# Brunei Darussalam
Country.BN = Country.BRN = Country.BruneiDarussalam = Country('BRN')
# Bulgaria
Country.BG = Country.BGR = Country.Bulgaria = Country('BGR')
# Burkina Faso
Country.BF = Country.BFA = Country.BurkinaFaso = Country('BFA')
# Burundi
Country.BI = Country.BDI = Country.Burundi = Country('BDI')
# Cabo Verde
Country.CV = Country.CPV = Country.CaboVerde = Country('CPV')
# Cambodia
Country.KH = Country.KHM = Country.Cambodia = Country('KHM')
# Cameroon
Country.CM = Country.CMR = Country.Cameroon = Country('CMR')
# Canada
Country.CA = Country.CAN = Country.Canada = Country('CAN')
# Cayman Islands
Country.KY = Country.CYM = Country.CaymanIslands = Country('CYM')
# Central African Republic
Country.CF = Country.CAF = Country.CentralAfricanRepublic = Country('CAF')
# Chad
Country.TD = Country.TCD = Country.Chad = Country('TCD')
# Chile
Country.CL = Country.CHL = Country.Chile = Country('CHL')
# China
Country.CN = Country.CHN = Country.China = Country('CHN')
# Christmas Island
Country.CX = Country.CXR = Country.ChristmasIsland = Country('CXR')
# Cocos (Keeling) Islands
Country.CC = Country.CCK = Country.CocosKeelingIslands = Country('CCK')
# Colombia
Country.CO = Country.COL = Country.Colombia = Country('COL')
# Comoros
Country.KM = Country.COM = Country.Comoros = Country('COM')
# Congo
Country.CG = Country.COG = Country.Congo = Country('COG')
# Congo, Democratic Republic of the
Country.CD = Country.COD = Country.CongoDemocraticRepublicOfThe = Country('COD')
# Cook Islands
Country.CK = Country.COK = Country.CookIslands = Country('COK')
# Costa Rica
Country.CR = Country.CRI = Country.CostaRica = Country('CRI')
# Côte d'Ivoire
Country.CI = Country.CIV = Country.CoteDIvoire = Country('CIV')
# Croatia
Country.HR = Country.HRV = Country.Croatia = Country('HRV')
# Cuba
Country.CU = Country.CUB = Country.Cuba = Country('CUB')
# Curaçao
Country.CW = Country.CUW = Country.Curacao = Country('CUW')
# Cyprus
Country.CY = Country.CYP = Country.Cyprus = Country('CYP')
# Czechia
Country.CZ = Country.CZE = Country.Czechia = Country('CZE')
# Denmark
Country.DK = Country.DNK = Country.Denmark = Country('DNK')
# Djibouti
Country.DJ = Country.DJI = Country.Djibouti = Country('DJI')
# Dominica
Country.DM = Country.DMA = Country.Dominica = Country('DMA')
# Dominican Republic
Country.DO = Country.DOM = Country.DominicanRepublic = Country('DOM')
# Ecuador
Country.EC = Country.ECU = Country.Ecuador = Country('ECU')
# Egypt
Country.EG = Country.EGY = Country.Egypt = Country('EGY')
# El Salvador
Country.SV = Country.SLV = Country.ElSalvador = Country('SLV')
# Equatorial Guinea
Country.GQ = Country.GNQ = Country.EquatorialGuinea = Country('GNQ')
# Eritrea
Country.ER = Country.ERI = Country.Eritrea = Country('ERI')
# Estonia
Country.EE = Country.EST = Country.Estonia = Country('EST')
# Eswatini
Country.SZ = Country.SWZ = Country.Eswatini = Country('SWZ')
# Ethiopia
Country.ET = Country.ETH = Country.Ethiopia = Country('ETH')
# Falkland Islands (Malvinas)
Country.FK = Country.FLK = Country.FalklandIslandsMalvinas = Country('FLK')
# Faroe Islands
Country.FO = Country.FRO = Country.FaroeIslands = Country('FRO')
# Fiji
Country.FJ = Country.FJI = Country.Fiji = Country('FJI')
# Finland
Country.FI = Country.FIN = Country.Finland = Country('FIN')
# France
Country.FR = Country.FRA = Country.France = Country('FRA')
# French Guiana
Country.GF = Country.GUF = Country.FrenchGuiana = Country('GUF')
# French Polynesia
Country.PF = Country.PYF = Country.FrenchPolynesia = Country('PYF')
# French Southern Territories
Country.TF = Country.ATF = Country.FrenchSouthernTerritories = Country('ATF')
# Gabon
Country.GA = Country.GAB = Country.Gabon = Country('GAB')
# Gambia
Country.GM = Country.GMB = Country.Gambia = Country('GMB')
# Georgia
Country.GE = Country.GEO = Country.Georgia = Country('GEO')
# Germany
Country.DE = Country.DEU = Country.Germany = Country('DEU')
# Ghana
Country.GH = Country.GHA = Country.Ghana = Country('GHA')
# Gibraltar
Country.GI = Country.GIB = Country.Gibraltar = Country('GIB')
# Greece
Country.GR = Country.GRC = Country.Greece = Country('GRC')
# Greenland
Country.GL = Country.GRL = Country.Greenland = Country('GRL')
# Grenada
Country.GD = Country.GRD = Country.Grenada = Country('GRD')
# Guadeloupe
Country.GP = Country.GLP = Country.Guadeloupe = Country('GLP')
# Guam
Country.GU = Country.GUM = Country.Guam = Country('GUM')
# Guatemala
Country.GT = Country.GTM = Country.Guatemala = Country('GTM')
# Guernsey
Country.GG = Country.GGY = Country.Guernsey = Country('GGY')
# Guinea
Country.GN = Country.GIN = Country.Guinea = Country('GIN')
# Guinea-Bissau
Country.GW = Country.GNB = Country.GuineaBissau = Country('GNB')
# Guyana
Country.GY = Country.GUY = Country.Guyana = Country('GUY')
# Haiti
Country.HT = Country.HTI = Country.Haiti = Country('HTI')
# Heard Island and McDonald Islands
Country.HM = Country.HMD = Country.HeardIslandAndMcDonaldIslands = Country('HMD')
# Holy See
Country.VA = Country.VAT = Country.HolySee = Country('VAT')
# Honduras
Country.HN = Country.HND = Country.Honduras = Country('HND')
# Hong Kong
Country.HK = Country.HKG = Country.HongKong = Country('HKG')
# Hungary
Country.HU = Country.HUN = Country.Hungary = Country('HUN')
# Iceland
Country.IS = Country.ISL = Country.Iceland = Country('ISL')
# India
Country.IN = Country.IND = Country.India = Country('IND')
# Indonesia
Country.ID = Country.IDN = Country.Indonesia = Country('IDN')
# Iran (Islamic Republic of)
Country.IR = Country.IRN = Country.IranIslamicRepublicOf = Country('IRN')
# Iraq
Country.IQ = Country.IRQ = Country.Iraq = Country('IRQ')
# Ireland
Country.IE = Country.IRL = Country.Ireland = Country('IRL')
# Isle of Man
Country.IM = Country.IMN = Country.IsleOfMan = Country('IMN')
# Israel
Country.IL = Country.ISR = Country.Israel = Country('ISR')
# Italy
Country.IT = Country.ITA = Country.Italy = Country('ITA')
# Jamaica
Country.JM = Country.JAM = Country.Jamaica = Country('JAM')
# Japan
Country.JP = Country.JPN = Country.Japan = Country('JPN')
# Jersey
Country.JE = Country.JEY = Country.Jersey = Country('JEY')
# Jordan
Country.JO = Country.JOR = Country.Jordan = Country('JOR')
# Kazakhstan
Country.KZ = Country.KAZ = Country.Kazakhstan = Country('KAZ')
# Kenya
Country.KE = Country.KEN = Country.Kenya = Country('KEN')
# Kiribati
Country.KI = Country.KIR = Country.Kiribati = Country('KIR')
# Korea (Democratic People's Republic of)
Country.KP = Country.PRK = Country.KoreaDemocraticPeoplesRepublicOf = Country('PRK')
# Korea, Republic of
Country.KR = Country.KOR = Country.KoreaRepublicOf = Country('KOR')
# Kuwait
Country.KW = Country.KWT = Country.Kuwait = Country('KWT')
# Kyrgyzstan
Country.KG = Country.KGZ = Country.Kyrgyzstan = Country('KGZ')
# Lao People's Democratic Republic
Country.LA = Country.LAO = Country.LaoPeoplesDemocraticRepublic = Country('LAO')
# Latvia
Country.LV = Country.LVA = Country.Latvia = Country('LVA')
# Lebanon
Country.LB = Country.LBN = Country.Lebanon = Country('LBN')
# Lesotho
Country.LS = Country.LSO = Country.Lesotho = Country('LSO')
# Liberia
Country.LR = Country.LBR = Country.Liberia = Country('LBR')
# Libya
Country.LY = Country.LBY = Country.Libya = Country('LBY')
# Liechtenstein
Country.LI = Country.LIE = Country.Liechtenstein = Country('LIE')
# Lithuania
Country.LT = Country.LTU = Country.Lithuania = Country('LTU')
# Luxembourg
Country.LU = Country.LUX = Country.Luxembourg = Country('LUX')
# Macao
Country.MO = Country.MAC = Country.Macao = Country('MAC')
# Madagascar
Country.MG = Country.MDG = Country.Madagascar = Country('MDG')
# Malawi
Country.MW = Country.MWI = Country.Malawi = Country('MWI')
# Malaysia
Country.MY = Country.MYS = Country.Malaysia = Country('MYS')
# Maldives
Country.MV = Country.MDV = Country.Maldives = Country('MDV')
# Mali
Country.ML = Country.MLI = Country.Mali = Country('MLI')
# Malta
Country.MT = Country.MLT = Country.Malta = Country('MLT')
# Marshall Islands
Country.MH = Country.MHL = Country.MarshallIslands = Country('MHL')
# Martinique
Country.MQ = Country.MTQ = Country.Martinique = Country('MTQ')
# Mauritania
Country.MR = Country.MRT = Country.Mauritania = Country('MRT')
# Mauritius
Country.MU = Country.MUS = Country.Mauritius = Country('MUS')
# Mayotte
Country.YT = Country.MYT = Country.Mayotte = Country('MYT')
# Mexico
Country.MX = Country.MEX = Country.Mexico = Country('MEX')
# Micronesia (Federated States of)
Country.FM = Country.FSM = Country.MicronesiaFederatedStatesOf = Country('FSM')
# Moldova, Republic of
Country.MD = Country.MDA = Country.MoldovaRepublicOf = Country('MDA')
# Monaco
Country.MC = Country.MCO = Country.Monaco = Country('MCO')
# Mongolia
Country.MN = Country.MNG = Country.Mongolia = Country('MNG')
# Montenegro
Country.ME = Country.MNE = Country.Montenegro = Country('MNE')
# Montserrat
Country.MS = Country.MSR = Country.Montserrat = Country('MSR')
# Morocco
Country.MA = Country.MAR = Country.Morocco = Country('MAR')
# Mozambique
Country.MZ = Country.MOZ = Country.Mozambique = Country('MOZ')
# Myanmar
Country.MM = Country.MMR = Country.Myanmar = Country('MMR')
# Namibia
Country.NA = Country.NAM = Country.Namibia = Country('NAM')
# Nauru
Country.NR = Country.NRU = Country.Nauru = Country('NRU')
# Nepal
Country.NP = Country.NPL = Country.Nepal = Country('NPL')
# Netherlands
Country.NL = Country.NLD = Country.Netherlands = Country('NLD')
# New Caledonia
Country.NC = Country.NCL = Country.NewCaledonia = Country('NCL')
# New Zealand
Country.NZ = Country.NZL = Country.NewZealand = Country('NZL')
# Nicaragua
Country.NI = Country.NIC = Country.Nicaragua = Country('NIC')
# Niger
Country.NE = Country.NER = Country.Niger = Country('NER')
# Nigeria
Country.NG = Country.NGA = Country.Nigeria = Country('NGA')
# Niue
Country.NU = Country.NIU = Country.Niue = Country('NIU')
# Norfolk Island
Country.NF = Country.NFK = Country.NorfolkIsland = Country('NFK')
# North Macedonia
Country.MK = Country.MKD = Country.NorthMacedonia = Country('MKD')
# Northern Mariana Islands
Country.MP = Country.MNP = Country.NorthernMarianaIslands = Country('MNP')
# Norway
Country.NO = Country.NOR = Country.Norway = Country('NOR')
# Oman
Country.OM = Country.OMN = Country.Oman = Country('OMN')
# Pakistan
Country.PK = Country.PAK = Country.Pakistan = Country('PAK')
# Palau
Country.PW = Country.PLW = Country.Palau = Country('PLW')
# Palestine, State of
Country.PS = Country.PSE = Country.PalestineStateOf = Country('PSE')
# Panama
Country.PA = Country.PAN = Country.Panama = Country('PAN')
# Papua New Guinea
Country.PG = Country.PNG = Country.PapuaNewGuinea = Country('PNG')
# Paraguay
Country.PY = Country.PRY = Country.Paraguay = Country('PRY')
# Peru
Country.PE = Country.PER = Country.Peru = Country('PER')
# Philippines
Country.PH = Country.PHL = Country.Philippines = Country('PHL')
# Pitcairn
Country.PN = Country.PCN = Country.Pitcairn = Country('PCN')
# Poland
Country.PL = Country.POL = Country.Poland = Country('POL')
# Portugal
Country.PT = Country.PRT = Country.Portugal = Country('PRT')
# Puerto Rico
Country.PR = Country.PRI = Country.PuertoRico = Country('PRI')
# Qatar
Country.QA = Country.QAT = Country.Qatar = Country('QAT')
# Réunion
Country.RE = Country.REU = Country.Reunion = Country('REU')
# Romania
Country.RO = Country.ROU = Country.Romania = Country('ROU')
# Russian Federation
Country.RU = Country.RUS = Country.RussianFederation = Country('RUS')
# Rwanda
Country.RW = Country.RWA = Country.Rwanda = Country('RWA')
# Saint Barthélemy
Country.BL = Country.BLM = Country.SaintBarthelemy = Country('BLM')
# Saint Helena, Ascension and Tristan da Cunha
Country.SH = Country.SHN = Country.SaintHelenaAscensionAndTristanDaCunha = Country('SHN')
# Saint Kitts and Nevis
Country.KN = Country.KNA = Country.SaintKittsAndNevis = Country('KNA')
# Saint Lucia
Country.LC = Country.LCA = Country.SaintLucia = Country('LCA')
# Saint Martin (French part)
Country.MF = Country.MAF = Country.SaintMartinFrenchPart = Country('MAF')
# Saint Pierre and Miquelon
Country.PM = Country.SPM = Country.SaintPierreAndMiquelon = Country('SPM')
# Saint Vincent and the Grenadines
Country.VC = Country.VCT = Country.SaintVincentAndTheGrenadines = Country('VCT')
# Samoa
Country.WS = Country.WSM = Country.Samoa = Country('WSM')
# San Marino
Country.SM = Country.SMR = Country.SanMarino = Country('SMR')
# Sao Tome and Principe
Country.ST = Country.STP = Country.SaoTomeAndPrincipe = Country('STP')
# Saudi Arabia
Country.SA = Country.SAU = Country.SaudiArabia = Country('SAU')
# Senegal
Country.SN = Country.SEN = Country.Senegal = Country('SEN')
# Serbia
Country.RS = Country.SRB = Country.Serbia = Country('SRB')
# Seychelles
Country.SC = Country.SYC = Country.Seychelles = Country('SYC')
# Sierra Leone
Country.SL = Country.SLE = Country.SierraLeone = Country('SLE')
# Singapore
Country.SG = Country.SGP = Country.Singapore = Country('SGP')
# Sint Maarten (Dutch part)
Country.SX = Country.SXM = Country.SintMaartenDutchPart = Country('SXM')
# Slovakia
Country.SK = Country.SVK = Country.Slovakia = Country('SVK')
# Slovenia
Country.SI = Country.SVN = Country.Slovenia = Country('SVN')
# Solomon Islands
Country.SB = Country.SLB = Country.SolomonIslands = Country('SLB')
# Somalia
Country.SO = Country.SOM = Country.Somalia = Country('SOM')
# South Africa
Country.ZA = Country.ZAF = Country.SouthAfrica = Country('ZAF')
# South Georgia and the South Sandwich Islands
Country.GS = Country.SGS = Country.SouthGeorgiaAndTheSouthSandwichIslands = Country('SGS')
# South Sudan
Country.SS = Country.SSD = Country.SouthSudan = Country('SSD')
# Spain
Country.ES = Country.ESP = Country.Spain = Country('ESP')
# Sri Lanka
Country.LK = Country.LKA = Country.SriLanka = Country('LKA')
# Sudan
Country.SD = Country.SDN = Country.Sudan = Country('SDN')
# Suriname
Country.SR = Country.SUR = Country.Suriname = Country('SUR')
# Svalbard and Jan Mayen
Country.SJ = Country.SJM = Country.SvalbardAndJanMayen = Country('SJM')
# Sweden
Country.SE = Country.SWE = Country.Sweden = Country('SWE')
# Switzerland
Country.CH = Country.CHE = Country.Switzerland = Country('CHE')
# Syrian Arab Republic
Country.SY = Country.SYR = Country.SyrianArabRepublic = Country('SYR')
# Taiwan, Province of China
Country.TW = Country.TWN = Country.TaiwanProvinceOfChina = Country('TWN')
# Tajikistan
Country.TJ = Country.TJK = Country.Tajikistan = Country('TJK')
# Tanzania, United Republic of
Country.TZ = Country.TZA = Country.TanzaniaUnitedRepublicOf = Country('TZA')
# Thailand
Country.TH = Country.THA = Country.Thailand = Country('THA')
# Timor-Leste
Country.TL = Country.TLS = Country.TimorLeste = Country('TLS')
# Togo
Country.TG = Country.TGO = Country.Togo = Country('TGO')
# Tokelau
Country.TK = Country.TKL = Country.Tokelau = Country('TKL')
# Tonga
Country.TO = Country.TON = Country.Tonga = Country('TON')
# Trinidad and Tobago
Country.TT = Country.TTO = Country.TrinidadAndTobago = Country('TTO')
# Tunisia
Country.TN = Country.TUN = Country.Tunisia = Country('TUN')
# Turkey
Country.TR = Country.TUR = Country.Turkey = Country('TUR')
# Turkmenistan
Country.TM = Country.TKM = Country.Turkmenistan = Country('TKM')
# Turks and Caicos Islands
Country.TC = Country.TCA = Country.TurksAndCaicosIslands = Country('TCA')
# Tuvalu
Country.TV = Country.TUV = Country.Tuvalu = Country('TUV')
# Uganda
Country.UG = Country.UGA = Country.Uganda = Country('UGA')
# Ukraine
Country.UA = Country.UKR = Country.Ukraine = Country('UKR')
# United Arab Emirates
Country.AE = Country.ARE = Country.UnitedArabEmirates = Country('ARE')
# United Kingdom of Great Britain and Northern Ireland
Country.GB = Country.GBR = Country.UnitedKingdomOfGreatBritainAndNorthernIreland = Country('GBR')
# United States of America
Country.US = Country.USA = Country.UnitedStatesOfAmerica = Country('USA')
# United States Minor Outlying Islands
Country.UM = Country.UMI = Country.UnitedStatesMinorOutlyingIslands = Country('UMI')
# Uruguay
Country.UY = Country.URY = Country.Uruguay = Country('URY')
# Uzbekistan
Country.UZ = Country.UZB = Country.Uzbekistan = Country('UZB')
# Vanuatu
Country.VU = Country.VUT = Country.Vanuatu = Country('VUT')
# Venezuela (Bolivarian Republic of)
Country.VE = Country.VEN = Country.VenezuelaBolivarianRepublicOf = Country('VEN')
# Viet Nam
Country.VN = Country.VNM = Country.VietNam = Country('VNM')
# Virgin Islands (British)
Country.VG = Country.VGB = Country.VirginIslandsBritish = Country('VGB')
# Virgin Islands (U.S.)
Country.VI = Country.VIR = Country.VirginIslandsUS = Country('VIR')
# Wallis and Futuna
Country.WF = Country.WLF = Country.WallisAndFutuna = Country('WLF')
# Western Sahara
Country.EH = Country.ESH = Country.WesternSahara = Country('ESH')
# Yemen
Country.YE = Country.YEM = Country.Yemen = Country('YEM')
# Zambia
Country.ZM = Country.ZMB = Country.Zambia = Country('ZMB')
# Zimbabwe
Country.ZW = Country.ZWE = Country.Zimbabwe = Country('ZWE')
