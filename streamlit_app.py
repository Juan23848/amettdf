
import streamlit as st

# Diccionario de cargos actualizado
cargos_dict = {
    "100 - Supervisor Nivel Inicial.": 3536.9669757838124,
    "101 - Dir. Nivel Inicial-T.C.": 3274.4465402185783,
    "102 -  Dir. 1\u00aa Nivel Inicial- T.S.": 2728.7082334422803,
    "103 - Dir. 2\u00aa Nivel Inicial.-T.S.": 2545.013064728296,
    "104 - Dir. 3\u00aa Nivel Inical.- T.S.": 2388.0371932818,
    "105 - Vicedir. Nivel Inical.- T.C.": 3069.3792736027613,
    "106 - Vicedir. Nivel Inical. T.S.": 2558.3727133620405,
    "107 - Sec.Nivel Inicial.- T.C.": 2865.64463193816,
    "108 - Sec. Nivel Inicial. -T-S.": 2243.6602098761236,
    "109 - Mtro.(secci\u00f3n) Nivel Inicial- T.S.": 1432.82231596908,
    "110 - Mtro.Bibliotecario. - T.S.": 1432.82231596908,
    "111 - Mtro.DeProyectos especificos - T.S.": 1432.82231596908,
    "112 - Mtro.Secc.NivelInicial (aux.sala).-T.S.": 1432.82231596908,
    "113 - Mtro. Aux. Secr.Nivel Inicial- T.S. ": 1432.82231596908,
    "114 - Maestro Tutor.- T.S.": 1432.82231596908,
    "115 - Hora C\u00e1tedra Nivel Inicial.": 68.23224446597742,
    "116 - Pareja Pedag\u00f3gica T.S.": 1432.82231596908,
    "200 - Supervisor Nivel EGB 1 Y 2.": 3536.9669757838124,
    "201 - Dir. Pers. Unico EGB 1 Y 2.- T.C.": 2830.018902248175,
    "202 - Dir. 1\u00aa Nivel EGB 1 Y 2.- T.C.": 3274.4465402185783,
    "203 - Dir. 2\u00aa nivel EGB 1 Y 2.- T.C.": 3002.2187565030063,
    "204 - Dir.3\u00aa Nivel EGB 1 Y 2.- T.C.": 2831.6381453380627,
    "205 - Dir. 1\u00aaNivel EGB 1 Y 2 .- T.S.": 2728.7082334422803,
    "206 - Dir. 2\u00aa Nivel EGB 1 Y 2.- T.S.": 2545.013064728296,
    "207 - Dir. 3\u00aa Nivel EGB 1 Y 2 .- T.S.": 2388.0371932818,
    "208 - Vicedir. Nivel EGB 1 Y 2 .- T.C.": 3069.3792736027613,
    "209 - Vicedir. Nivel EGB 1 Y 2.- T.S.": 2558.3727133620405,
    "210 - Sec. Nivel EGB. 1 Y 2. T.C.": 2865.64463193816,
    "211 - Sec. Nivel EGB 1 Y 2.- T.S.": 2243.6602098761236,
    "212 - Mtro. (a\u00f1o) Nivel EGB. 1 Y 2.- T.S.": 1432.82231596908,
    "213 - Mtro. Bibliotecario. T.S.": 1432.82231596908,
    "214 - Mtro. Computaci\u00f3n.- T.S.": 1432.82231596908,
    "215 - Mtro. Domic. Hospit.- T.S.": 1432.82231596908,
    "216 - Mtro. de Proyectos Especificos.- T.S.": 1432.82231596908,
    "217 - Mtro. Recuperador.- T.S.": 1432.82231596908,
    "218 - Mtro. Tutor.- T.S.": 1432.82231596908,
    "219 - Mtro. (a\u00f1o) Nivel EGB 1 Y 2.- T.C.": 2748.565693746,
    "220 - Mtro. Aux. secr. EGB 1 Y 2.- T.S.": 1432.82231596908,
    "221 - Hora C\u00e1tedra Nivel EGB 1 Y 2": 68.23224446597742,
    "222 - Coord. Ciclo EGB 1Y2-T.C.": 2650.7769497454383,
    "223 - Coord. Ciclo EGB 1Y2-T.S.": 1500.7338631906136,
    "224 - Pareja Pedag\u00f3gica T.S.": 1432.82231596908,
    "230 - Maestro Bibliotecario T.C.": 2748.565693746,
    "231 - Maestro de Computaci\u00f3n T.C.": 2748.565693746,
    "232 - Mtro. Domiciliario/Hospitalario T.C.": 2748.565693746,
    "233 - Mtro. de Proyectos Especificos T.C.": 2748.565693746,
    "234 - Mtro. Recuperador T.C.": 2748.565693746,
    "235 - Tutor/a Docente T.C.": 2748.565693746,
    "236 - Mtro. Aux. de Secretar\u00eda T.C.": 2748.565693746,
    "300 - Supervisor Modalidad Especial.": 3536.9669757838124,
    "301 - Dir. Modalidad Especial - T.C.": 3274.4465402185783,
    "302 - Vicedir. Modalidad Especial - T.C.": 3069.3792736027613,
    "303 - Sec. Modalidad Especial - T.C.": 2865.64463193816,
    "304 - Docente de Grupo - T.S.": 1432.82231596908,
    "305 - Docente de Secci\u00f3n - T.S.": 1432.82231596908,
    "306 - Docente de Ciclo - T.S.": 1432.82231596908,
    "307 - Docente Bibliotecario. - T.S.": 1432.82231596908,
    "308 - Docente de Proyectos Especificos - T.S.": 1432.82231596908,
    "309 - Docente Tutor - T.S.": 1432.82231596908,
    "310 - Docente Auxiliar de Secretar\u00eda - T.S.": 1432.82231596908,
    "311 - Docente Auxiliar de Grupo - T.S.": 1432.82231596908,
    "312 - Hora C\u00e1tedra": 68.23224446597742,
    "313 - Enfermero/a - T.S.": 1432.82231596908,
    "314 - Coordinador/a Pedag\u00f3gico/a - T.S.": 2455.9487405033337,
    "315 - Coordinador/a T\u00e9cnico/a - T.S.": 2455.9487405033337,
    "316 - H.C. Docente Equipo Interdisc. Institucional": 68.23224446597742,
    "400 - Supervisor Nivel Jovenes y Adul.": 3561.903319824936,
    "401 - Dir. Cent. Sec.CENS.- T.S.": 2794.4562425754248,
    "402 - Vicedir. Cent. Sec. CENS -T.S.": 2568.5002200929075,
    "403 - Coord. de Ciclo Cent. Sec. CENS.- T.S.": 2085.31830582018,
    "404 - Secretario Cent. Sec. CENS.- T.S.": 2046.8890228129712,
    "405 - ProSecretario Cent. Sec. CENS.- T.S.": 1910.4297546254397,
    "406 - Dir. Esc. Nivel Jov.y ad..- T.C.": 3274.4465402185783,
    "407 - Vicedir. Esc. Nivel Jov.y ad..- T.C.": 3069.3792736027613,
    "408 - Sec.Nivel Jovenes y Adultos.- T.C.": 2865.64463193816,
    "409 - Mtro. Ciclo Nivel Jovenes y Ad.- T.S.": 1432.82231596908,
    "410 - Mtro.Aux.secr.Nivel jov.y ad.- T.S.": 1432.82231596908,
    "411 - Bibliotecario Escolar": 1432.82231596908,
    "412 - Mtro. Proyectos Especificos - T.S.": 1432.82231596908,
    "413 - Mtro. Computaci\u00f3n.- T.S.": 1432.82231596908,
    "414 - Mtro.p/pers.Priv. De la libertad.- T.S.": 1432.82231596908,
    "415 - Tutor Docente Nivel J\u00f3vene y Adultos": 1432.82231596908,
    "416 - Mtro.Activ. Pr\u00e1ct.Nivel Jov. Y Ad.": 1432.82231596908,
    "417 - Auxiliar administrativo docenteT.C.": 1154.9137908726898,
    "418 - Jefe de laboratorio.": 1227.9743702516669,
    "419 - Ay. T\u00e9c. Trab. Pr\u00e1c.(ATTP)": 1211.1223392710992,
    "420 - Preceptor.": 1296.4265182336942,
    "421 - Hora C\u00e1tedra Nivel Jovenes y ad.": 68.23224446597742,
    "422 - Auxiliar de Secretar\u00eda T.S.": 1296.426518233694,
    "423 - Auxiliar de Secretar\u00eda T.C.": 2415.3131425756947,
    "451 - DIRECTOR DE EDUCACI\u00d3N ESPECIAL NO FORMAL T.C.": 3274.4465402185783,
    "452 - VICE DIRECTOR EDUCACION ESPECIAL NO FORMAL T.C.": 3069.3792736027613,
    "453 - SECRETARIO ADMINISTRATIVO EDUCACION ESPECIAL NO FORMAL T.S.": 2046.8890228129712,
    "454 - MAESTRO TUTOR EDUCACI\u00d3N ESPECIAL NO FORMAL T.S.": 1432.82231596908,
    "455 - TALLERISTA EDICACI\u00d3N ESPECIAL NO FORMAL T.S.": 1275.8464445225839,
    "456 - HORA C\u00c1TEDRA EDUCACI\u00d3N ESPECIAL NO FORMAL": 68.23224446597742,
    "457 - HORA CATEDRA EDUCACI\u00d3N ESP. NO FORMAL- EQUIPO MULTIDISCIPLINARIO": 68.23224446597742,
    "458 - DIRECTOR EDUCACI\u00d3N NO FORMAL T.C.": 3274.4465402185783,
    "459 - VICEDIRECTOR EDUCACI\u00d3N NO FORMAL T.C.": 3069.3792736027613,
    "460 - COORDINADOR EDUCACI\u00d3N NO FORMAL T.C.": 2634.077388953258,
    "461 - SECRETARIO ADMINISTRATIVO EDUCACI\u00d3N NO FORMAL T.C.": 2865.64463193816,
    "462 - PRECEPTOR EDUCACI\u00d3N NO FORMAL T.C.": 2415.3131425756947,
    "463 - JEFE GENERAL ENSA\u00d1ANZA PR\u00c1CTICA EDUCACI\u00d3N NO FORMAL T.S.": 2148.6768219272135,
    "464 - REGENTE ENSE\u00d1ANZA PRACTICA EDUCACI\u00d3N NO FORMAL T.S. ": 2148.6768219272135,
    "465 - COORDINADOR EDUCACI\u00d3N NO FORMAL T.S.": 2012.8537274841467,
    "466 - SECRETARIO ADMINISTRATIVO EDUCACI\u00d3N NO FORMAL T.S.": 2046.8890228129712,
    "467 - MAESTRO DE ENSE\u00d1ANZA PR\u00c1CTICA JEFE SECCI\u00d3N EDUC. NO FORMAL T.S.": 1637.5112182503772,
    "468 - PROSECRETARIO EDUCACI\u00d3N NO FORMAL T.S.": 1910.4297546254397,
    "469 - MAESTRO DE ENSA\u00d1ANZA PR\u00c1CTICA EDUCACI\u00d3N NO FORMAL T.S.": 1432.82231596908,
    "470 - MAESTRO TUTOR EDUCACI\u00d3N NO FORMAL T.S.": 1432.82231596908,
    "471 -  BIBLIOTECARIO EDUCACI\u00d3N NO FORMAL T.S.": 1432.82231596908,
    "472 - PRECEPTOR EDUCACI\u00d3N NO FORMAL T.S.": 1296.4265182336942,
    "473 - AYUDANTE DE TRABAJOS PRACTICOS (ATTP) EDUCACI\u00d3N NO FORMAL T.S.": 1211.0760051643413,
    "474 - HORA C\u00c1TEDRA EDUCACI\u00d3N NO FORMAL T.S.": 68.23224446597742,
    "475 - Auxiliar de Secretar\u00eda T.S.": 1296.426518233694,
    "476 - Auxiliar de Secretar\u00eda T.C.": 2415.3131425756947,
    "500 - Supervisor Dptal. de Gabinete P.y A.E.": 3536.9669757838124,
    "501 - Director Dptal. de Gabinete P.y A.E.": 3274.4465402185783,
    "502 - Secretario de Gabinete P.y A.E.": 2865.64463193816,
    "503 - Asistente Social": 2728.7082334422803,
    "504 - Asistente Educacional": 2728.7082334422803,
    "505 - Psic\u00f3logo": 2728.7082334422803,
    "506 - Psicomotricista": 2728.7082334422803,
    "507 - Psicopedagogo": 2728.7082334422803,
    "508 - M\u00fasicoterapeuta": 2728.7082334422803,
    "509 - Terapista Ocupacional": 2728.7082334422803,
    "510 - Fonoaudi\u00f3logo": 2728.7082334422803,
    "511 - Vicedirector de Cl\u00ednica Terap\u00e9utica GPyAE": 3069.3792736027613,
    "512 - Viced. de Prevenci\u00f3n y Promoci\u00f3n GPyAE": 3069.3792736027613,
    "513 - Viced. Equipos Interdiscipl. Escolares GPyAE": 3069.3792736027613,
    "514 - Aux. de Secretar\u00eda de Gabinete P.y A.E.": 2728.7082334422803,
    "600 - S.T.S.Niv.Inicial,EGB1y2,Esp.Y Gab.": 3445.6760434532266,
    "601 - S.T.S Nivel EGB 3 y Polim.": 3445.6760434532266,
    "602 - S.T.S.Nivel Jovenes y Adultos.": 3445.6760434532266,
    "700 - Dir. De Biblioteca.-T.C.": 3274.4465402185783,
    "701 - Vice-Director Departamental de Biblioteca ": 3069.3792736027613,
    "702 - Secret. Tecn. Administ. Dptal.Bibliotecas ": 2865.64463193816,
    "703 - Supervision Departamental de Bibliotecas": 3445.6760434532266,
    "704 - Supervision Prov.de Bibliotecas Escolares": 3536.9669757838124,
    "800 - Supervisor Nivel EGB3 y Polimodal": 3536.9669757838124,
    "801 - Dir.-/Rector 1\u00aa Agricola.- T.C.": 3274.4465402185783,
    "802 - Dir.-/Rector 1\u00aa .- T.C.": 3274.4465402185783,
    "803 - Dir.-/Rector 2\u00aa .- T.C.": 2940.038870986753,
    "804 - Dir.-/Rector3\u00aa .- T.C.": 2744.1906582677325,
    "805 - Dir.-/Rector 2\u00aa .- T.S.": 2545.013064728296,
    "806 - Dir.-/Rector3\u00aa .- T.S.": 2388.0371932818,
    "807 - Vicedir./Vicered.1\u00aa.- T.C.": 3069.3792736027613,
    "808 - Vicedir./Vicered.2\u00aa.- T.C.": 2912.403402156265,
    "809 - Vicedir./Vicered.3\u00aa.- T.C.": 2779.9202198716334,
    "810 - Vicedir./Vicered.1\u00aa.- T.S.": 2558.3727133620405,
    "811 - Vicedir./Vicered.2\u00aa.- T.S.": 2175.396119194703,
    "812 - Vicedir./Vicered.3\u00aa.- T.S.": 2032.8932004347628,
    "813 - Secretario 1\u00aa.- T.C.": 2865.64463193816,
    "814 - Secretario 2\u00aa.- T.C.": 2439.249179711153,
    "815 - Secretario 3\u00aa.- T.C.": 2217.70167320156,
    "816 - Secretario 1\u00aa.- T.S.": 2046.8890228129712,
    "817 - Secretario 2\u00aa.- T.S.": 1910.4297546254397,
    "818 - Secretario 3\u00aa.- T.S.": 1773.4933561295607,
    "819 - ProSecretario 1\u00aa.- T.S.": 1910.4297546254397,
    "820 - ProSecretario 2\u00aa.- T.S.": 1773.4933561295607,
    "821 - Coord. de Ciclo EGB 3.- T.C.": 2634.077388953258,
    "822 - Coord. de Ciclo Polim.T.C.": 2634.077388953258,
    "823 - Coord. deTAP.-T.C.": 2634.077388953258,
    "824 - Coord. de Ciclo EGB 3.- T.S..": 2012.8537274841467,
    "825 - Coord. de Ciclo Polim.T.S.": 2012.8537274841467,
    "826 - Regente 1\u00aa Ens. T\u00e9cnica": 2148.6768219272135,
    "827 - Regente 3\u00aa Ens. T\u00e9cnica": 1853.6512479320265,
    "828 - Jefe Gral. Ens. Pr\u00e1ctica 1\u00aa": 2148.6768219272135,
    "829 - Coordinador Inter-Area": 1773.4933561295607,
    "830 - Coordinador de Area.": 272.92897786390967,
    "831 - J. Secci\u00f3n Ens. Pr\u00e1c. Agricola- T.C.": 3073.403867753676,
    "832 - Instructor Agricola.": 2865.64463193816,
    "833 - Mtro.Ens. Pr\u00e1ct. Ens.T\u00e9cn.": 1432.82231596908,
    "834 - Mtro.Ens. Pr\u00e1ct. Jefe Secci\u00f3n.": 1637.5112182503772,
    "835 - Jefe de Area de TAP- T.S.": 1637.5112182503772,
    "836 - Jefe de Laboratorio.": 1228.1334136877829,
    "837 - Jefe PRCT 1\u00aa-T.S.": 1603.1578360493202,
    "838 - Jefe PRCT 2\u00aa-T.S.": 1463.9948294478168,
    "839 - SubJefe PRCT 1\u00aa-T.S.": 1409.4429308600272,
    "840 - SubJefe PRCT 2\u00aa-T.S.": 1360.457552536298,
    "841 - Preceptor.-T.C.": 2415.3131425756947,
    "842 - Preceptor.T.S.": 1296.4265182336942,
    "843 - Asesor Pedag\u00f3gico(ASPD) .": 2455.9487405033337,
    "844 - Ayud. Dpto. Orientaci\u00f3n .": 1091.6741455002514,
    "845 - Psicoped. Dpto.  Orien.": 1091.6741455002514,
    "846 - Auxiliar Administrativo Docente": 1154.9137908726898,
    "847 - Referente Institucional Inform\u00e1tico": 1296.426518233694,
    "848 - Ayud.T\u00e9c. Trabajos Pr\u00e1cticos(ATTP)": 1211.0760051643413,
    "849 - Ayudante Clases Pr\u00e1cticas.": 1211.0760051643413,
    "850 - Ayudante de C\u00e1tedra (Art\u00edstica)": 1211.0760051643413,
    "851 - Bibliotecario. - T.S.": 1432.82231596908,
    "852 - Hora C\u00e1tedra Nivel EGB 3 y polimod.": 68.23224446597742,
    "853 - Prof.T.P. 02 24Hs.": 1637.573867183458,
    "854 - Prof.T.P. 03 18Hs.": 1228.1804003875936,
    "855 - Mtro.Ens. Pr\u00e1ct. Agricola.": 1432.82231596908,
    "856 - Mtro.TUTOR-T.S.": 1432.82231596908,
    "857 - Mtro.Cult. Rural/dom. Agricola.": 1432.82231596908,
    "858 - Mtro.Especial(Artistica).": 682.3224446597743,
    "859 - Coordinador T.T.P.-T.C.": 2634.077388953258,
    "860 - Coordinador T.T.P.-T.S.": 2012.8537274841467,
    "861 - Coordinador T.A.P.-T.S.": 2012.8537274841467,
    "862 - Director Departamental de Bibliotecas": 3274.4465402185783,
    "863 - Vice Director Deptal. de Bibliotecas": 3069.3792736027613,
    "864 - Sec. T\u00e9cn. Adm. Deptal. De Bibliotecas": 2865.64463193816,
    "865 - Tutor T.I.y F.E.": 1637.5112182503772,
    "866 - Auxiliar de Secretar\u00eda T.S.": 1296.426518233694,
    "867 - Auxiliar de Secretar\u00eda T.C.": 2415.3131425756947,
    "900 - Supervisor Nivel Terciario.": 3894.9400968898562,
    "901 - Dir.-/Rector 1 Turno": 3709.46675894272,
    "902 - Vicedirector./Vicerector.": 3477.625086508799,
    "903 - Bedel": 1825.255012125075,
    "904 - Encargado de Laboratorio": 1412.3820535594514,
    "905 - Secretario/a Administrativo/a ": 2467.5174051068934,
    "906 - ProSecretario/a": 2197.0387499813683,
    "907 - Bibliotecario/a Especializado/a": 1718.39108245014,
    "908 - Preceptor/a": 1490.8477232016428,
    "909 - Ayudante de Laboratorio/ A.T.T.P.": 1392.7656361489032,
    "910 - Hora C\u00e1tedra ": 78.46534623059999,
    "911 - Secretario/a o Coordinador/a Acad\u00e9mico/a": 2467.5174051068934,
    "912 - Jefe/a de Formaci\u00f3n Inicial": 1569.3069246119999,
    "913 - Jefe/a de Formaci\u00f3n Permanente y Extensi\u00f3n": 1569.3069246119999,
    "914 - Jefe/a de Investigaci\u00f3n Educativa": 1569.3069246119999,
    "915 - Jefe/a de Pol\u00edticas Estudiantiles": 1569.3069246119999,
    "916 - Jefe de Bedeles": 1825.2546574285714,
    "917 - Referente de Entornos Formativos": 1804.7029633037998,
    "918 - Coordinador/a Interinstitucional de Pr\u00e1cticas": 1318.2178166740798,
    "919 - Coordinador/a de Vinculaci\u00f3n Socioproductiva": 1318.2178166740798,
    "920 - Coord.  Ciclo/Curso de Ingreso/Introductorio": 1318.2178166740798,
    "921 - Coordinador/a de Entornos Multimediales": 1318.2178166740798,
    "922 - Coordinador/a de Carreras": 855.27227391354,
    "923 - Coordinador/a del \u00c1rea del Conocimiento": 855.27227391354,
    "924 - Coordinador/a de Formaci\u00f3n Permanente": 855.27227391354,
    "925 - Coordinador/a de Extensi\u00f3n": 855.27227391354,
    "926 - Coordinador/a de Comunicaci\u00f3n Institucional": 855.27227391354,
    "927 - Coordinador/a de Centro de Documentaci\u00f3n": 1976.1497448176606,
    "928 - Tutor/a docente de carrera o de Curso de Ingreso": 499.039602026616,
    "929 - Docente co-formador/a": 499.039602026616,
    "930 - Asistente T\u00e9cnico": 1490.841159333,
    "931 - Auxiliar de Secretar\u00eda": 1490.841159333,
    "932 - Tutor/a del Depto. de Pol\u00edticas Estudiantiles": 855.27227391354,
    "933 - Tramo docente 1 (categor\u00eda A/B) ": 941.5841547672001,
    "934 - Tramo docente 2 (categor\u00eda A/B) ": 1569.3069246119999,
    "935 - Tramo docente 3 (categor\u00eda A/B) ": 2353.960386918,
    "936 - Tramo docente 4 (categor\u00eda A/B) ": 3138.6138492239998,
    "937 - Tramo pr\u00e1cticas 1 (categor\u00eda A/B)": 941.5841547672001,
    "938 - Tramo pr\u00e1cticas 2 (categor\u00eda A/B)": 1569.3069246119999,
    "939 - Tramo pr\u00e1cticas 3 (categor\u00eda A/B)": 2353.960386918,
    "940 - Tramo pr\u00e1cticas 4 (categor\u00eda A/B)": 3138.6138492239998,
    "949 - Supervisor Departamental de Bibliotecas": 3445.6760434532266,
    "950 - Supervisor General.": 3663.7576479317577,
    "951 - Super.deAreasCompl.(art\u00edsitica)": 3536.9669757838124,
    "952 - Super.deAreasCompl.(educ. f\u00edsic.)": 3536.9669757838124,
    "953 - Supervisor de Bibliotecas.": 3536.9669757838124,
    "954 - Supervisor General de Nivel Secundario": 3663.7576479317577,
    "955 - Supervisor Escolar Departamental de Nivel Secundario": 3536.9669757838124,
    "956 - Supervisor T\u00e9cnico Departamental de Nivel Secundario": 3445.6760434532266,
    "957 - Sup. Deptal. Lenguajes Art\u00edsticos N. Primario": 3368.6576690796905,
    "958 - Sup. Deptal. de Educaci\u00f3n F\u00edsica N. Primario": 3368.6576690796905,
    "959 - Sup. Deptal. de Tecnolog\u00eda Nivel Primario": 3368.6576690796905
}

