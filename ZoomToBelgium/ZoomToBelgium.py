# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ZoomToBelgium
                                 A QGIS plugin
 A button to zoom to any of the Belgian Municipalities
                              -------------------
        begin                : 2017-09-19
        copyright            : (C) 2017 by Michel Stuyts
        email                : info@stuyts.xyz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
try:
    from qgis.PyQt.QtCore import *
except ImportError:
    from PyQt4.QtCore import *
try:
    from qgis.PyQt.QtGui import *
    from qgis.PyQt.QtWidgets import QAction
except ImportError:
    from PyQt4.QtGui import *
try:
    from .resources import *
except ImportError:
    from .resources3 import *
from .ZoomToBelgium_dialog import ZoomToBelgiumDialog
import os.path,unicodedata
from collections import OrderedDict
from qgis.core import *

class ZoomToBelgium:
    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ZoomToBelgium', message)

    def __init__(self, iface):
        self.dlg = ZoomToBelgiumDialog()
        global municipality_name
        global municipality_xmax
        global municipality_xmin
        global municipality_ymax
        global municipality_ymin
        municipality_name=OrderedDict()
        municipality_name[518]=u"Aalst"
        municipality_name[458]=u"Aalter"
        municipality_name[446]=u"Aarschot"
        municipality_name[286]=u"Aartselaar"
        municipality_name[330]=u"Affligem"
        municipality_name[34]=u"Aiseau-Presles"
        municipality_name[484]=u"Alken"
        municipality_name[550]=u"Alveringem"
        municipality_name[237]=u"Amay"
        municipality_name[268]=u"Amblève (Amel)"
        municipality_name[202]=u"Andenne"
        municipality_name[127]=u"Anderlecht"
        municipality_name[152]=u"Anderlues"
        municipality_name[179]=u"Anhée"
        municipality_name[172]=u"Ans"
        municipality_name[52]=u"Anthisnes"
        municipality_name[255]=u"Antoing"
        municipality_name[476]=u"Antwerpen"
        municipality_name[500]=u"Anzegem"
        municipality_name[300]=u"Ardooie"
        municipality_name[559]=u"Arendonk"
        municipality_name[97]=u"Arlon"
        municipality_name[566]=u"As"
        municipality_name[475]=u"Asse"
        municipality_name[405]=u"Assenede"
        municipality_name[147]=u"Assesse"
        municipality_name[279]=u"Ath"
        municipality_name[50]=u"Attert"
        municipality_name[141]=u"Aubange"
        municipality_name[270]=u"Aubel"
        municipality_name[37]=u"Auderghem"
        municipality_name[522]=u"Avelgem"
        municipality_name[154]=u"Awans"
        municipality_name[201]=u"Aywaille"
        municipality_name[577]=u"Baarle-Hertog"
        municipality_name[247]=u"Baelen"
        municipality_name[485]=u"Balen"
        municipality_name[169]=u"Bassenge"
        municipality_name[265]=u"Bastogne"
        municipality_name[26]=u"Beaumont"
        municipality_name[224]=u"Beauraing"
        municipality_name[96]=u"Beauvechain"
        municipality_name[414]=u"Beernem"
        municipality_name[507]=u"Beerse"
        municipality_name[396]=u"Beersel"
        municipality_name[528]=u"Begijnendijk"
        municipality_name[341]=u"Bekkevoort"
        municipality_name[137]=u"Belœil"
        municipality_name[105]=u"Berchem-Sainte-Agathe"
        municipality_name[561]=u"Beringen"
        municipality_name[386]=u"Berlaar"
        municipality_name[543]=u"Berlare"
        municipality_name[233]=u"Berloz"
        municipality_name[119]=u"Bernissart"
        municipality_name[579]=u"Bertem"
        municipality_name[228]=u"Bertogne"
        municipality_name[259]=u"Bertrix"
        municipality_name[504]=u"Bever"
        municipality_name[565]=u"Beveren"
        municipality_name[104]=u"Beyne-Heusay"
        municipality_name[470]=u"Bierbeek"
        municipality_name[139]=u"Bièvre"
        municipality_name[392]=u"Bilzen"
        municipality_name[281]=u"Binche"
        municipality_name[497]=u"Blankenberge"
        municipality_name[67]=u"Blégny"
        municipality_name[574]=u"Bocholt"
        municipality_name[372]=u"Boechout"
        municipality_name[304]=u"Bonheiden"
        municipality_name[416]=u"Boom"
        municipality_name[582]=u"Boortmeerbeek"
        municipality_name[447]=u"Borgloon"
        municipality_name[527]=u"Bornem"
        municipality_name[373]=u"Borsbeek"
        municipality_name[261]=u"Bouillon"
        municipality_name[62]=u"Boussu"
        municipality_name[498]=u"Boutersem"
        municipality_name[84]=u"Braine-lAlleud"
        municipality_name[112]=u"Braine-le-Château"
        municipality_name[41]=u"Braine-le-Comte"
        municipality_name[223]=u"Braives"
        municipality_name[531]=u"Brakel"
        municipality_name[564]=u"Brasschaat"
        municipality_name[459]=u"Brecht"
        municipality_name[393]=u"Bredene"
        municipality_name[346]=u"Bree"
        municipality_name[213]=u"Brugelette"
        municipality_name[420]=u"Brugge"
        municipality_name[88]=u"Brunehaut"
        municipality_name[38]=u"Bruxelles"
        municipality_name[329]=u"Buggenhout"
        municipality_name[244]=u"Bullange (Büllingen)"
        municipality_name[94]=u"Burdinne"
        municipality_name[46]=u"Burg-Reuland"
        municipality_name[253]=u"Butgenbach (Bütgenbach)"
        municipality_name[194]=u"Celles"
        municipality_name[167]=u"Cerfontaine"
        municipality_name[140]=u"Chapelle-lez-Herlaimont"
        municipality_name[205]=u"Charleroi"
        municipality_name[29]=u"Chastre"
        municipality_name[219]=u"Châtelet"
        municipality_name[39]=u"Chaudfontaine"
        municipality_name[117]=u"Chaumont-Gistoux"
        municipality_name[245]=u"Chièvres"
        municipality_name[171]=u"Chimay"
        municipality_name[187]=u"Chiny"
        municipality_name[258]=u"Ciney"
        municipality_name[212]=u"Clavier"
        municipality_name[153]=u"Colfontaine"
        municipality_name[142]=u"Comblain-au-Pont"
        municipality_name[7]=u"Comines-Warneton"
        municipality_name[130]=u"Courcelles"
        municipality_name[236]=u"Court-Saint-Étienne"
        municipality_name[178]=u"Couvin"
        municipality_name[3]=u"Crisnée"
        municipality_name[78]=u"Dalhem"
        municipality_name[310]=u"Damme"
        municipality_name[19]=u"Daverdisse"
        municipality_name[399]=u"De Haan"
        municipality_name[584]=u"De Panne"
        municipality_name[576]=u"De Pinte"
        municipality_name[536]=u"Deerlijk"
        municipality_name[568]=u"Deinze"
        municipality_name[491]=u"Denderleeuw"
        municipality_name[473]=u"Dendermonde"
        municipality_name[370]=u"Dentergem"
        municipality_name[532]=u"Dessel"
        municipality_name[508]=u"Destelbergen"
        municipality_name[398]=u"Diepenbeek"
        municipality_name[423]=u"Diest"
        municipality_name[466]=u"Diksmuide"
        municipality_name[375]=u"Dilbeek"
        municipality_name[461]=u"Dilsen-Stokkem"
        municipality_name[115]=u"Dinant"
        municipality_name[101]=u"Dison"
        municipality_name[240]=u"Doische"
        municipality_name[4]=u"Donceel"
        municipality_name[76]=u"Dour"
        municipality_name[364]=u"Drogenbos"
        municipality_name[415]=u"Duffel"
        municipality_name[121]=u"Durbuy"
        municipality_name[189]=u"Écaussinnes"
        municipality_name[514]=u"Edegem"
        municipality_name[450]=u"Eeklo"
        municipality_name[155]=u"Éghezée"
        municipality_name[166]=u"Ellezelles"
        municipality_name[200]=u"Enghien"
        municipality_name[185]=u"Engis"
        municipality_name[175]=u"Érezée"
        municipality_name[378]=u"Erpe-Mere"
        municipality_name[103]=u"Erquelinnes"
        municipality_name[251]=u"Esneux"
        municipality_name[517]=u"Essen"
        municipality_name[192]=u"Estaimpuis"
        municipality_name[246]=u"Estinnes"
        municipality_name[57]=u"Étalle"
        municipality_name[9]=u"Etterbeek"
        municipality_name[106]=u"Eupen"
        municipality_name[263]=u"Evere"
        municipality_name[471]=u"Evergem"
        municipality_name[15]=u"Faimes"
        municipality_name[32]=u"Farciennes"
        municipality_name[138]=u"Fauvillers"
        municipality_name[173]=u"Fernelmont"
        municipality_name[226]=u"Ferrières"
        municipality_name[197]=u"Fexhe-le-Haut-Clocher"
        municipality_name[218]=u"Flémalle"
        municipality_name[229]=u"Fléron"
        municipality_name[196]=u"Fleurus"
        municipality_name[176]=u"Flobecq"
        municipality_name[60]=u"Floreffe"
        municipality_name[146]=u"Florennes"
        municipality_name[2]=u"Florenville"
        municipality_name[160]=u"Fontaine-lÉvêque"
        municipality_name[208]=u"Forest"
        municipality_name[58]=u"Fosses-la-Ville"
        municipality_name[136]=u"Frameries"
        municipality_name[234]=u"Frasnes-lez-Anvaing"
        municipality_name[48]=u"Froidchapelle"
        municipality_name[546]=u"Galmaarden"
        municipality_name[100]=u"Ganshoren"
        municipality_name[477]=u"Gavere"
        municipality_name[61]=u"Gedinne"
        municipality_name[525]=u"Geel"
        municipality_name[260]=u"Geer"
        municipality_name[530]=u"Geetbets"
        municipality_name[267]=u"Gembloux"
        municipality_name[51]=u"Genappe"
        municipality_name[581]=u"Genk"
        municipality_name[319]=u"Gent"
        municipality_name[520]=u"Geraardsbergen"
        municipality_name[145]=u"Gerpinnes"
        municipality_name[180]=u"Gesves"
        municipality_name[555]=u"Gingelom"
        municipality_name[544]=u"Gistel"
        municipality_name[580]=u"Glabbeek"
        municipality_name[513]=u"Gooik"
        municipality_name[275]=u"Gouvy"
        municipality_name[177]=u"Grâce-Hollogne"
        municipality_name[90]=u"Grez-Doiceau"
        municipality_name[439]=u"Grimbergen"
        municipality_name[429]=u"Grobbendonk"
        municipality_name[361]=u"Haacht"
        municipality_name[552]=u"Haaltert"
        municipality_name[98]=u"Habay"
        municipality_name[404]=u"Halen"
        municipality_name[482]=u"Halle"
        municipality_name[456]=u"Ham"
        municipality_name[354]=u"Hamme"
        municipality_name[81]=u"Hamoir"
        municipality_name[99]=u"Hamois"
        municipality_name[334]=u"Hamont-Achel"
        municipality_name[66]=u"Ham-sur-Heure-Nalinnes"
        municipality_name[45]=u"Hannut"
        municipality_name[326]=u"Harelbeke"
        municipality_name[578]=u"Hasselt"
        municipality_name[280]=u"Hastière"
        municipality_name[150]=u"Havelange"
        municipality_name[349]=u"Hechtel-Eksel"
        municipality_name[407]=u"Heers"
        municipality_name[292]=u"Heist-op-den-Berg"
        municipality_name[204]=u"Hélécine"
        municipality_name[521]=u"Hemiksem"
        municipality_name[221]=u"Hensies"
        municipality_name[250]=u"Herbeumont"
        municipality_name[395]=u"Herent"
        municipality_name[309]=u"Herentals"
        municipality_name[554]=u"Herenthout"
        municipality_name[509]=u"Herk-de-Stad"
        municipality_name[465]=u"Herne"
        municipality_name[126]=u"Héron"
        municipality_name[534]=u"Herselt"
        municipality_name[12]=u"Herstal"
        municipality_name[318]=u"Herstappe"
        municipality_name[129]=u"Herve"
        municipality_name[448]=u"Herzele"
        municipality_name[430]=u"Heusden-Zolder"
        municipality_name[589]=u"Heuvelland"
        municipality_name[410]=u"Hoegaarden"
        municipality_name[492]=u"Hoeilaart"
        municipality_name[585]=u"Hoeselt"
        municipality_name[481]=u"Holsbeek"
        municipality_name[203]=u"Honnelles"
        municipality_name[359]=u"Hooglede"
        municipality_name[454]=u"Hoogstraten"
        municipality_name[486]=u"Horebeke"
        municipality_name[91]=u"Hotton"
        municipality_name[230]=u"Houffalize"
        municipality_name[387]=u"Houthalen-Helchteren"
        municipality_name[436]=u"Houthulst"
        municipality_name[93]=u"Houyet"
        municipality_name[541]=u"Hove"
        municipality_name[293]=u"Huldenberg"
        municipality_name[512]=u"Hulshout"
        municipality_name[44]=u"Huy"
        municipality_name[307]=u"Ichtegem"
        municipality_name[553]=u"Ieper"
        municipality_name[225]=u"Incourt"
        municipality_name[406]=u"Ingelmunster"
        municipality_name[108]=u"Ittre"
        municipality_name[23]=u"Ixelles"
        municipality_name[350]=u"Izegem"
        municipality_name[353]=u"Jabbeke"
        municipality_name[235]=u"Jalhay"
        municipality_name[113]=u"Jemeppe-sur-Sambre"
        municipality_name[59]=u"Jette"
        municipality_name[95]=u"Jodoigne"
        municipality_name[27]=u"Juprelle"
        municipality_name[156]=u"Jurbise"
        municipality_name[472]=u"Kalmthout"
        municipality_name[426]=u"Kampenhout"
        municipality_name[391]=u"Kapellen"
        municipality_name[299]=u"Kapelle-op-den-Bos"
        municipality_name[413]=u"Kaprijke"
        municipality_name[337]=u"Kasterlee"
        municipality_name[306]=u"Keerbergen"
        municipality_name[379]=u"Kinrooi"
        municipality_name[340]=u"Kluisbergen"
        municipality_name[526]=u"Knesselare"
        municipality_name[291]=u"Knokke-Heist"
        municipality_name[422]=u"Koekelare"
        municipality_name[77]=u"Koekelberg"
        municipality_name[288]=u"Koksijde"
        municipality_name[376]=u"Kontich"
        municipality_name[516]=u"Kortemark"
        municipality_name[440]=u"Kortenaken"
        municipality_name[384]=u"Kortenberg"
        municipality_name[462]=u"Kortessem"
        municipality_name[419]=u"Kortrijk"
        municipality_name[367]=u"Kraainem"
        municipality_name[463]=u"Kruibeke"
        municipality_name[533]=u"Kruishoutem"
        municipality_name[432]=u"Kuurne"
        municipality_name[232]=u"La Bruyère"
        municipality_name[198]=u"La Calamine (Kelmis)"
        municipality_name[271]=u"La Hulpe"
        municipality_name[10]=u"La Louvière"
        municipality_name[71]=u"La Roche-en-Ardenne"
        municipality_name[355]=u"Laakdal"
        municipality_name[294]=u"Laarne"
        municipality_name[315]=u"Lanaken"
        municipality_name[400]=u"Landen"
        municipality_name[402]=u"Langemark-Poelkapelle"
        municipality_name[20]=u"Lasne"
        municipality_name[278]=u"Le Roeulx"
        municipality_name[502]=u"Lebbeke"
        municipality_name[434]=u"Lede"
        municipality_name[408]=u"Ledegem"
        municipality_name[13]=u"LÉglise"
        municipality_name[389]=u"Lendelede"
        municipality_name[496]=u"Lennik"
        municipality_name[114]=u"Lens"
        municipality_name[495]=u"Leopoldsburg"
        municipality_name[277]=u"Les Bons Villers"
        municipality_name[252]=u"Lessines"
        municipality_name[338]=u"Leuven"
        municipality_name[162]=u"Leuze-en-Hainaut"
        municipality_name[55]=u"Libin"
        municipality_name[128]=u"Libramont-Chevigny"
        municipality_name[519]=u"Lichtervelde"
        municipality_name[545]=u"Liedekerke"
        municipality_name[92]=u"Liège"
        municipality_name[325]=u"Lier"
        municipality_name[588]=u"Lierde"
        municipality_name[54]=u"Lierneux"
        municipality_name[332]=u"Lille"
        municipality_name[17]=u"Limbourg"
        municipality_name[85]=u"Lincent"
        municipality_name[499]=u"Linkebeek"
        municipality_name[562]=u"Lint"
        municipality_name[302]=u"Linter"
        municipality_name[124]=u"Lobbes"
        municipality_name[303]=u"Lochristi"
        municipality_name[488]=u"Lokeren"
        municipality_name[358]=u"Lommel"
        municipality_name[305]=u"Londerzeel"
        municipality_name[64]=u"Lontzen"
        municipality_name[314]=u"Lo-Reninge"
        municipality_name[313]=u"Lovendegem"
        municipality_name[510]=u"Lubbeek"
        municipality_name[397]=u"Lummen"
        municipality_name[345]=u"Maarkedal"
        municipality_name[342]=u"Maaseik"
        municipality_name[417]=u"Maasmechelen"
        municipality_name[501]=u"Machelen"
        municipality_name[529]=u"Maldegem"
        municipality_name[282]=u"Malle"
        municipality_name[125]=u"Malmedy"
        municipality_name[33]=u"Manage"
        municipality_name[111]=u"Manhay"
        municipality_name[199]=u"Marche-en-Famenne"
        municipality_name[144]=u"Marchin"
        municipality_name[87]=u"Martelange"
        municipality_name[469]=u"Mechelen"
        municipality_name[487]=u"Meerhout"
        municipality_name[377]=u"Meeuwen-Gruitrode"
        municipality_name[298]=u"Meise"
        municipality_name[181]=u"Meix-devant-Virton"
        municipality_name[323]=u"Melle"
        municipality_name[312]=u"Menen"
        municipality_name[207]=u"Merbes-le-Château"
        municipality_name[418]=u"Merchtem"
        municipality_name[333]=u"Merelbeke"
        municipality_name[571]=u"Merksplas"
        municipality_name[549]=u"Mesen"
        municipality_name[266]=u"Messancy"
        municipality_name[174]=u"Mettet"
        municipality_name[321]=u"Meulebeke"
        municipality_name[569]=u"Middelkerke"
        municipality_name[109]=u"Modave"
        municipality_name[557]=u"Moerbeke"
        municipality_name[348]=u"Mol"
        municipality_name[231]=u"Molenbeek-Saint-Jean"
        municipality_name[269]=u"Momignies"
        municipality_name[264]=u"Mons"
        municipality_name[40]=u"Mont-de-lEnclus"
        municipality_name[69]=u"Montigny-le-Tilleul"
        municipality_name[35]=u"Mont-Saint-Guibert"
        municipality_name[587]=u"Moorslede"
        municipality_name[74]=u"Morlanwelz"
        municipality_name[343]=u"Mortsel"
        municipality_name[1]=u"Mouscron"
        municipality_name[135]=u"Musson"
        municipality_name[157]=u"Namur"
        municipality_name[238]=u"Nandrin"
        municipality_name[73]=u"Nassogne"
        municipality_name[556]=u"Nazareth"
        municipality_name[374]=u"Neerpelt"
        municipality_name[28]=u"Neufchâteau"
        municipality_name[254]=u"Neupré"
        municipality_name[494]=u"Nevele"
        municipality_name[573]=u"Niel"
        municipality_name[563]=u"Nieuwerkerken"
        municipality_name[382]=u"Nieuwpoort"
        municipality_name[371]=u"Nijlen"
        municipality_name[467]=u"Ninove"
        municipality_name[239]=u"Nivelles"
        municipality_name[164]=u"Ohey"
        municipality_name[523]=u"Olen"
        municipality_name[30]=u"Olne"
        municipality_name[241]=u"Onhaye"
        municipality_name[411]=u"Oostende"
        municipality_name[368]=u"Oosterzele"
        municipality_name[363]=u"Oostkamp"
        municipality_name[317]=u"Oostrozebeke"
        municipality_name[409]=u"Opglabbeek"
        municipality_name[394]=u"Opwijk"
        municipality_name[161]=u"Oreye"
        municipality_name[132]=u"Orp-Jauche"
        municipality_name[86]=u"Ottignies-Louvain-la-Neuve"
        municipality_name[425]=u"Oudenaarde"
        municipality_name[449]=u"Oudenburg"
        municipality_name[301]=u"Oud-Heverlee"
        municipality_name[490]=u"Oud-Turnhout"
        municipality_name[222]=u"Ouffet"
        municipality_name[31]=u"Oupeye"
        municipality_name[547]=u"Overijse"
        municipality_name[586]=u"Overpelt"
        municipality_name[14]=u"Paliseul"
        municipality_name[16]=u"Pecq"
        municipality_name[560]=u"Peer"
        municipality_name[443]=u"Pepingen"
        municipality_name[42]=u"Pepinster"
        municipality_name[110]=u"Péruwelz"
        municipality_name[272]=u"Perwez"
        municipality_name[53]=u"Philippeville"
        municipality_name[572]=u"Pittem"
        municipality_name[80]=u"Plombières"
        municipality_name[215]=u"Pont-à-Celles"
        municipality_name[295]=u"Poperinge"
        municipality_name[209]=u"Profondeville"
        municipality_name[457]=u"Putte"
        municipality_name[424]=u"Puurs"
        municipality_name[165]=u"Quaregnon"
        municipality_name[21]=u"Quévy"
        municipality_name[5]=u"Quiévrain"
        municipality_name[148]=u"Raeren"
        municipality_name[131]=u"Ramillies"
        municipality_name[331]=u"Ranst"
        municipality_name[362]=u"Ravels"
        municipality_name[276]=u"Rebecq"
        municipality_name[149]=u"Remicourt"
        municipality_name[72]=u"Rendeux"
        municipality_name[383]=u"Retie"
        municipality_name[328]=u"Riemst"
        municipality_name[505]=u"Rijkevorsel"
        municipality_name[8]=u"Rixensart"
        municipality_name[227]=u"Rochefort"
        municipality_name[464]=u"Roeselare"
        municipality_name[357]=u"Ronse"
        municipality_name[401]=u"Roosdaal"
        municipality_name[431]=u"Rotselaar"
        municipality_name[47]=u"Rouvroy"
        municipality_name[421]=u"Ruiselede"
        municipality_name[11]=u"Rumes"
        municipality_name[360]=u"Rumst"
        municipality_name[184]=u"Sainte-Ode"
        municipality_name[123]=u"Saint-Georges-sur-Meuse"
        municipality_name[6]=u"Saint-Ghislain"
        municipality_name[82]=u"Saint-Gilles"
        municipality_name[134]=u"Saint-Hubert"
        municipality_name[120]=u"Saint-Josse-ten-Noode"
        municipality_name[158]=u"Saint-Léger"
        municipality_name[49]=u"Saint-Nicolas"
        municipality_name[249]=u"Saint-Vith (Sankt Vith)"
        municipality_name[274]=u"Sambreville"
        municipality_name[122]=u"Schaerbeek"
        municipality_name[583]=u"Schelle"
        municipality_name[451]=u"Scherpenheuvel-Zichem"
        municipality_name[365]=u"Schilde"
        municipality_name[352]=u"Schoten"
        municipality_name[217]=u"Seneffe"
        municipality_name[163]=u"Seraing"
        municipality_name[182]=u"Silly"
        municipality_name[347]=u"Sint-Amands"
        municipality_name[511]=u"Sint-Genesius-Rode"
        municipality_name[369]=u"Sint-Gillis-Waas"
        municipality_name[283]=u"Sint-Katelijne-Waver"
        municipality_name[322]=u"Sint-Laureins"
        municipality_name[336]=u"Sint-Lievens-Houtem"
        municipality_name[483]=u"Sint-Martens-Latem"
        municipality_name[537]=u"Sint-Niklaas"
        municipality_name[524]=u"Sint-Pieters-Leeuw"
        municipality_name[381]=u"Sint-Truiden"
        municipality_name[43]=u"Sivry-Rance"
        municipality_name[116]=u"Soignies"
        municipality_name[168]=u"Sombreffe"
        municipality_name[151]=u"Somme-Leuze"
        municipality_name[63]=u"Soumagne"
        municipality_name[220]=u"Spa"
        municipality_name[452]=u"Spiere-Helkijn"
        municipality_name[75]=u"Sprimont"
        municipality_name[455]=u"Stabroek"
        municipality_name[427]=u"Staden"
        municipality_name[206]=u"Stavelot"
        municipality_name[344]=u"Steenokkerzeel"
        municipality_name[412]=u"Stekene"
        municipality_name[211]=u"Stoumont"
        municipality_name[183]=u"Tellin"
        municipality_name[460]=u"Temse"
        municipality_name[133]=u"Tenneville"
        municipality_name[335]=u"Ternat"
        municipality_name[570]=u"Tervuren"
        municipality_name[575]=u"Tessenderlo"
        municipality_name[170]=u"Theux"
        municipality_name[190]=u"Thimister-Clermont"
        municipality_name[216]=u"Thuin"
        municipality_name[403]=u"Tielt"
        municipality_name[437]=u"Tielt-Winge"
        municipality_name[287]=u"Tienen"
        municipality_name[186]=u"Tinlot"
        municipality_name[248]=u"Tintigny"
        municipality_name[296]=u"Tongeren"
        municipality_name[435]=u"Torhout"
        municipality_name[68]=u"Tournai"
        municipality_name[297]=u"Tremelo"
        municipality_name[159]=u"Trois-Ponts"
        municipality_name[79]=u"Trooz"
        municipality_name[36]=u"Tubize"
        municipality_name[444]=u"Turnhout"
        municipality_name[256]=u"Uccle"
        municipality_name[243]=u"Vaux-sur-Sûre"
        municipality_name[210]=u"Verlaine"
        municipality_name[273]=u"Verviers"
        municipality_name[356]=u"Veurne"
        municipality_name[242]=u"Vielsalm"
        municipality_name[22]=u"Villers-la-Ville"
        municipality_name[262]=u"Villers-le-Bouillet"
        municipality_name[320]=u"Vilvoorde"
        municipality_name[25]=u"Viroinval"
        municipality_name[193]=u"Virton"
        municipality_name[257]=u"Visé"
        municipality_name[540]=u"Vleteren"
        municipality_name[290]=u"Voeren"
        municipality_name[388]=u"Vorselaar"
        municipality_name[442]=u"Vosselaar"
        municipality_name[188]=u"Vresse-sur-Semois"
        municipality_name[441]=u"Waarschoot"
        municipality_name[493]=u"Waasmunster"
        municipality_name[308]=u"Wachtebeke"
        municipality_name[195]=u"Waimes (Weismes)"
        municipality_name[89]=u"Walcourt"
        municipality_name[56]=u"Walhain"
        municipality_name[83]=u"Wanze"
        municipality_name[438]=u"Waregem"
        municipality_name[191]=u"Waremme"
        municipality_name[118]=u"Wasseiges"
        municipality_name[107]=u"Waterloo"
        municipality_name[214]=u"Watermael-Boitsfort"
        municipality_name[65]=u"Wavre"
        municipality_name[24]=u"Welkenraedt"
        municipality_name[285]=u"Wellen"
        municipality_name[18]=u"Wellin"
        municipality_name[535]=u"Wemmel"
        municipality_name[366]=u"Wervik"
        municipality_name[316]=u"Westerlo"
        municipality_name[433]=u"Wetteren"
        municipality_name[339]=u"Wevelgem"
        municipality_name[390]=u"Wezembeek-Oppem"
        municipality_name[506]=u"Wichelen"
        municipality_name[503]=u"Wielsbeke"
        municipality_name[567]=u"Wijnegem"
        municipality_name[445]=u"Willebroek"
        municipality_name[311]=u"Wingene"
        municipality_name[102]=u"Woluwe-Saint-Lambert"
        municipality_name[143]=u"Woluwe-Saint-Pierre"
        municipality_name[479]=u"Wommelgem"
        municipality_name[474]=u"Wortegem-Petegem"
        municipality_name[515]=u"Wuustwezel"
        municipality_name[70]=u"Yvoir"
        municipality_name[468]=u"Zandhoven"
        municipality_name[489]=u"Zaventem"
        municipality_name[428]=u"Zedelgem"
        municipality_name[385]=u"Zele"
        municipality_name[538]=u"Zelzate"
        municipality_name[551]=u"Zemst"
        municipality_name[284]=u"Zingem"
        municipality_name[380]=u"Zoersel"
        municipality_name[453]=u"Zomergem"
        municipality_name[351]=u"Zonhoven"
        municipality_name[327]=u"Zonnebeke"
        municipality_name[289]=u"Zottegem"
        municipality_name[478]=u"Zoutleeuw"
        municipality_name[542]=u"Zuienkerke"
        municipality_name[539]=u"Zulte"
        municipality_name[558]=u"Zutendaal"
        municipality_name[548]=u"Zwalm"
        municipality_name[324]=u"Zwevegem"
        municipality_name[480]=u"Zwijndrecht"
        
        municipality_xmax={1: 76601, 2: 226282, 3: 225058, 4: 221265, 5: 105550, 6: 115296, 7: 55567, 8: 163987, 9: 153062, 10: 140143, 11: 78848, 12: 241094, 13: 246199, 14: 209848, 15: 214901, 16: 81518, 17: 264248, 18: 207969, 19: 206128, 20: 161143, 21: 127751, 22: 165731, 23: 152459, 24: 265367, 25: 175264, 26: 148328, 27: 236878, 28: 233443, 29: 171585, 30: 249347, 31: 243401, 32: 164989, 33: 143815, 34: 167652, 35: 171040, 36: 141374, 37: 158005, 38: 154807, 39: 242893, 40: 92057, 41: 141861, 42: 255344, 43: 145395, 44: 217731, 45: 206096, 46: 280261, 47: 234293, 48: 152329, 49: 233530, 50: 255480, 51: 162240, 52: 234085, 53: 175767, 54: 257819, 55: 219022, 56: 176707, 57: 246103, 58: 180608, 59: 148021, 60: 182759, 61: 195972, 62: 112641, 63: 249110, 64: 270436, 65: 169638, 66: 157688, 67: 249398, 68: 93935, 69: 153488, 70: 196710, 71: 248217, 72: 238741, 73: 228445, 74: 143898, 75: 248869, 76: 113268, 77: 147820, 78: 252419, 79: 249497, 80: 266580, 81: 239139, 82: 149268, 83: 213561, 84: 153057, 85: 198880, 86: 169756, 87: 249944, 88: 86333, 89: 162585, 90: 176929, 91: 230901, 92: 242352, 93: 203638, 94: 206522, 95: 190948, 96: 183133, 97: 261321, 98: 246838, 99: 211957, 100: 147004, 101: 259375, 102: 156551, 103: 139406, 104: 243741, 105: 146166, 106: 284786, 107: 155118, 108: 146851, 109: 219943, 110: 97550, 111: 248266, 112: 147502, 113: 175849, 114: 122406, 115: 198446, 116: 133123, 117: 178342, 118: 199059, 119: 106353, 120: 151092, 121: 240218, 122: 153117, 123: 222626, 124: 145405, 125: 274092, 126: 206972, 127: 147998, 128: 235017, 129: 255561, 130: 152578, 131: 190489, 132: 195811, 133: 237892, 134: 228221, 135: 248845, 136: 120183, 137: 106885, 138: 251717, 139: 203919, 140: 147046, 141: 258791, 142: 239925, 143: 157613, 144: 215032, 145: 166040, 146: 179906, 147: 202086, 148: 282068, 149: 222618, 150: 220798, 151: 223549, 152: 144677, 153: 114711, 154: 229354, 155: 193940, 156: 123608, 157: 193657, 158: 249293, 159: 266270, 160: 149125, 161: 222384, 162: 103584, 163: 234768, 164: 211704, 165: 115637, 166: 107481, 167: 160697, 168: 169584, 169: 242923, 170: 259999, 171: 155509, 172: 233649, 173: 198588, 174: 178384, 175: 241591, 176: 108197, 177: 230906, 178: 166954, 179: 187623, 180: 205204, 181: 234168, 182: 128641, 183: 217853, 184: 240360, 185: 225947, 186: 226396, 187: 230359, 188: 194742, 189: 140145, 190: 259552, 191: 216712, 192: 77262, 193: 242251, 194: 90931, 195: 282152, 196: 166467, 197: 225770, 198: 269592, 199: 228918, 200: 131972, 201: 251176, 202: 206451, 203: 112340, 204: 195992, 205: 159864, 206: 268208, 207: 142787, 208: 148916, 209: 189140, 210: 219361, 211: 260925, 212: 225366, 213: 117655, 214: 157154, 215: 156196, 216: 151872, 217: 147704, 218: 229308, 219: 163806, 220: 260952, 221: 108281, 222: 232959, 223: 209572, 224: 200918, 225: 184145, 226: 245311, 227: 215429, 228: 247609, 229: 245357, 230: 259179, 231: 148574, 232: 187566, 233: 211231, 234: 104929, 235: 270851, 236: 167147, 237: 219526, 238: 228582, 239: 152643, 240: 180770, 241: 187416, 242: 267515, 243: 246499, 244: 295152, 245: 112363, 246: 136973, 247: 275508, 248: 235725, 249: 288169, 250: 223991, 251: 238432, 252: 117850, 253: 287194, 254: 234073, 255: 90454, 256: 153124, 257: 245725, 258: 213709, 259: 221882, 260: 210656, 261: 209131, 262: 215758, 263: 154069, 264: 129838, 265: 257521, 266: 259200, 267: 181045, 268: 286544, 269: 146116, 270: 259802, 271: 160172, 272: 184182, 273: 260255, 274: 171494, 275: 268902, 276: 136727, 277: 160239, 278: 137049, 279: 117771, 280: 187914, 281: 141723, 282: 178461, 283: 166834, 284: 102030, 285: 220677, 286: 152800, 287: 195888, 288: 37168, 289: 114700, 290: 258879, 291: 81470, 292: 181483, 293: 170235, 294: 119807, 295: 39747, 296: 233542, 297: 178470, 298: 148935, 299: 151518, 300: 71004, 301: 176617, 302: 201089, 303: 118781, 304: 168665, 305: 147525, 306: 173915, 307: 59718, 308: 118785, 309: 185922, 310: 82293, 311: 78585, 312: 68997, 313: 100842, 314: 43726, 315: 245333, 316: 190719, 317: 80243, 318: 225378, 319: 113655, 320: 158319, 321: 78608, 322: 102424, 323: 112609, 324: 85779, 325: 169207, 326: 78181, 327: 58514, 328: 242996, 329: 141051, 330: 134643, 331: 169228, 332: 187580, 333: 109423, 334: 233243, 335: 138614, 336: 119715, 337: 196313, 338: 178265, 339: 69303, 340: 94908, 341: 197560, 342: 252623, 343: 158062, 344: 161636, 345: 103687, 346: 244480, 347: 143434, 348: 210915, 349: 224752, 350: 70904, 351: 227014, 352: 162853, 353: 65668, 354: 138110, 355: 201253, 356: 38425, 357: 101242, 358: 223199, 359: 64483, 360: 157148, 361: 172542, 362: 201170, 363: 75298, 364: 146968, 365: 168444, 366: 61085, 367: 158753, 368: 113635, 369: 135883, 370: 86259, 371: 174602, 372: 163733, 373: 159809, 374: 231060, 375: 144450, 376: 158247, 377: 240885, 378: 124879, 379: 254043, 380: 176156, 381: 214744, 382: 41891, 383: 205163, 384: 167290, 385: 130639, 386: 173240, 387: 230908, 388: 182640, 389: 72871, 390: 160469, 391: 160467, 392: 238469, 393: 55252, 394: 139925, 395: 173467, 396: 149101, 397: 212052, 398: 228070, 399: 62592, 400: 203134, 401: 134636, 402: 53049, 403: 85692, 404: 204140, 405: 109983, 406: 74676, 407: 222907, 408: 68354, 409: 238401, 410: 191295, 411: 54664, 412: 130765, 413: 100782, 414: 83004, 415: 164464, 416: 152634, 417: 248189, 418: 145293, 419: 78720, 420: 76038, 421: 85296, 422: 55086, 423: 205485, 424: 149450, 425: 102758, 426: 167577, 427: 60025, 428: 69304, 429: 179673, 430: 218978, 431: 180542, 432: 74857, 433: 118735, 434: 125798, 435: 65123, 436: 52046, 437: 190993, 438: 87227, 439: 154051, 440: 200876, 441: 99547, 442: 188045, 443: 138258, 444: 192985, 445: 153977, 446: 189826, 447: 223238, 448: 120463, 449: 58398, 450: 96884, 451: 195880, 452: 81927, 453: 97044, 454: 183545, 455: 153371, 456: 210313, 457: 172461, 458: 90937, 459: 174718, 460: 144193, 461: 250414, 462: 226144, 463: 147312, 464: 66292, 465: 132191, 466: 50657, 467: 129332, 468: 176109, 469: 162656, 470: 181769, 471: 110166, 472: 161593, 473: 137742, 474: 95089, 475: 145243, 476: 159023, 477: 106885, 478: 205227, 479: 163526, 480: 149196, 481: 185365, 482: 145986, 483: 99922, 484: 219210, 485: 212518, 486: 104028, 487: 203318, 488: 126546, 489: 161806, 490: 198060, 491: 130352, 492: 160072, 493: 134118, 494: 97049, 495: 215291, 496: 138946, 497: 66924, 498: 187374, 499: 149912, 500: 89836, 501: 157104, 502: 135975, 503: 84269, 504: 122132, 505: 181961, 506: 124551, 507: 186738, 508: 113252, 509: 210567, 510: 188170, 511: 153890, 512: 185067, 513: 134739, 514: 156641, 515: 174243, 516: 58904, 517: 162476, 518: 135570, 519: 66847, 520: 124276, 521: 149276, 522: 90430, 523: 189031, 524: 146101, 525: 199557, 526: 90947, 527: 147164, 528: 181110, 529: 92377, 530: 207631, 531: 111287, 532: 207030, 533: 95126, 534: 192084, 535: 147915, 536: 81370, 537: 139720, 538: 114180, 539: 90907, 540: 40398, 541: 159911, 542: 67990, 543: 127060, 544: 54275, 545: 132939, 546: 127648, 547: 167260, 548: 107661, 549: 47965, 550: 37868, 551: 161230, 552: 126996, 553: 51929, 554: 180913, 555: 211766, 556: 101505, 557: 124113, 558: 237575, 559: 203826, 560: 232479, 561: 218359, 562: 161110, 563: 212959, 564: 163253, 565: 146724, 566: 239417, 567: 162875, 568: 96838, 569: 48927, 570: 165350, 571: 189314, 572: 75796, 573: 149611, 574: 240244, 575: 207123, 576: 103816, 577: 190598, 578: 223529, 579: 170506, 580: 193985, 581: 236078, 582: 167146, 583: 150550, 584: 28482, 585: 230648, 586: 225077, 587: 63128, 588: 115686, 589: 50694}
        municipality_xmin={1: 65912, 2: 206122, 3: 220266, 4: 214559, 5: 100197, 6: 105140, 7: 42250, 8: 157659, 9: 150723, 10: 128791, 11: 72754, 12: 233830, 13: 225105, 14: 198440, 15: 208278, 16: 74698, 17: 258225, 18: 196031, 19: 193295, 20: 151842, 21: 113853, 22: 156021, 23: 148483, 24: 257221, 25: 161297, 26: 135530, 27: 228356, 28: 218005, 29: 164491, 30: 243799, 31: 236451, 32: 160538, 33: 138317, 34: 161484, 35: 165584, 36: 133206, 37: 151795, 38: 146139, 39: 236401, 40: 85415, 41: 125788, 42: 248006, 43: 132708, 44: 203950, 45: 193739, 46: 266977, 47: 227616, 48: 143806, 49: 230477, 50: 244294, 51: 150485, 52: 225865, 53: 157712, 54: 245010, 55: 204139, 56: 168332, 57: 233619, 58: 165305, 59: 144740, 60: 173195, 61: 180223, 62: 106648, 63: 243356, 64: 262073, 65: 161378, 66: 148422, 67: 240105, 68: 70469, 69: 147596, 70: 184531, 71: 227965, 72: 226589, 73: 212476, 74: 137806, 75: 236206, 76: 104235, 77: 145665, 78: 244143, 79: 240114, 80: 256906, 81: 230686, 82: 146996, 83: 204091, 84: 145160, 85: 194048, 86: 158723, 87: 244771, 88: 75725, 89: 144096, 90: 167757, 91: 221343, 92: 231638, 93: 184549, 94: 196660, 95: 178532, 96: 173192, 97: 244517, 98: 231625, 99: 196664, 100: 144631, 101: 254014, 102: 152200, 103: 126776, 104: 239644, 105: 143693, 106: 265367, 107: 149024, 108: 137846, 109: 211496, 110: 88103, 111: 235968, 112: 140731, 113: 167881, 114: 111609, 115: 184676, 116: 120497, 117: 168093, 118: 193224, 119: 96521, 120: 149054, 121: 219295, 122: 149190, 123: 217788, 124: 136872, 125: 263710, 126: 197184, 127: 141257, 128: 216300, 129: 246230, 130: 144193, 131: 182707, 132: 188338, 133: 223117, 134: 211712, 135: 240233, 136: 112250, 137: 96107, 138: 239615, 139: 190383, 140: 142511, 141: 246513, 142: 232816, 143: 152503, 144: 208806, 145: 156322, 146: 159683, 147: 187489, 148: 268089, 149: 214991, 150: 204124, 151: 210229, 152: 139988, 153: 110563, 154: 224344, 155: 179622, 156: 109679, 157: 175140, 158: 240128, 159: 248988, 160: 144406, 161: 216049, 162: 91925, 163: 227983, 164: 200263, 165: 111636, 166: 98373, 167: 149489, 168: 163371, 169: 231198, 170: 247200, 171: 137696, 172: 227138, 173: 188885, 174: 165179, 175: 226412, 176: 101818, 177: 219361, 178: 151221, 179: 175472, 180: 191952, 181: 222745, 182: 115206, 183: 206071, 184: 224909, 185: 218394, 186: 216683, 187: 217770, 188: 184491, 189: 132622, 190: 252944, 191: 209734, 192: 70216, 193: 231933, 194: 79177, 195: 270136, 196: 157778, 197: 219247, 198: 263939, 199: 209798, 200: 121202, 201: 239114, 202: 192119, 203: 99414, 204: 189296, 205: 148562, 206: 255390, 207: 133188, 208: 145319, 209: 176477, 210: 212430, 211: 242613, 212: 210586, 213: 111079, 214: 151662, 215: 145653, 216: 139882, 217: 137067, 218: 221601, 219: 158173, 220: 252735, 221: 99359, 222: 222088, 223: 200399, 224: 182213, 225: 175656, 226: 231727, 227: 199049, 228: 233756, 229: 240293, 230: 241719, 231: 143973, 232: 176637, 233: 206245, 234: 87765, 235: 256992, 236: 160155, 237: 213307, 238: 218517, 239: 141282, 240: 165274, 241: 176196, 242: 245675, 243: 230997, 244: 281283, 245: 103606, 246: 125700, 247: 260720, 248: 225562, 249: 264624, 250: 210944, 251: 230059, 252: 105945, 253: 275028, 254: 224714, 255: 81940, 256: 145989, 257: 240268, 258: 195158, 259: 206806, 260: 204527, 261: 193234, 262: 208131, 263: 151300, 264: 113508, 265: 240993, 266: 248297, 267: 168176, 268: 271055, 269: 133275, 270: 250921, 271: 153892, 272: 175801, 273: 252193, 274: 164495, 275: 251354, 276: 130381, 277: 150292, 278: 126629, 279: 99517, 280: 177422, 281: 127797, 282: 168507, 283: 156586, 284: 93377, 285: 213092, 286: 148948, 287: 184030, 288: 26301, 289: 106258, 290: 242765, 291: 70305, 292: 170361, 293: 163149, 294: 111749, 295: 25355, 296: 221970, 297: 169953, 298: 143103, 299: 146548, 300: 65389, 301: 168567, 302: 193935, 303: 109228, 304: 159404, 305: 139647, 306: 166130, 307: 52917, 308: 112252, 309: 178463, 310: 71619, 311: 65094, 312: 59198, 313: 95193, 314: 32546, 315: 234549, 316: 181035, 317: 73853, 318: 223907, 319: 94653, 320: 149419, 321: 69918, 322: 87638, 323: 107489, 324: 74997, 325: 159600, 326: 72519, 327: 49314, 328: 230663, 329: 134953, 330: 129279, 331: 161281, 332: 177409, 333: 101809, 334: 224633, 335: 131518, 336: 111654, 337: 184427, 338: 169120, 339: 60804, 340: 85825, 341: 188722, 342: 236876, 343: 154488, 344: 156268, 345: 94244, 346: 232437, 347: 137253, 348: 196595, 349: 212432, 350: 65913, 351: 215454, 352: 156040, 353: 57095, 354: 128294, 355: 189241, 356: 23572, 357: 91381, 358: 209098, 359: 55222, 360: 149346, 361: 165231, 362: 188913, 363: 64626, 364: 144348, 365: 161212, 366: 53442, 367: 155658, 368: 104959, 369: 128347, 370: 79195, 371: 165987, 372: 157774, 373: 157079, 374: 221967, 375: 135721, 376: 151939, 377: 226124, 378: 116527, 379: 240144, 380: 166679, 381: 202036, 382: 33240, 383: 195189, 384: 160292, 385: 122159, 386: 166549, 387: 217786, 388: 174968, 389: 66944, 390: 157159, 391: 151597, 392: 225413, 393: 50351, 394: 134132, 395: 166155, 396: 142101, 397: 201966, 398: 220086, 399: 53367, 400: 193386, 401: 126888, 402: 42769, 403: 74041, 404: 197287, 405: 97195, 406: 69961, 407: 211105, 408: 60310, 409: 230662, 410: 180445, 411: 43060, 412: 122211, 413: 94573, 414: 73361, 415: 156730, 416: 148032, 417: 236135, 418: 136839, 419: 67622, 420: 63639, 421: 77029, 422: 47117, 423: 193935, 424: 141593, 425: 91669, 426: 160139, 427: 50952, 428: 58215, 429: 172627, 430: 210014, 431: 171152, 432: 70583, 433: 111540, 434: 114792, 435: 57105, 436: 40240, 437: 183335, 438: 76189, 439: 146460, 440: 192247, 441: 93504, 442: 182671, 443: 129045, 444: 186247, 445: 146775, 446: 178458, 447: 212140, 448: 112642, 449: 49869, 450: 89889, 451: 187463, 452: 76203, 453: 89846, 454: 170708, 455: 147031, 456: 200881, 457: 163662, 458: 77336, 459: 161991, 460: 133163, 461: 238000, 462: 219247, 463: 140435, 464: 58119, 465: 121034, 466: 35998, 467: 118257, 468: 167727, 469: 150095, 470: 172735, 471: 98479, 472: 151034, 473: 123878, 474: 85418, 475: 133840, 476: 139400, 477: 97631, 478: 197490, 479: 157942, 480: 144509, 481: 174393, 482: 136109, 483: 95430, 484: 211482, 485: 200379, 486: 100918, 487: 194966, 488: 116952, 489: 153675, 490: 191356, 491: 126060, 492: 152576, 493: 125043, 494: 89023, 495: 208318, 496: 131702, 497: 61793, 498: 180096, 499: 146680, 500: 80627, 501: 153302, 502: 129106, 503: 75537, 504: 116098, 505: 174285, 506: 117880, 507: 177682, 508: 107040, 509: 202550, 510: 176690, 511: 146643, 512: 177902, 513: 126473, 514: 151983, 515: 159605, 516: 48910, 517: 150739, 518: 122834, 519: 60811, 520: 110146, 521: 146771, 522: 80953, 523: 182986, 524: 136238, 525: 186759, 526: 79913, 527: 136245, 528: 176964, 529: 79497, 530: 199025, 531: 102812, 532: 197599, 533: 86552, 534: 180188, 535: 143603, 536: 76488, 537: 123169, 538: 107764, 539: 82945, 540: 31938, 541: 156254, 542: 58810, 543: 119118, 544: 45368, 545: 128177, 546: 119118, 547: 155848, 548: 100678, 549: 44236, 550: 24934, 551: 150052, 552: 119614, 553: 37389, 554: 174178, 555: 201718, 556: 91658, 557: 117337, 558: 231550, 559: 196059, 560: 221452, 561: 202789, 562: 157253, 563: 204893, 564: 154982, 565: 134889, 566: 231400, 567: 157867, 568: 82879, 569: 36523, 570: 155550, 571: 180642, 572: 69497, 573: 145749, 574: 227511, 575: 192883, 576: 97683, 577: 181836, 578: 209297, 579: 162516, 580: 187785, 581: 221389, 582: 160102, 583: 145728, 584: 22041, 585: 224714, 586: 216531, 587: 55615, 588: 108743, 589: 33318}
        municipality_ymax={1: 162338, 2: 52629, 3: 158793, 4: 152010, 5: 123695, 6: 136868, 7: 167558, 8: 159826, 9: 170477, 10: 134949, 11: 140715, 12: 155388, 13: 66231, 14: 75947, 15: 152297, 16: 157428, 17: 150339, 18: 90447, 19: 81746, 20: 157069, 21: 122082, 22: 143450, 23: 170026, 24: 155532, 25: 89237, 26: 109329, 27: 160578, 28: 66364, 29: 146766, 30: 145272, 31: 160976, 32: 126667, 33: 134757, 34: 125329, 35: 150313, 36: 157640, 37: 168508, 38: 178089, 39: 145670, 40: 162704, 41: 150953, 42: 144595, 43: 100504, 44: 136853, 45: 156354, 46: 107247, 47: 29800, 48: 103593, 49: 149605, 50: 54861, 51: 149786, 52: 135250, 53: 102272, 54: 118003, 55: 81914, 56: 150539, 57: 45160, 58: 124198, 59: 175891, 60: 129077, 61: 82396, 62: 126981, 63: 151520, 64: 156064, 65: 161473, 66: 116786, 67: 156079, 68: 153562, 69: 121512, 70: 117160, 71: 103044, 72: 106638, 73: 99239, 74: 129309, 75: 139204, 76: 123420, 77: 173015, 78: 161352, 79: 143585, 80: 162457, 81: 128973, 82: 169973, 83: 141678, 84: 158192, 85: 160253, 86: 153999, 87: 61615, 88: 140078, 89: 113120, 90: 165432, 91: 112518, 92: 153705, 93: 104696, 94: 144451, 95: 162693, 96: 166391, 97: 47255, 98: 53321, 99: 119467, 100: 174641, 101: 148132, 102: 172519, 103: 115483, 104: 149686, 105: 173832, 106: 152693, 107: 158371, 108: 152098, 109: 135346, 110: 141292, 111: 118670, 112: 154431, 113: 133579, 114: 145270, 115: 110566, 116: 147057, 117: 157034, 118: 148631, 119: 134002, 120: 172232, 121: 124944, 122: 174517, 123: 147433, 124: 119779, 125: 135602, 126: 141204, 127: 171092, 128: 79895, 129: 155662, 130: 134798, 131: 154951, 132: 159213, 133: 93939, 134: 87626, 135: 33746, 136: 123812, 137: 141448, 138: 70937, 139: 78502, 140: 132923, 141: 34240, 142: 134191, 143: 170920, 144: 133352, 145: 118707, 146: 112471, 147: 123239, 148: 158415, 149: 155219, 150: 123283, 151: 120215, 152: 124135, 153: 125032, 154: 159309, 155: 148781, 156: 138415, 157: 135744, 158: 37991, 159: 121085, 160: 126255, 161: 160209, 162: 148554, 163: 147036, 164: 130118, 165: 127745, 166: 162791, 167: 103229, 168: 139915, 169: 167177, 170: 140787, 171: 90877, 172: 157522, 173: 145497, 174: 118845, 175: 115297, 176: 163693, 177: 150567, 178: 92041, 179: 116852, 180: 128194, 181: 37044, 182: 153968, 183: 89160, 184: 85785, 185: 143000, 186: 133278, 187: 53749, 188: 68950, 189: 142916, 190: 155180, 191: 157956, 192: 157381, 193: 37057, 194: 161308, 195: 141518, 196: 136859, 197: 154015, 198: 161719, 199: 107975, 200: 155875, 201: 135457, 202: 135879, 203: 119517, 204: 162331, 205: 131349, 206: 133001, 207: 117361, 208: 168916, 209: 122324, 210: 147789, 211: 129345, 212: 128339, 213: 147156, 214: 167168, 215: 139094, 216: 118480, 217: 143445, 218: 147060, 219: 125830, 220: 134564, 221: 128368, 222: 130769, 223: 149070, 224: 95051, 225: 159966, 226: 128451, 227: 103323, 228: 90283, 229: 149091, 230: 103672, 231: 173436, 232: 140381, 233: 157328, 234: 158500, 235: 143815, 236: 149745, 237: 142795, 238: 137547, 239: 147182, 240: 99946, 241: 111214, 242: 116342, 243: 78596, 244: 134091, 245: 144940, 246: 124454, 247: 150084, 248: 52931, 249: 117106, 250: 58224, 251: 141830, 252: 160252, 253: 136117, 254: 140714, 255: 142265, 256: 167311, 257: 167657, 258: 114598, 259: 69315, 260: 154496, 261: 63787, 262: 146910, 263: 175066, 264: 133742, 265: 90471, 266: 39706, 267: 144573, 268: 123146, 269: 83534, 270: 157409, 271: 160720, 272: 152229, 273: 147198, 274: 131345, 275: 107846, 276: 156272, 277: 139331, 278: 137373, 279: 154273, 280: 104118, 281: 126235, 282: 224168, 283: 197756, 284: 181377, 285: 173488, 286: 204555, 287: 172797, 288: 205632, 289: 178856, 290: 164585, 291: 229649, 292: 201975, 293: 169446, 294: 196307, 295: 182175, 296: 168611, 297: 190801, 298: 188240, 299: 191192, 300: 191322, 301: 171361, 302: 173323, 303: 204492, 304: 192982, 305: 192569, 306: 190482, 307: 206909, 308: 212675, 309: 211885, 310: 222539, 311: 199871, 312: 169841, 313: 203452, 314: 190856, 315: 182340, 316: 204337, 317: 184276, 318: 158851, 319: 208920, 320: 183226, 321: 185839, 322: 222089, 323: 191356, 324: 169136, 325: 206214, 326: 177983, 327: 180679, 328: 171052, 329: 192577, 330: 180275, 331: 214048, 332: 221135, 333: 190967, 334: 221745, 335: 175502, 336: 182850, 337: 219810, 338: 181581, 339: 173493, 340: 167086, 341: 184549, 342: 203090, 343: 208844, 344: 183253, 345: 169094, 346: 209081, 347: 196476, 348: 223978, 349: 208452, 350: 183349, 351: 189642, 352: 221602, 353: 215029, 354: 200190, 355: 200863, 356: 199878, 357: 163979, 358: 218879, 359: 190636, 360: 200992, 361: 187176, 362: 242185, 363: 209063, 364: 166960, 365: 220672, 366: 172318, 367: 172981, 368: 185421, 369: 220353, 370: 186151, 371: 207954, 372: 208956, 373: 210440, 374: 219037, 375: 175608, 376: 204421, 377: 204671, 378: 182921, 379: 209731, 380: 220476, 381: 174457, 382: 207313, 383: 221103, 384: 180525, 385: 199126, 386: 202825, 387: 199825, 388: 215774, 389: 177161, 390: 172409, 391: 228297, 392: 179730, 393: 217957, 394: 186565, 395: 181841, 396: 163512, 397: 192696, 398: 182809, 399: 223499, 400: 165123, 401: 172049, 402: 183951, 403: 194219, 404: 187882, 405: 219224, 406: 182495, 407: 164997, 408: 176485, 409: 195633, 410: 167116, 411: 216054, 412: 215602, 413: 215767, 414: 210623, 415: 200766, 416: 199568, 417: 190015, 418: 187597, 419: 174442, 420: 228798, 421: 199505, 422: 203610, 423: 193543, 424: 199086, 425: 177319, 426: 184496, 427: 188550, 428: 207047, 429: 211873, 430: 196260, 431: 186271, 432: 174968, 433: 191023, 434: 186389, 435: 200108, 436: 189684, 437: 183804, 438: 178328, 439: 186712, 440: 180467, 441: 207563, 442: 224265, 443: 164387, 444: 231889, 445: 197225, 446: 192080, 447: 171053, 448: 178756, 449: 213570, 450: 212434, 451: 193059, 452: 160199, 453: 206934, 454: 244027, 455: 227449, 456: 203737, 457: 197445, 458: 201813, 459: 230345, 460: 207297, 461: 197832, 462: 175261, 463: 209785, 464: 187781, 465: 160891, 466: 201711, 467: 173535, 468: 215469, 469: 196504, 470: 173998, 471: 210050, 472: 238256, 473: 195842, 474: 175481, 475: 181587, 476: 229770, 477: 183144, 478: 175152, 479: 212573, 480: 216844, 481: 183766, 482: 163081, 483: 191952, 484: 178176, 485: 211609, 486: 172644, 487: 205744, 488: 206144, 489: 176901, 490: 228394, 491: 177912, 492: 163563, 493: 204034, 494: 199288, 495: 204497, 496: 170335, 497: 224782, 498: 173668, 499: 163267, 500: 173254, 501: 179340, 502: 190188, 503: 182173, 504: 158161, 505: 231519, 506: 191652, 507: 226183, 508: 197062, 509: 184876, 510: 178042, 511: 162536, 512: 197701, 513: 167370, 514: 207025, 515: 235929, 516: 196444, 517: 241423, 518: 187233, 519: 196145, 520: 169719, 521: 205752, 522: 167487, 523: 209789, 524: 168575, 525: 214949, 526: 205972, 527: 201667, 528: 192165, 529: 218753, 530: 179302, 531: 170938, 532: 218045, 533: 182849, 534: 198050, 535: 179749, 536: 173464, 537: 210884, 538: 211748, 539: 186285, 540: 184187, 541: 205921, 542: 220862, 543: 196052, 544: 210661, 545: 175428, 546: 163564, 547: 166499, 548: 178163, 549: 162863, 550: 193925, 551: 188799, 552: 178513, 553: 182059, 554: 206140, 555: 162537, 556: 186708, 557: 212902, 558: 185949, 559: 231763, 560: 209394, 561: 199924, 562: 203599, 563: 178147, 564: 226804, 565: 227029, 566: 192662, 567: 214722, 568: 191412, 569: 211331, 570: 173058, 571: 233720, 572: 192485, 573: 200670, 574: 213220, 575: 197511, 576: 189580, 577: 238597, 578: 186122, 579: 175655, 580: 176935, 581: 190648, 582: 188142, 583: 202741, 584: 201832, 585: 175887, 586: 215733, 587: 180515, 588: 169889, 589: 169805}
        municipality_ymin={1: 156098, 2: 33761, 3: 153289, 4: 146474, 5: 117878, 6: 125411, 7: 154546, 8: 153844, 9: 167999, 10: 124747, 11: 134050, 12: 150087, 13: 47605, 14: 57412, 15: 145417, 16: 149038, 17: 141787, 18: 78541, 19: 72467, 20: 148142, 21: 113009, 22: 134971, 23: 165577, 24: 147326, 25: 74935, 26: 94181, 27: 152655, 28: 52500, 29: 138866, 30: 140099, 31: 153104, 32: 122558, 33: 128295, 34: 117323, 35: 144053, 36: 149067, 37: 164369, 38: 165088, 39: 138446, 40: 155150, 41: 139367, 42: 137382, 43: 89901, 44: 128836, 45: 143405, 46: 92325, 47: 21192, 48: 85725, 49: 145331, 50: 43688, 51: 138191, 52: 128105, 53: 86668, 54: 105807, 55: 66659, 56: 142669, 57: 35115, 58: 116403, 59: 172687, 60: 120321, 61: 67445, 62: 120597, 63: 144086, 64: 150084, 65: 152480, 66: 108751, 67: 148305, 68: 138429, 69: 116072, 70: 107893, 71: 87269, 72: 95312, 73: 85761, 74: 123479, 75: 130333, 76: 115982, 77: 171815, 78: 153202, 79: 138263, 80: 153141, 81: 122485, 82: 167791, 83: 133386, 84: 146120, 85: 154418, 86: 148746, 87: 52057, 88: 131599, 89: 100615, 90: 154501, 91: 101140, 92: 139598, 93: 91431, 94: 138516, 95: 152018, 96: 158880, 97: 35391, 98: 42576, 99: 109192, 100: 172801, 101: 143953, 102: 169340, 103: 105099, 104: 145289, 105: 171715, 106: 138977, 107: 151146, 108: 144742, 109: 123364, 110: 131045, 111: 101753, 112: 149855, 113: 123378, 114: 136537, 115: 96705, 116: 132241, 117: 149114, 118: 142149, 119: 125903, 120: 170727, 121: 110411, 122: 170331, 123: 139344, 124: 112008, 125: 116812, 126: 132826, 127: 166295, 128: 63106, 129: 143623, 130: 124039, 131: 145059, 132: 147832, 133: 82340, 134: 74759, 135: 26121, 136: 114736, 137: 130254, 138: 57289, 139: 59223, 140: 123726, 141: 26128, 142: 128265, 143: 167558, 144: 124395, 145: 111523, 146: 98550, 147: 113770, 148: 144822, 149: 150999, 150: 109590, 151: 103538, 152: 118779, 153: 118832, 154: 150335, 155: 135165, 156: 130960, 157: 119753, 158: 31489, 159: 113199, 160: 117265, 161: 154714, 162: 137691, 163: 138003, 164: 121135, 165: 122398, 166: 152754, 167: 90082, 168: 130379, 169: 158446, 170: 125764, 171: 70028, 172: 149357, 173: 132826, 174: 105630, 175: 104699, 176: 157839, 177: 145296, 178: 69535, 179: 107745, 180: 118281, 181: 28582, 182: 142240, 183: 79775, 184: 72252, 185: 136223, 186: 126703, 187: 38362, 188: 52801, 189: 134918, 190: 147286, 191: 149821, 192: 149724, 193: 22322, 194: 149401, 195: 119483, 196: 125257, 197: 148117, 198: 154734, 199: 94446, 200: 146756, 201: 121311, 202: 126524, 203: 110448, 204: 157205, 205: 115776, 206: 115138, 207: 107787, 208: 165252, 209: 114801, 210: 140779, 211: 117016, 212: 117526, 213: 139959, 214: 162428, 215: 128615, 216: 106229, 217: 131731, 218: 139053, 219: 117475, 220: 125764, 221: 122557, 222: 122459, 223: 140350, 224: 78686, 225: 149340, 226: 117947, 227: 87142, 228: 78050, 229: 142982, 230: 84443, 231: 170420, 232: 130798, 233: 152906, 234: 146416, 235: 129583, 236: 142811, 237: 134407, 238: 131344, 239: 136949, 240: 86774, 241: 100563, 242: 101832, 243: 62394, 244: 112416, 245: 135256, 246: 113307, 247: 135695, 248: 34846, 249: 103668, 250: 50128, 251: 133148, 252: 151099, 253: 121966, 254: 134970, 255: 135628, 256: 161466, 257: 152009, 258: 99973, 259: 51453, 260: 148436, 261: 44481, 262: 138224, 263: 171302, 264: 118610, 265: 67311, 266: 29964, 267: 131823, 268: 109847, 269: 71472, 270: 152893, 271: 156132, 272: 142087, 273: 138654, 274: 121061, 275: 89904, 276: 146542, 277: 129455, 278: 128030, 279: 139280, 280: 93145, 281: 115388, 282: 214789, 283: 191616, 284: 174960, 285: 167235, 286: 199934, 287: 160339, 288: 198108, 289: 166765, 290: 156568, 291: 221269, 292: 187646, 293: 158964, 294: 189816, 295: 166157, 296: 157177, 297: 185491, 298: 178930, 299: 184259, 300: 182204, 301: 164533, 302: 163064, 303: 193462, 304: 186682, 305: 184849, 306: 186147, 307: 194711, 308: 203882, 309: 199309, 310: 209576, 311: 190209, 312: 161195, 313: 196264, 314: 178169, 315: 169964, 316: 194954, 317: 177658, 318: 156931, 319: 185681, 320: 176293, 321: 179300, 322: 212056, 323: 184713, 324: 159031, 325: 195873, 326: 168035, 327: 166451, 328: 162119, 329: 185790, 330: 174786, 331: 204270, 332: 210878, 333: 180574, 334: 211765, 335: 170054, 336: 177038, 337: 209537, 338: 168240, 339: 165532, 340: 161143, 341: 175992, 342: 190610, 343: 205674, 344: 175424, 345: 161880, 346: 199953, 347: 191301, 348: 205061, 349: 197993, 350: 176271, 351: 184078, 352: 213940, 353: 204576, 354: 191350, 355: 191810, 356: 187585, 357: 156983, 358: 205695, 359: 183781, 360: 195718, 361: 179393, 362: 227209, 363: 194673, 364: 163248, 365: 212221, 366: 162981, 367: 167536, 368: 176193, 369: 207305, 370: 179184, 371: 201434, 372: 202186, 373: 207851, 374: 208546, 375: 166922, 376: 198111, 377: 191660, 378: 173832, 379: 202045, 380: 212142, 381: 160183, 382: 198611, 383: 212248, 384: 171732, 385: 191394, 386: 196163, 387: 188460, 388: 208191, 389: 174055, 390: 168411, 391: 220311, 392: 167984, 393: 212482, 394: 180211, 395: 174269, 396: 155879, 397: 183141, 398: 174269, 399: 213011, 400: 155004, 401: 166820, 402: 174073, 403: 183912, 404: 177877, 405: 206637, 406: 176819, 407: 156439, 408: 171527, 409: 190476, 410: 159280, 411: 209310, 412: 206599, 413: 206687, 414: 199259, 415: 195829, 416: 196725, 417: 178677, 418: 177629, 419: 158339, 420: 206039, 421: 190900, 422: 193335, 423: 181600, 424: 190724, 425: 164701, 426: 177676, 427: 179327, 428: 197783, 429: 204455, 430: 185383, 431: 179847, 432: 170461, 433: 182450, 434: 182027, 435: 190041, 436: 181136, 437: 174573, 438: 170949, 439: 176733, 440: 170756, 441: 201246, 442: 219599, 443: 155017, 444: 217106, 445: 189574, 446: 182649, 447: 162595, 448: 168008, 449: 204706, 450: 206129, 451: 182697, 452: 155931, 453: 198120, 454: 229580, 455: 220816, 456: 196219, 457: 189701, 458: 189989, 459: 218426, 460: 199052, 461: 188058, 462: 166885, 463: 201498, 464: 175885, 465: 153049, 466: 186005, 467: 162356, 468: 207284, 469: 186758, 470: 164239, 471: 197685, 472: 226973, 473: 186160, 474: 166468, 475: 173678, 476: 203698, 477: 177089, 478: 163434, 479: 208524, 480: 208401, 481: 176373, 482: 153215, 483: 185990, 484: 171870, 485: 200960, 486: 165544, 487: 198436, 488: 195776, 489: 169333, 490: 218665, 491: 172737, 492: 158292, 493: 197910, 494: 189297, 495: 198770, 496: 163273, 497: 219232, 498: 164520, 499: 160639, 500: 165064, 501: 174270, 502: 184113, 503: 174947, 504: 153240, 505: 222605, 506: 184647, 507: 218225, 508: 187115, 509: 176122, 510: 171389, 511: 156060, 512: 190989, 513: 159462, 514: 203861, 515: 225322, 516: 186897, 517: 233980, 518: 176606, 519: 187502, 520: 157542, 521: 202138, 522: 159318, 523: 202986, 524: 159900, 525: 197838, 526: 200283, 527: 194249, 528: 185388, 529: 204429, 530: 172235, 531: 159824, 532: 212301, 533: 173627, 534: 189027, 535: 175561, 536: 167229, 537: 202206, 538: 208135, 539: 176689, 540: 175953, 541: 202282, 542: 212154, 543: 188270, 544: 200999, 545: 171064, 546: 156585, 547: 157428, 548: 169392, 549: 161253, 550: 178753, 551: 181806, 552: 172075, 553: 165752, 554: 200259, 555: 154164, 556: 180065, 557: 203064, 558: 176801, 559: 220436, 560: 194427, 561: 189878, 562: 200625, 563: 171556, 564: 217636, 565: 206278, 566: 185942, 567: 211781, 568: 182267, 569: 199411, 570: 164851, 571: 225320, 572: 184391, 573: 198397, 574: 202933, 575: 189714, 576: 182871, 577: 231591, 578: 173481, 579: 167568, 580: 169133, 581: 178696, 582: 183118, 583: 200293, 584: 194410, 585: 167599, 586: 206540, 587: 170383, 588: 162825, 589: 156372}
        global combovalues
        combovalues=[]
        combovaluesutf8=[]
        for key,value in municipality_name.items():
            combovalues.append(value.encode('utf-8').strip())
        self.dlg.comboGemeentes.clear()
        for combovalue in combovalues:
            combovaluesutf8.append(combovalue.decode('utf-8'))
        self.dlg.comboGemeentes.addItems(combovaluesutf8)
        global selectedmunicipality
        global s
        s = QSettings()
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ZoomToBelgium_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&ZoomToBelgium')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'ZoomToBelgium')
        self.toolbar.setObjectName(u'ZoomToBelgium')
        self.dlg.button_box.accepted.connect(self.savesettings)



    def add_action(
        # the action for the menu items
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=False,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)
        return action

    def add_action_toolbar(
        # The action for the toolbar button
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=False,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        icon = QIcon(icon_path)
        actiontoolbar = QAction(icon, text, parent)
        actiontoolbar.triggered.connect(callback)
        actiontoolbar.setEnabled(enabled_flag)

        if status_tip is not None:
            actiontoolbar.setStatusTip(status_tip)

        if whats_this is not None:
            actiontoolbar.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(actiontoolbar)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                actiontoolbar)

        self.actions.append(actiontoolbar)
        return actiontoolbar

    def initGui(self):
        icon_path = ':/plugins/ZoomToBelgium/icon.png'
        settings_icon_path = ':/plugins/ZoomToBelgium/settings.png'
        self.add_action_toolbar(
            icon_path,
            text=self.tr(u'Zoom to Municipality'),
            callback=self.run,
            parent=self.iface.mainWindow())
        self.add_action(
            icon_path,
            text=self.tr(u'Zoom to Municipality'),
            callback=self.run,
            parent=self.iface.mainWindow())
        self.add_action(
            settings_icon_path,
            text=self.tr(u'Select Municipality'),
            callback=self.opensettings,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&ZoomToBelgium'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def nomunicipalityselected(self):
        self.opensettings()
        
    def zoomtomunicipality(self, id):
        canvas = self.iface.mapCanvas()
        PROJECTsrs = canvas.mapSettings().destinationCrs()
        try:
            if not canvas.hasCrsTransformEnabled():
                canvas.setCrsTransformEnabled(True)
        except:
            pass
        my_crs = QgsCoordinateReferenceSystem(31370)
        canvas.setDestinationCrs(my_crs)

        selectedmunicipality=s.value("zoomtobelgium/municipality", 518)
        selectedmunicipality_int=int(selectedmunicipality[0])
        xmax_setting=municipality_xmax[selectedmunicipality_int]+100
        xmin_setting=municipality_xmin[selectedmunicipality_int]-100
        ymax_setting=municipality_ymax[selectedmunicipality_int]+100
        ymin_setting=municipality_ymin[selectedmunicipality_int]-100

        canvas.setExtent(QgsRectangle(xmin_setting,ymin_setting,xmax_setting,ymax_setting))

        canvas.setDestinationCrs(PROJECTsrs)
        canvas.refresh()
    
    def opensettings(self):
        selectedmunicipality=[]
        selectedmunicipality=s.value("zoomtobelgium/municipality")
        if len(selectedmunicipality)==0:
            selectedmunicipality.append(518)
        try:
            selectedmunicipalityindex=municipality_name.keys().index(int(selectedmunicipality[0]))
        except:
            selectedmunicipalityindex=list(municipality_name).index(int(selectedmunicipality[0]))
        self.dlg.comboGemeentes.setCurrentIndex(selectedmunicipalityindex)
        introsubtext=self.tr(u'Select Municipality')
        introtext=u'<html><head/><body><p><span style=" font-size:16pt;">'+introsubtext+'</span></p></body></html>'
        self.dlg.intro.setText(introtext.replace("&lt;","<").replace("&gt;",">").replace("&quot;",'"'))
        #self.dlg.intro.setHtml(introtext)
        self.dlg.show()
        
    def savesettings(self):
        s.setValue("zoomtobelgium/municipality", self.searchmunicipality(municipality_name,self.dlg.comboGemeentes.currentText().strip()))

    def searchmunicipality(self,list,search_municipality):
        try:
            return [id for id,municipality in list.iteritems() if municipality == search_municipality]
        except:
            return [id for id,municipality in list.items() if municipality == search_municipality]

    def run(self):
        selectedmunicipality=s.value("zoomtobelgium/municipality", 0)
        if selectedmunicipality=="" or selectedmunicipality==0 or selectedmunicipality is None:
            self.nomunicipalityselected()
        else:
            self.zoomtomunicipality(selectedmunicipality)
