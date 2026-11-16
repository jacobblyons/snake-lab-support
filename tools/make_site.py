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
 short="The short version: Snake Lab collects nothing. No ads, no analytics, no accounts.",
 h_collect="WHAT THE APP COLLECTS", collect="Nothing. There are no ads, no accounts and no analytics, and the app makes no network requests of its own. Your runs, scores, unlocks and settings live on your device.",
 h_icloud="ICLOUD", icloud="If you are signed in to iCloud, your scores and unlocks are kept in your own iCloud account so they follow you to your other devices. Apple stores them under Apple's Privacy Policy; we cannot see them.",
 h_gc="GAME CENTER", gc="If you sign in to Apple's Game Center, your best scores are submitted to Apple's leaderboard service under Apple's Privacy Policy. We never see or store your Game Center identity or scores on any server of ours; we have no servers.",
 h_children="CHILDREN", children="The app is suitable for all ages and is not directed at children. It collects no data from anyone.",
 h_changes="CHANGES", changes="If this policy ever changes, the new version will be posted at this address with an updated date below.",
 h_contact="CONTACT", contact='Questions? Open an issue on our <a href="{issues}">support page</a>.', date="Effective date: November 16, 2026",
 h_bug="FOUND A BUG? HAVE AN IDEA?", bug='The fastest way to reach us is to <a href="{issues}">open an issue on GitHub</a>. Bug reports, feature requests and rule questions are all welcome. Tell us what happened and what you expected.',
 h_faq="COMMON QUESTIONS",
 faq=[("How does a run work?", "Choose a route through the map. Each stage is a different kind of game; clear it and pick an upgrade card. Crash and you lose a snake. Lose your last one and the run is over."),
      ("What is the difference between Classic and Modern?", "Both are Endless mode: one board, no end, played for a high score. Modern has the jump and pick-ups. Classic is Snake exactly as you remember it."),
      ("How do I jump?", "Tap the JUMP button and your snake hops over its own body."),
      ("Where are my scores kept?", "On your device, and in your iCloud account if you are signed in. Sign in to Game Center to put your best scores on the world leaderboards.")],
 h_fine="THE FINE PRINT", fine='Snake Lab has no ads and no in-app purchases. It collects no data; see the <a href="privacy.html">privacy policy</a>.')
T["es"] = dict(home="INICIO", support="SOPORTE", privacy="PRIVACIDAD", privacy_title="POLÍTICA DE PRIVACIDAD",
 tagline="Un roguelike de Snake", lead="Snake, reconstruido como un roguelike.",
 pitch="Elige tu ruta por fases que se juegan cada una a su manera, escoge una mejora tras cada fase y mantén viva tu última serpiente. Sin anuncios ni compras dentro de la app.",
 avail="Disponible en el App Store para iPhone.",
 short="En resumen: Snake Lab no recopila nada. Sin anuncios, sin analíticas, sin cuentas.",
 h_collect="QUÉ RECOPILA LA APP", collect="Nada. No hay anuncios, ni cuentas, ni analíticas, y la app no hace peticiones de red propias. Tus partidas, puntuaciones, desbloqueos y ajustes se guardan en tu dispositivo.",
 h_icloud="ICLOUD", icloud="Si has iniciado sesión en iCloud, tus puntuaciones y desbloqueos se guardan en tu propia cuenta de iCloud para que te acompañen en tus otros dispositivos. Apple los guarda según su Política de Privacidad; nosotros no podemos verlos.",
 h_gc="GAME CENTER", gc="Si inicias sesión en Game Center de Apple, tus mejores puntuaciones se envían al servicio de clasificaciones de Apple según su Política de Privacidad. Nunca vemos ni guardamos tu identidad de Game Center ni tus puntuaciones en ningún servidor nuestro; no tenemos servidores.",
 h_children="MENORES", children="La app es apta para todas las edades y no está dirigida a menores. No recopila datos de nadie.",
 h_changes="CAMBIOS", changes="Si esta política cambia, la nueva versión se publicará en esta dirección con una fecha actualizada abajo.",
 h_contact="CONTACTO", contact='¿Preguntas? Abre una incidencia en nuestra <a href="{issues}">página de soporte</a>.', date="Fecha de entrada en vigor: 16 de noviembre de 2026",
 h_bug="¿HAS ENCONTRADO UN ERROR? ¿TIENES UNA IDEA?", bug='La forma más rápida de contactarnos es <a href="{issues}">abrir una incidencia en GitHub</a>. Informes de errores, sugerencias y dudas sobre las reglas son bienvenidos. Cuéntanos qué pasó y qué esperabas.',
 h_faq="PREGUNTAS FRECUENTES",
 faq=[("¿Cómo funciona una partida?", "Elige una ruta en el mapa. Cada fase es un tipo de juego distinto; supérala y elige una carta de mejora. Si chocas, pierdes una serpiente. Si pierdes la última, la partida termina."),
      ("¿Qué diferencia hay entre Clásico y Moderno?", "Los dos son el modo Infinito: un solo tablero, sin final, a por la mejor puntuación. Moderno tiene el salto y los objetos. Clásico es el Snake tal y como lo recuerdas."),
      ("¿Cómo salto?", "Pulsa el botón SALTO y tu serpiente saltará por encima de su propio cuerpo."),
      ("¿Dónde se guardan mis puntuaciones?", "En tu dispositivo, y en tu cuenta de iCloud si has iniciado sesión. Inicia sesión en Game Center para poner tus mejores puntuaciones en las clasificaciones mundiales.")],
 h_fine="LA LETRA PEQUEÑA", fine='Snake Lab no tiene anuncios ni compras dentro de la app. No recopila datos; consulta la <a href="privacy.html">política de privacidad</a>.')
