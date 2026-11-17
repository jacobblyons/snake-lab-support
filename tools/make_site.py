# Snake Lab's support site: docs/ (served by GitHub Pages) in 13 languages, made from the table below.
import os, shutil, html
ROOT = "https://jacobblyons.github.io/snake-lab-support/"
ISSUES = "https://github.com/jacobblyons/snake-lab-support/issues"
LANGS = [("en", "EN"), ("es", "ES"), ("fr", "FR"), ("de", "DE"), ("it", "IT"), ("pt-BR", "PT"), ("pl", "PL"), ("tr", "TR"), ("ru", "RU"), ("ja", "日本語"), ("ko", "한국어"), ("zh-Hans", "简体"), ("zh-Hant", "繁體")]
T = {}
T["en"] = dict(home="HOME", support="SUPPORT", privacy="PRIVACY", privacy_title="PRIVACY POLICY",
 tagline="A snake roguelike", lead="Snake, rebuilt as a roguelike.",
 pitch="Pick your route through stages that each play differently, choose an upgrade after every stage, and keep your last snake alive. No ads, no in-app purchases.",
 avail="Available on the App Store for iPhone.",
 short="The short version: Snake Lab collects no personal data. No ads, no accounts. It sends anonymous gameplay statistics that help us improve the game.",
 h_collect="WHAT THE APP COLLECTS", collect="No personal data. There are no ads and no accounts. Your runs, scores, unlocks and settings live on your device. The only thing the app sends us is the anonymous gameplay statistics described below.",
 h_stats="ANONYMOUS GAMEPLAY STATISTICS", stats="To learn which stages are too hard, which upgrades get picked and how long runs last, the app sends short records of play: when the app is opened and closed, the mode and rooms you choose, the cards you pick, stages won, how each snake was lost, and scores and times. Each record also carries the app version, the iPhone model, the iOS version, the game's language and your phone's Region setting.",
 stats2="The records share a random number made when the app is installed, so we can tell how many people play. It is not linked to your name, Apple ID, Game Center account, advertising identifier or location, your IP address is not recorded, and deleting the app discards the number. The records are stored with Microsoft Azure Application Insights, deleted after 90 days, and used only to improve Snake Lab. They are never sold, shared, or used for advertising or tracking.",
 h_icloud="ICLOUD", icloud="If you are signed in to iCloud, your scores and unlocks are kept in your own iCloud account so they follow you to your other devices. Apple stores them under Apple's Privacy Policy; we cannot see them.",
 h_gc="GAME CENTER", gc="If you sign in to Apple's Game Center, your best scores are submitted to Apple's leaderboard service under Apple's Privacy Policy. We never see your Game Center identity.",
 h_children="CHILDREN", children="The app is suitable for all ages and is not directed at children. It collects no personal data from anyone.",
 h_changes="CHANGES", changes="If this policy ever changes, the new version will be posted at this address with an updated date below.",
 h_contact="CONTACT", contact='Questions? Open an issue on our <a href="{issues}">support page</a>.', date="Effective date: November 16, 2026",
 h_bug="FOUND A BUG? HAVE AN IDEA?", bug='The fastest way to reach us is to <a href="{issues}">open an issue on GitHub</a>. Bug reports, feature requests and rule questions are all welcome. Tell us what happened and what you expected.',
 h_faq="COMMON QUESTIONS",
 faq=[("How does a run work?", "Choose a route through the map. Each stage is a different kind of game; clear it and pick an upgrade card. Crash and you lose a snake. Lose your last one and the run is over."),
      ("What is the difference between Classic and Modern?", "Both are Endless mode: one board, no end, played for a high score. Modern has the jump and pick-ups. Classic is Snake exactly as you remember it."),
      ("How do I jump?", "Tap the JUMP button and your snake hops over its own body."),
      ("Where are my scores kept?", "On your device, and in your iCloud account if you are signed in. Sign in to Game Center to put your best scores on the world leaderboards.")],
 h_fine="THE FINE PRINT", fine='Snake Lab has no ads and no in-app purchases. It collects no personal data, only anonymous gameplay statistics; see the <a href="privacy.html">privacy policy</a>.')
T["es"] = dict(home="INICIO", support="SOPORTE", privacy="PRIVACIDAD", privacy_title="POLÍTICA DE PRIVACIDAD",
 tagline="Un roguelike de Snake", lead="Snake, reconstruido como un roguelike.",
 pitch="Elige tu ruta por fases que se juegan cada una a su manera, escoge una mejora tras cada fase y mantén viva tu última serpiente. Sin anuncios ni compras dentro de la app.",
 avail="Disponible en el App Store para iPhone.",
 short="En resumen: Snake Lab no recopila datos personales. Sin anuncios ni cuentas. Envía estadísticas de juego anónimas que nos ayudan a mejorar el juego.",
 h_collect="QUÉ RECOPILA LA APP", collect="Ningún dato personal. No hay anuncios ni cuentas. Tus partidas, puntuaciones, desbloqueos y ajustes se guardan en tu dispositivo. Lo único que la app nos envía son las estadísticas de juego anónimas que se describen a continuación.",
 h_stats="ESTADÍSTICAS DE JUEGO ANÓNIMAS", stats="Para saber qué fases son demasiado difíciles, qué mejoras se eligen y cuánto duran las partidas, la app envía breves registros de juego: cuándo se abre y se cierra la app, el modo y las salas que eliges, las cartas que escoges, las fases superadas, cómo se perdió cada serpiente, y puntuaciones y tiempos. Cada registro incluye también la versión de la app, el modelo de iPhone, la versión de iOS, el idioma del juego y el ajuste de región de tu teléfono.",
 stats2="Los registros comparten un número aleatorio creado al instalar la app, para que sepamos cuántas personas juegan. No está vinculado a tu nombre, Apple ID, cuenta de Game Center, identificador de publicidad ni ubicación; tu dirección IP no se registra, y al borrar la app el número se descarta. Los registros se almacenan en Microsoft Azure Application Insights, se eliminan a los 90 días y solo se usan para mejorar Snake Lab. Nunca se venden, se comparten ni se usan para publicidad o seguimiento.",
 h_icloud="ICLOUD", icloud="Si has iniciado sesión en iCloud, tus puntuaciones y desbloqueos se guardan en tu propia cuenta de iCloud para que te acompañen en tus otros dispositivos. Apple los guarda según su Política de Privacidad; nosotros no podemos verlos.",
 h_gc="GAME CENTER", gc="Si inicias sesión en Game Center de Apple, tus mejores puntuaciones se envían al servicio de clasificaciones de Apple según la Política de privacidad de Apple. Nunca vemos tu identidad de Game Center.",
 h_children="MENORES", children="La app es apta para todas las edades y no está dirigida a niños. No recopila datos personales de nadie.",
 h_changes="CAMBIOS", changes="Si esta política cambia, la nueva versión se publicará en esta dirección con una fecha actualizada abajo.",
 h_contact="CONTACTO", contact='¿Preguntas? Abre una incidencia en nuestra <a href="{issues}">página de soporte</a>.', date="Fecha de entrada en vigor: 16 de noviembre de 2026",
 h_bug="¿HAS ENCONTRADO UN ERROR? ¿TIENES UNA IDEA?", bug='La forma más rápida de contactarnos es <a href="{issues}">abrir una incidencia en GitHub</a>. Informes de errores, sugerencias y dudas sobre las reglas son bienvenidos. Cuéntanos qué pasó y qué esperabas.',
 h_faq="PREGUNTAS FRECUENTES",
 faq=[("¿Cómo funciona una partida?", "Elige una ruta en el mapa. Cada fase es un tipo de juego distinto; supérala y elige una carta de mejora. Si chocas, pierdes una serpiente. Si pierdes la última, la partida termina."),
      ("¿Qué diferencia hay entre Clásico y Moderno?", "Los dos son el modo Infinito: un solo tablero, sin final, a por la mejor puntuación. Moderno tiene el salto y los objetos. Clásico es el Snake tal y como lo recuerdas."),
      ("¿Cómo salto?", "Pulsa el botón SALTO y tu serpiente saltará por encima de su propio cuerpo."),
      ("¿Dónde se guardan mis puntuaciones?", "En tu dispositivo, y en tu cuenta de iCloud si has iniciado sesión. Inicia sesión en Game Center para poner tus mejores puntuaciones en las clasificaciones mundiales.")],
 h_fine="LA LETRA PEQUEÑA", fine='Snake Lab no tiene anuncios ni compras dentro de la app. No recopila datos personales, solo estadísticas de juego anónimas; consulta la <a href="privacy.html">política de privacidad</a>.')
