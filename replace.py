# -*- coding: utf-8 -*-
import re
s = r'''\documentclass[10pt,a5paper]{book}
\usepackage[latin1]{inputenc}
\usepackage{graphicx}
\usepackage{hyperref}
\graphicspath{{./figs/}}
\let\endtitlepage\relax
%\usepackage{biblatex}
%\addbibresource{C:/Users/Lois/Documents/Thesis/library.bib}
%\bibliography{C:/Users/Lois/Documents/Thesis/library.bib} % or
%\usepackage[           
%  backend=biber,
%  style=archaeologie,
%]{biblatex} 
%\addbibresource{/../library.bib}
%\usepackage{natbib}
%\usepackage{qrcode}
%\DeclareCiteCommand{\citepath}
%  {\boolfalse{citetracker}%
%   \boolfalse{pagetracker}%
%   \usebibmacro{prenote}}
%  {\thefield{file}}
%  {\multicitedelim}
%  {\usebibmacro{postnote}}
%\DeclareCiteCommand{\citeimg}
%  {\boolfalse{citetracker}%
%   \boolfalse{pagetracker}%
%   \usebibmacro{prenote}}
%  {\includegraphics[scale=1]{\thefield{file}}
%  {\multicitedelim}
%  {\usebibmacro{postnote}}

\begin{document}

\begin{titlepage}
	
	
	\title{Birds of Finland - Suomen linnut}
	\date{}
	
	
	\author{Lois Overvoorde}
	
	\maketitle
	\thispagestyle{empty}
	
	\begin{center}
		\includegraphics[width=0.9\textwidth]{Hazel_grouse.png}
	\end{center}
	
\end{titlepage}


%\citeauthor{Hazel_grouse}
%\cite{Hazel_grouse}
%\citepath{HazelGrouse}
%\citepath2{Hazel_grouse}
%\includegraphics[width=\linewidth]{./figs/Hazel_grouse.png}
%\citeimg{Hazel_grouse}

\chapter{Swans, geese and ducks}
Order: Anseriformes   Family: Anatidae

\section{Mute Swan - Kyhmyjoutsen}
\textit{Cygnus olor}
\includegraphics[width=5cm]{Mute_Swan.png}

\section{Tundra Swan - Pikkujoutsen}
\textit{Cygnus columbianus}
\includegraphics[width=5cm]{Tundra Swan.png}

\section{Whooper Swan - Laulujoutsen}
\textit{Cygnus cygnus}
\includegraphics[width=5cm]{Whooper Swan.png}

\section{Bean Goose - Metsähanhi}
\textit{Anser fabalis}
\includegraphics[width=5cm]{Bean Goose.png}

\section{Pink-footed Goose - Lyhytnokkahanhi}
\textit{Anser brachyrhynchus}
\includegraphics[width=5cm]{Pink-footed Goose.png}

Greater white-fronted goose, Anser albifrons

\section{Lesser White-fronted Goose - Kiljuhanhi}
\textit{Anser erythropus}
\includegraphics[width=5cm]{Lesser White-fronted Goose.png}

Greylag goose, Anser anser
Snow goose, Anser caerulescens

\section{Canada Goose - Kanadanhanhi}
\textit{Branta canadensis} I
\includegraphics[width=5cm]{Canada Goose.png}

Barnacle goose, Branta leucopsis
Brent goose, Branta bernicla
Red-breasted goose, Branta ruficollis
Ruddy shelduck, Tadorna ferruginea

\section{Common Shelduck - Ristisorsa}
\textit{Tadorna tadorna}
\includegraphics[width=5cm]{Common Shelduck.png}

Mandarin duck, Aix galericulata I

\section{Eurasian Wigeon - Haapana}
\textit{Anas penelope}
\includegraphics[width=5cm]{Eurasian Wigeon.png}

American wigeon, Mareca americana R

\section{Gadwall - Harmaasorsa}
\textit{Mareca strepera}
\includegraphics[width=5cm]{Gadwall.png}

\section{Common Teal - Tavi}
\textit{Anas crecca}
\includegraphics[width=5cm]{Common Teal.png}

Green-winged teal, Anas carolinensis R

\section{Mallard - Sinisorsa}
\textit{Anas platyrhynchos}
\includegraphics[width=5cm]{Mallard.png}

American black duck, Anas rubribes R

\section{Northern Pintail - Jouhisorsa}
\textit{Anas acuta}
\includegraphics[width=5cm]{Northern Pintail.png}

\section{Garganey - Heinätavi}
\textit{Anas querquedula}
\includegraphics[width=5cm]{Garganey.png}

Blue-winged teal, Spatula discors R

\section{Northern Shoveler - Lapasorsa}
\textit{Anas clypeata}
\includegraphics[width=5cm]{Northern Shoveler.png}

Red-crested pochard, Netta rufina R

\section{Common Pochard - Punasotka}
\textit{Aythya ferina}
\includegraphics[width=5cm]{Common Pochard.png}

Ring-necked duck, Aythya collaris R
Ferruginous duck, Aythya nyroca R

\section{Tufted Duck - Tukkasotka}
\textit{Aythya fuligula}
\includegraphics[width=5cm]{Tufted Duck.png}

\section{Greater Scaup - Lapasotka}
\textit{Aythya marila}
\includegraphics[width=5cm]{Greater Scaup.png}

\section{Lesser Scaup - }
\textit{Aythya affinis}
\includegraphics[width=5cm]{Lesser Scaup.png}

\section{Common Eider - Haahka}
\textit{Somateria mollissima}
\includegraphics[width=5cm]{Common Eider.png}

\section{King Eider - Kyhmyhaahka}
\textit{Somateria spectabilis}
\includegraphics[width=5cm]{King Eider.png}

Steller's eider, Polysticta stelleri
Harlequin duck, Histrionicus histrionicus R

\section{Long-tailed duck - Alli}
\textit{Clangula hyemalis}
\includegraphics[width=5cm]{Long-tailed duck.png}

\section{Black Scoter (Common Scoter) - Mustalintu}
\textit{Melanitta nigra}
\includegraphics[width=5cm]{Black Scoter.png}

Surf scoter, Melanitta perspicillata R

\section{White-winged Scoter (Velvet Scoter) - Pilkkasiipi}
\textit{Melanitta fusca}
\includegraphics[width=5cm]{White-winged Scoter.png}

\section{Common Goldeneye - Telkkä}
\textit{Bucephala clangula}
\includegraphics[width=5cm]{Common Goldeneye.png}

\section{Smew - }
\textit{Mergellus albellus}
\includegraphics[width=5cm]{Smew.png}

Red-breasted merganser, Mergus serrator
Goosander, Mergus merganser
Ruddy duck, Oxyura jamaicensis I R





\chapter{Grouse}
Order: Galliformes   Family: Tetraonidae

\section{Hazel Grouse - Pyy}
\textit{Bonasa bonasia}
\includegraphics[width=5cm]{Hazel_grouse.png}

\section{Rock Ptarmigan - Kiiruna}
\textit{Lagopus mutus}
\includegraphics[width=5cm]{Rock_Ptarmigan.png}

\section{Black Grouse - Teeri}
\textit{Tetrao tetrix}
\includegraphics[width=5cm]{Black_Grouse.png}

\section{Willow Ptarmigan - Riekko}
\textit{Lagopus lagopus}
\includegraphics[width=5cm]{Willow Ptarmigan.png}

\section{Western Capercaillie - Metso; Koppelo}
\textit{Tetrao urogallus}
\includegraphics[width=5cm]{Western Capercaillie.png}



\chapter{Pheasants and partridges}
Order: Galliformes   Family: Phasianidae

\section{Grey Partridge - Peltopyy}
\textit{Perdix perdix}
\includegraphics[width=5cm]{Grey Partridge.png}

\section{Common Quail - Viiriäinen}
\textit{Coturnix coturnix}
\includegraphics[width=5cm]{Common Quail.png}

\section{Common Pheasant - Fasaani}
\textit{Phasianus colchicus} I 
\includegraphics[width=5cm]{Common Pheasant.png}





\chapter{Divers}
Order: Gaviiformes   Family: Gaviidae

\section{Red-throated Loon (Red-throated Diver) - Kaakkuri}
\textit{Gavia stellata}
\includegraphics[width=5cm]{Red-throated Loon.png}

\section{Arctic Loon (Black-throated Diver) - Kuikka}
\textit{Gavia arctica}
\includegraphics[width=5cm]{Arctic Loon.png}

Great northern diver, Gavia immer R
Yellow-billed diver, Gavia adamsii






\chapter{Grebes}
Order: Podicipediformes   Family: Podicipedidae

Little grebe, Tachybaptus ruficollis

\section{Great Crested Grebe - Silkkiuikku}
\textit{Podiceps cristatus}
\includegraphics[width=5cm]{Great Crested Grebe.png}

\section{Red-necked Grebe - Härkälintu}
\textit{Podiceps grisegena}
\includegraphics[width=5cm]{Red-necked Grebe.png}

\section{Horned Grebe - Mustakurkku-uikku}
\textit{Podiceps auritus}
\includegraphics[width=5cm]{Horned Grebe.png}

\section{Black-necked Grebe - Mustakaulauikku}
\textit{Podiceps nigricollis}
\includegraphics[width=5cm]{Black-necked Grebe.png} R





\chapter{Shearwaters and petrels}
Order: Procellariiformes   Family: Procellariidae

Northern fulmar, Fulmarus glacialis R
Sooty shearwater, Ardenna griseus R
Manx shearwater, Puffinus puffinus R






\chapter{Storm petrels}
Order: Procellariiformes   Family: Hydrobatidae

European storm petrel, Hydrobates pelagicus R
Leach's storm petrel, Oceanodroma leucorhoa R
Band-rumped storm petrel, Oceanodroma castro R




\chapter{Gannets}
Order: Suliformes   Family: Sulidae

Northern gannet, Morus bassanus R




\chapter{Cormorants}
Order: Suliformes   Family: Phalacrocoracidae

\section{Great Cormorant - Merimetso}
\textit{Phalacrocorax carbo}
\includegraphics[width=5cm]{Great Cormorant.png}

European shag, Phalacrocorax aristotelis R





\chapter{Pelicans}
Order: Pelecaniformes   Family: Pelecanidae

Great white pelican, Pelecanus onocrotalus H R




\chapter{Bitterns, herons and egrets}
Order: Pelecaniformes   Family: Ardeidae

Great bittern, Botaurus stellaris
Little bittern, Ixobrychus minutus R
Black-crowned night heron, Nycticorax nycticorax R
Cattle egret, Bubulcus ibis R
Squacco heron, Ardeola ralloides R
Little egret, Egretta garzetta R
Great egret, Egretta alba

\section{Grey Heron - Harmaahaikara}
\textit{Ardea cinerea}
\includegraphics[width=5cm]{Grey Heron.png}

Purple heron, Ardea purpurea R





\chapter{Ibises and spoonbills}
Order: Pelecaniformes   Family: Threskiornithidae

Glossy ibis, Plegadis falcinellus R
Eurasian spoonbill, Platalea leucorodia R




\chapter{Storks}
Order: Ciconiiformes   Family: Ciconiidae

Black stork, Ciconia nigra
White stork, Ciconia ciconia




\chapter{Kites, hawks and eagles}
Order: Accipitriformes   Family: Accipitridae

\section{European Honey-buzzard - Mehiläishaukka}
\textit{Pernis apivorus}
\includegraphics[width=5cm]{European Honey-buzzard.png}

\section{Black Kite - Haarahaukka}
\textit{Milvus migrans}
\includegraphics[width=5cm]{Black Kite.png}

Red kite, Milvus milvus R
Pallas's fish eagle, Haliaeetus leucoryphus H R

\section{White-tailed Eagle - Merikotka}
\textit{Haliaeetus albicilla}
\includegraphics[width=5cm]{White-tailed Eagle.png}

Egyptian vulture, Neophron percnopterus R
Eurasian griffon vulture, Gyps fulvus R
Short-toed snake eagle, Circaetus gallicus R

\section{Western Marsh Harrier - Ruskosuohaukka}
\textit{Circus aeruginosus}
\includegraphics[width=5cm]{Western Marsh-Harrier.png}

\section{Northern Harrier (Hen Harrier) - Sinisuohaukka}
\textit{Circus cyaneus}
\includegraphics[width=5cm]{Northern Harrier.png}

Pallid harrier, Circus macrourus R

\section{Montagu's Harrier - Niittysuohaukka}
\textit{Circus pygargus}
\includegraphics[width=5cm]{Montagu's Harrier.png}

\section{Northern Goshawk - Kanahaukka}
\textit{Accipiter gentilis}
\includegraphics[width=5cm]{Northern Goshawk.png}

\section{Eurasian Sparrowhawk - Varpushaukka}
\textit{Accipiter nisus}
\includegraphics[width=5cm]{Eurasian Sparrowhawk.png}

\section{Common Buzzard - Hiirihaukka}
\textit{Buteo buteo}
\includegraphics[width=5cm]{Common Buzzard.png}

Long-legged buzzard, Buteo rufinus R

\section{Rough-legged Hawk (Rough-legged Buzzard) - Piekana}
\textit{Buteo lagopus}
\includegraphics[width=5cm]{Rough-legged Hawk.png}

Lesser spotted eagle, Clanga pomarina R

\section{Greater Spotted Eagle - Kiljukotka}
\textit{Aquila clanga}
\includegraphics[width=5cm]{Greater Spotted Eagle.png}

Steppe eagle, Aquila nipalensis R
Eastern imperial eagle, Aquila heliaca R

\section{Golden Eagle - Maakotka}
\textit{Aquila chrysaetos}
\includegraphics[width=5cm]{Golden Eagle.png}

Booted eagle, Hieraaetus pennatus R






\chapter{Osprey}
Order: Accipitriformes   Family: Pandionidae

\section{Osprey - Kalasääski}
\textit{Pandion haliaetus}
\includegraphics[width=5cm]{Osprey.png}






\chapter{Falcons}
Order: Falconiformes   Family: Falconidae

Lesser kestrel, Falco naumanni R

\section{Common Kestrel - Tuulihaukka}
\textit{Falco tinnunculus}
\includegraphics[width=5cm]{Common Kestrel.png}

Red-footed falcon, Falco vespertinus

\section{Merlin - Ampuhaukka}
\textit{Falco columbarius}
\includegraphics[width=5cm]{Merlin.png}

\section{Eurasian Hobby - Nuolihaukka}
\textit{Falco subbuteo}
\includegraphics[width=5cm]{Eurasian Hobby.png}

Eleonora's falcon, Falco eleonorae R
Saker falcon, Falco cherrug R

\section{Gyrfalcon (Gyr Falcon) - Tunturihaukka}
\textit{Falco rusticolus}
\includegraphics[width=5cm]{Gyrfalcon.png}

\section{Peregrine Falcon - Muuttohaukka}
\textit{Falco peregrinus}
\includegraphics[width=5cm]{Peregrine Falcon.png}





\chapter{Rails, crakes, gallinules and coots}
Order: Gruiformes   Family: Rallidae

\section{Water Rail - Luhtakana}
\textit{Rallus aquaticus}
\includegraphics[width=5cm]{Water Rail.png}

\section{Spotted Crake - Luhtahuitti}
\textit{Porzana porzana}
\includegraphics[width=5cm]{Spotted Crake.png}

Little crake, Porzana parva
Baillon's crake, Porzana pusilla R

\section{Corn Crake - Ruisrääkkä}
\textit{Crex crex}
\includegraphics[width=5cm]{Corn Crake.png}

Common moorhen, Gallinula chloropus
Allen's gallinule, Porphyrio alleni R

\section{Common Coot (Eurasian coot) - Nokikana}
\textit{Fulica atra}
\includegraphics[width=5cm]{Common Coot.png}




\chapter{Cranes}
Order: Gruiformes   Family: Gruidae

\section{Common Crane - Kurki}
\textit{Grus grus}
\includegraphics[width=5cm]{Common Crane.png}

Demoiselle crane, Grus virgo R





\chapter{Bustards}
Order: Otidiformes   Family: Otididae

Little bustard, Tetrax tetrax R
Macqueen's bustard, Chlamydotis macqueenii H R
Great bustard, Otis tarda H R






\chapter{Oystercatchers}
Order: Charadriiformes   Family: Haematopodidae

\section{Eurasian Oystercatcher - Meriharakka}
\textit{Haematopus ostralegus}
\includegraphics[width=5cm]{Eurasian Oystercatcher.png}





\chapter{Avocets and stilts}
Order: Charadriiformes   Family: Recurvirostridae

Black-winged stilt, Himantopus himantopus R
Pied avocet, Recurvirostra avosetta




\chapter{Thick-knees}
Order: Charadriiformes   Family: Burhinidae

Eurasian stone-curlew, Burhinus oedicnemus R



\chapter{Pratincoles and coursers}
Order: Charadriiformes   Family: Glareolidae

Cream-coloured courser, Cursorius cursor R
Collared pratincole, Glareola pratincola R
Black-winged pratincole, Glareola nordmanni R



\chapter{Plovers and lapwings}
Order: Charadriiformes   Family: Charadriidae

\section{Little Ringed Plover - Pikkutylli}
\textit{Charadrius dubius}
\includegraphics[width=5cm]{Little Ringed Plover.png}

\section{Common Ringed Plover - Tylli}
\textit{Charadrius hiaticula}
\includegraphics[width=5cm]{Common Ringed Plover.png}

Kentish plover, Charadrius alexandrinus R
Greater sand plover, Charadrius leschenaultii R
Caspian plover, Charadrius asiaticus
Oriental plover, Charadrius veredus R

\section{Eurasian Dotterel - }
\textit{Eudromias morinellus}
\includegraphics[width=5cm]{Eurasian Dotterel.png}

Pacific golden plover, Pluvialis fulva R

\section{European Golden-Plover - Kapustarinta}
\textit{Pluvialis apricaria}
\includegraphics[width=5cm]{European Golden-Plover.png}

Grey plover, Pluvialis squatarola
Sociable lapwing, Vanellus gregarius R
White-tailed lapwing, Vanellus leucurus R

\section{Northern Lapwing - Töyhtöhyyppä}
\textit{Vanellus vanellus}
\includegraphics[width=5cm]{Northern Lapwing.png}




\chapter{Sandpipers and allies}
Order: Charadriiformes   Family: Scolopacidae

Red knot, Calidris canutus
Sanderling, Calidris alba
Red-necked stint, Calidris ruficollis R
Little stint, Calidris minuta

\section{Temminck's Stint - Lapinsirri}
\textit{Calidris temminckii}
\includegraphics[width=5cm]{Temminck's Stint.png}

Least sandpiper, Calidris minutilla H R
White-rumped sandpiper, Calidris fuscicollis R
Baird's sandpiper, Calidris bairdii R
Pectoral sandpiper, Calidris melanotos R
Sharp-tailed sandpiper, Calidris acuminata R
Curlew sandpiper, Calidris ferruginea
Stilt sandpiper, Calidris himantopus R

\section{Purple Sandpiper - Merisirri}
\textit{Calidris maritima}
\includegraphics[width=5cm]{Purple Sandpiper.png}

\section{Dunlin - Suosirri}
\textit{Calidris alpina}
\includegraphics[width=5cm]{Dunlin.png}

\section{Broad-billed Sandpiper - Jänkäsirriäinen}
\textit{Limicola falcinellus}
\includegraphics[width=5cm]{Broad-billed Sandpiper.png}

Buff-breasted sandpiper, Calidris subruficollis R

\section{Ruff - Suokukko}
\textit{Philomachus pugnax}
\includegraphics[width=5cm]{Ruff.png}

\section{Jack Snipe - Jänkäkurppa}
\textit{Lymnocryptes minimus}
\includegraphics[width=5cm]{Jack Snipe.png}

\section{Common Snipe - Taivaanvuohi}
\textit{Gallinago gallinago}
\includegraphics[width=5cm]{Common Snipe.png}

Great snipe, Gallinago media
Long-billed dowitcher, Limnodromus scolopaceus R

\section{Eurasian Woodcock - Lehtokurppa}
\textit{Scolopax rusticola}
\includegraphics[width=5cm]{Eurasian Woodcock.png}

\section{Black-tailed Godwit - Mustapyrstökuiri}
\textit{Limosa limosa}
\includegraphics[width=5cm]{Black-tailed Godwit.png}

\section{Bar-tailed Godwit - Punakuiri}
\textit{Limosa lapponica}
\includegraphics[width=5cm]{Bar-tailed Godwit.png}

Little curlew, Numenius minutus R

\section{Whimbrel - Pikkukuovi}
\textit{Numenius phaeopus}
\includegraphics[width=5cm]{Whimbrel.png}

\section{Eurasian Curlew - Isokuovi}
\textit{Numenius arquata}
\includegraphics[width=5cm]{Eurasian Curlew.png}

\section{Spotted Redshank - Mustaviklo}
\textit{Tringa erythropus}
\includegraphics[width=5cm]{Spotted Redshank.png}

\section{Common Redshank - Punajalkaviklo}
\textit{Tringa totanus}
\includegraphics[width=5cm]{Common Redshank.png}

Marsh sandpiper, Tringa stagnatilis

\section{Common Greenshank - Valkoviklo}
\textit{Tringa nebularia}
\includegraphics[width=5cm]{Common Greenshank.png}

Lesser yellowlegs, Tringa flavipes R

\section{Green Sandpiper - Metsäviklo}
\textit{Tringa ochropus}
\includegraphics[width=5cm]{Green Sandpiper.png}

\section{Wood Sandpiper - Liro}
\textit{Tringa glareola}
\includegraphics[width=5cm]{Wood Sandpiper.png}

Willet, Tringa semipalmata R

\section{Terek Sandpiper - Rantakurvi}
\textit{Xenus cinereus}
\includegraphics[width=5cm]{Terek Sandpiper.png}

\section{Common Sandpiper - Rantasipi}
\textit{Actitis hypoleucos}
\includegraphics[width=5cm]{Common Sandpiper.png}

Spotted sandpiper, Actitis macularius R

\section{Ruddy Turnstone - Karikukko}
\textit{Arenaria interpres}
\includegraphics[width=5cm]{Ruddy Turnstone.png}

Wilson's phalarope, Phalaropus tricolor R

\section{Red-necked Phalarope - Vesipääsky}
\textit{Phalaropus lobatus}
\includegraphics[width=5cm]{Red-necked Phalarope.png}

Red phalarope, Phalaropus fulicarius R






































\chapter{Skuas}
Order: Charadriiformes   Family: Stercorariidae

Pomarine skua, Stercorarius pomarinus

\section{Parasitic Jaeger (Arctic skua) - }
\textit{Stercorarius parasiticus}
\includegraphics[width=5cm]{Parasitic Jaeger.png}

\section{Long-tailed Jaeger (Long-tailed Skua) - Tunturikihu}
\textit{Stercorarius longicaudus}
\includegraphics[width=5cm]{Long-tailed Jaeger.png}

Great skua, Stercorarius skua R








\chapter{Gulls, terns, and skimmers}
Order: Charadriiformes   Family: Laridae

Mediterranean gull, Ichthyaetus melanocephalus R
Laughing gull, Leucophaeus atricilla R
Franklin's gull, Leucophaeus pipixcan R

\section{Little Gull - Pikkulokki}
\textit{Larus minutus/Hydrocoloeus minutus}
\includegraphics[width=5cm]{Little Gull.png}

Sabine's gull, Xema sabini R

\section{Black-headed Gull - Naurulokki}
\textit{Larus ridibundus/Chroicocephalus ridibundus}
\includegraphics[width=5cm]{Black-headed Gull.png}

Slender-billed gull, Chroicocephalus genei R

\section{Common Gull - Kalalokki}
\textit{Larus canus}
\includegraphics[width=5cm]{Common Gull.png}

\section{Lesser Black-backed Gull - Selkälokki}
\textit{Larus fuscus}
\includegraphics[width=5cm]{Lesser Black-backed Gull.png}

Herring gull, Larus argentatus
Caspian gull, Larus cachinnans R
Yellow-legged gull, Larus michahellis R
Iceland gull, Larus glaucoides R

\section{Glaucous Gull - Isolokki}
\textit{Larus hyperboreus}
\includegraphics[width=5cm]{Glaucous Gull.png}

\section{Great Black-backed Gull - Merilokki}
\textit{Larus marinus}
\includegraphics[width=5cm]{Great Black-backed Gull.png}

Ross's gull, Rhodostethia rosea R

\section{Black-legged Kittiwake - Pikkukajava}
\textit{Rissa tridactyla}
\includegraphics[width=5cm]{Black-legged Kittiwake.png}

Ivory gull, Pagophila eburnea R
Gull-billed tern, Gelochelidon nilotica R

\section{Caspian Tern - Räyska}
\textit{Sterna caspia}
\includegraphics[width=5cm]{Caspian Tern.png}

Sandwich tern, Thalasseus sandvicensis

\section{Common Tern - Kalatiira}
\textit{Sterna hirundo}
\includegraphics[width=5cm]{Common Tern.png}

\section{Arctic Tern - Lapintiira}
\textit{Sterna paradisaea}
\includegraphics[width=5cm]{Arctic Tern.png}

\section{Little Tern - Pikkutiira}
\textit{Sterna albifrons}
\includegraphics[width=5cm]{Little Tern.png}

Whiskered tern, Chlidonias hybrida R

\section{Black Tern - Mustatiira}
\textit{Chlidonias niger}
\includegraphics[width=5cm]{Black Tern.png}

White-winged tern, Chlidonias leucopterus R





\chapter{Auks}
Order: Charadriiformes   Family: Alcidae

\section{Common Murre (Common Guillemot) - Etelänkiisla}
\textit{Uria aalge}
\includegraphics[width=5cm]{Common Murre.png}

\section{Thick-billed Murre (Brünnich's Guillemot) - Pohjankiisla}
\textit{Uria lomvia}
\includegraphics[width=5cm]{Thick-billed Murre.png} R

\section{Razorbill - Ruokki}
\textit{Alca torda}
\includegraphics[width=5cm]{Razorbill.png}

\section{Black Guillemot - Riskilä}
\textit{Cepphus grylle}
\includegraphics[width=5cm]{Black Guillemot.png}

Little auk, Alle alle
Atlantic puffin, Fratercula arctica R







\chapter{Sandgrouse}
Order: Pterocliformes   Family: Pteroclidae

Pallas's sandgrouse, Syrrhaptes paradoxus R




\chapter{Pigeons and doves}
Order: Columbiformes   Family: Columbidae

Rock dove, Columba livia I

\section{Stock Pigeon (Stock Dove) - Uuttukyyhky}
\textit{Columba oenas}
\includegraphics[width=5cm]{Stock Pigeon.png}

\section{Common Wood Pigeon - Sepelkyyhky}
\textit{Columba palumbus}
\includegraphics[width=5cm]{Common Wood Pigeon.png}

\section{Eurasian Collared Dove - Turturikyyhky}
\textit{Streptopelia decaocto}
\includegraphics[width=5cm]{Eurasian Collared Dove.png}

European turtle dove, Streptopelia turtur
Oriental turtle dove, Streptopelia orientalis R



\chapter{Cuckoos}
Order: Cuculiformes   Family: Cuculidae

Great spotted cuckoo, Clamator glandarius H R

\section{Common Cuckoo - Käki}
\textit{Cuculus canorus}
\includegraphics[width=5cm]{Common Cuckoo.png}




\chapter{Barn owls}
Order: Strigiformes   Family: Tytonidae

Barn owl, Tyto alba R




\chapter{Typical owls}
Order: Strigiformes   Family: Strigidae

\section{Eurasian Eagle-Owl - Huuhkaja}
\textit{Bubo bubo}
\includegraphics[width=5cm]{Eurasian Eagle-Owl.png}

\section{Snowy Owl - Tunturipöllö}
\textit{Nyctea scandiaca/Bubo scandiacus}
\includegraphics[width=5cm]{Snowy Owl.png}

\section{Northern Hawk Owl - Hiiripöllö}
\textit{Surnia ulula}
\includegraphics[width=5cm]{Northern Hawk Owl.png}

\section{Eurasian Pygmy-Owl - Varpuspöllö}
\textit{Glaucidium passerinum}
\includegraphics[width=5cm]{Eurasian Pygmy-Owl.png}

Little owl, Athene noctua R

\section{Tawny Owl - Lehtopöllö}
\textit{Strix aluco}
\includegraphics[width=5cm]{Tawny Owl.png}

\section{Ural Owl - Viirupöllö}
\textit{Strix uralensis}
\includegraphics[width=5cm]{Ural Owl.png}

\section{Great Grey Owl - Lapinpöllö}
\textit{Strix nebulosa}
\includegraphics[width=5cm]{Great Grey Owl.png}

\section{Long-eared Owl - Sarvipöllö}
\textit{Asio otus}
\includegraphics[width=5cm]{Long-eared Owl.png}

\section{Short-eared Owl - Suopöllö}
\textit{Asio flammeus}
\includegraphics[width=5cm]{Short-eared Owl.png}

\section{Boreal Owl (Tengmalm's Owl) - Helmipöllö}
\textit{Aegolius funereus}
\includegraphics[width=5cm]{Boreal Owl.png}




\chapter{Nightjars}
Order: Caprimulgiformes   Family: Caprimulgidae

\section{Eurasian Nightjar (European nightjar) - Kehrääjä}
\textit{Caprimulgus europaeus}
\includegraphics[width=5cm]{Eurasian Nightjar.png}




\chapter{Swifts}
Order: Apodiformes   Family: Apodidae

White-throated needletail, Hirundapus caudacutus R

\section{Common Swift - Tervakirskuja}
\textit{Apus apus}
\includegraphics[width=5cm]{Common Swift.png}

Pallid swift, Apus pallidus R
Alpine swift, Apus melba R
White-rumped swift, Apus caffer R





\chapter{Kingfishers}
Order: Coraciiformes   Family: Alcedinidae

\section{Common Kingfisher - Kuningaskalastaja}
\textit{Alcedo atthis}
\includegraphics[width=5cm]{Common Kingfisher.png}






\chapter{Bee-eaters}
Order: Coraciiformes   Family: Meropidae

Blue-cheeked bee-eater, Merops persicus R
European bee-eater, Merops apiaster




\chapter{Rollers}
Order: Coraciiformes   Family: Coraciidae

European roller, Coracias garrulus




\chapter{Hoopoes}
Order: Coraciiformes   Family: Upupidae

Eurasian hoopoe, Upupa epops




\chapter{Woodpeckers}
Order: Piciformes   Family: Picidae

\section{Eurasian Wryneck - Käenpiika}
\textit{Jynx torquilla}
\includegraphics[width=5cm]{Eurasian Wryneck.png}

\section{Grey-faced Woodpecker (Grey-headed woodpecker) - Harmaapäätikka}
\textit{Picus canus}
\includegraphics[width=5cm]{Grey-faced Woodpecker.png}

\section{Eurasian Green Woodpecker - Vihertikka}
\textit{Picus viridis}
\includegraphics[width=5cm]{Eurasian Green Woodpecker.png} R

\section{Black Woodpecker - Palokärki}
\textit{Dryocopus martius}
\includegraphics[width=5cm]{Black Woodpecker.png}

\section{Great Spotted Woodpecker - Käpytikka}
\textit{Dendrocopos major}
\includegraphics[width=5cm]{Great Spotted Woodpecker.png}

\section{White-backed Woodpecker - Valkoselkätikka}
\textit{Dendrocopos leucotos}
\includegraphics[width=5cm]{White-backed Woodpecker.png}

\section{Lesser Spotted Woodpecker - Pikkutikka}
\textit{Dendrocopos minor/Dryobates minor}
\includegraphics[width=5cm]{Lesser Spotted Woodpecker.png}

\section{Eurasian Three-toed Woodpecker - Pohjantikka}
\textit{Picoides tridactylus}
\includegraphics[width=5cm]{Eurasian Three-toed Woodpecker.png}





\chapter{Larks}
Order: Passeriformes   Family: Alaudidae

Calandra lark, Melanocorypha calandra R
Bimaculated lark, Melanocorypha bimaculata R
Black lark, Melanocorypha yeltoniensis R
Greater short-toed lark, Calandrella brachydactyla R
Lesser short-toed lark, Alaudala rufescens R
Crested lark, Galerida cristata R

\section{Wood Lark - Kangaskiuru}
\textit{Lullula arborea}
\includegraphics[width=5cm]{Wood Lark.png}

\section{Sky Lark (Eurasian skylark) - Kiuru (Leivonen)}
\textit{Alauda arvensis}
\includegraphics[width=5cm]{Sky Lark.png}

White-winged lark, Alauda leucoptera R
Horned lark, Eremophila alpestris







\chapter{Swallows and martins}
Order: Passeriformes   Family: Hirundinidae

\section{Sand Martin - Törmäpääsky}
\textit{Riparia riparia}
\includegraphics[width=5cm]{Sand Martin.png}

Eurasian crag martin, Ptyonoprogne rupestris R

\section{Barn Swallow - Haarapääsky}
\textit{Hirundo rustica}
\includegraphics[width=5cm]{Barn Swallow.png}

Red-rumped swallow, Hirundo daurica R

\section{Northern House-Martin (Common House Martin) - Räystäspääsky}
\textit{Delichon urbicum}
\includegraphics[width=5cm]{Northern House-Martin.png}






\chapter{Pipits and wagtails}
Order: Passeriformes   Family: Motacillidae

Richard's pipit, Anthus richardi
Blyth's pipit, Anthus godlewskii R
Tawny pipit, Anthus campestris R
Olive-backed pipit, Anthus hodgsoni R

\section{Tree Pipit - Metsäkirvinen}
\textit{Anthus trivialis}
\includegraphics[width=5cm]{Tree Pipit.png}

Pechora pipit, Anthus gustavi R

\section{Meadow Pipit - Niittykirvinen}
\textit{Anthus pratensis}
\includegraphics[width=5cm]{Meadow Pipit.png}

\section{Red-throated Pipit - Lapinkirvinen}
\textit{Anthus cervinus}
\includegraphics[width=5cm]{Red-throated Pipit.png}

\section{Rock Pipit - }
\textit{Anthus petrosus}
\includegraphics[width=5cm]{Rock Pipit.png}

\section{Yellow Wagtail - VäsKeltavästäräkkitäräkki}
\textit{Motacilla flava}
\includegraphics[width=5cm]{Yellow Wagtail.png}

Citrine wagtail, Motacilla citreola

\section{Grey Wagtail - Vuorivästäräkki}
\textit{Motacilla cinerea}
\includegraphics[width=5cm]{Grey Wagtail.png}

\section{White Wagtail - Västäräkki}
\textit{Motacilla alba}
\includegraphics[width=5cm]{White Wagtail.png}




\chapter{Waxwings}
Order: Passeriformes   Family: Bombycillidae

\section{Bohemian Waxwing - Tilhi}
\textit{Bombycilla garrulus}
\includegraphics[width=5cm]{Bohemian Waxwing.png}




\chapter{Dippers}
Order: Passeriformes   Family: Cinclidae

\section{White-throated Dipper - Koskikara}
\textit{Cinclus cinclus}
\includegraphics[width=5cm]{White-throated Dipper.png}




\chapter{Wrens}
Order: Passeriformes   Family: Troglodytidae


\section{Winter Wren (Eurasian Wren) - Peukaloinen}
\textit{Troglodytes troglodytes}
\includegraphics[width=5cm]{Winter Wren.png}



\chapter{Accentors}
Order: Passeriformes   Family: Prunellidae

\section{Dunnock (Hedge Accentor) - Rautiainen}
\textit{Prunella modularis}
\includegraphics[width=5cm]{Hedge Accentor.png}

Siberian accentor, Prunella montanella R
Black-throated accentor, Prunella atrogularis R
Alpine accentor, Prunella collaris R




\chapter{Thrushes and allies}
Order: Passeriformes   Family: Turdidae

White's thrush, Zoothera dauma R
Swainson's thrush, Catharus ustulatus R
Ring ouzel, Turdus torquatus

\section{Eurasian Blackbird (Common Blackbird) - Mustarastas}
\textit{Turdus merula}
\includegraphics[width=5cm]{Eurasian Blackbird.png}

Eyebrowed thrush, Turdus obscurus R
Dusky thrush, Turdus naumanni R
Dark-throated thrush, Turdus ruficollis R

\section{Fieldfare - Räkättirastas}
\textit{Turdus pilaris}
\includegraphics[width=5cm]{Fieldfare.png}

\section{Song Thrush - Laulurastas}
\textit{Turdus philomelos}
\includegraphics[width=5cm]{Song Thrush.png}

\section{Redwing - Punakylkirastas}
\textit{Turdus iliacus}
\includegraphics[width=5cm]{Redwing.png}

\section{Mistle Thrush - Kulorastas}
\textit{Turdus viscivorus}
\includegraphics[width=5cm]{Mistle Thrush.png}




\chapter{Locustellid warblers}
Order: Passeriformes   Family: Locustellidae

Lanceolated warbler, Locustella lanceolata R

\section{Common Grasshopper-Warbler - Pensassirkkalintu}
\textit{Locustella naevia}
\includegraphics[width=5cm]{Common Grasshopper-Warbler.png}

\section{Eurasian River Warbler - Viitasirkkalintu}
\textit{Locustella fluviatilis}
\includegraphics[width=5cm]{Eurasian River Warbler.png}

Savi's warbler, Locustella luscinioides R


\chapter{Acrocephalid warblers}
Order: Passeriformes   Family: Acrocephalidae

Aquatic warbler, Acrocephalus paludicola R

\section{Sedge Warbler - Ruokokerttunen}
\textit{Acrocephalus schoenobaenus}
\includegraphics[width=5cm]{Sedge Warbler.png}

\section{Eurasian Reed-Warbler - Rytikerttunen}
\textit{Acrocephalus scirpaceus}
\includegraphics[width=5cm]{Eurasian Reed-Warbler.png}

\section{Marsh Warbler - Luhtakerttunen}
\textit{Acrocephalus palustris}
\includegraphics[width=5cm]{Marsh Warbler.png}

\section{Blyth's Reed-Warbler - Viitakerttunen}
\textit{Acrocephalus dumetorum}
\includegraphics[width=5cm]{Blyth's Reed-Warbler.png}

Paddyfield warbler, Acrocephalus agricola R

\section{Great Reed-Warbler - Rastaskerttunen}
\textit{Acrocephalus arundinaceus}
\includegraphics[width=5cm]{Great Reed-Warbler.png}

Thick-billed warbler, Iduna aedon R
Eastern olivaceous warbler, Iduna pallida R
Booted warbler, Iduna caligata R
Sykes's warbler, Iduna rama R

\section{Icterine Warbler - Kultarinta}
\textit{Hippolais icterina}
\includegraphics[width=5cm]{Icterine Warbler.png}


\chapter{Phylloscopid warblers}
Order: Passeriformes   Family: Phylloscopidae

Eastern crowned warbler, Phylloscopus coronatus R

\section{Greenish Warbler - Idänuunilintu}
\textit{Phylloscopus trochiloides}
\includegraphics[width=5cm]{Greenish Warbler.png}

\section{Arctic Warbler - Lapinuunilintu}
\textit{Phylloscopus borealis}
\includegraphics[width=5cm]{Arctic Warbler.png}

Pallas's leaf warbler, Phylloscopus proregulus
Yellow-browed warbler, Phylloscopus inornatus
Hume's leaf warbler, Phylloscopus humei R
Radde's warbler, Phylloscopus schwarzi R
Dusky warbler, Phylloscopus fuscatus R
Western Bonelli's warbler, Phylloscopus bonelli R
Eastern Bonelli's warbler, Phylloscopus orientalis R

\section{Wood Warbler - Sirittäjä}
\textit{Phylloscopus sibilatrix}
\includegraphics[width=5cm]{Wood Warbler.png}

\section{Eurasian Chiffchaff (Common Chiffchaff) - Tiltaltti}
\textit{Phylloscopus collybita}
\includegraphics[width=5cm]{Eurasian Chiffchaff.png}

\section{Willow Warbler - Pajulintu}
\textit{Phylloscopus trochilus}
\includegraphics[width=5cm]{Willow Warbler.png}


\chapter{Old World warblers}
Order: Passeriformes   Family: Sylviidae

\section{Eurasian Blackcap - Mustapääkertut}
\textit{Sylvia atricapilla}
\includegraphics[width=5cm]{Blackcap.png}

\section{Garden Warbler - Lehtokerttu}
\textit{Sylvia borin}
\includegraphics[width=5cm]{Garden Warbler.png}

\section{Barred Warbler - Kirjokerttu}
\textit{Sylvia nisoria}
\includegraphics[width=5cm]{Barred Warbler.png}

\section{Lesser Whitethroat - Hernekerttu}
\textit{Sylvia curruca}
\includegraphics[width=5cm]{Lesser Whitethroat.png}

\section{Common Whitethroat - Pensaskerttu}
\textit{Sylvia communis}
\includegraphics[width=5cm]{Common Whitethroat.png}

Asian desert warbler, Sylvia nana R
Dartford warbler, Sylvia undata R
Subalpine warbler, Sylvia cantillans R
Sardinian warbler, Sylvia melanocephala R
Rüppell's warbler, Sylvia ruppeli R




\chapter{Kinglets}
Order: Passeriformes   Family: Regulidae

\section{Goldcrest - Hippiäinen}
\textit{Regulus regulus}
\includegraphics[width=5cm]{Goldcrest.png}

Common firecrest, Regulus ignicapilla R





\chapter{Old World flycatchers}
Order: Passeriformes   Family: Muscicapidae

Rufous-tailed scrub robin, Cercotrichas galactotes R

\section{European Robin - Punarinta}
\textit{Erithacus rubecula}
\includegraphics[width=5cm]{European Robin.png}

\section{Thrush Nightingale - Satakieli}
\textit{Luscinia luscinia}
\includegraphics[width=5cm]{Thrush Nightingale.png}

Common nightingale, Luscinia megarhynchos R

\section{Bluethroat - Sinirinta}
\textit{Luscinia svecica}
\includegraphics[width=5cm]{Bluethroat.png}

Siberian rubythroat, Calliope calliope R
Red-flanked bluetail, Tarsiger cyanurus

\section{Black Redstart - Mustaleppälintu}
\textit{Phoenicurus ochruros}
\includegraphics[width=5cm]{Black Redstart.png}

\section{Common Redstart - Leppälintu}
\textit{Phoenicurus phoenicurus}
\includegraphics[width=5cm]{Common Redstart.png}

\section{Whinchat - Pensastasku}
\textit{Saxicola rubetra}
\includegraphics[width=5cm]{Whinchat.png}

Common stonechat, Saxicola torquatus R
Isabelline wheatear, Oenanthe isabellina R

\section{Northern Wheatear - Kivitasku}
\textit{Oenanthe oenanthe}
\includegraphics[width=5cm]{Northern Wheatear.png}

Pied wheatear, Oenanthe pleschanka R
Black-eared wheatear, Oenanthe hispanica R
Desert wheatear, Oenanthe deserti R
Common rock thrush, Monticola saxatilis R
Blue rock thrush, Monticola solitarius R

\section{Spotted Flycatcher - Harmaasieppo}
\textit{Muscicapa striata}
\includegraphics[width=5cm]{Spotted Flycatcher.png}

\section{Red-breasted Flycatcher - Pikkusieppo}
\textit{Ficedula parva}
\includegraphics[width=5cm]{Red-breasted Flycatcher.png}

Collared flycatcher, Ficedula albicollis R

\section{European Pied Flycatcher - Kirjosieppo}
\textit{Ficedula hypoleuca}
\includegraphics[width=5cm]{European Pied Flycatcher.png}










\chapter{Bearded reedling}
Order: Passeriformes   Family: Panuridae

Bearded reedling, Panurus biarmicus




\chapter{Long-tailed tits}
Order: Passeriformes   Family: Aegithalidae

\section{Long-tailed Tit - Pyrstötiainen}
\textit{Aegithalos caudatus}
\includegraphics[width=5cm]{Long-tailed Tit.png}


\chapter{Tits}
Order: Passeriformes   Family: Paridae

Marsh tit, Parus palustris R

\section{Willow Tit - Hömötiainen}
\textit{Poecile montanus}
\includegraphics[width=5cm]{Willow Tit.png}

\section{Siberian Tit (Grey-headed Chickadee) - Lapintiainen}
\textit{Poecile cinctus}
\includegraphics[width=5cm]{Siberian Tit.png}

\section{Crested Tit - Töyhtötiainen}
\textit{Lophophanes cristatus}
\includegraphics[width=5cm]{Crested Tit.png}

\section{Coal Tit - Kuusitiainen}
\textit{Periparus ater}
\includegraphics[width=5cm]{Coal Tit.png}

\section{Eurasian Blue Tit - Sinitiainen}
\textit{Cyanistes caeruleus}
\includegraphics[width=5cm]{Eurasian Blue Tit.png}

Azure tit, Parus cyanus R

\section{Great Tit - Talitiainen}
\textit{Parus major}
\includegraphics[width=5cm]{Great Tit.png}




\chapter{Nuthatches}
Order: Passeriformes   Family: Sittidae

Eurasian nuthatch, Sitta europaea





\chapter{Treecreepers}
Order: Passeriformes   Family: Certhiidae

\section{Eurasian Tree-Creeper - Puukiipijä}
\textit{Certhia familiaris}
\includegraphics[width=5cm]{Eurasian Tree-Creeper.png}



\chapter{Penduline tits}
Order: Passeriformes   Family: Remizidae

Eurasian penduline tit, Remiz pendulinus



\chapter{Old World orioles}
Order: Passeriformes   Family: Oriolidae

\section{Eurasian Golden Oriole - Kuhankeittäjä}
\textit{Oriolus oriolus}
\includegraphics[width=5cm]{Eurasian Golden-Oriole.png}




\chapter{Shrikes}
Order: Passeriformes   Family: Laniidae

Isabelline shrike, Lanius isabellinus R

\section{Red-backed Shrike - Valko-Pikkulepinkäinen}
\textit{Lanius collurio}
\includegraphics[width=5cm]{Red-backed Shrike.png}

Lesser grey shrike, Lanius minor

\section{Northern Shrike (Great Grey Shrike) - Isolepinkäinen (Lapinharakka)}
\textit{Lanius excubitor}
\includegraphics[width=5cm]{Northern Shrike.png}

Southern grey shrike, Lanius meridionalis R
Woodchat shrike, Lanius senator R
Masked shrike, Lanius nubicus R






\chapter{Jays, magpies, crows and ravens}
Order: Passeriformes   Family: Corvidae

\section{Eurasian Jay - Närhi}
\textit{Garrulus glandarius}
\includegraphics[width=5cm]{Eurasian Jay.png}

\section{Siberian Jay - Kuukkeli}
\textit{Perisoreus infaustus}
\includegraphics[width=5cm]{Siberian Jay.png}

\section{Black-billed Magpie (Common Magpie)- Harakka}
\textit{Pica pica}
\includegraphics[width=5cm]{Black-billed Magpie.png}

\section{Spotted Nutcracker - Pähkinähakki}
\textit{Nucifraga caryocatactes}
\includegraphics[width=5cm]{Spotted Nutcracker.png}

\section{Eurasian Jackdaw - Naakka}
\textit{Corvus monedula}
\includegraphics[width=5cm]{Eurasian Jackdaw.png}

Daurian jackdaw, Corvus dauuricus H R

\section{Rook - Mustavaris}
\textit{Corvus frugilegus}
\includegraphics[width=5cm]{Rook.png}

Hooded crow, Corvus cornix

\section{Common Raven - Korppi}
\textit{Corvus corax}
\includegraphics[width=5cm]{Common Raven.png}






\chapter{Starlings}
Order: Passeriformes   Family: Sturnidae

\section{Common Starling - Kottarainen}
\textit{Sturnus vulgaris}
\includegraphics[width=5cm]{Common Starling.png}

Rosy starling, Pastor roseus




\chapter{Sparrows}
Order: Passeriformes   Family: Passeridae

\section{House Sparrow - Varpunen}
\textit{Passer domesticus}
\includegraphics[width=5cm]{House Sparrow.png}

Spanish sparrow, Passer hispaniolensis R

\section{Eurasian Tree Sparrow - Pikkuvarpunen}
\textit{Passer montanus}
\includegraphics[width=5cm]{Eurasian Tree Sparrow.png}



\chapter{Finches}
Order: Passeriformes   Family: Fringillidae

\section{Chaffinch - Peippo}
\textit{Fringilla coelebs}
\includegraphics[width=5cm]{Chaffinch.png}

\section{Brambling - Järripeippo}
\textit{Fringilla montifringilla}
\includegraphics[width=5cm]{Brambling.png}

European serin, Serinus serinus
European greenfinch, Chloris chloris
European goldfinch, Carduelis carduelis
Eurasian siskin, Spinus spinus
Common linnet, Linaria cannabina
Twite, Linaria flavirostris
Common redpoll, Acanthis flammea
Arctic redpoll, Acanthis hornemanni
Two-barred crossbill, Loxia leucoptera
Common crossbill, Loxia curvirostra
Parrot crossbill, Loxia pytyopsittacus
Trumpeter finch, Bucanetes githagineus
Common rosefinch, Carpodacus erythrinus
Pine grosbeak, Pinicola enucleator
Eurasian bullfinch, Pyrrhula pyrrhula

\section{Hawfinch - Nokkavarpunen}
\textit{Coccothraustes coccothraustes}
\includegraphics[width=5cm]{Hawfinch.png}





\chapter{Longspurs and snow buntings}
Order: Passeriformes Family: Calcariidae

Lapland longspur, Calcarius lapponicus
Snow bunting, Plectrophenax nivalis




\chapter{Buntings, sparrows, seedeaters and allies}
Order: Passeriformes Family: Emberizidae

White-throated sparrow, Zonotrichia albicollis R
Black-faced bunting, Emberiza spodocephala R
Pine bunting, Emberiza leucocephalos R
Yellowhammer, Emberiza citrinella
Grey-necked bunting, Emberiza buchanani
Ortolan bunting, Emberiza hortulana
Cretzschmar's bunting, Emberiza caesia R
Rustic bunting, Emberiza rustica
Little bunting, Emberiza pusilla
Chestnut bunting, Emberiza rutila R
Yellow-breasted bunting, Emberiza aureola
Reed bunting, Emberiza schoeniclus
Black-headed bunting, Emberiza melanocephala R
Corn bunting, Emberiza calandra R


\bibliography{C:/Users/Lois/Documents/Thesis/library}
\bibliographystyle{Thesis}
\end{document}\documentclass[10pt,a5paper]{book}
\usepackage[latin1]{inputenc}
\usepackage{graphicx}
\usepackage{hyperref}
\graphicspath{{./figs/}}
\let\endtitlepage\relax
%\usepackage{biblatex}
%\addbibresource{C:/Users/Lois/Documents/Thesis/library.bib}
%\bibliography{C:/Users/Lois/Documents/Thesis/library.bib} % or
%\usepackage[           
%  backend=biber,
%  style=archaeologie,
%]{biblatex} 
%\addbibresource{/../library.bib}
%\usepackage{natbib}
%\usepackage{qrcode}
%\DeclareCiteCommand{\citepath}
%  {\boolfalse{citetracker}%
%   \boolfalse{pagetracker}%
%   \usebibmacro{prenote}}
%  {\thefield{file}}
%  {\multicitedelim}
%  {\usebibmacro{postnote}}
%\DeclareCiteCommand{\citeimg}
%  {\boolfalse{citetracker}%
%   \boolfalse{pagetracker}%
%   \usebibmacro{prenote}}
%  {\includegraphics[scale=1]{\thefield{file}}
%  {\multicitedelim}
%  {\usebibmacro{postnote}}

\begin{document}

\begin{titlepage}
	
	
	\title{Birds of Finland - Suomen linnut}
	\date{}
	
	
	\author{Lois Overvoorde}
	
	\maketitle
	\thispagestyle{empty}
	
	\begin{center}
		\includegraphics[width=0.9\textwidth]{Hazel_grouse.png}
	\end{center}
	
\end{titlepage}


%\citeauthor{Hazel_grouse}
%\cite{Hazel_grouse}
%\citepath{HazelGrouse}
%\citepath2{Hazel_grouse}
%\includegraphics[width=\linewidth]{./figs/Hazel_grouse.png}
%\citeimg{Hazel_grouse}

\chapter{Swans, geese and ducks}
Order: Anseriformes   Family: Anatidae

\section{Mute Swan - Kyhmyjoutsen}
\textit{Cygnus olor}
\includegraphics[width=5cm]{Mute_Swan.png}

\section{Tundra Swan - Pikkujoutsen}
\textit{Cygnus columbianus}
\includegraphics[width=5cm]{Tundra_Swan.png}

\section{Whooper Swan - Laulujoutsen}
\textit{Cygnus cygnus}
\includegraphics[width=5cm]{Whooper_Swan.png}

\section{Bean Goose - Metsähanhi}
\textit{Anser fabalis}
\includegraphics[width=5cm]{Bean_Goose.png}

\section{Pink-footed Goose - Lyhytnokkahanhi}
\textit{Anser brachyrhynchus}
\includegraphics[width=5cm]{Pink-footed_Goose.png}

Greater white-fronted goose, Anser albifrons

\section{Lesser White-fronted Goose - Kiljuhanhi}
\textit{Anser erythropus}
\includegraphics[width=5cm]{Lesser White-fronted_Goose.png}

Greylag goose, Anser anser
Snow goose, Anser caerulescens

\section{Canada Goose - Kanadanhanhi}
\textit{Branta canadensis} I
\includegraphics[width=5cm]{Canada_Goose.png}

Barnacle goose, Branta leucopsis
Brent goose, Branta bernicla
Red-breasted goose, Branta ruficollis
Ruddy shelduck, Tadorna ferruginea

\section{Common Shelduck - Ristisorsa}
\textit{Tadorna tadorna}
\includegraphics[width=5cm]{Common_Shelduck.png}

Mandarin duck, Aix galericulata I

\section{Eurasian Wigeon - Haapana}
\textit{Anas penelope}
\includegraphics[width=5cm]{Eurasian_Wigeon.png}

American wigeon, Mareca americana R

\section{Gadwall - Harmaasorsa}
\textit{Mareca strepera}
\includegraphics[width=5cm]{Gadwall.png}

\section{Common Teal - Tavi}
\textit{Anas crecca}
\includegraphics[width=5cm]{Common_Teal.png}

Green-winged teal, Anas carolinensis R

\section{Mallard - Sinisorsa}
\textit{Anas platyrhynchos}
\includegraphics[width=5cm]{Mallard.png}

American black duck, Anas rubribes R

\section{Northern Pintail - Jouhisorsa}
\textit{Anas acuta}
\includegraphics[width=5cm]{Northern_Pintail.png}

\section{Garganey - Heinätavi}
\textit{Anas querquedula}
\includegraphics[width=5cm]{Garganey.png}

Blue-winged teal, Spatula discors R

\section{Northern Shoveler - Lapasorsa}
\textit{Anas clypeata}
\includegraphics[width=5cm]{Northern_Shoveler.png}

Red-crested pochard, Netta rufina R

\section{Common Pochard - Punasotka}
\textit{Aythya ferina}
\includegraphics[width=5cm]{Common_Pochard.png}

Ring-necked duck, Aythya collaris R
Ferruginous duck, Aythya nyroca R

\section{Tufted Duck - Tukkasotka}
\textit{Aythya fuligula}
\includegraphics[width=5cm]{Tufted_Duck.png}

\section{Greater Scaup - Lapasotka}
\textit{Aythya marila}
\includegraphics[width=5cm]{Greater_Scaup.png}

\section{Lesser Scaup - }
\textit{Aythya affinis}
\includegraphics[width=5cm]{Lesser_Scaup.png}

\section{Common Eider - Haahka}
\textit{Somateria mollissima}
\includegraphics[width=5cm]{Common_Eider.png}

\section{King Eider - Kyhmyhaahka}
\textit{Somateria spectabilis}
\includegraphics[width=5cm]{King_Eider.png}

Steller's eider, Polysticta stelleri
Harlequin duck, Histrionicus histrionicus R

\section{Long-tailed duck - Alli}
\textit{Clangula hyemalis}
\includegraphics[width=5cm]{Long-tailed_duck.png}

\section{Black Scoter (Common Scoter) - Mustalintu}
\textit{Melanitta nigra}
\includegraphics[width=5cm]{Black_Scoter.png}

Surf scoter, Melanitta perspicillata R

\section{White-winged Scoter (Velvet Scoter) - Pilkkasiipi}
\textit{Melanitta fusca}
\includegraphics[width=5cm]{White-winged_Scoter.png}

\section{Common Goldeneye - Telkkä}
\textit{Bucephala clangula}
\includegraphics[width=5cm]{Common_Goldeneye.png}

\section{Smew - }
\textit{Mergellus albellus}
\includegraphics[width=5cm]{Smew.png}

Red-breasted merganser, Mergus serrator
Goosander, Mergus merganser
Ruddy duck, Oxyura jamaicensis I R





\chapter{Grouse}
Order: Galliformes   Family: Tetraonidae

\section{Hazel Grouse - Pyy}
\textit{Bonasa bonasia}
\includegraphics[width=5cm]{Hazel_grouse.png}

\section{Rock Ptarmigan - Kiiruna}
\textit{Lagopus mutus}
\includegraphics[width=5cm]{Rock_Ptarmigan.png}

\section{Black Grouse - Teeri}
\textit{Tetrao tetrix}
\includegraphics[width=5cm]{Black_Grouse.png}

\section{Willow Ptarmigan - Riekko}
\textit{Lagopus lagopus}
\includegraphics[width=5cm]{Willow_Ptarmigan.png}

\section{Western Capercaillie - Metso; Koppelo}
\textit{Tetrao urogallus}
\includegraphics[width=5cm]{Western_Capercaillie.png}



\chapter{Pheasants and partridges}
Order: Galliformes   Family: Phasianidae

\section{Grey Partridge - Peltopyy}
\textit{Perdix perdix}
\includegraphics[width=5cm]{Grey_Partridge.png}

\section{Common Quail - Viiriäinen}
\textit{Coturnix coturnix}
\includegraphics[width=5cm]{Common_Quail.png}

\section{Common Pheasant - Fasaani}
\textit{Phasianus colchicus} I 
\includegraphics[width=5cm]{Common_Pheasant.png}





\chapter{Divers}
Order: Gaviiformes   Family: Gaviidae

\section{Red-throated Loon (Red-throated Diver) - Kaakkuri}
\textit{Gavia stellata}
\includegraphics[width=5cm]{Red-throated_Loon.png}

\section{Arctic Loon (Black-throated Diver) - Kuikka}
\textit{Gavia arctica}
\includegraphics[width=5cm]{Arctic_Loon.png}

Great northern diver, Gavia immer R
Yellow-billed diver, Gavia adamsii






\chapter{Grebes}
Order: Podicipediformes   Family: Podicipedidae

Little grebe, Tachybaptus ruficollis

\section{Great Crested Grebe - Silkkiuikku}
\textit{Podiceps cristatus}
\includegraphics[width=5cm]{Great Crested_Grebe.png}

\section{Red-necked Grebe - Härkälintu}
\textit{Podiceps grisegena}
\includegraphics[width=5cm]{Red-necked_Grebe.png}

\section{Horned Grebe - Mustakurkku-uikku}
\textit{Podiceps auritus}
\includegraphics[width=5cm]{Horned_Grebe.png}

\section{Black-necked Grebe - Mustakaulauikku}
\textit{Podiceps nigricollis}
\includegraphics[width=5cm]{Black-necked_Grebe.png} R





\chapter{Shearwaters and petrels}
Order: Procellariiformes   Family: Procellariidae

Northern fulmar, Fulmarus glacialis R
Sooty shearwater, Ardenna griseus R
Manx shearwater, Puffinus puffinus R






\chapter{Storm petrels}
Order: Procellariiformes   Family: Hydrobatidae

European storm petrel, Hydrobates pelagicus R
Leach's storm petrel, Oceanodroma leucorhoa R
Band-rumped storm petrel, Oceanodroma castro R




\chapter{Gannets}
Order: Suliformes   Family: Sulidae

Northern gannet, Morus bassanus R




\chapter{Cormorants}
Order: Suliformes   Family: Phalacrocoracidae

\section{Great Cormorant - Merimetso}
\textit{Phalacrocorax carbo}
\includegraphics[width=5cm]{Great_Cormorant.png}

European shag, Phalacrocorax aristotelis R





\chapter{Pelicans}
Order: Pelecaniformes   Family: Pelecanidae

Great white pelican, Pelecanus onocrotalus H R




\chapter{Bitterns, herons and egrets}
Order: Pelecaniformes   Family: Ardeidae

Great bittern, Botaurus stellaris
Little bittern, Ixobrychus minutus R
Black-crowned night heron, Nycticorax nycticorax R
Cattle egret, Bubulcus ibis R
Squacco heron, Ardeola ralloides R
Little egret, Egretta garzetta R
Great egret, Egretta alba

\section{Grey Heron - Harmaahaikara}
\textit{Ardea cinerea}
\includegraphics[width=5cm]{Grey_Heron.png}

Purple heron, Ardea purpurea R





\chapter{Ibises and spoonbills}
Order: Pelecaniformes   Family: Threskiornithidae

Glossy ibis, Plegadis falcinellus R
Eurasian spoonbill, Platalea leucorodia R




\chapter{Storks}
Order: Ciconiiformes   Family: Ciconiidae

Black stork, Ciconia nigra
White stork, Ciconia ciconia




\chapter{Kites, hawks and eagles}
Order: Accipitriformes   Family: Accipitridae

\section{European Honey-buzzard - Mehiläishaukka}
\textit{Pernis apivorus}
\includegraphics[width=5cm]{European_Honey-buzzard.png}

\section{Black Kite - Haarahaukka}
\textit{Milvus migrans}
\includegraphics[width=5cm]{Black_Kite.png}

Red kite, Milvus milvus R
Pallas's fish eagle, Haliaeetus leucoryphus H R

\section{White-tailed Eagle - Merikotka}
\textit{Haliaeetus albicilla}
\includegraphics[width=5cm]{White-tailed_Eagle.png}

Egyptian vulture, Neophron percnopterus R
Eurasian griffon vulture, Gyps fulvus R
Short-toed snake eagle, Circaetus gallicus R

\section{Western Marsh Harrier - Ruskosuohaukka}
\textit{Circus aeruginosus}
\includegraphics[width=5cm]{Western_Marsh-Harrier.png}

\section{Northern Harrier (Hen Harrier) - Sinisuohaukka}
\textit{Circus cyaneus}
\includegraphics[width=5cm]{Northern_Harrier.png}

Pallid harrier, Circus macrourus R

\section{Montagu's Harrier - Niittysuohaukka}
\textit{Circus pygargus}
\includegraphics[width=5cm]{Montagu's_Harrier.png}

\section{Northern Goshawk - Kanahaukka}
\textit{Accipiter gentilis}
\includegraphics[width=5cm]{Northern_Goshawk.png}

\section{Eurasian Sparrowhawk - Varpushaukka}
\textit{Accipiter nisus}
\includegraphics[width=5cm]{Eurasian_Sparrowhawk.png}

\section{Common Buzzard - Hiirihaukka}
\textit{Buteo buteo}
\includegraphics[width=5cm]{Common_Buzzard.png}

Long-legged buzzard, Buteo rufinus R

\section{Rough-legged Hawk (Rough-legged Buzzard) - Piekana}
\textit{Buteo lagopus}
\includegraphics[width=5cm]{Rough-legged_Hawk.png}

Lesser spotted eagle, Clanga pomarina R

\section{Greater Spotted Eagle - Kiljukotka}
\textit{Aquila clanga}
\includegraphics[width=5cm]{Greater Spotted_Eagle.png}

Steppe eagle, Aquila nipalensis R
Eastern imperial eagle, Aquila heliaca R

\section{Golden Eagle - Maakotka}
\textit{Aquila chrysaetos}
\includegraphics[width=5cm]{Golden_Eagle.png}

Booted eagle, Hieraaetus pennatus R






\chapter{Osprey}
Order: Accipitriformes   Family: Pandionidae

\section{Osprey - Kalasääski}
\textit{Pandion haliaetus}
\includegraphics[width=5cm]{Osprey.png}






\chapter{Falcons}
Order: Falconiformes   Family: Falconidae

Lesser kestrel, Falco naumanni R

\section{Common Kestrel - Tuulihaukka}
\textit{Falco tinnunculus}
\includegraphics[width=5cm]{Common_Kestrel.png}

Red-footed falcon, Falco vespertinus

\section{Merlin - Ampuhaukka}
\textit{Falco columbarius}
\includegraphics[width=5cm]{Merlin.png}

\section{Eurasian Hobby - Nuolihaukka}
\textit{Falco subbuteo}
\includegraphics[width=5cm]{Eurasian_Hobby.png}

Eleonora's falcon, Falco eleonorae R
Saker falcon, Falco cherrug R

\section{Gyrfalcon (Gyr Falcon) - Tunturihaukka}
\textit{Falco rusticolus}
\includegraphics[width=5cm]{Gyrfalcon.png}

\section{Peregrine Falcon - Muuttohaukka}
\textit{Falco peregrinus}
\includegraphics[width=5cm]{Peregrine_Falcon.png}





\chapter{Rails, crakes, gallinules and coots}
Order: Gruiformes   Family: Rallidae

\section{Water Rail - Luhtakana}
\textit{Rallus aquaticus}
\includegraphics[width=5cm]{Water_Rail.png}

\section{Spotted Crake - Luhtahuitti}
\textit{Porzana porzana}
\includegraphics[width=5cm]{Spotted_Crake.png}

Little crake, Porzana parva
Baillon's crake, Porzana pusilla R

\section{Corn Crake - Ruisrääkkä}
\textit{Crex crex}
\includegraphics[width=5cm]{Corn_Crake.png}

Common moorhen, Gallinula chloropus
Allen's gallinule, Porphyrio alleni R

\section{Common Coot (Eurasian coot) - Nokikana}
\textit{Fulica atra}
\includegraphics[width=5cm]{Common_Coot.png}




\chapter{Cranes}
Order: Gruiformes   Family: Gruidae

\section{Common Crane - Kurki}
\textit{Grus grus}
\includegraphics[width=5cm]{Common_Crane.png}

Demoiselle crane, Grus virgo R





\chapter{Bustards}
Order: Otidiformes   Family: Otididae

Little bustard, Tetrax tetrax R
Macqueen's bustard, Chlamydotis macqueenii H R
Great bustard, Otis tarda H R






\chapter{Oystercatchers}
Order: Charadriiformes   Family: Haematopodidae

\section{Eurasian Oystercatcher - Meriharakka}
\textit{Haematopus ostralegus}
\includegraphics[width=5cm]{Eurasian_Oystercatcher.png}





\chapter{Avocets and stilts}
Order: Charadriiformes   Family: Recurvirostridae

Black-winged stilt, Himantopus himantopus R
Pied avocet, Recurvirostra avosetta




\chapter{Thick-knees}
Order: Charadriiformes   Family: Burhinidae

Eurasian stone-curlew, Burhinus oedicnemus R



\chapter{Pratincoles and coursers}
Order: Charadriiformes   Family: Glareolidae

Cream-coloured courser, Cursorius cursor R
Collared pratincole, Glareola pratincola R
Black-winged pratincole, Glareola nordmanni R



\chapter{Plovers and lapwings}
Order: Charadriiformes   Family: Charadriidae

\section{Little Ringed Plover - Pikkutylli}
\textit{Charadrius dubius}
\includegraphics[width=5cm]{Little Ringed_Plover.png}

\section{Common Ringed Plover - Tylli}
\textit{Charadrius hiaticula}
\includegraphics[width=5cm]{Common Ringed_Plover.png}

Kentish plover, Charadrius alexandrinus R
Greater sand plover, Charadrius leschenaultii R
Caspian plover, Charadrius asiaticus
Oriental plover, Charadrius veredus R

\section{Eurasian Dotterel - }
\textit{Eudromias morinellus}
\includegraphics[width=5cm]{Eurasian_Dotterel.png}

Pacific golden plover, Pluvialis fulva R

\section{European Golden-Plover - Kapustarinta}
\textit{Pluvialis apricaria}
\includegraphics[width=5cm]{European_Golden-Plover.png}

Grey plover, Pluvialis squatarola
Sociable lapwing, Vanellus gregarius R
White-tailed lapwing, Vanellus leucurus R

\section{Northern Lapwing - Töyhtöhyyppä}
\textit{Vanellus vanellus}
\includegraphics[width=5cm]{Northern_Lapwing.png}




\chapter{Sandpipers and allies}
Order: Charadriiformes   Family: Scolopacidae

Red knot, Calidris canutus
Sanderling, Calidris alba
Red-necked stint, Calidris ruficollis R
Little stint, Calidris minuta

\section{Temminck's Stint - Lapinsirri}
\textit{Calidris temminckii}
\includegraphics[width=5cm]{Temminck's_Stint.png}

Least sandpiper, Calidris minutilla H R
White-rumped sandpiper, Calidris fuscicollis R
Baird's sandpiper, Calidris bairdii R
Pectoral sandpiper, Calidris melanotos R
Sharp-tailed sandpiper, Calidris acuminata R
Curlew sandpiper, Calidris ferruginea
Stilt sandpiper, Calidris himantopus R

\section{Purple Sandpiper - Merisirri}
\textit{Calidris maritima}
\includegraphics[width=5cm]{Purple_Sandpiper.png}

\section{Dunlin - Suosirri}
\textit{Calidris alpina}
\includegraphics[width=5cm]{Dunlin.png}

\section{Broad-billed Sandpiper - Jänkäsirriäinen}
\textit{Limicola falcinellus}
\includegraphics[width=5cm]{Broad-billed_Sandpiper.png}

Buff-breasted sandpiper, Calidris subruficollis R

\section{Ruff - Suokukko}
\textit{Philomachus pugnax}
\includegraphics[width=5cm]{Ruff.png}

\section{Jack Snipe - Jänkäkurppa}
\textit{Lymnocryptes minimus}
\includegraphics[width=5cm]{Jack_Snipe.png}

\section{Common Snipe - Taivaanvuohi}
\textit{Gallinago gallinago}
\includegraphics[width=5cm]{Common_Snipe.png}

Great snipe, Gallinago media
Long-billed dowitcher, Limnodromus scolopaceus R

\section{Eurasian Woodcock - Lehtokurppa}
\textit{Scolopax rusticola}
\includegraphics[width=5cm]{Eurasian_Woodcock.png}

\section{Black-tailed Godwit - Mustapyrstökuiri}
\textit{Limosa limosa}
\includegraphics[width=5cm]{Black-tailed_Godwit.png}

\section{Bar-tailed Godwit - Punakuiri}
\textit{Limosa lapponica}
\includegraphics[width=5cm]{Bar-tailed_Godwit.png}

Little curlew, Numenius minutus R

\section{Whimbrel - Pikkukuovi}
\textit{Numenius phaeopus}
\includegraphics[width=5cm]{Whimbrel.png}

\section{Eurasian Curlew - Isokuovi}
\textit{Numenius arquata}
\includegraphics[width=5cm]{Eurasian_Curlew.png}

\section{Spotted Redshank - Mustaviklo}
\textit{Tringa erythropus}
\includegraphics[width=5cm]{Spotted_Redshank.png}

\section{Common Redshank - Punajalkaviklo}
\textit{Tringa totanus}
\includegraphics[width=5cm]{Common_Redshank.png}

Marsh sandpiper, Tringa stagnatilis

\section{Common Greenshank - Valkoviklo}
\textit{Tringa nebularia}
\includegraphics[width=5cm]{Common_Greenshank.png}

Lesser yellowlegs, Tringa flavipes R

\section{Green Sandpiper - Metsäviklo}
\textit{Tringa ochropus}
\includegraphics[width=5cm]{Green_Sandpiper.png}

\section{Wood Sandpiper - Liro}
\textit{Tringa glareola}
\includegraphics[width=5cm]{Wood_Sandpiper.png}

Willet, Tringa semipalmata R

\section{Terek Sandpiper - Rantakurvi}
\textit{Xenus cinereus}
\includegraphics[width=5cm]{Terek_Sandpiper.png}

\section{Common Sandpiper - Rantasipi}
\textit{Actitis hypoleucos}
\includegraphics[width=5cm]{Common_Sandpiper.png}

Spotted sandpiper, Actitis macularius R

\section{Ruddy Turnstone - Karikukko}
\textit{Arenaria interpres}
\includegraphics[width=5cm]{Ruddy_Turnstone.png}

Wilson's phalarope, Phalaropus tricolor R

\section{Red-necked Phalarope - Vesipääsky}
\textit{Phalaropus lobatus}
\includegraphics[width=5cm]{Red-necked_Phalarope.png}

Red phalarope, Phalaropus fulicarius R






































\chapter{Skuas}
Order: Charadriiformes   Family: Stercorariidae

Pomarine skua, Stercorarius pomarinus

\section{Parasitic Jaeger (Arctic skua) - }
\textit{Stercorarius parasiticus}
\includegraphics[width=5cm]{Parasitic_Jaeger.png}

\section{Long-tailed Jaeger (Long-tailed Skua) - Tunturikihu}
\textit{Stercorarius longicaudus}
\includegraphics[width=5cm]{Long-tailed_Jaeger.png}

Great skua, Stercorarius skua R








\chapter{Gulls, terns, and skimmers}
Order: Charadriiformes   Family: Laridae

Mediterranean gull, Ichthyaetus melanocephalus R
Laughing gull, Leucophaeus atricilla R
Franklin's gull, Leucophaeus pipixcan R

\section{Little Gull - Pikkulokki}
\textit{Larus minutus/Hydrocoloeus minutus}
\includegraphics[width=5cm]{Little_Gull.png}

Sabine's gull, Xema sabini R

\section{Black-headed Gull - Naurulokki}
\textit{Larus ridibundus/Chroicocephalus ridibundus}
\includegraphics[width=5cm]{Black-headed_Gull.png}

Slender-billed gull, Chroicocephalus genei R

\section{Common Gull - Kalalokki}
\textit{Larus canus}
\includegraphics[width=5cm]{Common_Gull.png}

\section{Lesser Black-backed Gull - Selkälokki}
\textit{Larus fuscus}
\includegraphics[width=5cm]{Lesser Black-backed_Gull.png}

Herring gull, Larus argentatus
Caspian gull, Larus cachinnans R
Yellow-legged gull, Larus michahellis R
Iceland gull, Larus glaucoides R

\section{Glaucous Gull - Isolokki}
\textit{Larus hyperboreus}
\includegraphics[width=5cm]{Glaucous_Gull.png}

\section{Great Black-backed Gull - Merilokki}
\textit{Larus marinus}
\includegraphics[width=5cm]{Great Black-backed_Gull.png}

Ross's gull, Rhodostethia rosea R

\section{Black-legged Kittiwake - Pikkukajava}
\textit{Rissa tridactyla}
\includegraphics[width=5cm]{Black-legged_Kittiwake.png}

Ivory gull, Pagophila eburnea R
Gull-billed tern, Gelochelidon nilotica R

\section{Caspian Tern - Räyska}
\textit{Sterna caspia}
\includegraphics[width=5cm]{Caspian_Tern.png}

Sandwich tern, Thalasseus sandvicensis

\section{Common Tern - Kalatiira}
\textit{Sterna hirundo}
\includegraphics[width=5cm]{Common_Tern.png}

\section{Arctic Tern - Lapintiira}
\textit{Sterna paradisaea}
\includegraphics[width=5cm]{Arctic_Tern.png}

\section{Little Tern - Pikkutiira}
\textit{Sterna albifrons}
\includegraphics[width=5cm]{Little_Tern.png}

Whiskered tern, Chlidonias hybrida R

\section{Black Tern - Mustatiira}
\textit{Chlidonias niger}
\includegraphics[width=5cm]{Black_Tern.png}

White-winged tern, Chlidonias leucopterus R





\chapter{Auks}
Order: Charadriiformes   Family: Alcidae

\section{Common Murre (Common Guillemot) - Etelänkiisla}
\textit{Uria aalge}
\includegraphics[width=5cm]{Common_Murre.png}

\section{Thick-billed Murre (Brünnich's Guillemot) - Pohjankiisla}
\textit{Uria lomvia}
\includegraphics[width=5cm]{Thick-billed_Murre.png} R

\section{Razorbill - Ruokki}
\textit{Alca torda}
\includegraphics[width=5cm]{Razorbill.png}

\section{Black Guillemot - Riskilä}
\textit{Cepphus grylle}
\includegraphics[width=5cm]{Black_Guillemot.png}

Little auk, Alle alle
Atlantic puffin, Fratercula arctica R







\chapter{Sandgrouse}
Order: Pterocliformes   Family: Pteroclidae

Pallas's sandgrouse, Syrrhaptes paradoxus R




\chapter{Pigeons and doves}
Order: Columbiformes   Family: Columbidae

Rock dove, Columba livia I

\section{Stock Pigeon (Stock Dove) - Uuttukyyhky}
\textit{Columba oenas}
\includegraphics[width=5cm]{Stock_Pigeon.png}

\section{Common Wood Pigeon - Sepelkyyhky}
\textit{Columba palumbus}
\includegraphics[width=5cm]{Common Wood_Pigeon.png}

\section{Eurasian Collared Dove - Turturikyyhky}
\textit{Streptopelia decaocto}
\includegraphics[width=5cm]{Eurasian Collared_Dove.png}

European turtle dove, Streptopelia turtur
Oriental turtle dove, Streptopelia orientalis R



\chapter{Cuckoos}
Order: Cuculiformes   Family: Cuculidae

Great spotted cuckoo, Clamator glandarius H R

\section{Common Cuckoo - Käki}
\textit{Cuculus canorus}
\includegraphics[width=5cm]{Common_Cuckoo.png}




\chapter{Barn owls}
Order: Strigiformes   Family: Tytonidae

Barn owl, Tyto alba R




\chapter{Typical owls}
Order: Strigiformes   Family: Strigidae

\section{Eurasian Eagle-Owl - Huuhkaja}
\textit{Bubo bubo}
\includegraphics[width=5cm]{Eurasian_Eagle-Owl.png}

\section{Snowy Owl - Tunturipöllö}
\textit{Nyctea scandiaca/Bubo scandiacus}
\includegraphics[width=5cm]{Snowy_Owl.png}

\section{Northern Hawk Owl - Hiiripöllö}
\textit{Surnia ulula}
\includegraphics[width=5cm]{Northern Hawk_Owl.png}

\section{Eurasian Pygmy-Owl - Varpuspöllö}
\textit{Glaucidium passerinum}
\includegraphics[width=5cm]{Eurasian_Pygmy-Owl.png}

Little owl, Athene noctua R

\section{Tawny Owl - Lehtopöllö}
\textit{Strix aluco}
\includegraphics[width=5cm]{Tawny_Owl.png}

\section{Ural Owl - Viirupöllö}
\textit{Strix uralensis}
\includegraphics[width=5cm]{Ural_Owl.png}

\section{Great Grey Owl - Lapinpöllö}
\textit{Strix nebulosa}
\includegraphics[width=5cm]{Great Grey_Owl.png}

\section{Long-eared Owl - Sarvipöllö}
\textit{Asio otus}
\includegraphics[width=5cm]{Long-eared_Owl.png}

\section{Short-eared Owl - Suopöllö}
\textit{Asio flammeus}
\includegraphics[width=5cm]{Short-eared_Owl.png}

\section{Boreal Owl (Tengmalm's Owl) - Helmipöllö}
\textit{Aegolius funereus}
\includegraphics[width=5cm]{Boreal_Owl.png}




\chapter{Nightjars}
Order: Caprimulgiformes   Family: Caprimulgidae

\section{Eurasian Nightjar (European nightjar) - Kehrääjä}
\textit{Caprimulgus europaeus}
\includegraphics[width=5cm]{Eurasian_Nightjar.png}




\chapter{Swifts}
Order: Apodiformes   Family: Apodidae

White-throated needletail, Hirundapus caudacutus R

\section{Common Swift - Tervakirskuja}
\textit{Apus apus}
\includegraphics[width=5cm]{Common_Swift.png}

Pallid swift, Apus pallidus R
Alpine swift, Apus melba R
White-rumped swift, Apus caffer R





\chapter{Kingfishers}
Order: Coraciiformes   Family: Alcedinidae

\section{Common Kingfisher - Kuningaskalastaja}
\textit{Alcedo atthis}
\includegraphics[width=5cm]{Common_Kingfisher.png}






\chapter{Bee-eaters}
Order: Coraciiformes   Family: Meropidae

Blue-cheeked bee-eater, Merops persicus R
European bee-eater, Merops apiaster




\chapter{Rollers}
Order: Coraciiformes   Family: Coraciidae

European roller, Coracias garrulus




\chapter{Hoopoes}
Order: Coraciiformes   Family: Upupidae

Eurasian hoopoe, Upupa epops




\chapter{Woodpeckers}
Order: Piciformes   Family: Picidae

\section{Eurasian Wryneck - Käenpiika}
\textit{Jynx torquilla}
\includegraphics[width=5cm]{Eurasian_Wryneck.png}

\section{Grey-faced Woodpecker (Grey-headed woodpecker) - Harmaapäätikka}
\textit{Picus canus}
\includegraphics[width=5cm]{Grey-faced_Woodpecker.png}

\section{Eurasian Green Woodpecker - Vihertikka}
\textit{Picus viridis}
\includegraphics[width=5cm]{Eurasian Green_Woodpecker.png} R

\section{Black Woodpecker - Palokärki}
\textit{Dryocopus martius}
\includegraphics[width=5cm]{Black_Woodpecker.png}

\section{Great Spotted Woodpecker - Käpytikka}
\textit{Dendrocopos major}
\includegraphics[width=5cm]{Great Spotted_Woodpecker.png}

\section{White-backed Woodpecker - Valkoselkätikka}
\textit{Dendrocopos leucotos}
\includegraphics[width=5cm]{White-backed_Woodpecker.png}

\section{Lesser Spotted Woodpecker - Pikkutikka}
\textit{Dendrocopos minor/Dryobates minor}
\includegraphics[width=5cm]{Lesser Spotted_Woodpecker.png}

\section{Eurasian Three-toed Woodpecker - Pohjantikka}
\textit{Picoides tridactylus}
\includegraphics[width=5cm]{Eurasian Three-toed_Woodpecker.png}





\chapter{Larks}
Order: Passeriformes   Family: Alaudidae

Calandra lark, Melanocorypha calandra R
Bimaculated lark, Melanocorypha bimaculata R
Black lark, Melanocorypha yeltoniensis R
Greater short-toed lark, Calandrella brachydactyla R
Lesser short-toed lark, Alaudala rufescens R
Crested lark, Galerida cristata R

\section{Wood Lark - Kangaskiuru}
\textit{Lullula arborea}
\includegraphics[width=5cm]{Wood_Lark.png}

\section{Sky Lark (Eurasian skylark) - Kiuru (Leivonen)}
\textit{Alauda arvensis}
\includegraphics[width=5cm]{Sky_Lark.png}

White-winged lark, Alauda leucoptera R
Horned lark, Eremophila alpestris







\chapter{Swallows and martins}
Order: Passeriformes   Family: Hirundinidae

\section{Sand Martin - Törmäpääsky}
\textit{Riparia riparia}
\includegraphics[width=5cm]{Sand_Martin.png}

Eurasian crag martin, Ptyonoprogne rupestris R

\section{Barn Swallow - Haarapääsky}
\textit{Hirundo rustica}
\includegraphics[width=5cm]{Barn_Swallow.png}

Red-rumped swallow, Hirundo daurica R

\section{Northern House-Martin (Common House Martin) - Räystäspääsky}
\textit{Delichon urbicum}
\includegraphics[width=5cm]{Northern_House-Martin.png}






\chapter{Pipits and wagtails}
Order: Passeriformes   Family: Motacillidae

Richard's pipit, Anthus richardi
Blyth's pipit, Anthus godlewskii R
Tawny pipit, Anthus campestris R
Olive-backed pipit, Anthus hodgsoni R

\section{Tree Pipit - Metsäkirvinen}
\textit{Anthus trivialis}
\includegraphics[width=5cm]{Tree_Pipit.png}

Pechora pipit, Anthus gustavi R

\section{Meadow Pipit - Niittykirvinen}
\textit{Anthus pratensis}
\includegraphics[width=5cm]{Meadow_Pipit.png}

\section{Red-throated Pipit - Lapinkirvinen}
\textit{Anthus cervinus}
\includegraphics[width=5cm]{Red-throated_Pipit.png}

\section{Rock Pipit - }
\textit{Anthus petrosus}
\includegraphics[width=5cm]{Rock_Pipit.png}

\section{Yellow Wagtail - VäsKeltavästäräkkitäräkki}
\textit{Motacilla flava}
\includegraphics[width=5cm]{Yellow_Wagtail.png}

Citrine wagtail, Motacilla citreola

\section{Grey Wagtail - Vuorivästäräkki}
\textit{Motacilla cinerea}
\includegraphics[width=5cm]{Grey_Wagtail.png}

\section{White Wagtail - Västäräkki}
\textit{Motacilla alba}
\includegraphics[width=5cm]{White_Wagtail.png}




\chapter{Waxwings}
Order: Passeriformes   Family: Bombycillidae

\section{Bohemian Waxwing - Tilhi}
\textit{Bombycilla garrulus}
\includegraphics[width=5cm]{Bohemian_Waxwing.png}




\chapter{Dippers}
Order: Passeriformes   Family: Cinclidae

\section{White-throated Dipper - Koskikara}
\textit{Cinclus cinclus}
\includegraphics[width=5cm]{White-throated_Dipper.png}




\chapter{Wrens}
Order: Passeriformes   Family: Troglodytidae


\section{Winter Wren (Eurasian Wren) - Peukaloinen}
\textit{Troglodytes troglodytes}
\includegraphics[width=5cm]{Winter_Wren.png}



\chapter{Accentors}
Order: Passeriformes   Family: Prunellidae

\section{Dunnock (Hedge Accentor) - Rautiainen}
\textit{Prunella modularis}
\includegraphics[width=5cm]{Hedge_Accentor.png}

Siberian accentor, Prunella montanella R
Black-throated accentor, Prunella atrogularis R
Alpine accentor, Prunella collaris R




\chapter{Thrushes and allies}
Order: Passeriformes   Family: Turdidae

White's thrush, Zoothera dauma R
Swainson's thrush, Catharus ustulatus R
Ring ouzel, Turdus torquatus

\section{Eurasian Blackbird (Common Blackbird) - Mustarastas}
\textit{Turdus merula}
\includegraphics[width=5cm]{Eurasian_Blackbird.png}

Eyebrowed thrush, Turdus obscurus R
Dusky thrush, Turdus naumanni R
Dark-throated thrush, Turdus ruficollis R

\section{Fieldfare - Räkättirastas}
\textit{Turdus pilaris}
\includegraphics[width=5cm]{Fieldfare.png}

\section{Song Thrush - Laulurastas}
\textit{Turdus philomelos}
\includegraphics[width=5cm]{Song_Thrush.png}

\section{Redwing - Punakylkirastas}
\textit{Turdus iliacus}
\includegraphics[width=5cm]{Redwing.png}

\section{Mistle Thrush - Kulorastas}
\textit{Turdus viscivorus}
\includegraphics[width=5cm]{Mistle_Thrush.png}




\chapter{Locustellid warblers}
Order: Passeriformes   Family: Locustellidae

Lanceolated warbler, Locustella lanceolata R

\section{Common Grasshopper-Warbler - Pensassirkkalintu}
\textit{Locustella naevia}
\includegraphics[width=5cm]{Common_Grasshopper-Warbler.png}

\section{Eurasian River Warbler - Viitasirkkalintu}
\textit{Locustella fluviatilis}
\includegraphics[width=5cm]{Eurasian River_Warbler.png}

Savi's warbler, Locustella luscinioides R


\chapter{Acrocephalid warblers}
Order: Passeriformes   Family: Acrocephalidae

Aquatic warbler, Acrocephalus paludicola R

\section{Sedge Warbler - Ruokokerttunen}
\textit{Acrocephalus schoenobaenus}
\includegraphics[width=5cm]{Sedge_Warbler.png}

\section{Eurasian Reed-Warbler - Rytikerttunen}
\textit{Acrocephalus scirpaceus}
\includegraphics[width=5cm]{Eurasian_Reed-Warbler.png}

\section{Marsh Warbler - Luhtakerttunen}
\textit{Acrocephalus palustris}
\includegraphics[width=5cm]{Marsh_Warbler.png}

\section{Blyth's Reed-Warbler - Viitakerttunen}
\textit{Acrocephalus dumetorum}
\includegraphics[width=5cm]{Blyth's_Reed-Warbler.png}

Paddyfield warbler, Acrocephalus agricola R

\section{Great Reed-Warbler - Rastaskerttunen}
\textit{Acrocephalus arundinaceus}
\includegraphics[width=5cm]{Great_Reed-Warbler.png}

Thick-billed warbler, Iduna aedon R
Eastern olivaceous warbler, Iduna pallida R
Booted warbler, Iduna caligata R
Sykes's warbler, Iduna rama R

\section{Icterine Warbler - Kultarinta}
\textit{Hippolais icterina}
\includegraphics[width=5cm]{Icterine_Warbler.png}


\chapter{Phylloscopid warblers}
Order: Passeriformes   Family: Phylloscopidae

Eastern crowned warbler, Phylloscopus coronatus R

\section{Greenish Warbler - Idänuunilintu}
\textit{Phylloscopus trochiloides}
\includegraphics[width=5cm]{Greenish_Warbler.png}

\section{Arctic Warbler - Lapinuunilintu}
\textit{Phylloscopus borealis}
\includegraphics[width=5cm]{Arctic_Warbler.png}

Pallas's leaf warbler, Phylloscopus proregulus
Yellow-browed warbler, Phylloscopus inornatus
Hume's leaf warbler, Phylloscopus humei R
Radde's warbler, Phylloscopus schwarzi R
Dusky warbler, Phylloscopus fuscatus R
Western Bonelli's warbler, Phylloscopus bonelli R
Eastern Bonelli's warbler, Phylloscopus orientalis R

\section{Wood Warbler - Sirittäjä}
\textit{Phylloscopus sibilatrix}
\includegraphics[width=5cm]{Wood_Warbler.png}

\section{Eurasian Chiffchaff (Common Chiffchaff) - Tiltaltti}
\textit{Phylloscopus collybita}
\includegraphics[width=5cm]{Eurasian_Chiffchaff.png}

\section{Willow Warbler - Pajulintu}
\textit{Phylloscopus trochilus}
\includegraphics[width=5cm]{Willow_Warbler.png}


\chapter{Old World warblers}
Order: Passeriformes   Family: Sylviidae

\section{Eurasian Blackcap - Mustapääkertut}
\textit{Sylvia atricapilla}
\includegraphics[width=5cm]{Blackcap.png}

\section{Garden Warbler - Lehtokerttu}
\textit{Sylvia borin}
\includegraphics[width=5cm]{Garden_Warbler.png}

\section{Barred Warbler - Kirjokerttu}
\textit{Sylvia nisoria}
\includegraphics[width=5cm]{Barred_Warbler.png}

\section{Lesser Whitethroat - Hernekerttu}
\textit{Sylvia curruca}
\includegraphics[width=5cm]{Lesser_Whitethroat.png}

\section{Common Whitethroat - Pensaskerttu}
\textit{Sylvia communis}
\includegraphics[width=5cm]{Common_Whitethroat.png}

Asian desert warbler, Sylvia nana R
Dartford warbler, Sylvia undata R
Subalpine warbler, Sylvia cantillans R
Sardinian warbler, Sylvia melanocephala R
Rüppell's warbler, Sylvia ruppeli R




\chapter{Kinglets}
Order: Passeriformes   Family: Regulidae

\section{Goldcrest - Hippiäinen}
\textit{Regulus regulus}
\includegraphics[width=5cm]{Goldcrest.png}

Common firecrest, Regulus ignicapilla R





\chapter{Old World flycatchers}
Order: Passeriformes   Family: Muscicapidae

Rufous-tailed scrub robin, Cercotrichas galactotes R

\section{European Robin - Punarinta}
\textit{Erithacus rubecula}
\includegraphics[width=5cm]{European_Robin.png}

\section{Thrush Nightingale - Satakieli}
\textit{Luscinia luscinia}
\includegraphics[width=5cm]{Thrush_Nightingale.png}

Common nightingale, Luscinia megarhynchos R

\section{Bluethroat - Sinirinta}
\textit{Luscinia svecica}
\includegraphics[width=5cm]{Bluethroat.png}

Siberian rubythroat, Calliope calliope R
Red-flanked bluetail, Tarsiger cyanurus

\section{Black Redstart - Mustaleppälintu}
\textit{Phoenicurus ochruros}
\includegraphics[width=5cm]{Black_Redstart.png}

\section{Common Redstart - Leppälintu}
\textit{Phoenicurus phoenicurus}
\includegraphics[width=5cm]{Common_Redstart.png}

\section{Whinchat - Pensastasku}
\textit{Saxicola rubetra}
\includegraphics[width=5cm]{Whinchat.png}

Common stonechat, Saxicola torquatus R
Isabelline wheatear, Oenanthe isabellina R

\section{Northern Wheatear - Kivitasku}
\textit{Oenanthe oenanthe}
\includegraphics[width=5cm]{Northern_Wheatear.png}

Pied wheatear, Oenanthe pleschanka R
Black-eared wheatear, Oenanthe hispanica R
Desert wheatear, Oenanthe deserti R
Common rock thrush, Monticola saxatilis R
Blue rock thrush, Monticola solitarius R

\section{Spotted Flycatcher - Harmaasieppo}
\textit{Muscicapa striata}
\includegraphics[width=5cm]{Spotted_Flycatcher.png}

\section{Red-breasted Flycatcher - Pikkusieppo}
\textit{Ficedula parva}
\includegraphics[width=5cm]{Red-breasted_Flycatcher.png}

Collared flycatcher, Ficedula albicollis R

\section{European Pied Flycatcher - Kirjosieppo}
\textit{Ficedula hypoleuca}
\includegraphics[width=5cm]{European Pied_Flycatcher.png}










\chapter{Bearded reedling}
Order: Passeriformes   Family: Panuridae

Bearded reedling, Panurus biarmicus




\chapter{Long-tailed tits}
Order: Passeriformes   Family: Aegithalidae

\section{Long-tailed Tit - Pyrstötiainen}
\textit{Aegithalos caudatus}
\includegraphics[width=5cm]{Long-tailed_Tit.png}


\chapter{Tits}
Order: Passeriformes   Family: Paridae

Marsh tit, Parus palustris R

\section{Willow Tit - Hömötiainen}
\textit{Poecile montanus}
\includegraphics[width=5cm]{Willow_Tit.png}

\section{Siberian Tit (Grey-headed Chickadee) - Lapintiainen}
\textit{Poecile cinctus}
\includegraphics[width=5cm]{Siberian_Tit.png}

\section{Crested Tit - Töyhtötiainen}
\textit{Lophophanes cristatus}
\includegraphics[width=5cm]{Crested_Tit.png}

\section{Coal Tit - Kuusitiainen}
\textit{Periparus ater}
\includegraphics[width=5cm]{Coal_Tit.png}

\section{Eurasian Blue Tit - Sinitiainen}
\textit{Cyanistes caeruleus}
\includegraphics[width=5cm]{Eurasian Blue_Tit.png}

Azure tit, Parus cyanus R

\section{Great Tit - Talitiainen}
\textit{Parus major}
\includegraphics[width=5cm]{Great_Tit.png}




\chapter{Nuthatches}
Order: Passeriformes   Family: Sittidae

Eurasian nuthatch, Sitta europaea





\chapter{Treecreepers}
Order: Passeriformes   Family: Certhiidae

\section{Eurasian Tree-Creeper - Puukiipijä}
\textit{Certhia familiaris}
\includegraphics[width=5cm]{Eurasian_Tree-Creeper.png}



\chapter{Penduline tits}
Order: Passeriformes   Family: Remizidae

Eurasian penduline tit, Remiz pendulinus



\chapter{Old World orioles}
Order: Passeriformes   Family: Oriolidae

\section{Eurasian Golden Oriole - Kuhankeittäjä}
\textit{Oriolus oriolus}
\includegraphics[width=5cm]{Eurasian_Golden-Oriole.png}




\chapter{Shrikes}
Order: Passeriformes   Family: Laniidae

Isabelline shrike, Lanius isabellinus R

\section{Red-backed Shrike - Valko-Pikkulepinkäinen}
\textit{Lanius collurio}
\includegraphics[width=5cm]{Red-backed_Shrike.png}

Lesser grey shrike, Lanius minor

\section{Northern Shrike (Great Grey Shrike) - Isolepinkäinen (Lapinharakka)}
\textit{Lanius excubitor}
\includegraphics[width=5cm]{Northern_Shrike.png}

Southern grey shrike, Lanius meridionalis R
Woodchat shrike, Lanius senator R
Masked shrike, Lanius nubicus R






\chapter{Jays, magpies, crows and ravens}
Order: Passeriformes   Family: Corvidae

\section{Eurasian Jay - Närhi}
\textit{Garrulus glandarius}
\includegraphics[width=5cm]{Eurasian_Jay.png}

\section{Siberian Jay - Kuukkeli}
\textit{Perisoreus infaustus}
\includegraphics[width=5cm]{Siberian_Jay.png}

\section{Black-billed Magpie (Common Magpie)- Harakka}
\textit{Pica pica}
\includegraphics[width=5cm]{Black-billed_Magpie.png}

\section{Spotted Nutcracker - Pähkinähakki}
\textit{Nucifraga caryocatactes}
\includegraphics[width=5cm]{Spotted_Nutcracker.png}

\section{Eurasian Jackdaw - Naakka}
\textit{Corvus monedula}
\includegraphics[width=5cm]{Eurasian_Jackdaw.png}

Daurian jackdaw, Corvus dauuricus H R

\section{Rook - Mustavaris}
\textit{Corvus frugilegus}
\includegraphics[width=5cm]{Rook.png}

Hooded crow, Corvus cornix

\section{Common Raven - Korppi}
\textit{Corvus corax}
\includegraphics[width=5cm]{Common_Raven.png}






\chapter{Starlings}
Order: Passeriformes   Family: Sturnidae

\section{Common Starling - Kottarainen}
\textit{Sturnus vulgaris}
\includegraphics[width=5cm]{Common_Starling.png}

Rosy starling, Pastor roseus




\chapter{Sparrows}
Order: Passeriformes   Family: Passeridae

\section{House Sparrow - Varpunen}
\textit{Passer domesticus}
\includegraphics[width=5cm]{House_Sparrow.png}

Spanish sparrow, Passer hispaniolensis R

\section{Eurasian Tree Sparrow - Pikkuvarpunen}
\textit{Passer montanus}
\includegraphics[width=5cm]{Eurasian Tree_Sparrow.png}



\chapter{Finches}
Order: Passeriformes   Family: Fringillidae

\section{Chaffinch - Peippo}
\textit{Fringilla coelebs}
\includegraphics[width=5cm]{Chaffinch.png}

\section{Brambling - Järripeippo}
\textit{Fringilla montifringilla}
\includegraphics[width=5cm]{Brambling.png}

European serin, Serinus serinus
European greenfinch, Chloris chloris
European goldfinch, Carduelis carduelis
Eurasian siskin, Spinus spinus
Common linnet, Linaria cannabina
Twite, Linaria flavirostris
Common redpoll, Acanthis flammea
Arctic redpoll, Acanthis hornemanni
Two-barred crossbill, Loxia leucoptera
Common crossbill, Loxia curvirostra
Parrot crossbill, Loxia pytyopsittacus
Trumpeter finch, Bucanetes githagineus
Common rosefinch, Carpodacus erythrinus
Pine grosbeak, Pinicola enucleator
Eurasian bullfinch, Pyrrhula pyrrhula

\section{Hawfinch - Nokkavarpunen}
\textit{Coccothraustes coccothraustes}
\includegraphics[width=5cm]{Hawfinch.png}





\chapter{Longspurs and snow buntings}
Order: Passeriformes Family: Calcariidae

Lapland longspur, Calcarius lapponicus
Snow bunting, Plectrophenax nivalis




\chapter{Buntings, sparrows, seedeaters and allies}
Order: Passeriformes Family: Emberizidae

White-throated sparrow, Zonotrichia albicollis R
Black-faced bunting, Emberiza spodocephala R
Pine bunting, Emberiza leucocephalos R
Yellowhammer, Emberiza citrinella
Grey-necked bunting, Emberiza buchanani
Ortolan bunting, Emberiza hortulana
Cretzschmar's bunting, Emberiza caesia R
Rustic bunting, Emberiza rustica
Little bunting, Emberiza pusilla
Chestnut bunting, Emberiza rutila R
Yellow-breasted bunting, Emberiza aureola
Reed bunting, Emberiza schoeniclus
Black-headed bunting, Emberiza melanocephala R
Corn bunting, Emberiza calandra R


\bibliography{C:/Users/Lois/Documents/Thesis/library}
\bibliographystyle{Thesis}
\end{document}'''
replaced = re.sub(r'({.*)( )(.*png})', r'\1_\3', s)
print(replaced) 