T["fr"] = dict(home="ACCUEIL", support="ASSISTANCE", privacy="CONFIDENTIALITÉ", privacy_title="POLITIQUE DE CONFIDENTIALITÉ",
 tagline="Un Snake roguelike", lead="Snake, reconstruit en roguelike.",
 pitch="Choisis ta route à travers des niveaux qui se jouent tous différemment, prends une amélioration après chaque niveau et garde ton dernier serpent en vie. Pas de publicité, pas d’achats intégrés.",
 avail="Disponible sur l’App Store pour iPhone.",
 short="En bref : Snake Lab ne collecte rien. Pas de publicité, pas d’analyses, pas de comptes.",
 h_collect="CE QUE L’APP COLLECTE", collect="Rien. Il n’y a ni publicité, ni compte, ni analyse, et l’app n’effectue aucune requête réseau de son propre chef. Tes parties, scores, déblocages et réglages restent sur ton appareil.",
 h_icloud="ICLOUD", icloud="Si tu es connecté à iCloud, tes scores et déblocages sont conservés dans ton propre compte iCloud pour te suivre sur tes autres appareils. Apple les stocke selon sa politique de confidentialité ; nous ne pouvons pas les voir.",
 h_gc="GAME CENTER", gc="Si tu te connectes à Game Center d’Apple, tes meilleurs scores sont envoyés au service de classements d’Apple selon sa politique de confidentialité. Nous ne voyons ni ne stockons jamais ton identité Game Center ou tes scores sur un serveur à nous ; nous n’avons pas de serveur.",
 h_children="ENFANTS", children="L’app convient à tous les âges et ne s’adresse pas spécialement aux enfants. Elle ne collecte aucune donnée, de personne.",
 h_changes="MODIFICATIONS", changes="Si cette politique change, la nouvelle version sera publiée à cette adresse avec une date mise à jour ci-dessous.",
 h_contact="CONTACT", contact='Des questions ? Ouvre un ticket sur notre <a href="{issues}">page d’assistance</a>.', date="Date d’entrée en vigueur : 16 novembre 2026",
 h_bug="UN BUG ? UNE IDÉE ?", bug='Le plus rapide pour nous joindre est d’<a href="{issues}">ouvrir un ticket sur GitHub</a>. Rapports de bugs, suggestions et questions sur les règles sont les bienvenus. Dis-nous ce qui s’est passé et ce que tu attendais.',
 h_faq="QUESTIONS FRÉQUENTES",
 faq=[("Comment se déroule une partie ?", "Choisis une route sur la carte. Chaque niveau est un jeu différent ; termine-le et choisis une carte d’amélioration. Un choc te coûte un serpent. Perds le dernier et la partie est finie."),
      ("Quelle différence entre Classique et Moderne ?", "Les deux sont le mode Infini : un seul plateau, sans fin, pour le meilleur score. Moderne a le saut et les bonus. Classique, c’est le Snake tel que tu t’en souviens."),
      ("Comment sauter ?", "Touche le bouton SAUT et ton serpent passe par-dessus son propre corps."),
      ("Où sont gardés mes scores ?", "Sur ton appareil, et dans ton compte iCloud si tu es connecté. Connecte-toi à Game Center pour mettre tes meilleurs scores dans les classements mondiaux.")],
 h_fine="LES PETITS CARACTÈRES", fine='Snake Lab n’a ni publicité ni achats intégrés. Il ne collecte aucune donnée ; voir la <a href="privacy.html">politique de confidentialité</a>.')