T["fr"] = dict(home="ACCUEIL", support="ASSISTANCE", privacy="CONFIDENTIALITÉ", privacy_title="POLITIQUE DE CONFIDENTIALITÉ",
 tagline="Un Snake roguelike", lead="Snake, reconstruit en roguelike.",
 pitch="Choisis ta route à travers des niveaux qui se jouent tous différemment, prends une amélioration après chaque niveau et garde ton dernier serpent en vie. Pas de publicité, pas d’achats intégrés.",
 avail="Disponible sur l’App Store pour iPhone.",
 short="En bref : Snake Lab ne collecte aucune donnée personnelle. Pas de publicité, pas de comptes. L’app envoie des statistiques de jeu anonymes qui nous aident à améliorer le jeu.",
 h_collect="CE QUE L’APP COLLECTE", collect="Aucune donnée personnelle. Il n’y a ni publicité ni compte. Tes parties, scores, déblocages et réglages restent sur ton appareil. La seule chose que l’app nous envoie, ce sont les statistiques de jeu anonymes décrites ci-dessous.",
 h_stats="STATISTIQUES DE JEU ANONYMES", stats="Pour savoir quelles étapes sont trop difficiles, quelles améliorations sont choisies et combien de temps durent les parties, l’app envoie de courts relevés de jeu : quand l’app est ouverte et fermée, le mode et les salles que tu choisis, les cartes que tu prends, les étapes gagnées, comment chaque serpent a été perdu, ainsi que les scores et les temps. Chaque relevé indique aussi la version de l’app, le modèle d’iPhone, la version d’iOS, la langue du jeu et le réglage de région de ton téléphone.",
 stats2="Les relevés partagent un numéro aléatoire créé à l’installation de l’app, pour que nous sachions combien de personnes jouent. Il n’est lié ni à ton nom, ni à ton identifiant Apple, ni à ton compte Game Center, ni à ton identifiant publicitaire, ni à ta position ; ton adresse IP n’est pas enregistrée, et supprimer l’app efface ce numéro. Les relevés sont stockés chez Microsoft Azure Application Insights, supprimés au bout de 90 jours et servent uniquement à améliorer Snake Lab. Ils ne sont jamais vendus, partagés ni utilisés pour la publicité ou le suivi.",
 h_icloud="ICLOUD", icloud="Si tu es connecté à iCloud, tes scores et déblocages sont conservés dans ton propre compte iCloud pour te suivre sur tes autres appareils. Apple les stocke selon sa politique de confidentialité ; nous ne pouvons pas les voir.",
 h_gc="GAME CENTER", gc="Si tu te connectes au Game Center d’Apple, tes meilleurs scores sont envoyés au service de classements d’Apple selon la politique de confidentialité d’Apple. Nous ne voyons jamais ton identité Game Center.",
 h_children="ENFANTS", children="L’app convient à tous les âges et ne s’adresse pas spécialement aux enfants. Elle ne collecte aucune donnée personnelle, de personne.",
 h_changes="MODIFICATIONS", changes="Si cette politique change, la nouvelle version sera publiée à cette adresse avec une date mise à jour ci-dessous.",
 h_contact="CONTACT", contact='Des questions ? Ouvre un ticket sur notre <a href="{issues}">page d’assistance</a>.', date="Date d’entrée en vigueur : 16 novembre 2026",
 h_bug="UN BUG ? UNE IDÉE ?", bug='Le plus rapide pour nous joindre est d’<a href="{issues}">ouvrir un ticket sur GitHub</a>. Rapports de bugs, suggestions et questions sur les règles sont les bienvenus. Dis-nous ce qui s’est passé et ce que tu attendais.',
 h_faq="QUESTIONS FRÉQUENTES",
 faq=[("Comment se déroule une partie ?", "Choisis une route sur la carte. Chaque niveau est un jeu différent ; termine-le et choisis une carte d’amélioration. Un choc te coûte un serpent. Perds le dernier et la partie est finie."),
      ("Quelle différence entre Classique et Moderne ?", "Les deux sont le mode Infini : un seul plateau, sans fin, pour le meilleur score. Moderne a le saut et les bonus. Classique, c’est le Snake tel que tu t’en souviens."),
      ("Comment sauter ?", "Touche le bouton SAUT et ton serpent passe par-dessus son propre corps."),
      ("Où sont gardés mes scores ?", "Sur ton appareil, et dans ton compte iCloud si tu es connecté. Connecte-toi à Game Center pour mettre tes meilleurs scores dans les classements mondiaux.")],
 h_fine="LES PETITS CARACTÈRES", fine='Snake Lab n’a ni publicité ni achats intégrés. Il ne collecte aucune donnée personnelle, seulement des statistiques de jeu anonymes ; voir la <a href="privacy.html">politique de confidentialité</a>.')
T["de"] = dict(home="START", support="SUPPORT", privacy="DATENSCHUTZ", privacy_title="DATENSCHUTZERKLÄRUNG",
 tagline="Ein Snake-Roguelike", lead="Snake, neu gebaut als Roguelike.",
 pitch="Wähle deinen Weg durch Stufen, die sich alle anders spielen, nimm nach jeder Stufe ein Upgrade und halte deine letzte Schlange am Leben. Keine Werbung, keine In-App-Käufe.",
 avail="Im App Store für iPhone erhältlich.",
 short="Kurz gesagt: Snake Lab sammelt keine personenbezogenen Daten. Keine Werbung, keine Konten. Die App sendet anonyme Spielstatistiken, die uns helfen, das Spiel zu verbessern.",
 h_collect="WAS DIE APP SAMMELT", collect="Keine personenbezogenen Daten. Es gibt keine Werbung und keine Konten. Deine Läufe, Punkte, Freischaltungen und Einstellungen bleiben auf deinem Gerät. Das Einzige, was die App uns sendet, sind die unten beschriebenen anonymen Spielstatistiken.",
 h_stats="ANONYME SPIELSTATISTIKEN", stats="Um herauszufinden, welche Stufen zu schwer sind, welche Upgrades gewählt werden und wie lange Läufe dauern, sendet die App kurze Spielprotokolle: wann die App geöffnet und geschlossen wird, welchen Modus und welche Räume du wählst, welche Karten du nimmst, gewonnene Stufen, wie jede Schlange verloren ging sowie Punkte und Zeiten. Jedes Protokoll enthält außerdem die App-Version, das iPhone-Modell, die iOS-Version, die Spielsprache und die Regionseinstellung deines Telefons.",
 stats2="Die Protokolle tragen eine Zufallszahl, die bei der Installation der App erzeugt wird, damit wir sehen, wie viele Menschen spielen. Sie ist weder mit deinem Namen, deiner Apple-ID, deinem Game-Center-Konto, deiner Werbe-ID noch mit deinem Standort verknüpft; deine IP-Adresse wird nicht gespeichert, und wenn du die App löschst, verfällt die Zahl. Die Protokolle werden bei Microsoft Azure Application Insights gespeichert, nach 90 Tagen gelöscht und nur zur Verbesserung von Snake Lab verwendet. Sie werden nie verkauft, weitergegeben oder für Werbung oder Tracking genutzt.",
 h_icloud="ICLOUD", icloud="Wenn du bei iCloud angemeldet bist, werden deine Punkte und Freischaltungen in deinem eigenen iCloud-Konto gespeichert, damit sie dir auf deine anderen Geräte folgen. Apple speichert sie gemäß Apples Datenschutzrichtlinie; wir können sie nicht sehen.",
 h_gc="GAME CENTER", gc="Wenn du dich bei Apples Game Center anmeldest, werden deine besten Punktzahlen gemäß Apples Datenschutzrichtlinie an Apples Bestenlisten-Dienst übermittelt. Deine Game-Center-Identität sehen wir nie.",
 h_children="KINDER", children="Die App ist für alle Altersgruppen geeignet und richtet sich nicht speziell an Kinder. Sie sammelt von niemandem personenbezogene Daten.",
 h_changes="ÄNDERUNGEN", changes="Falls sich diese Erklärung ändert, wird die neue Fassung unter dieser Adresse mit aktualisiertem Datum veröffentlicht.",
 h_contact="KONTAKT", contact='Fragen? Eröffne ein Issue auf unserer <a href="{issues}">Support-Seite</a>.', date="Gültig ab: 16. November 2026",
 h_bug="FEHLER GEFUNDEN? EINE IDEE?", bug='Am schnellsten erreichst du uns, wenn du <a href="{issues}">ein Issue auf GitHub eröffnest</a>. Fehlerberichte, Wünsche und Fragen zu den Regeln sind willkommen. Schreib, was passiert ist und was du erwartet hast.',
 h_faq="HÄUFIGE FRAGEN",
 faq=[("Wie läuft ein Lauf ab?", "Wähle einen Weg über die Karte. Jede Stufe ist eine andere Art Spiel; schaffe sie und wähle eine Upgrade-Karte. Ein Crash kostet eine Schlange. Verlierst du die letzte, ist der Lauf vorbei."),
      ("Was ist der Unterschied zwischen Klassisch und Modern?", "Beides ist der Endlosmodus: ein Brett, kein Ende, auf Highscore gespielt. Modern hat den Sprung und Extras. Klassisch ist Snake, wie du es kennst."),
      ("Wie springe ich?", "Tippe auf SPRUNG und deine Schlange hüpft über ihren eigenen Körper."),
      ("Wo werden meine Punkte gespeichert?", "Auf deinem Gerät und, wenn du angemeldet bist, in deinem iCloud-Konto. Melde dich bei Game Center an, um deine Bestwerte in die weltweiten Bestenlisten zu bringen.")],
 h_fine="DAS KLEINGEDRUCKTE", fine='Snake Lab hat keine Werbung und keine In-App-Käufe. Es sammelt keine personenbezogenen Daten, nur anonyme Spielstatistiken; siehe die <a href="privacy.html">Datenschutzerklärung</a>.')