VALOR_INDICE = 87.608881

antiguedad_tabla = {
    range(0, 6): 0.40, range(6, 8): 0.50, range(8, 10): 0.60,
    range(10, 12): 0.70, range(12, 14): 0.80, range(14, 16): 0.90,
    range(16, 18): 1.00, range(18, 20): 1.10, range(20, 22): 1.20,
    range(22, 24): 1.30, range(24, 100): 1.35
}

def calcular_antiguedad_factor(antiguedad):
    for r in antiguedad_tabla:
        if antiguedad in r:
            return antiguedad_tabla[r]
    return 0

st.title("Simulador Salarial Docente - Versión Web (Mayo 2025)")

antiguedad = st.number_input("Antigüedad (años):", min_value=0, max_value=40, value=0)

cargo_seleccionado = []
cantidad_seleccionada = []

for i in range(3):
    col1, col2 = st.columns([3, 1])
    with col1:
        cargo = st.selectbox("Cargo u horas #{}".format(i+1), options=[""] + list(cargos_dict.keys()), key="cargo_{}".format(i))
    with col2:
        cantidad = st.number_input("Cantidad:", min_value=0, value=0, key="cantidad_{}".format(i))
    cargo_seleccionado.append(cargo)
    cantidad_seleccionada.append(cantidad)