T["de"] = dict(home="START", support="SUPPORT", privacy="DATENSCHUTZ", privacy_title="DATENSCHUTZERKLÄRUNG",
 tagline="Ein Snake-Roguelike", lead="Snake, neu gebaut als Roguelike.",
 pitch="Wähle deinen Weg durch Stufen, die sich alle anders spielen, nimm nach jeder Stufe ein Upgrade und halte deine letzte Schlange am Leben. Keine Werbung, keine In-App-Käufe.",
 avail="Im App Store für iPhone erhältlich.",
 short="Kurz gesagt: Snake Lab sammelt nichts. Keine Werbung, keine Analysen, keine Konten.",
 h_collect="WAS DIE APP SAMMELT", collect="Nichts. Es gibt keine Werbung, keine Konten und keine Analysen, und die App stellt selbst keine Netzwerkanfragen. Deine Läufe, Punkte, Freischaltungen und Einstellungen bleiben auf deinem Gerät.",
 h_icloud="ICLOUD", icloud="Wenn du bei iCloud angemeldet bist, werden deine Punkte und Freischaltungen in deinem eigenen iCloud-Konto gespeichert, damit sie dir auf deine anderen Geräte folgen. Apple speichert sie gemäß Apples Datenschutzrichtlinie; wir können sie nicht sehen.",
 h_gc="GAME CENTER", gc="Wenn du dich bei Apples Game Center anmeldest, werden deine Bestwerte gemäß Apples Datenschutzrichtlinie an Apples Bestenlisten-Dienst übermittelt. Wir sehen oder speichern deine Game-Center-Identität oder Punkte nie auf eigenen Servern; wir haben keine Server.",
 h_children="KINDER", children="Die App ist für alle Altersgruppen geeignet und richtet sich nicht an Kinder. Sie sammelt von niemandem Daten.",
 h_changes="ÄNDERUNGEN", changes="Falls sich diese Erklärung ändert, wird die neue Fassung unter dieser Adresse mit aktualisiertem Datum veröffentlicht.",
 h_contact="KONTAKT", contact='Fragen? Eröffne ein Issue auf unserer <a href="{issues}">Support-Seite</a>.', date="Gültig ab: 16. November 2026",
 h_bug="FEHLER GEFUNDEN? EINE IDEE?", bug='Am schnellsten erreichst du uns, wenn du <a href="{issues}">ein Issue auf GitHub eröffnest</a>. Fehlerberichte, Wünsche und Fragen zu den Regeln sind willkommen. Schreib, was passiert ist und was du erwartet hast.',
 h_faq="HÄUFIGE FRAGEN",
 faq=[("Wie läuft ein Lauf ab?", "Wähle einen Weg über die Karte. Jede Stufe ist eine andere Art Spiel; schaffe sie und wähle eine Upgrade-Karte. Ein Crash kostet eine Schlange. Verlierst du die letzte, ist der Lauf vorbei."),
      ("Was ist der Unterschied zwischen Klassisch und Modern?", "Beides ist der Endlosmodus: ein Brett, kein Ende, auf Highscore gespielt. Modern hat den Sprung und Extras. Klassisch ist Snake, wie du es kennst."),
      ("Wie springe ich?", "Tippe auf SPRUNG und deine Schlange hüpft über ihren eigenen Körper."),
      ("Wo werden meine Punkte gespeichert?", "Auf deinem Gerät und, wenn du angemeldet bist, in deinem iCloud-Konto. Melde dich bei Game Center an, um deine Bestwerte in die weltweiten Bestenlisten zu bringen.")],
 h_fine="DAS KLEINGEDRUCKTE", fine='Snake Lab hat keine Werbung und keine In-App-Käufe. Es sammelt keine Daten; siehe die <a href="privacy.html">Datenschutzerklärung</a>.')
T["it"] = dict(home="HOME", support="ASSISTENZA", privacy="PRIVACY", privacy_title="INFORMATIVA SULLA PRIVACY",
 tagline="Uno Snake roguelike", lead="Snake, ricostruito come un roguelike.",
 pitch="Scegli il tuo percorso tra livelli che si giocano ognuno in modo diverso, prendi un potenziamento dopo ogni livello e tieni in vita l’ultimo serpente. Niente pubblicità, niente acquisti in-app.",
 avail="Disponibile sull’App Store per iPhone.",
 short="In breve: Snake Lab non raccoglie nulla. Niente pubblicità, niente analisi, niente account.",
 h_collect="COSA RACCOGLIE L’APP", collect="Nulla. Non ci sono pubblicità, account o analisi, e l’app non effettua richieste di rete proprie. Partite, punteggi, sblocchi e impostazioni restano sul tuo dispositivo.",
 h_icloud="ICLOUD", icloud="Se hai effettuato l’accesso a iCloud, punteggi e sblocchi sono conservati nel tuo account iCloud per seguirti sugli altri dispositivi. Apple li conserva secondo la propria informativa sulla privacy; noi non possiamo vederli.",
 h_gc="GAME CENTER", gc="Se accedi a Game Center di Apple, i tuoi punteggi migliori vengono inviati al servizio di classifiche di Apple secondo la sua informativa sulla privacy. Non vediamo né conserviamo mai la tua identità Game Center o i tuoi punteggi su server nostri; non abbiamo server.",
 h_children="MINORI", children="L’app è adatta a tutte le età e non è rivolta ai bambini. Non raccoglie dati di nessuno.",
 h_changes="MODIFICHE", changes="Se questa informativa cambierà, la nuova versione sarà pubblicata a questo indirizzo con una data aggiornata qui sotto.",
 h_contact="CONTATTI", contact='Domande? Apri una segnalazione sulla nostra <a href="{issues}">pagina di assistenza</a>.', date="Data di entrata in vigore: 16 novembre 2026",
 h_bug="HAI TROVATO UN BUG? HAI UN’IDEA?", bug='Il modo più rapido per contattarci è <a href="{issues}">aprire una segnalazione su GitHub</a>. Segnalazioni di bug, proposte e domande sulle regole sono benvenute. Raccontaci cosa è successo e cosa ti aspettavi.',
 h_faq="DOMANDE FREQUENTI",
 faq=[("Come funziona una partita?", "Scegli un percorso sulla mappa. Ogni livello è un tipo di gioco diverso; superalo e scegli una carta potenziamento. Se ti schianti perdi un serpente. Perso l’ultimo, la partita è finita."),
      ("Che differenza c’è tra Classico e Moderno?", "Sono entrambi la modalità Infinita: un solo tabellone, senza fine, per il punteggio più alto. Moderno ha il salto e i bonus. Classico è lo Snake che ricordi."),
      ("Come si salta?", "Tocca il pulsante SALTO e il serpente scavalca il proprio corpo."),
      ("Dove sono salvati i miei punteggi?", "Sul tuo dispositivo e, se hai effettuato l’accesso, nel tuo account iCloud. Accedi a Game Center per portare i tuoi migliori punteggi nelle classifiche mondiali.")],
 h_fine="NOTE LEGALI", fine='Snake Lab non ha pubblicità né acquisti in-app. Non raccoglie dati; vedi l’<a href="privacy.html">informativa sulla privacy</a>.')