T["it"] = dict(home="HOME", support="ASSISTENZA", privacy="PRIVACY", privacy_title="INFORMATIVA SULLA PRIVACY",
 tagline="Uno Snake roguelike", lead="Snake, ricostruito come un roguelike.",
 pitch="Scegli il tuo percorso tra livelli che si giocano ognuno in modo diverso, prendi un potenziamento dopo ogni livello e tieni in vita l’ultimo serpente. Niente pubblicità, niente acquisti in-app.",
 avail="Disponibile sull’App Store per iPhone.",
 short="In breve: Snake Lab non raccoglie dati personali. Niente pubblicità, niente account. Invia statistiche di gioco anonime che ci aiutano a migliorare il gioco.",
 h_collect="COSA RACCOGLIE L’APP", collect="Nessun dato personale. Non ci sono pubblicità né account. Partite, punteggi, sblocchi e impostazioni restano sul tuo dispositivo. L’unica cosa che l’app ci invia sono le statistiche di gioco anonime descritte qui sotto.",
 h_stats="STATISTICHE DI GIOCO ANONIME", stats="Per capire quali livelli sono troppo difficili, quali potenziamenti vengono scelti e quanto durano le partite, l’app invia brevi registrazioni di gioco: quando l’app viene aperta e chiusa, la modalità e le stanze che scegli, le carte che prendi, i livelli superati, come è stato perso ogni serpente, e punteggi e tempi. Ogni registrazione riporta anche la versione dell’app, il modello di iPhone, la versione di iOS, la lingua del gioco e l’impostazione della regione del telefono.",
 stats2="Le registrazioni condividono un numero casuale creato all’installazione dell’app, così sappiamo quante persone giocano. Non è collegato al tuo nome, all’ID Apple, all’account Game Center, all’identificativo pubblicitario né alla tua posizione; il tuo indirizzo IP non viene registrato e, se elimini l’app, il numero viene scartato. Le registrazioni sono conservate in Microsoft Azure Application Insights, eliminate dopo 90 giorni e usate solo per migliorare Snake Lab. Non vengono mai vendute, condivise o usate per pubblicità o tracciamento.",
 h_icloud="ICLOUD", icloud="Se hai effettuato l’accesso a iCloud, punteggi e sblocchi sono conservati nel tuo account iCloud per seguirti sugli altri dispositivi. Apple li conserva secondo la propria informativa sulla privacy; noi non possiamo vederli.",
 h_gc="GAME CENTER", gc="Se accedi a Game Center di Apple, i tuoi punteggi migliori vengono inviati al servizio di classifiche di Apple secondo la sua informativa sulla privacy. Non vediamo mai la tua identità Game Center.",
 h_children="MINORI", children="L’app è adatta a tutte le età e non è rivolta ai bambini. Non raccoglie dati personali da nessuno.",
 h_changes="MODIFICHE", changes="Se questa informativa cambierà, la nuova versione sarà pubblicata a questo indirizzo con una data aggiornata qui sotto.",
 h_contact="CONTATTI", contact='Domande? Apri una segnalazione sulla nostra <a href="{issues}">pagina di assistenza</a>.', date="Data di entrata in vigore: 16 novembre 2026",
 h_bug="HAI TROVATO UN BUG? HAI UN’IDEA?", bug='Il modo più rapido per contattarci è <a href="{issues}">aprire una segnalazione su GitHub</a>. Segnalazioni di bug, proposte e domande sulle regole sono benvenute. Raccontaci cosa è successo e cosa ti aspettavi.',
 h_faq="DOMANDE FREQUENTI",
 faq=[("Come funziona una partita?", "Scegli un percorso sulla mappa. Ogni livello è un tipo di gioco diverso; superalo e scegli una carta potenziamento. Se ti schianti perdi un serpente. Perso l’ultimo, la partita è finita."),
      ("Che differenza c’è tra Classico e Moderno?", "Sono entrambi la modalità Infinita: un solo tabellone, senza fine, per il punteggio più alto. Moderno ha il salto e i bonus. Classico è lo Snake che ricordi."),
      ("Come si salta?", "Tocca il pulsante SALTO e il serpente scavalca il proprio corpo."),
      ("Dove sono salvati i miei punteggi?", "Sul tuo dispositivo e, se hai effettuato l’accesso, nel tuo account iCloud. Accedi a Game Center per portare i tuoi migliori punteggi nelle classifiche mondiali.")],
 h_fine="NOTE LEGALI", fine='Snake Lab non ha pubblicità né acquisti in-app. Non raccoglie dati personali, solo statistiche di gioco anonime; vedi l’<a href="privacy.html">informativa sulla privacy</a>.')