if st.button("Calcular Sueldo"):
    total_puntaje = 0
    total_horas_catedra = 0
    cargos_simples = 0
    tiene_cargo_completo = False
    desglose_items = ""

    for i in range(3):
        cargo = cargo_seleccionado[i]
        cantidad = cantidad_seleccionada[i]
        if not cargo or cantidad <= 0:
            continue
        puntaje_unitario = cargos_dict.get(cargo, 0)
        puntaje_total = puntaje_unitario * cantidad
        basico_parcial = puntaje_total * VALOR_INDICE
        total_puntaje += puntaje_total

        if "HORA CÁTEDRA" in cargo.upper():
            total_horas_catedra += cantidad
        elif "COMPLETO" in cargo.upper():
            tiene_cargo_completo = True
        elif "SIMPLE" in cargo.upper():
            cargos_simples += cantidad

        desglose_items += f"{cargo}\n  Cantidad: {cantidad} - Puntaje: {puntaje_total:.2f} - Básico: ${basico_parcial:,.2f}\n"

    if tiene_cargo_completo:
        unidades_bono = 38
    else:
        unidades_bono = min(19 * min(cargos_simples, 2) + total_horas_catedra, 38)

    basico = total_puntaje * VALOR_INDICE
    funcion_docente = basico * 2.30
    antiguedad_valor = basico * calcular_antiguedad_factor(antiguedad)
    transformacion = basico * 1.23
    subtotal = basico + funcion_docente + antiguedad_valor + transformacion
    zona = subtotal
    total_remunerativo = subtotal + zona

    jubilacion = total_remunerativo * 0.16
    obra_social = total_remunerativo * 0.03
    seguro = 3000
    descuentos = jubilacion + obra_social + seguro

    bono_foid_conectividad = unidades_bono * (90000 / 38)
    bono_ayuda_material = unidades_bono * (142600 / 38)
    total_bonos = bono_foid_conectividad + bono_ayuda_material

    neto = total_remunerativo - descuentos + total_bonos

    st.text_area("Desglose:", desglose_items, height=200)
    st.markdown("### 🧾 Neto estimado: ${neto:,.2f}")