T["pt-BR"] = dict(home="INÍCIO", support="SUPORTE", privacy="PRIVACIDADE", privacy_title="POLÍTICA DE PRIVACIDADE",
 tagline="Um Snake roguelike", lead="Snake, reconstruído como um roguelike.",
 pitch="Escolha seu caminho por fases que se jogam cada uma de um jeito, pegue uma melhoria depois de cada fase e mantenha sua última cobra viva. Sem anúncios, sem compras no app.",
 avail="Disponível na App Store para iPhone.",
 short="Resumindo: o Snake Lab não coleta nada. Sem anúncios, sem análises, sem contas.",
 h_collect="O QUE O APP COLETA", collect="Nada. Não há anúncios, contas nem análises, e o app não faz requisições de rede próprias. Suas partidas, pontuações, desbloqueios e ajustes ficam no seu aparelho.",
 h_icloud="ICLOUD", icloud="Se você estiver conectado ao iCloud, suas pontuações e desbloqueios ficam na sua própria conta do iCloud para acompanhar você nos outros aparelhos. A Apple os guarda conforme a Política de Privacidade dela; nós não podemos vê-los.",
 h_gc="GAME CENTER", gc="Se você entrar no Game Center da Apple, suas melhores pontuações são enviadas ao serviço de placares da Apple conforme a Política de Privacidade dela. Nunca vemos nem guardamos sua identidade do Game Center ou suas pontuações em servidores nossos; não temos servidores.",
 h_children="CRIANÇAS", children="O app é adequado para todas as idades e não é voltado para crianças. Ele não coleta dados de ninguém.",
 h_changes="ALTERAÇÕES", changes="Se esta política mudar, a nova versão será publicada neste endereço com a data atualizada abaixo.",
 h_contact="CONTATO", contact='Dúvidas? Abra uma issue na nossa <a href="{issues}">página de suporte</a>.', date="Data de vigência: 16 de novembro de 2026",
 h_bug="ACHOU UM BUG? TEM UMA IDEIA?", bug='O jeito mais rápido de falar com a gente é <a href="{issues}">abrir uma issue no GitHub</a>. Relatos de bugs, sugestões e dúvidas sobre as regras são bem-vindos. Conte o que aconteceu e o que você esperava.',
 h_faq="PERGUNTAS FREQUENTES",
 faq=[("Como funciona uma partida?", "Escolha um caminho no mapa. Cada fase é um tipo diferente de jogo; conclua-a e escolha uma carta de melhoria. Se bater, você perde uma cobra. Perdeu a última, a partida acaba."),
      ("Qual a diferença entre Clássico e Moderno?", "Os dois são o modo Infinito: um tabuleiro só, sem fim, valendo recorde. O Moderno tem o pulo e os itens. O Clássico é o Snake do jeito que você lembra."),
      ("Como eu pulo?", "Toque no botão PULO e sua cobra salta por cima do próprio corpo."),
      ("Onde ficam minhas pontuações?", "No seu aparelho e, se você estiver conectado, na sua conta do iCloud. Entre no Game Center para colocar suas melhores pontuações nos rankings mundiais.")],
 h_fine="LETRAS MIÚDAS", fine='O Snake Lab não tem anúncios nem compras no app. Ele não coleta dados; veja a <a href="privacy.html">política de privacidade</a>.')
T["pl"] = dict(home="START", support="POMOC", privacy="PRYWATNOŚĆ", privacy_title="POLITYKA PRYWATNOŚCI",
 tagline="Snake w wersji roguelike", lead="Snake przebudowany na roguelike.",
 pitch="Wybierz trasę przez etapy, z których każdy gra się inaczej, po każdym etapie weź ulepszenie i utrzymaj przy życiu ostatniego węża. Bez reklam i bez zakupów w aplikacji.",
 avail="Dostępne w App Store na iPhone’a.",
 short="W skrócie: Snake Lab niczego nie zbiera. Bez reklam, bez analityki, bez kont.",
 h_collect="CO ZBIERA APLIKACJA", collect="Nic. Nie ma reklam, kont ani analityki, a aplikacja sama nie wysyła żadnych zapytań sieciowych. Twoje gry, wyniki, odblokowania i ustawienia zostają na urządzeniu.",
 h_icloud="ICLOUD", icloud="Jeśli jesteś zalogowany do iCloud, twoje wyniki i odblokowania są przechowywane na twoim własnym koncie iCloud, aby były dostępne na innych urządzeniach. Apple przechowuje je zgodnie ze swoją polityką prywatności; my ich nie widzimy.",
 h_gc="GAME CENTER", gc="Jeśli zalogujesz się do Game Center firmy Apple, twoje najlepsze wyniki są wysyłane do usługi rankingów Apple zgodnie z polityką prywatności Apple. Nigdy nie widzimy ani nie przechowujemy twojej tożsamości Game Center ani wyników na żadnym naszym serwerze; nie mamy serwerów.",
 h_children="DZIECI", children="Aplikacja jest odpowiednia dla każdego wieku i nie jest skierowana do dzieci. Nie zbiera danych od nikogo.",
 h_changes="ZMIANY", changes="Jeśli ta polityka się zmieni, nowa wersja zostanie opublikowana pod tym adresem z zaktualizowaną datą poniżej.",
 h_contact="KONTAKT", contact='Pytania? Zgłoś je na naszej <a href="{issues}">stronie pomocy</a>.', date="Data wejścia w życie: 16 listopada 2026",
 h_bug="ZNALAZŁEŚ BŁĄD? MASZ POMYSŁ?", bug='Najszybciej skontaktujesz się z nami, <a href="{issues}">zgłaszając problem na GitHubie</a>. Zgłoszenia błędów, propozycje i pytania o zasady są mile widziane. Napisz, co się stało i czego się spodziewałeś.',
 h_faq="CZĘSTE PYTANIA",
 faq=[("Jak wygląda gra?", "Wybierz trasę na mapie. Każdy etap to inny rodzaj gry; ukończ go i wybierz kartę ulepszenia. Zderzenie kosztuje węża. Gdy stracisz ostatniego, gra się kończy."),
      ("Czym różni się tryb klasyczny od nowoczesnego?", "Oba to tryb bez końca: jedna plansza, bez końca, gra o rekord. Nowoczesny ma skok i bonusy. Klasyczny to Snake, jakiego pamiętasz."),
      ("Jak skakać?", "Stuknij przycisk SKOK, a wąż przeskoczy nad własnym ciałem."),
      ("Gdzie są zapisane moje wyniki?", "Na twoim urządzeniu, a jeśli jesteś zalogowany, także na koncie iCloud. Zaloguj się do Game Center, by umieścić najlepsze wyniki w światowych rankingach.")],
 h_fine="DROBNY DRUK", fine='Snake Lab nie ma reklam ani zakupów w aplikacji. Nie zbiera danych; zobacz <a href="privacy.html">politykę prywatności</a>.')