T["pt-BR"] = dict(home="INÍCIO", support="SUPORTE", privacy="PRIVACIDADE", privacy_title="POLÍTICA DE PRIVACIDADE",
 tagline="Um Snake roguelike", lead="Snake, reconstruído como um roguelike.",
 pitch="Escolha seu caminho por fases que se jogam cada uma de um jeito, pegue uma melhoria depois de cada fase e mantenha sua última cobra viva. Sem anúncios, sem compras no app.",
 avail="Disponível na App Store para iPhone.",
 short="Resumindo: o Snake Lab não coleta dados pessoais. Sem anúncios, sem contas. Ele envia estatísticas de jogo anônimas que nos ajudam a melhorar o jogo.",
 h_collect="O QUE O APP COLETA", collect="Nenhum dado pessoal. Não há anúncios nem contas. Suas partidas, pontuações, desbloqueios e ajustes ficam no seu aparelho. A única coisa que o app nos envia são as estatísticas de jogo anônimas descritas abaixo.",
 h_stats="ESTATÍSTICAS DE JOGO ANÔNIMAS", stats="Para descobrir quais fases são difíceis demais, quais melhorias são escolhidas e quanto duram as partidas, o app envia registros curtos de jogo: quando o app é aberto e fechado, o modo e as salas que você escolhe, as cartas que você pega, as fases vencidas, como cada cobra foi perdida, e pontuações e tempos. Cada registro também traz a versão do app, o modelo do iPhone, a versão do iOS, o idioma do jogo e o ajuste de região do seu telefone.",
 stats2="Os registros compartilham um número aleatório criado quando o app é instalado, para sabermos quantas pessoas jogam. Ele não está ligado ao seu nome, Apple ID, conta do Game Center, identificador de publicidade nem localização; seu endereço IP não é registrado, e apagar o app descarta o número. Os registros ficam armazenados no Microsoft Azure Application Insights, são apagados após 90 dias e usados apenas para melhorar o Snake Lab. Nunca são vendidos, compartilhados nem usados para publicidade ou rastreamento.",
 h_icloud="ICLOUD", icloud="Se você estiver conectado ao iCloud, suas pontuações e desbloqueios ficam na sua própria conta do iCloud para acompanhar você nos outros aparelhos. A Apple os guarda conforme a Política de Privacidade dela; nós não podemos vê-los.",
 h_gc="GAME CENTER", gc="Se você entrar no Game Center da Apple, suas melhores pontuações são enviadas ao serviço de rankings da Apple conforme a Política de Privacidade da Apple. Nunca vemos sua identidade do Game Center.",
 h_children="CRIANÇAS", children="O app é adequado para todas as idades e não é voltado para crianças. Ele não coleta dados pessoais de ninguém.",
 h_changes="ALTERAÇÕES", changes="Se esta política mudar, a nova versão será publicada neste endereço com a data atualizada abaixo.",
 h_contact="CONTATO", contact='Dúvidas? Abra uma issue na nossa <a href="{issues}">página de suporte</a>.', date="Data de vigência: 16 de novembro de 2026",
 h_bug="ACHOU UM BUG? TEM UMA IDEIA?", bug='O jeito mais rápido de falar com a gente é <a href="{issues}">abrir uma issue no GitHub</a>. Relatos de bugs, sugestões e dúvidas sobre as regras são bem-vindos. Conte o que aconteceu e o que você esperava.',
 h_faq="PERGUNTAS FREQUENTES",
 faq=[("Como funciona uma partida?", "Escolha um caminho no mapa. Cada fase é um tipo diferente de jogo; conclua-a e escolha uma carta de melhoria. Se bater, você perde uma cobra. Perdeu a última, a partida acaba."),
      ("Qual a diferença entre Clássico e Moderno?", "Os dois são o modo Infinito: um tabuleiro só, sem fim, valendo recorde. O Moderno tem o pulo e os itens. O Clássico é o Snake do jeito que você lembra."),
      ("Como eu pulo?", "Toque no botão PULO e sua cobra salta por cima do próprio corpo."),
      ("Onde ficam minhas pontuações?", "No seu aparelho e, se você estiver conectado, na sua conta do iCloud. Entre no Game Center para colocar suas melhores pontuações nos rankings mundiais.")],
 h_fine="LETRAS MIÚDAS", fine='O Snake Lab não tem anúncios nem compras no app. Ele não coleta dados pessoais, apenas estatísticas de jogo anônimas; veja a <a href="privacy.html">política de privacidade</a>.')
T["pl"] = dict(home="START", support="POMOC", privacy="PRYWATNOŚĆ", privacy_title="POLITYKA PRYWATNOŚCI",
 tagline="Snake w wersji roguelike", lead="Snake przebudowany na roguelike.",
 pitch="Wybierz trasę przez etapy, z których każdy gra się inaczej, po każdym etapie weź ulepszenie i utrzymaj przy życiu ostatniego węża. Bez reklam i bez zakupów w aplikacji.",
 avail="Dostępne w App Store na iPhone’a.",
 short="W skrócie: Snake Lab nie zbiera danych osobowych. Bez reklam, bez kont. Wysyła anonimowe statystyki gry, które pomagają nam ją ulepszać.",
 h_collect="CO ZBIERA APLIKACJA", collect="Żadnych danych osobowych. Nie ma reklam ani kont. Twoje gry, wyniki, odblokowania i ustawienia zostają na urządzeniu. Jedyne, co aplikacja nam wysyła, to opisane niżej anonimowe statystyki gry.",
 h_stats="ANONIMOWE STATYSTYKI GRY", stats="Aby wiedzieć, które etapy są za trudne, które ulepszenia są wybierane i jak długo trwają rozgrywki, aplikacja wysyła krótkie zapisy gry: kiedy aplikacja jest otwierana i zamykana, jaki tryb i jakie pokoje wybierasz, jakie karty bierzesz, wygrane etapy, jak stracono każdego węża oraz wyniki i czasy. Każdy zapis zawiera też wersję aplikacji, model iPhone’a, wersję iOS, język gry i ustawienie regionu w telefonie.",
 stats2="Zapisy łączy losowy numer tworzony przy instalacji aplikacji, dzięki czemu wiemy, ile osób gra. Nie jest on powiązany z Twoim imieniem, Apple ID, kontem Game Center, identyfikatorem reklamowym ani lokalizacją; Twój adres IP nie jest zapisywany, a usunięcie aplikacji kasuje ten numer. Zapisy są przechowywane w Microsoft Azure Application Insights, usuwane po 90 dniach i używane wyłącznie do ulepszania Snake Lab. Nigdy nie są sprzedawane, udostępniane ani używane do reklam czy śledzenia.",
 h_icloud="ICLOUD", icloud="Jeśli jesteś zalogowany do iCloud, twoje wyniki i odblokowania są przechowywane na twoim własnym koncie iCloud, aby były dostępne na innych urządzeniach. Apple przechowuje je zgodnie ze swoją polityką prywatności; my ich nie widzimy.",
 h_gc="GAME CENTER", gc="Jeśli zalogujesz się do Game Center Apple, Twoje najlepsze wyniki trafiają do usługi rankingów Apple zgodnie z Polityką prywatności Apple. Nigdy nie widzimy Twojej tożsamości w Game Center.",
 h_children="DZIECI", children="Aplikacja jest odpowiednia dla każdego wieku i nie jest skierowana do dzieci. Nie zbiera od nikogo danych osobowych.",
 h_changes="ZMIANY", changes="Jeśli ta polityka się zmieni, nowa wersja zostanie opublikowana pod tym adresem z zaktualizowaną datą poniżej.",
 h_contact="KONTAKT", contact='Pytania? Zgłoś je na naszej <a href="{issues}">stronie pomocy</a>.', date="Data wejścia w życie: 16 listopada 2026",
 h_bug="ZNALAZŁEŚ BŁĄD? MASZ POMYSŁ?", bug='Najszybciej skontaktujesz się z nami, <a href="{issues}">zgłaszając problem na GitHubie</a>. Zgłoszenia błędów, propozycje i pytania o zasady są mile widziane. Napisz, co się stało i czego się spodziewałeś.',
 h_faq="CZĘSTE PYTANIA",
 faq=[("Jak wygląda gra?", "Wybierz trasę na mapie. Każdy etap to inny rodzaj gry; ukończ go i wybierz kartę ulepszenia. Zderzenie kosztuje węża. Gdy stracisz ostatniego, gra się kończy."),
      ("Czym różni się tryb klasyczny od nowoczesnego?", "Oba to tryb bez końca: jedna plansza, bez końca, gra o rekord. Nowoczesny ma skok i bonusy. Klasyczny to Snake, jakiego pamiętasz."),
      ("Jak skakać?", "Stuknij przycisk SKOK, a wąż przeskoczy nad własnym ciałem."),
      ("Gdzie są zapisane moje wyniki?", "Na twoim urządzeniu, a jeśli jesteś zalogowany, także na koncie iCloud. Zaloguj się do Game Center, by umieścić najlepsze wyniki w światowych rankingach.")],
 h_fine="DROBNY DRUK", fine='Snake Lab nie ma reklam ani zakupów w aplikacji. Nie zbiera danych osobowych, tylko anonimowe statystyki gry; zobacz <a href="privacy.html">politykę prywatności</a>.')
T["tr"] = dict(home="ANA SAYFA", support="DESTEK", privacy="GİZLİLİK", privacy_title="GİZLİLİK POLİTİKASI",
 tagline="Roguelike yılan oyunu", lead="Yılan oyunu, roguelike olarak yeniden tasarlandı.",
 pitch="Her biri farklı oynanan bölümler arasında rotanı seç, her bölümden sonra bir geliştirme al ve son yılanını hayatta tut. Reklam yok, uygulama içi satın alma yok.",
 avail="iPhone için App Store’da.",
 short="Kısacası: Snake Lab kişisel veri toplamaz. Reklam yok, hesap yok. Oyunu geliştirmemize yardımcı olan anonim oyun istatistikleri gönderir.",
 h_collect="UYGULAMA NE TOPLAR", collect="Kişisel veri yok. Reklam ve hesap yoktur. Oyunların, skorların, açtığın içerikler ve ayarların cihazında kalır. Uygulamanın bize gönderdiği tek şey, aşağıda anlatılan anonim oyun istatistikleridir.",
 h_stats="ANONİM OYUN İSTATİSTİKLERİ", stats="Hangi aşamaların fazla zor olduğunu, hangi geliştirmelerin seçildiğini ve oyunların ne kadar sürdüğünü öğrenmek için uygulama kısa oyun kayıtları gönderir: uygulamanın ne zaman açılıp kapandığı, seçtiğin mod ve odalar, aldığın kartlar, kazanılan aşamalar, her yılanın nasıl kaybedildiği, skorlar ve süreler. Her kayıt ayrıca uygulama sürümünü, iPhone modelini, iOS sürümünü, oyunun dilini ve telefonunun bölge ayarını içerir.",
 stats2="Kayıtlar, uygulama yüklendiğinde oluşturulan rastgele bir numarayı paylaşır; böylece kaç kişinin oynadığını biliriz. Bu numara adına, Apple kimliğine, Game Center hesabına, reklam kimliğine ya da konumuna bağlı değildir; IP adresin kaydedilmez ve uygulamayı silmek numarayı da siler. Kayıtlar Microsoft Azure Application Insights’ta saklanır, 90 gün sonra silinir ve yalnızca Snake Lab’i geliştirmek için kullanılır. Asla satılmaz, paylaşılmaz, reklam ya da takip için kullanılmaz.",
 h_icloud="ICLOUD", icloud="iCloud’a giriş yaptıysan skorların ve açtığın içerikler, diğer cihazlarında da seninle olsun diye kendi iCloud hesabında saklanır. Apple bunları kendi Gizlilik Politikası’na göre saklar; biz göremeyiz.",
 h_gc="GAME CENTER", gc="Apple’ın Game Center’ına giriş yaparsan en iyi skorların Apple’ın Gizlilik Politikası’na göre Apple’ın skor tablosu hizmetine gönderilir. Game Center kimliğini hiçbir zaman görmeyiz.",
 h_children="ÇOCUKLAR", children="Uygulama her yaşa uygundur ve çocuklara yönelik değildir. Kimseden kişisel veri toplamaz.",
 h_changes="DEĞİŞİKLİKLER", changes="Bu politika değişirse yeni sürüm, aşağıda güncellenmiş tarihle bu adreste yayımlanır.",
 h_contact="İLETİŞİM", contact='Sorun mu var? <a href="{issues}">Destek sayfamızda</a> bir kayıt aç.', date="Yürürlük tarihi: 16 Kasım 2026",
 h_bug="HATA MI BULDUN? FİKRİN Mİ VAR?", bug='Bize ulaşmanın en hızlı yolu <a href="{issues}">GitHub’da bir kayıt açmak</a>. Hata bildirimleri, öneriler ve kurallarla ilgili sorular memnuniyetle karşılanır. Ne olduğunu ve ne beklediğini yaz.',
 h_faq="SIK SORULANLAR",
 faq=[("Bir oyun nasıl ilerler?", "Haritada bir rota seç. Her bölüm farklı türde bir oyundur; bitir ve bir geliştirme kartı seç. Çarparsan bir yılan kaybedersin. Sonuncuyu da kaybedersen oyun biter."),
      ("Klasik ile Modern arasındaki fark ne?", "İkisi de Sonsuz mod: tek tahta, sonu yok, en yüksek skor için oynanır. Modern’de zıplama ve güçlendirmeler vardır. Klasik, hatırladığın yılan oyunudur."),
      ("Nasıl zıplarım?", "ZIPLA düğmesine dokun, yılanın kendi gövdesinin üstünden atlar."),
      ("Skorlarım nerede saklanıyor?", "Cihazında ve giriş yaptıysan iCloud hesabında. En iyi skorlarını dünya skor tablolarına taşımak için Game Center’a giriş yap.")],
 h_fine="İNCE AYRINTILAR", fine='Snake Lab’de reklam ve uygulama içi satın alma yoktur. Kişisel veri toplamaz, yalnızca anonim oyun istatistikleri gönderir; <a href="privacy.html">gizlilik politikasına</a> bak.')
T["ru"] = dict(home="ГЛАВНАЯ", support="ПОДДЕРЖКА", privacy="КОНФИДЕНЦИАЛЬНОСТЬ", privacy_title="ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ",
 tagline="Змейка-рогалик", lead="«Змейка», переосмысленная как рогалик.",
 pitch="Выбирай путь через этапы, каждый из которых играется по-своему, бери улучшение после каждого этапа и сохрани жизнь последней змейке. Без рекламы и встроенных покупок.",
 avail="Доступно в App Store для iPhone.",
 short="Коротко: Snake Lab не собирает персональные данные. Ни рекламы, ни аккаунтов. Приложение отправляет анонимную игровую статистику, которая помогает нам улучшать игру.",
 h_collect="ЧТО СОБИРАЕТ ПРИЛОЖЕНИЕ", collect="Никаких персональных данных. Здесь нет рекламы и аккаунтов. Твои забеги, очки, открытия и настройки хранятся на устройстве. Единственное, что приложение нам отправляет, — анонимная игровая статистика, описанная ниже.",
 h_stats="АНОНИМНАЯ ИГРОВАЯ СТАТИСТИКА", stats="Чтобы понять, какие этапы слишком сложные, какие улучшения выбирают и сколько длятся забеги, приложение отправляет короткие записи об игре: когда приложение открывают и закрывают, какой режим и какие комнаты ты выбираешь, какие карты берёшь, пройденные этапы, как была потеряна каждая змейка, а также очки и время. В каждой записи также есть версия приложения, модель iPhone, версия iOS, язык игры и настройка региона на твоём телефоне.",
 stats2="Записи объединяет случайный номер, созданный при установке приложения, — так мы знаем, сколько людей играет. Он не связан с твоим именем, Apple ID, учётной записью Game Center, рекламным идентификатором или местоположением; твой IP-адрес не записывается, а при удалении приложения номер пропадает. Записи хранятся в Microsoft Azure Application Insights, удаляются через 90 дней и используются только для улучшения Snake Lab. Они никогда не продаются, не передаются и не используются для рекламы или отслеживания.",
 h_icloud="ICLOUD", icloud="Если ты вошёл в iCloud, твои очки и открытия хранятся в твоей собственной учётной записи iCloud, чтобы они были доступны на других устройствах. Apple хранит их по своей политике конфиденциальности; мы их не видим.",
 h_gc="GAME CENTER", gc="Если ты войдёшь в Game Center от Apple, твои лучшие результаты отправляются в сервис таблиц лидеров Apple по её политике конфиденциальности. Мы никогда не видим твою учётную запись Game Center.",
 h_children="ДЕТИ", children="Приложение подходит для любого возраста и не предназначено специально для детей. Оно ни у кого не собирает персональные данные.",
 h_changes="ИЗМЕНЕНИЯ", changes="Если политика изменится, новая версия будет опубликована по этому адресу с обновлённой датой ниже.",
 h_contact="КОНТАКТЫ", contact='Есть вопросы? Создай обращение на нашей <a href="{issues}">странице поддержки</a>.', date="Дата вступления в силу: 16 ноября 2026 г.",
 h_bug="НАШЁЛ ОШИБКУ? ЕСТЬ ИДЕЯ?", bug='Быстрее всего связаться с нами — <a href="{issues}">создать обращение на GitHub</a>. Мы рады сообщениям об ошибках, предложениям и вопросам о правилах. Расскажи, что произошло и чего ты ожидал.',
 h_faq="ЧАСТЫЕ ВОПРОСЫ",
 faq=[("Как устроен забег?", "Выбери путь по карте. Каждый этап — другая игра; пройди его и выбери карту улучшения. Врезался — теряешь змейку. Потерял последнюю — забег окончен."),
      ("Чем «Классика» отличается от «Модерна»?", "Оба — бесконечный режим: одно поле, без конца, игра на рекорд. В «Модерне» есть прыжок и бонусы. «Классика» — та самая «Змейка», которую ты помнишь."),
      ("Как прыгать?", "Нажми кнопку ПРЫЖОК, и змейка перепрыгнет через своё тело."),
      ("Где хранятся мои очки?", "На устройстве и, если ты вошёл, в твоей учётной записи iCloud. Войди в Game Center, чтобы попасть в мировые таблицы лидеров.")],
 h_fine="МЕЛКИЙ ШРИФТ", fine='В Snake Lab нет рекламы и встроенных покупок. Приложение не собирает персональные данные, только анонимную игровую статистику; см. <a href="privacy.html">политику конфиденциальности</a>.')