T["tr"] = dict(home="ANA SAYFA", support="DESTEK", privacy="GİZLİLİK", privacy_title="GİZLİLİK POLİTİKASI",
 tagline="Roguelike yılan oyunu", lead="Yılan oyunu, roguelike olarak yeniden tasarlandı.",
 pitch="Her biri farklı oynanan bölümler arasında rotanı seç, her bölümden sonra bir geliştirme al ve son yılanını hayatta tut. Reklam yok, uygulama içi satın alma yok.",
 avail="iPhone için App Store’da.",
 short="Kısacası: Snake Lab hiçbir şey toplamaz. Reklam yok, analiz yok, hesap yok.",
 h_collect="UYGULAMA NE TOPLAR", collect="Hiçbir şey. Reklam, hesap ya da analiz yoktur ve uygulama kendi başına ağ isteği yapmaz. Oyunların, skorların, açtığın içerikler ve ayarların cihazında kalır.",
 h_icloud="ICLOUD", icloud="iCloud’a giriş yaptıysan skorların ve açtığın içerikler, diğer cihazlarında da seninle olsun diye kendi iCloud hesabında saklanır. Apple bunları kendi Gizlilik Politikası’na göre saklar; biz göremeyiz.",
 h_gc="GAME CENTER", gc="Apple’ın Game Center’ına giriş yaparsan en iyi skorların Apple’ın Gizlilik Politikası’na göre Apple’ın skor tablosu hizmetine gönderilir. Game Center kimliğini ya da skorlarını hiçbir zaman görmez ve kendi sunucularımızda saklamayız; sunucumuz yoktur.",
 h_children="ÇOCUKLAR", children="Uygulama her yaşa uygundur ve çocuklara yönelik değildir. Kimseden veri toplamaz.",
 h_changes="DEĞİŞİKLİKLER", changes="Bu politika değişirse yeni sürüm, aşağıda güncellenmiş tarihle bu adreste yayımlanır.",
 h_contact="İLETİŞİM", contact='Sorun mu var? <a href="{issues}">Destek sayfamızda</a> bir kayıt aç.', date="Yürürlük tarihi: 16 Kasım 2026",
 h_bug="HATA MI BULDUN? FİKRİN Mİ VAR?", bug='Bize ulaşmanın en hızlı yolu <a href="{issues}">GitHub’da bir kayıt açmak</a>. Hata bildirimleri, öneriler ve kurallarla ilgili sorular memnuniyetle karşılanır. Ne olduğunu ve ne beklediğini yaz.',
 h_faq="SIK SORULANLAR",
 faq=[("Bir oyun nasıl ilerler?", "Haritada bir rota seç. Her bölüm farklı türde bir oyundur; bitir ve bir geliştirme kartı seç. Çarparsan bir yılan kaybedersin. Sonuncuyu da kaybedersen oyun biter."),
      ("Klasik ile Modern arasındaki fark ne?", "İkisi de Sonsuz mod: tek tahta, sonu yok, en yüksek skor için oynanır. Modern’de zıplama ve güçlendirmeler vardır. Klasik, hatırladığın yılan oyunudur."),
      ("Nasıl zıplarım?", "ZIPLA düğmesine dokun, yılanın kendi gövdesinin üstünden atlar."),
      ("Skorlarım nerede saklanıyor?", "Cihazında ve giriş yaptıysan iCloud hesabında. En iyi skorlarını dünya skor tablolarına taşımak için Game Center’a giriş yap.")],
 h_fine="İNCE AYRINTILAR", fine='Snake Lab’de reklam ve uygulama içi satın alma yoktur. Veri toplamaz; <a href="privacy.html">gizlilik politikasına</a> bak.')