T["ja"] = dict(home="ホーム", support="サポート", privacy="プライバシー", privacy_title="プライバシーポリシー",
 tagline="スネークのローグライク", lead="スネークを、ローグライクとして作り直しました。",
 pitch="ステージごとに遊び方が変わるルートを選び、クリアするたびにアップグレードを選んで、最後のヘビを生き残らせよう。広告なし、アプリ内課金なし。",
 avail="iPhone版をApp Storeで配信中。",
 short="要するに：Snake Lab は個人データを収集しません。広告なし、アカウントなし。ゲームの改善に役立つ匿名のプレイ統計を送信します。",
 h_collect="アプリが収集する情報", collect="個人データは収集しません。広告やアカウントはありません。ラン、スコア、解放した要素、設定はお使いの端末に保存されます。アプリが送信するのは、以下で説明する匿名のプレイ統計だけです。",
 h_stats="匿名のプレイ統計", stats="どのステージが難しすぎるか、どのアップグレードが選ばれるか、ランがどれくらい続くかを知るため、アプリは短いプレイ記録を送信します。内容は、アプリを開いた・閉じたタイミング、選んだモードと部屋、選んだカード、クリアしたステージ、各スネークを失った理由、スコアと時間です。各記録には、アプリのバージョン、iPhone の機種、iOS のバージョン、ゲームの言語、端末の地域設定も含まれます。",
 stats2="記録には、アプリのインストール時に作られるランダムな番号が付きます。これはプレイしている人数を知るためのものです。この番号はお名前、Apple ID、Game Center アカウント、広告識別子、位置情報とは結び付いておらず、IP アドレスも記録されません。アプリを削除すると番号は破棄されます。記録は Microsoft Azure Application Insights に保存され、90 日後に削除され、Snake Lab の改善にのみ使われます。販売、共有、広告やトラッキングへの利用は一切ありません。",
 h_icloud="ICLOUD", icloud="iCloud にサインインしている場合、スコアと解放した要素はほかの端末でも使えるよう、ご自身の iCloud アカウントに保存されます。保存は Apple のプライバシーポリシーに基づいて Apple が行い、開発者が見ることはできません。",
 h_gc="GAME CENTER", gc="Apple の Game Center にサインインすると、ベストスコアが Apple のプライバシーポリシーに基づいて Apple のランキングサービスに送信されます。開発者が Game Center のアカウントを見ることはありません。",
 h_children="お子さまについて", children="このアプリは全年齢向けですが、子ども向けに作られたものではありません。誰の個人データも収集しません。",
 h_changes="変更について", changes="このポリシーを変更する場合は、新しい内容をこのアドレスに掲載し、下の日付を更新します。",
 h_contact="お問い合わせ", contact='ご質問は<a href="{issues}">サポートページ</a>で Issue を作成してください。', date="発効日：2026年11月16日",
 h_bug="バグを見つけた？アイデアがある？", bug='いちばん早い連絡方法は <a href="{issues}">GitHub で Issue を作成する</a>ことです。バグ報告、ご要望、ルールについての質問を歓迎します。何が起きて、どうなると思っていたかを教えてください。',
 h_faq="よくある質問",
 faq=[("ランはどう進むの？", "マップでルートを選びます。ステージごとに別の種類のゲームになっていて、クリアするとアップグレードカードを選べます。ぶつかるとヘビを1匹失い、最後の1匹を失うとランは終わりです。"),
      ("クラシックとモダンの違いは？", "どちらもエンドレスモードで、1つの盤面で終わりなくハイスコアを目指します。モダンにはジャンプとアイテムがあります。クラシックは昔ながらのスネークそのものです。"),
      ("ジャンプするには？", "ジャンプボタンをタップすると、ヘビが自分の体を飛び越えます。"),
      ("スコアはどこに保存されるの？", "端末と、サインインしていれば iCloud アカウントに保存されます。Game Center にサインインすると、ベストスコアが世界ランキングに載ります。")],
 h_fine="補足事項", fine='Snake Lab には広告もアプリ内課金もありません。個人データは収集せず、匿名のプレイ統計のみを送信します。<a href="privacy.html">プライバシーポリシー</a>をご覧ください。')
T["ko"] = dict(home="홈", support="지원", privacy="개인정보", privacy_title="개인정보 처리방침",
 tagline="스네이크 로그라이크", lead="스네이크를 로그라이크로 새롭게 만들었습니다.",
 pitch="스테이지마다 플레이 방식이 다른 경로를 고르고, 스테이지를 깰 때마다 업그레이드를 골라 마지막 뱀을 살려 두세요. 광고 없음, 인앱 구매 없음.",
 avail="iPhone용 App Store에서 만나 보세요.",
 short="요약: Snake Lab은 개인 데이터를 수집하지 않습니다. 광고와 계정이 없습니다. 게임 개선에 도움이 되는 익명 플레이 통계를 전송합니다.",
 h_collect="앱이 수집하는 정보", collect="개인 데이터는 수집하지 않습니다. 광고와 계정이 없습니다. 게임 기록, 점수, 해금 항목, 설정은 기기에 저장됩니다. 앱이 저희에게 보내는 것은 아래에 설명된 익명 플레이 통계뿐입니다.",
 h_stats="익명 플레이 통계", stats="어떤 스테이지가 너무 어려운지, 어떤 업그레이드가 선택되는지, 한 판이 얼마나 이어지는지 알기 위해 앱은 짧은 플레이 기록을 전송합니다. 앱을 열고 닫은 시점, 선택한 모드와 방, 고른 카드, 클리어한 스테이지, 각 뱀을 잃은 이유, 점수와 시간이 포함됩니다. 각 기록에는 앱 버전, iPhone 모델, iOS 버전, 게임 언어, 휴대폰의 지역 설정도 함께 담깁니다.",
 stats2="기록에는 앱을 설치할 때 만들어지는 무작위 번호가 붙으며, 이를 통해 몇 명이 플레이하는지 알 수 있습니다. 이 번호는 이름, Apple ID, Game Center 계정, 광고 식별자, 위치와 연결되지 않으며, IP 주소도 기록되지 않습니다. 앱을 삭제하면 번호도 사라집니다. 기록은 Microsoft Azure Application Insights에 저장되고 90일 후 삭제되며, Snake Lab 개선에만 사용됩니다. 판매되거나 공유되지 않으며 광고나 추적에 사용되지 않습니다.",
 h_icloud="ICLOUD", icloud="iCloud에 로그인되어 있으면 점수와 해금 항목이 다른 기기에서도 이어지도록 본인의 iCloud 계정에 보관됩니다. Apple이 Apple의 개인정보 처리방침에 따라 보관하며, 저희는 볼 수 없습니다.",
 h_gc="GAME CENTER", gc="Apple의 Game Center에 로그인하면 최고 점수가 Apple의 개인정보 처리방침에 따라 Apple의 순위표 서비스로 전송됩니다. 저희는 Game Center 계정을 볼 수 없습니다.",
 h_children="어린이", children="이 앱은 모든 연령에 적합하지만 어린이를 대상으로 하지는 않습니다. 누구의 개인 데이터도 수집하지 않습니다.",
 h_changes="변경 사항", changes="이 방침이 바뀌면 새 버전을 이 주소에 게시하고 아래 날짜를 갱신합니다.",
 h_contact="문의", contact='궁금한 점은 <a href="{issues}">지원 페이지</a>에 이슈로 남겨 주세요.', date="시행일: 2026년 11월 16일",
 h_bug="버그를 찾았나요? 아이디어가 있나요?", bug='가장 빠른 연락 방법은 <a href="{issues}">GitHub에 이슈를 남기는 것</a>입니다. 버그 제보, 기능 제안, 규칙 질문 모두 환영합니다. 무슨 일이 있었고 무엇을 기대했는지 알려 주세요.',
 h_faq="자주 묻는 질문",
 faq=[("게임은 어떻게 진행되나요?", "지도에서 경로를 고르세요. 스테이지마다 다른 종류의 게임이며, 클리어하면 업그레이드 카드를 고릅니다. 부딪히면 뱀을 하나 잃고, 마지막 뱀을 잃으면 게임이 끝납니다."),
      ("클래식과 모던은 무엇이 다른가요?", "둘 다 무한 모드로, 하나의 보드에서 끝없이 최고 점수를 노립니다. 모던에는 점프와 아이템이 있고, 클래식은 기억하는 그대로의 스네이크입니다."),
      ("점프는 어떻게 하나요?", "점프 버튼을 누르면 뱀이 자기 몸을 뛰어넘습니다."),
      ("점수는 어디에 저장되나요?", "기기에 저장되고, 로그인되어 있다면 iCloud 계정에도 저장됩니다. Game Center에 로그인하면 최고 점수가 세계 순위표에 올라갑니다.")],
 h_fine="참고 사항", fine='Snake Lab에는 광고도 인앱 구매도 없습니다. 개인 데이터는 수집하지 않으며 익명 플레이 통계만 전송합니다. <a href="privacy.html">개인정보 처리방침</a>을 참고하세요.')
T["zh-Hans"] = dict(home="首页", support="支持", privacy="隐私", privacy_title="隐私政策",
 tagline="Roguelike 贪吃蛇", lead="贪吃蛇，以 Roguelike 的方式重新打造。",
 pitch="选择穿过玩法各不相同的关卡的路线，每关之后选一项升级，让最后一条蛇活下去。无广告，无内购。",
 avail="现已登陆 iPhone 版 App Store。",
 short="简而言之：Snake Lab 不收集个人数据。没有广告，没有账号。它会发送匿名的游戏统计，帮助我们改进游戏。",
 h_collect="应用收集的信息", collect="不收集个人数据。没有广告，也没有账号。你的对局、分数、解锁内容和设置都保存在你的设备上。应用唯一发送给我们的，是下文所述的匿名游戏统计。",
 h_stats="匿名游戏统计", stats="为了了解哪些关卡太难、哪些升级被选择、一局能持续多久，应用会发送简短的游戏记录：应用何时打开和关闭、你选择的模式和房间、你拿的卡牌、通过的关卡、每条蛇是怎么失去的，以及分数和时间。每条记录还包含应用版本、iPhone 型号、iOS 版本、游戏语言和你手机的地区设置。",
 stats2="这些记录共用一个在安装应用时生成的随机编号，让我们知道有多少人在玩。它与你的姓名、Apple ID、Game Center 账号、广告标识符或位置都没有关联；你的 IP 地址不会被记录，删除应用后该编号即被丢弃。记录存储在 Microsoft Azure Application Insights 中，90 天后删除，仅用于改进 Snake Lab。它们绝不会被出售、共享，也不会用于广告或跟踪。",
 h_icloud="ICLOUD", icloud="如果你已登录 iCloud，分数和解锁内容会保存在你自己的 iCloud 账户中，方便在其他设备上继续使用。Apple 依照其隐私政策保存这些数据，我们无法查看。",
 h_gc="GAME CENTER", gc="如果你登录 Apple 的 Game Center，你的最高分会依照 Apple 的隐私政策提交到 Apple 的排行榜服务。我们从不查看你的 Game Center 身份。",
 h_children="儿童", children="本应用适合所有年龄段，但并非专为儿童设计。它不收集任何人的个人数据。",
 h_changes="变更", changes="如果本政策有变，新版本将发布在此地址，并更新下方日期。",
 h_contact="联系方式", contact='有疑问？请在我们的<a href="{issues}">支持页面</a>提交 issue。', date="生效日期：2026年11月16日",
 h_bug="发现了 bug？有好点子？", bug='联系我们最快的方式是<a href="{issues}">在 GitHub 上提交 issue</a>。欢迎反馈 bug、提出功能建议或询问规则。请告诉我们发生了什么，以及你原本的预期。',
 h_faq="常见问题",
 faq=[("一局是怎么进行的？", "在地图上选择路线。每一关都是不同类型的游戏；通关后选择一张升级卡。撞上就会失去一条蛇，失去最后一条，这一局就结束了。"),
      ("经典和现代有什么区别？", "两者都是无尽模式：一个棋盘，没有尽头，挑战最高分。现代模式有跳跃和道具，经典模式就是你记忆中的贪吃蛇。"),
      ("怎么跳跃？", "点击“跳”按钮，蛇就会跃过自己的身体。"),
      ("我的分数保存在哪里？", "保存在你的设备上，如果已登录，也会保存在你的 iCloud 账户中。登录 Game Center 即可让最高分登上全球排行榜。")],
 h_fine="附注", fine='Snake Lab 没有广告，也没有内购。它不收集个人数据，只发送匿名的游戏统计；请参阅<a href="privacy.html">隐私政策</a>。')
T["zh-Hant"] = dict(home="首頁", support="支援", privacy="隱私", privacy_title="隱私權政策",
 tagline="Roguelike 貪食蛇", lead="貪食蛇，以 Roguelike 的方式重新打造。",
 pitch="選擇穿越玩法各不相同的關卡的路線，每關之後選一項升級，讓最後一條蛇活下去。無廣告，無內購。",
 avail="現已登上 iPhone 版 App Store。",
 short="簡而言之：Snake Lab 不收集個人資料。沒有廣告，沒有帳號。它會傳送匿名的遊戲統計，幫助我們改進遊戲。",
 h_collect="App 收集的資訊", collect="不收集個人資料。沒有廣告，也沒有帳號。你的對局、分數、解鎖內容和設定都儲存在你的裝置上。App 唯一傳送給我們的，是下文所述的匿名遊戲統計。",
 h_stats="匿名遊戲統計", stats="為了了解哪些關卡太難、哪些升級被選擇、一局能持續多久，App 會傳送簡短的遊戲紀錄：App 何時開啟和關閉、你選擇的模式和房間、你拿的卡牌、通過的關卡、每條蛇是怎麼失去的，以及分數和時間。每筆紀錄還包含 App 版本、iPhone 型號、iOS 版本、遊戲語言和你手機的地區設定。",
 stats2="這些紀錄共用一個在安裝 App 時產生的隨機編號，讓我們知道有多少人在玩。它與你的姓名、Apple ID、Game Center 帳號、廣告識別碼或位置都沒有關聯；你的 IP 位址不會被記錄，刪除 App 後該編號即被捨棄。紀錄儲存在 Microsoft Azure Application Insights 中，90 天後刪除，僅用於改進 Snake Lab。它們絕不會被出售、分享，也不會用於廣告或追蹤。",
 h_icloud="ICLOUD", icloud="如果你已登入 iCloud，分數和解鎖內容會保存在你自己的 iCloud 帳號中，方便在其他裝置上繼續使用。Apple 依照其隱私權政策保存這些資料，我們無法查看。",
 h_gc="GAME CENTER", gc="如果你登入 Apple 的 Game Center，你的最高分會依照 Apple 的隱私權政策提交到 Apple 的排行榜服務。我們從不查看你的 Game Center 身分。",
 h_children="兒童", children="本 App 適合所有年齡層，但並非專為兒童設計。它不收集任何人的個人資料。",
 h_changes="變更", changes="如果本政策有變，新版本將發布在此網址，並更新下方日期。",
 h_contact="聯絡方式", contact='有疑問？請在我們的<a href="{issues}">支援頁面</a>提交 issue。', date="生效日期：2026年11月16日",
 h_bug="發現了 bug？有好點子？", bug='聯絡我們最快的方式是<a href="{issues}">在 GitHub 上提交 issue</a>。歡迎回報 bug、提出功能建議或詢問規則。請告訴我們發生了什麼，以及你原本的預期。',
 h_faq="常見問題",
 faq=[("一局是怎麼進行的？", "在地圖上選擇路線。每一關都是不同類型的遊戲；過關後選擇一張升級卡。撞上就會失去一條蛇，失去最後一條，這一局就結束了。"),
      ("經典和現代有什麼不同？", "兩者都是無盡模式：一個棋盤，沒有盡頭，挑戰最高分。現代模式有跳躍和道具，經典模式就是你記憶中的貪食蛇。"),
      ("怎麼跳躍？", "點擊「跳」按鈕，蛇就會躍過自己的身體。"),
      ("我的分數保存在哪裡？", "保存在你的裝置上，如果已登入，也會保存在你的 iCloud 帳號中。登入 Game Center 即可讓最高分登上全球排行榜。")],
 h_fine="附註", fine='Snake Lab 沒有廣告，也沒有內購。它不收集個人資料，只傳送匿名的遊戲統計；請參閱<a href="privacy.html">隱私權政策</a>。')