T["ru"] = dict(home="ГЛАВНАЯ", support="ПОДДЕРЖКА", privacy="КОНФИДЕНЦИАЛЬНОСТЬ", privacy_title="ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ",
 tagline="Змейка-рогалик", lead="«Змейка», переосмысленная как рогалик.",
 pitch="Выбирай путь через этапы, каждый из которых играется по-своему, бери улучшение после каждого этапа и сохрани жизнь последней змейке. Без рекламы и встроенных покупок.",
 avail="Доступно в App Store для iPhone.",
 short="Коротко: Snake Lab ничего не собирает. Ни рекламы, ни аналитики, ни аккаунтов.",
 h_collect="ЧТО СОБИРАЕТ ПРИЛОЖЕНИЕ", collect="Ничего. Здесь нет рекламы, аккаунтов и аналитики, и приложение само не делает сетевых запросов. Твои забеги, очки, открытия и настройки хранятся на устройстве.",
 h_icloud="ICLOUD", icloud="Если ты вошёл в iCloud, твои очки и открытия хранятся в твоей собственной учётной записи iCloud, чтобы они были доступны на других устройствах. Apple хранит их по своей политике конфиденциальности; мы их не видим.",
 h_gc="GAME CENTER", gc="Если ты войдёшь в Game Center от Apple, твои лучшие результаты отправляются в сервис таблиц лидеров Apple по её политике конфиденциальности. Мы никогда не видим и не храним твою учётную запись Game Center или очки на своих серверах; серверов у нас нет.",
 h_children="ДЕТИ", children="Приложение подходит для любого возраста и не предназначено специально для детей. Оно ни у кого не собирает данных.",
 h_changes="ИЗМЕНЕНИЯ", changes="Если политика изменится, новая версия будет опубликована по этому адресу с обновлённой датой ниже.",
 h_contact="КОНТАКТЫ", contact='Есть вопросы? Создай обращение на нашей <a href="{issues}">странице поддержки</a>.', date="Дата вступления в силу: 16 ноября 2026 г.",
 h_bug="НАШЁЛ ОШИБКУ? ЕСТЬ ИДЕЯ?", bug='Быстрее всего связаться с нами — <a href="{issues}">создать обращение на GitHub</a>. Мы рады сообщениям об ошибках, предложениям и вопросам о правилах. Расскажи, что произошло и чего ты ожидал.',
 h_faq="ЧАСТЫЕ ВОПРОСЫ",
 faq=[("Как устроен забег?", "Выбери путь по карте. Каждый этап — другая игра; пройди его и выбери карту улучшения. Врезался — теряешь змейку. Потерял последнюю — забег окончен."),
      ("Чем «Классика» отличается от «Модерна»?", "Оба — бесконечный режим: одно поле, без конца, игра на рекорд. В «Модерне» есть прыжок и бонусы. «Классика» — та самая «Змейка», которую ты помнишь."),
      ("Как прыгать?", "Нажми кнопку ПРЫЖОК, и змейка перепрыгнет через своё тело."),
      ("Где хранятся мои очки?", "На устройстве и, если ты вошёл, в твоей учётной записи iCloud. Войди в Game Center, чтобы попасть в мировые таблицы лидеров.")],
 h_fine="МЕЛКИЙ ШРИФТ", fine='В Snake Lab нет рекламы и встроенных покупок. Приложение не собирает данных; см. <a href="privacy.html">политику конфиденциальности</a>.')
T["ja"] = dict(home="ホーム", support="サポート", privacy="プライバシー", privacy_title="プライバシーポリシー",
 tagline="スネークのローグライク", lead="スネークを、ローグライクとして作り直しました。",
 pitch="ステージごとに遊び方が変わるルートを選び、クリアするたびにアップグレードを選んで、最後のヘビを生き残らせよう。広告なし、アプリ内課金なし。",
 avail="iPhone版をApp Storeで配信中。",
 short="要するに：Snake Lab は何も収集しません。広告なし、解析なし、アカウントなし。",
 h_collect="アプリが収集する情報", collect="ありません。広告・アカウント・解析はなく、アプリ自身がネットワーク通信を行うこともありません。ラン、スコア、解放した要素、設定はお使いの端末に保存されます。",
 h_icloud="ICLOUD", icloud="iCloud にサインインしている場合、スコアと解放した要素はほかの端末でも使えるよう、ご自身の iCloud アカウントに保存されます。保存は Apple のプライバシーポリシーに基づいて Apple が行い、開発者が見ることはできません。",
 h_gc="GAME CENTER", gc="Apple の Game Center にサインインすると、ベストスコアが Apple のプライバシーポリシーに基づいて Apple のランキングサービスに送信されます。開発者が Game Center のアカウントやスコアを見たり自社サーバーに保存したりすることはありません。サーバーは持っていません。",
 h_children="お子さまについて", children="このアプリは全年齢向けですが、子ども向けに作られたものではありません。誰のデータも収集しません。",
 h_changes="変更について", changes="このポリシーを変更する場合は、新しい内容をこのアドレスに掲載し、下の日付を更新します。",
 h_contact="お問い合わせ", contact='ご質問は<a href="{issues}">サポートページ</a>で Issue を作成してください。', date="発効日：2026年11月16日",
 h_bug="バグを見つけた？アイデアがある？", bug='いちばん早い連絡方法は <a href="{issues}">GitHub で Issue を作成する</a>ことです。バグ報告、ご要望、ルールについての質問を歓迎します。何が起きて、どうなると思っていたかを教えてください。',
 h_faq="よくある質問",
 faq=[("ランはどう進むの？", "マップでルートを選びます。ステージごとに別の種類のゲームになっていて、クリアするとアップグレードカードを選べます。ぶつかるとヘビを1匹失い、最後の1匹を失うとランは終わりです。"),
      ("クラシックとモダンの違いは？", "どちらもエンドレスモードで、1つの盤面で終わりなくハイスコアを目指します。モダンにはジャンプとアイテムがあります。クラシックは昔ながらのスネークそのものです。"),
      ("ジャンプするには？", "ジャンプボタンをタップすると、ヘビが自分の体を飛び越えます。"),
      ("スコアはどこに保存されるの？", "端末と、サインインしていれば iCloud アカウントに保存されます。Game Center にサインインすると、ベストスコアが世界ランキングに載ります。")],
 h_fine="補足事項", fine='Snake Lab には広告もアプリ内課金もありません。データも収集しません。<a href="privacy.html">プライバシーポリシー</a>をご覧ください。')