# CREDITS on the support page: the heading and roles as the game's own CREDITS screen says them, then
# the sentence on Fusion Pixel's license ({ofl} is the link to it).
C = {
    "en": ("CREDITS", "A GAME BY", "TEXTURES", "SOUNDS", "FONTS", "Fusion Pixel is used under the {ofl}; its license ships inside the app."),
    "es": ("CRÉDITOS", "UN JUEGO DE", "TEXTURAS", "SONIDOS", "FUENTES", "Fusion Pixel se usa bajo la {ofl}; su licencia viene dentro de la app."),
    "fr": ("CRÉDITS", "UN JEU DE", "TEXTURES", "SONS", "POLICES", "Fusion Pixel est utilisée sous la {ofl} ; sa licence est fournie dans l’app."),
    "de": ("MITWIRKENDE", "EIN SPIEL VON", "TEXTUREN", "TÖNE", "SCHRIFTEN", "Fusion Pixel wird unter der {ofl} verwendet; die Lizenz liegt der App bei."),
    "it": ("RICONOSCIMENTI", "UN GIOCO DI", "TEXTURE", "SUONI", "FONT", "Fusion Pixel è usato con la {ofl}; la licenza è inclusa nell’app."),
    "pt-BR": ("CRÉDITOS", "UM JOGO DE", "TEXTURAS", "SONS", "FONTES", "A Fusion Pixel é usada sob a {ofl}; a licença acompanha o app."),
    "pl": ("TWÓRCY", "GRA AUTORSTWA", "TEKSTURY", "DŹWIĘKI", "CZCIONKI", "Fusion Pixel jest używany na licencji {ofl}; jej tekst jest dołączony do aplikacji."),
    "tr": ("EMEĞİ GEÇENLER", "YAPIMCI", "DOKULAR", "SESLER", "YAZI TİPLERİ", "Fusion Pixel, {ofl} ile kullanılır; lisans metni uygulamanın içindedir."),
    "ru": ("АВТОРЫ", "ИГРА ОТ", "ТЕКСТУРЫ", "ЗВУКИ", "ШРИФТЫ", "Fusion Pixel используется по лицензии {ofl}; её текст входит в приложение."),
    "ja": ("クレジット", "ゲーム制作", "テクスチャ", "サウンド", "フォント", "Fusion Pixel は {ofl} のもとで使用しています。ライセンス文はアプリに同梱しています。"),
    "ko": ("크레딧", "제작", "텍스처", "효과음", "글꼴", "Fusion Pixel은 {ofl}에 따라 사용합니다. 라이선스 전문은 앱에 포함되어 있습니다."),
    "zh-Hans": ("制作人员", "制作", "纹理", "音效", "字体", "Fusion Pixel 依据 {ofl} 使用，许可证全文随应用附带。"),
    "zh-Hant": ("製作人員", "製作", "材質", "音效", "字型", "Fusion Pixel 依據 {ofl} 使用，授權條款全文隨應用程式附帶。"),
}
OFL = '<a href="https://github.com/TakWolf/fusion-pixel-font/blob/master/LICENSE-OFL">SIL Open Font License 1.1</a>'
def link(name, url): return f'<a href="{url}">{name}</a>'
WHO = ["Jacob Lyons",
       link("flakdeau19", "https://flakdeau19.itch.io/pixel-art-texture-pack-256x256") + " (Pixel Art Texture Pack)",
       link("SoundFellas", "https://soundfellas.com/") + " (Technology Labs)",
       " · ".join([link("Not Jam", "https://not-jam.itch.io/") + " (Not Jam UI)", link("somepx", "https://somepx.itch.io/pixel-font-awesome") + " (Awesome 9)",
                   link("TakWolf", "https://github.com/TakWolf/fusion-pixel-font") + " (Fusion Pixel)"])]
LABEL = {"index": "LAB", "support": "SUPPORT", "privacy": "PRIVACY"}
def page(lang, kind, title, body):
    up = "" if lang == "en" else "../"
    file = "" if kind == "index" else kind + ".html"
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{ROOT}{"" if l == "en" else l + "/"}{file}">' for l, _ in LANGS)
    langs = " ".join(f'<a class="key{" lit" if l == lang else ""}" href="{up}{"" if l == "en" else l + "/"}{file}" hreflang="{l}">{n}</a>' for l, n in LANGS)
    t = T[lang]
    keys = [("index", t["home"]), ("support", t["support"]), ("privacy", t["privacy"])]
    nav = " ".join(f'<a class="key{" lit" if k == kind else ""}" href="{k}.html">{n}</a>' for k, n in keys)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Snake Lab</title>
<meta name="description" content="{html.escape(t["tagline"])}">
<link rel="icon" href="{up}assets/icon.png">
{alts}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&family=VT323&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="wrap">
  <header class="plate">
    <div class="hazard"></div>
    <div class="hud">
      <div class="name"><img src="{up}assets/icon.png" alt="" width="56" height="56"><div><small>{"SNAKE LAB" if kind != "index" else html.escape(t["tagline"]).upper()}</small><h1>{title}</h1></div></div>
      <nav class="pages">{nav}</nav>
    </div>
    <nav class="langs">{langs}</nav>
  </header>
  <main class="console">
    <p class="label">{LABEL[kind]} · {html.escape(t["tagline"]).upper()}</p>
    <div class="screen">
{body}
      <div class="snake" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i class="head"></i><b></b></div>
    </div>
  </main>
  <footer>© 2026 JACOB LYONS</footer>
</div>
</body>
</html>
'''
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); docs = os.path.join(here, "docs")
for lang, _ in LANGS:
    t = T[lang]; up = "" if lang == "en" else "../"; d = docs if lang == "en" else os.path.join(docs, lang); os.makedirs(d, exist_ok=True)
    media = up + "assets/" + ("" if lang == "en" else lang + "/")  # each language's own film and screenshots
    shots = "".join(f'<img src="{media}shot{i}.jpg" alt="" loading="lazy">' for i in (1, 2, 3, 4))
    home = f'''      <div class="hero">
        <p class="lead">{t["lead"]}</p>
        <p>{t["pitch"]}</p>
        <div class="media"><video src="{media}film.mp4" poster="{media}poster.jpg" muted loop playsinline autoplay></video>{shots}</div>
        <p><strong>{t["avail"]}</strong></p>
      </div>'''
    sec = lambda h, p: f'      <h2>{h}</h2><p>{p}</p>'
    priv = "\n".join([f'      <p><strong>{t["short"]}</strong></p>', sec(t["h_collect"], t["collect"]), sec(t["h_stats"], t["stats"]) + f'<p>{t["stats2"]}</p>', sec(t["h_icloud"], t["icloud"]), sec(t["h_gc"], t["gc"]),
                      sec(t["h_children"], t["children"]), sec(t["h_changes"], t["changes"]), sec(t["h_contact"], t["contact"].format(issues=ISSUES)),
                      f'      <p class="small">{t["date"]}</p>'])
    sup = "\n".join([sec(t["h_bug"], t["bug"].format(issues=ISSUES)), f'      <h2>{t["h_faq"]}</h2>'] +
                    [f'      <p class="qa"><strong>{html.escape(q)}</strong>{html.escape(a)}</p>' for q, a in t["faq"]] + [sec(t["h_fine"], t["fine"])] +
                    [f'      <h2>{C[lang][0]}</h2>'] + [f'      <p class="qa"><strong>{role}</strong>{who}</p>' for role, who in zip(C[lang][1:5], WHO)] +
                    [f'      <p class="small">{C[lang][5].format(ofl=OFL)}</p>'])
    open(os.path.join(d, "index.html"), "w").write(page(lang, "index", "SNAKE LAB", home))
    open(os.path.join(d, "privacy.html"), "w").write(page(lang, "privacy", t["privacy_title"], priv))
    open(os.path.join(d, "support.html"), "w").write(page(lang, "support", t["support"], sup))
print("pages:", sum(len(f) for _, _, f in os.walk(docs)))