T["ko"] = dict(home="홈", support="지원", privacy="개인정보", privacy_title="개인정보 처리방침",
 tagline="스네이크 로그라이크", lead="스네이크를 로그라이크로 새롭게 만들었습니다.",
 pitch="스테이지마다 플레이 방식이 다른 경로를 고르고, 스테이지를 깰 때마다 업그레이드를 골라 마지막 뱀을 살려 두세요. 광고 없음, 인앱 구매 없음.",
 avail="iPhone용 App Store에서 만나 보세요.",
 short="요약: Snake Lab은 아무것도 수집하지 않습니다. 광고, 분석, 계정이 없습니다.",
 h_collect="앱이 수집하는 정보", collect="없습니다. 광고, 계정, 분석이 없으며 앱이 자체적으로 네트워크 요청을 보내지 않습니다. 게임 기록, 점수, 해금 항목, 설정은 기기에 저장됩니다.",
 h_icloud="ICLOUD", icloud="iCloud에 로그인되어 있으면 점수와 해금 항목이 다른 기기에서도 이어지도록 본인의 iCloud 계정에 보관됩니다. Apple이 Apple의 개인정보 처리방침에 따라 보관하며, 저희는 볼 수 없습니다.",
 h_gc="GAME CENTER", gc="Apple의 Game Center에 로그인하면 최고 점수가 Apple의 개인정보 처리방침에 따라 Apple의 순위표 서비스로 전송됩니다. 저희는 Game Center 계정이나 점수를 보거나 자체 서버에 저장하지 않습니다. 저희에게는 서버가 없습니다.",
 h_children="어린이", children="이 앱은 모든 연령에 적합하지만 어린이를 대상으로 하지는 않습니다. 누구의 데이터도 수집하지 않습니다.",
 h_changes="변경 사항", changes="이 방침이 바뀌면 새 버전을 이 주소에 게시하고 아래 날짜를 갱신합니다.",
 h_contact="문의", contact='궁금한 점은 <a href="{issues}">지원 페이지</a>에 이슈로 남겨 주세요.', date="시행일: 2026년 11월 16일",
 h_bug="버그를 찾았나요? 아이디어가 있나요?", bug='가장 빠른 연락 방법은 <a href="{issues}">GitHub에 이슈를 남기는 것</a>입니다. 버그 제보, 기능 제안, 규칙 질문 모두 환영합니다. 무슨 일이 있었고 무엇을 기대했는지 알려 주세요.',
 h_faq="자주 묻는 질문",
 faq=[("게임은 어떻게 진행되나요?", "지도에서 경로를 고르세요. 스테이지마다 다른 종류의 게임이며, 클리어하면 업그레이드 카드를 고릅니다. 부딪히면 뱀을 하나 잃고, 마지막 뱀을 잃으면 게임이 끝납니다."),
      ("클래식과 모던은 무엇이 다른가요?", "둘 다 무한 모드로, 하나의 보드에서 끝없이 최고 점수를 노립니다. 모던에는 점프와 아이템이 있고, 클래식은 기억하는 그대로의 스네이크입니다."),
      ("점프는 어떻게 하나요?", "점프 버튼을 누르면 뱀이 자기 몸을 뛰어넘습니다."),
      ("점수는 어디에 저장되나요?", "기기에 저장되고, 로그인되어 있다면 iCloud 계정에도 저장됩니다. Game Center에 로그인하면 최고 점수가 세계 순위표에 올라갑니다.")],
 h_fine="참고 사항", fine='Snake Lab에는 광고도 인앱 구매도 없습니다. 데이터도 수집하지 않습니다. <a href="privacy.html">개인정보 처리방침</a>을 참고하세요.')
T["zh-Hans"] = dict(home="首页", support="支持", privacy="隐私", privacy_title="隐私政策",
 tagline="Roguelike 贪吃蛇", lead="贪吃蛇，以 Roguelike 的方式重新打造。",
 pitch="选择穿过玩法各不相同的关卡的路线，每关之后选一项升级，让最后一条蛇活下去。无广告，无内购。",
 avail="现已登陆 iPhone 版 App Store。",
 short="简而言之：Snake Lab 不收集任何信息。没有广告，没有分析，没有账号。",
 h_collect="应用收集的信息", collect="没有。没有广告、账号和分析，应用自身也不发出任何网络请求。你的对局、分数、解锁内容和设置都保存在你的设备上。",
 h_icloud="ICLOUD", icloud="如果你已登录 iCloud，分数和解锁内容会保存在你自己的 iCloud 账户中，方便在其他设备上继续使用。Apple 依照其隐私政策保存这些数据，我们无法查看。",
 h_gc="GAME CENTER", gc="如果你登录 Apple 的 Game Center，你的最高分会依照 Apple 的隐私政策提交到 Apple 的排行榜服务。我们从不查看或在自己的服务器上保存你的 Game Center 身份或分数；我们没有服务器。",
 h_children="儿童", children="本应用适合所有年龄段，但并非专为儿童设计。它不收集任何人的数据。",
 h_changes="变更", changes="如果本政策有变，新版本将发布在此地址，并更新下方日期。",
 h_contact="联系方式", contact='有疑问？请在我们的<a href="{issues}">支持页面</a>提交 issue。', date="生效日期：2026年11月16日",
 h_bug="发现了 bug？有好点子？", bug='联系我们最快的方式是<a href="{issues}">在 GitHub 上提交 issue</a>。欢迎反馈 bug、提出功能建议或询问规则。请告诉我们发生了什么，以及你原本的预期。',
 h_faq="常见问题",
 faq=[("一局是怎么进行的？", "在地图上选择路线。每一关都是不同类型的游戏；通关后选择一张升级卡。撞上就会失去一条蛇，失去最后一条，这一局就结束了。"),
      ("经典和现代有什么区别？", "两者都是无尽模式：一个棋盘，没有尽头，挑战最高分。现代模式有跳跃和道具，经典模式就是你记忆中的贪吃蛇。"),
      ("怎么跳跃？", "点击“跳”按钮，蛇就会跃过自己的身体。"),
      ("我的分数保存在哪里？", "保存在你的设备上，如果已登录，也会保存在你的 iCloud 账户中。登录 Game Center 即可让最高分登上全球排行榜。")],
 h_fine="附注", fine='Snake Lab 没有广告，也没有内购。它不收集任何数据；请参阅<a href="privacy.html">隐私政策</a>。')
T["zh-Hant"] = dict(home="首頁", support="支援", privacy="隱私", privacy_title="隱私權政策",
 tagline="Roguelike 貪食蛇", lead="貪食蛇，以 Roguelike 的方式重新打造。",
 pitch="選擇穿越玩法各不相同的關卡的路線，每關之後選一項升級，讓最後一條蛇活下去。無廣告，無內購。",
 avail="現已登上 iPhone 版 App Store。",
 short="簡而言之：Snake Lab 不收集任何資訊。沒有廣告，沒有分析，沒有帳號。",
 h_collect="App 收集的資訊", collect="沒有。沒有廣告、帳號和分析，App 本身也不發出任何網路請求。你的對局、分數、解鎖內容和設定都儲存在你的裝置上。",
 h_icloud="ICLOUD", icloud="如果你已登入 iCloud，分數和解鎖內容會保存在你自己的 iCloud 帳號中，方便在其他裝置上繼續使用。Apple 依照其隱私權政策保存這些資料，我們無法查看。",
 h_gc="GAME CENTER", gc="如果你登入 Apple 的 Game Center，你的最高分會依照 Apple 的隱私權政策提交到 Apple 的排行榜服務。我們從不查看或在自己的伺服器上保存你的 Game Center 身分或分數；我們沒有伺服器。",
 h_children="兒童", children="本 App 適合所有年齡層，但並非專為兒童設計。它不收集任何人的資料。",
 h_changes="變更", changes="如果本政策有變，新版本將發布在此網址，並更新下方日期。",
 h_contact="聯絡方式", contact='有疑問？請在我們的<a href="{issues}">支援頁面</a>提交 issue。', date="生效日期：2026年11月16日",
 h_bug="發現了 bug？有好點子？", bug='聯絡我們最快的方式是<a href="{issues}">在 GitHub 上提交 issue</a>。歡迎回報 bug、提出功能建議或詢問規則。請告訴我們發生了什麼，以及你原本的預期。',
 h_faq="常見問題",
 faq=[("一局是怎麼進行的？", "在地圖上選擇路線。每一關都是不同類型的遊戲；過關後選擇一張升級卡。撞上就會失去一條蛇，失去最後一條，這一局就結束了。"),
      ("經典和現代有什麼不同？", "兩者都是無盡模式：一個棋盤，沒有盡頭，挑戰最高分。現代模式有跳躍和道具，經典模式就是你記憶中的貪食蛇。"),
      ("怎麼跳躍？", "點擊「跳」按鈕，蛇就會躍過自己的身體。"),
      ("我的分數保存在哪裡？", "保存在你的裝置上，如果已登入，也會保存在你的 iCloud 帳號中。登入 Game Center 即可讓最高分登上全球排行榜。")],
 h_fine="附註", fine='Snake Lab 沒有廣告，也沒有內購。它不收集任何資料；請參閱<a href="privacy.html">隱私權政策</a>。')

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
    priv = "\n".join([f'      <p><strong>{t["short"]}</strong></p>', sec(t["h_collect"], t["collect"]), sec(t["h_icloud"], t["icloud"]), sec(t["h_gc"], t["gc"]),
                      sec(t["h_children"], t["children"]), sec(t["h_changes"], t["changes"]), sec(t["h_contact"], t["contact"].format(issues=ISSUES)),
                      f'      <p class="small">{t["date"]}</p>'])
    sup = "\n".join([sec(t["h_bug"], t["bug"].format(issues=ISSUES)), f'      <h2>{t["h_faq"]}</h2>'] +
                    [f'      <p class="qa"><strong>{html.escape(q)}</strong>{html.escape(a)}</p>' for q, a in t["faq"]] + [sec(t["h_fine"], t["fine"])])
    open(os.path.join(d, "index.html"), "w").write(page(lang, "index", "SNAKE LAB", home))
    open(os.path.join(d, "privacy.html"), "w").write(page(lang, "privacy", t["privacy_title"], priv))
    open(os.path.join(d, "support.html"), "w").write(page(lang, "support", t["support"], sup))
print("pages:", sum(len(f) for _, _, f in os.walk(docs)))
