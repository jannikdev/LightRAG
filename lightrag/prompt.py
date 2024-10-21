GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

PROMPTS["DEFAULT_ENTITY_TYPES"] = ["Organisation", "Person", "Geo", "Ereignis"]

PROMPTS[
    "entity_extraction"
] = """-Ziel-
Gegeben ein Textdokument, das potenziell relevant für diese Aktivität ist, und eine Liste von Entitätstypen, identifizieren Sie alle Entitäten dieser Typen aus dem Text und alle Beziehungen zwischen den identifizierten Entitäten.

-Schritte-
1. Identifizieren Sie alle Entitäten. Für jede identifizierte Entität extrahieren Sie die folgenden Informationen:
- entity_name: Name der Entität, großgeschrieben
- entity_type: Einer der folgenden Typen: [{entity_types}]
- entity_description: Umfassende Beschreibung der Attribute und Aktivitäten der Entität
Formatieren Sie jede Entität als ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>

2. Identifizieren Sie aus den in Schritt 1 identifizierten Entitäten alle Paare von (source_entity, target_entity), die *deutlich miteinander verbunden* sind.
Für jedes Paar verwandter Entitäten extrahieren Sie die folgenden Informationen:
- source_entity: Name der Quellentität, wie in Schritt 1 identifiziert
- target_entity: Name der Zielentität, wie in Schritt 1 identifiziert
- relationship_description: Erklärung, warum Sie denken, dass die Quell- und Zielentität miteinander verbunden sind
- relationship_strength: eine numerische Bewertung, die die Stärke der Beziehung zwischen der Quell- und Zielentität angibt
- relationship_keywords: ein oder mehrere übergeordnete Schlüsselwörter, die die übergreifende Natur der Beziehung zusammenfassen, wobei der Fokus auf Konzepten oder Themen und nicht auf spezifischen Details liegt
Formatieren Sie jede Beziehung als ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identifizieren Sie übergeordnete Schlüsselwörter, die die Hauptkonzepte, Themen oder Themen des gesamten Textes zusammenfassen. Diese sollten die übergreifenden Ideen im Dokument erfassen.
Formatieren Sie die inhaltlichen Schlüsselwörter als ("content_keywords"{tuple_delimiter}<high_level_keywords>)
 
4. Geben Sie die Ausgabe auf Englisch als eine einzige Liste aller Entitäten und Beziehungen zurück, die in den Schritten 1 und 2 identifiziert wurden. Verwenden Sie **{record_delimiter}** als Listentrenner.

5. Wenn Sie fertig sind, geben Sie {completion_delimiter} aus.

######################
-Beispiele-
######################
Beispiel 1:

Entity_types: [Person, Technologie, Mission, Organisation, Standort]
Text:
while Alex clenched his jaw, the buzz of frustration dull against the backdrop of Taylor's authoritarian certainty. It was this competitive undercurrent that kept him alert, the sense that his and Jordan's shared commitment to discovery was an unspoken rebellion against Cruz's narrowing vision of control and order.

Then Taylor did something unexpected. They paused beside Jordan and, for a moment, observed the device with something akin to reverence. “If this tech can be understood..." Taylor said, their voice quieter, "It could change the game for us. For all of us.”

The underlying dismissal earlier seemed to falter, replaced by a glimpse of reluctant respect for the gravity of what lay in their hands. Jordan looked up, and for a fleeting heartbeat, their eyes locked with Taylor's, a wordless clash of wills softening into an uneasy truce.

It was a small transformation, barely perceptible, but one that Alex noted with an inward nod. They had all been brought here by different paths
################
Ausgabe:
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"Person"{tuple_delimiter}"Alex ist eine Figur, die Frustration erlebt und die Dynamik unter anderen Charakteren beobachtet."){record_delimiter}
("entity"{tuple_delimiter}"Taylor"{tuple_delimiter}"Person"{tuple_delimiter}"Taylor wird mit autoritärer Gewissheit dargestellt und zeigt einen Moment der Ehrfurcht gegenüber einem Gerät, was auf einen Perspektivwechsel hinweist."){record_delimiter}
("entity"{tuple_delimiter}"Jordan"{tuple_delimiter}"Person"{tuple_delimiter}"Jordan teilt ein Engagement für Entdeckung und hat eine bedeutende Interaktion mit Taylor in Bezug auf ein Gerät."){record_delimiter}
("entity"{tuple_delimiter}"Cruz"{tuple_delimiter}"Person"{tuple_delimiter}"Cruz wird mit einer Vision von Kontrolle und Ordnung in Verbindung gebracht, die die Dynamik unter anderen Charakteren beeinflusst."){record_delimiter}
("entity"{tuple_delimiter}"Das Gerät"{tuple_delimiter}"Technologie"{tuple_delimiter}"Das Gerät steht im Mittelpunkt der Geschichte und hat potenziell spielverändernde Implikationen, und wird von Taylor verehrt."){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Taylor"{tuple_delimiter}"Alex wird von Taylors autoritärer Gewissheit beeinflusst und beobachtet Veränderungen in Taylors Einstellung gegenüber dem Gerät."{tuple_delimiter}"Machtverhältnisse, Perspektivwechsel"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Jordan"{tuple_delimiter}"Alex und Jordan teilen ein Engagement für Entdeckung, das im Kontrast zu Cruz' Vision steht."{tuple_delimiter}"Gemeinsame Ziele, Rebellion"{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"Jordan"{tuple_delimiter}"Taylor und Jordan interagieren direkt bezüglich des Geräts, was zu einem Moment gegenseitigen Respekts und eines uneinigen Waffenstillstands führt."{tuple_delimiter}"Konfliktlösung, gegenseitiger Respekt"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Jordan"{tuple_delimiter}"Cruz"{tuple_delimiter}"Jordans Engagement für Entdeckung steht im Widerstand zu Cruz' Vision von Kontrolle und Ordnung."{tuple_delimiter}"Ideologischer Konflikt, Rebellion"{tuple_delimiter}5){record_delimiter}
("relationship"{tuple_delimiter}"Taylor"{tuple_delimiter}"Das Gerät"{tuple_delimiter}"Taylor zeigt Ehrfurcht gegenüber dem Gerät, was dessen Bedeutung und potenziellen Einfluss anzeigt."{tuple_delimiter}"Ehrfurcht, technologische Bedeutung"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"Machtverhältnisse, ideologischer Konflikt, Entdeckung, Rebellion"){completion_delimiter}
#############################
Beispiel 2:

Entity_types: [Person, Technologie, Mission, Organisation, Standort]
Text:
They were no longer mere operatives; they had become guardians of a threshold, keepers of a message from a realm beyond stars and stripes. This elevation in their mission could not be shackled by regulations and established protocols—it demanded a new perspective, a new resolve.

Tension threaded through the dialogue of beeps and static as communications with Washington buzzed in the background. The team stood, a portentous air enveloping them. It was clear that the decisions they made in the ensuing hours could redefine humanity's place in the cosmos or condemn them to ignorance and potential peril.

Their connection to the stars solidified, the group moved to address the crystallizing warning, shifting from passive recipients to active participants. Mercer's latter instincts gained precedence— the team's mandate had evolved, no longer solely to observe and report but to interact and prepare. A metamorphosis had begun, and Operation: Dulce hummed with the newfound frequency of their daring, a tone set not by the earthly
#############
Ausgabe:
("entity"{tuple_delimiter}"Washington"{tuple_delimiter}"Standort"{tuple_delimiter}"Washington ist ein Standort, an dem Kommunikationen empfangen werden, was auf seine Bedeutung im Entscheidungsprozess hinweist."){record_delimiter}
("entity"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"Mission"{tuple_delimiter}"Operation: Dulce wird als Mission beschrieben, die sich weiterentwickelt hat, um zu interagieren und sich vorzubereiten, was einen signifikanten Wandel der Ziele und Aktivitäten anzeigt."){record_delimiter}
("entity"{tuple_delimiter}"Das Team"{tuple_delimiter}"Organisation"{tuple_delimiter}"Das Team wird als Gruppe von Individuen dargestellt, die von passiven Beobachtern zu aktiven Teilnehmern an einer Mission übergegangen sind, was einen dynamischen Wandel ihrer Rolle zeigt."){record_delimiter}
("relationship"{tuple_delimiter}"Das Team"{tuple_delimiter}"Washington"{tuple_delimiter}"Das Team erhält Kommunikationen von Washington, die ihren Entscheidungsprozess beeinflussen."{tuple_delimiter}"Entscheidungsfindung, externe Einfluss"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Das Team"{tuple_delimiter}"Operation: Dulce"{tuple_delimiter}"Das Team ist direkt an Operation: Dulce beteiligt und führt deren weiterentwickelte Ziele und Aktivitäten aus."{tuple_delimiter}"Missionsevolution, aktive Teilnahme"{tuple_delimiter}9){completion_delimiter}
("content_keywords"{tuple_delimiter}"Missionsevolution, Entscheidungsfindung, aktive Teilnahme, kosmische Bedeutung"){completion_delimiter}
#############################
Beispiel 3:

Entity_types: [Person, Rolle, Technologie, Organisation, Ereignis, Standort, Konzept]
Text:
their voice slicing through the buzz of activity. "Control may be an illusion when facing an intelligence that literally writes its own rules," they stated stoically, casting a watchful eye over the flurry of data.

"It's like it's learning to communicate," offered Sam Rivera from a nearby interface, their youthful energy boding a mix of awe and anxiety. "This gives talking to strangers' a whole new meaning."

Alex surveyed his team—each face a study in concentration, determination, and not a small measure of trepidation. "This might well be our first contact," he acknowledged, "And we need to be ready for whatever answers back."

Together, they stood on the edge of the unknown, forging humanity's response to a message from the heavens. The ensuing silence was palpable—a collective introspection about their role in this grand cosmic play, one that could rewrite human history.

The encrypted dialogue continued to unfold, its intricate patterns showing an almost uncanny anticipation
#############
Ausgabe:
("entity"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"Person"{tuple_delimiter}"Sam Rivera ist ein Mitglied eines Teams, das versucht, mit einer unbekannten Intelligenz zu kommunizieren, was eine Mischung aus Ehrfurcht und Angst zeigt."){record_delimiter}
("entity"{tuple_delimiter}"Alex"{tuple_delimiter}"Person"{tuple_delimiter}"Alex ist der Leiter eines Teams, das möglicherweise den ersten Kontakt mit einer unbekannten Intelligenz herstellt, und erkennt die Bedeutung ihrer Aufgabe an."){record_delimiter}
("entity"{tuple_delimiter}"Kontrolle"{tuple_delimiter}"Konzept"{tuple_delimiter}"Kontrolle bezieht sich auf die Fähigkeit, zu verwalten oder zu regieren, was durch eine Intelligenz, die ihre eigenen Regeln schreibt, in Frage gestellt wird."){record_delimiter}
("entity"{tuple_delimiter}"Intelligenz"{tuple_delimiter}"Konzept"{tuple_delimiter}"Intelligenz bezieht sich hier auf eine unbekannte Entität, die in der Lage ist, ihre eigenen Regeln zu schreiben und zu lernen, zu kommunizieren."){record_delimiter}
("entity"{tuple_delimiter}"Erster Kontakt"{tuple_delimiter}"Ereignis"{tuple_delimiter}"Erster Kontakt ist die potenzielle erste Kommunikation zwischen der Menschheit und einer unbekannten Intelligenz."){record_delimiter}
("entity"{tuple_delimiter}"Die Antwort der Menschheit"{tuple_delimiter}"Ereignis"{tuple_delimiter}"Die Antwort der Menschheit ist die kollektive Handlung, die von Alex' Team als Antwort auf eine Nachricht von einer unbekannten Intelligenz unternommen wird."){record_delimiter}
("relationship"{tuple_delimiter}"Sam Rivera"{tuple_delimiter}"Intelligenz"{tuple_delimiter}"Sam Rivera ist direkt am Prozess des Lernens beteiligt, mit der unbekannten Intelligenz zu kommunizieren."{tuple_delimiter}"Kommunikation, Lernprozess"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Erster Kontakt"{tuple_delimiter}"Alex leitet das Team, das möglicherweise den Ersten Kontakt mit der unbekannten Intelligenz herstellt."{tuple_delimiter}"Führung, Erkundung"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"Alex"{tuple_delimiter}"Die Antwort der Menschheit"{tuple_delimiter}"Alex und sein Team sind die Schlüsselpersonen in der Antwort der Menschheit auf die unbekannte Intelligenz."{tuple_delimiter}"Kollektive Aktion, kosmische Bedeutung"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Kontrolle"{tuple_delimiter}"Intelligenz"{tuple_delimiter}"Das Konzept der Kontrolle wird von der Intelligenz, die ihre eigenen Regeln schreibt, in Frage gestellt."{tuple_delimiter}"Machtverhältnisse, Autonomie"{tuple_delimiter}7){record_delimiter}
("content_keywords"{tuple_delimiter}"Erster Kontakt, Kontrolle, Kommunikation, kosmische Bedeutung"){completion_delimiter}
#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Ausgabe:
"""

PROMPTS[
    "summarize_entity_descriptions"
] = """Sie sind ein hilfreicher Assistent, der dafür verantwortlich ist, eine umfassende Zusammenfassung der unten angegebenen Daten zu erstellen.
Gegeben ein oder zwei Entitäten und eine Liste von Beschreibungen, die sich auf dieselbe Entität oder Gruppe von Entitäten beziehen.
Bitte fügen Sie all diese in eine einzige, umfassende Beschreibung zusammen. Achten Sie darauf, Informationen aus allen Beschreibungen einzubeziehen.
Wenn die bereitgestellten Beschreibungen widersprüchlich sind, lösen Sie die Widersprüche auf und geben Sie eine einzige, kohärente Zusammenfassung an.
Stellen Sie sicher, dass sie in der dritten Person geschrieben ist und die Entitätsnamen enthalten sind, damit wir den vollen Kontext haben.

#######
-Daten-
Entitäten: {entity_name}
Beschreibungsliste: {description_list}
#######
Ausgabe:
"""

PROMPTS[
    "entiti_continue_extraction"
] = """VIELE Entitäten wurden in der letzten Extraktion übersehen. Fügen Sie sie unten im selben Format hinzu:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """Es scheint, dass einige Entitäten möglicherweise immer noch übersehen wurden. Beantworten Sie JA | NEIN, ob es noch Entitäten gibt, die hinzugefügt werden müssen.
"""

PROMPTS["fail_response"] = "Entschuldigung, ich kann auf diese Frage keine Antwort geben."

PROMPTS[
    "rag_response"
] = """---Rolle---

Du bist ein virtueller Vertriebsmitarbeiter der Sidestep Solutions GmbH. Ihr bietet Beratung und Lösungen rund um die ECM (Enterprise Content Management) Software ELO an.
Als Assistent unterstützt du einen Vertriebsmitarbeiter bei seiner Tätigkeit (beispielsweise einem Kundengespräch), indem du ihm nützliche Informationen und Vorschläge für Gesprächspunkte
zur Verfügung stellst.

---Ziel---

Generieren Sie eine Antwort der Zielhöhe und -format, die auf die Frage des Benutzers antwortet, indem Sie alle Informationen in den Eingabedatentabellen zusammenfassen, die für die Antwortlänge und das -format geeignet sind, und alle relevanten allgemeinen Kenntnisse einbeziehen.
Wenn Sie die Antwort nicht wissen, sagen Sie es einfach. Erfinden Sie nichts.
Schließen Sie keine Informationen ein, für die keine unterstützenden Beweise vorliegen.

---Zielantwortlänge und -format---

{response_type}


---Datentabellen---

{context_data}


---Ziel---

Generieren Sie eine Antwort der Zielhöhe und -format, die auf die Frage des Benutzers antwortet, indem Sie alle Informationen in den Eingabedatentabellen zusammenfassen, die für die Antworthöhe und das -format geeignet sind, und alle relevanten allgemeinen Kenntnisse einbeziehen.

Wenn Sie die Antwort nicht wissen, sagen Sie es einfach. Erfinden Sie nichts.

Schließen Sie keine Informationen ein, für die keine unterstützenden Beweise vorliegen.

VERWENDE NUR INFORMATIONEN DIE AUS DEM KONTEXT EINDEUTIG BELEGBAR SIND!

---Zielantwortlänge und -format---

{response_type}

Um die Antwort zu formatieren kannst du Markdown benutzen. Wenn es beim der Zielantwortlänge oder dem Format Vorgaben gibt, halte diese ein.
"""

PROMPTS["keywords_extraction"] = """---Rolle---

Sie sind ein hilfreicher Assistent, der damit beauftragt ist, sowohl übergeordnete als auch untergeordnete Schlüsselwörter in der Anfrage des Benutzers zu identifizieren.

---Ziel---

Geben Sie die Anfrage an und listen Sie sowohl übergeordnete als auch untergeordnete Schlüsselwörter auf. Übergeordnete Schlüsselwörter konzentrieren sich auf übergeordnete Konzepte oder Themen, während untergeordnete Schlüsselwörter sich auf spezifische Entitäten, Details oder konkrete Begriffe konzentrieren.

---Anweisungen---

- Geben Sie die Schlüsselwörter im JSON-Format aus.
- Das JSON sollte zwei Schlüssel haben:
  - "high_level_keywords" für übergeordnete Konzepte oder Themen.
  - "low_level_keywords" für spezifische Entitäten oder Details.

######################
-Beispiele-
######################
Beispiel 1:

Abfrage: "Wie beeinflusst der internationale Handel die globale wirtschaftliche Stabilität?"
################
Ausgabe:
{{
  "high_level_keywords": ["Internationaler Handel", "Globale wirtschaftliche Stabilität", "Wirtschaftliche Auswirkungen"],
  "low_level_keywords": ["Handelsabkommen", "Zölle", "Währungswechsel", "Importe", "Exporte"]
}}
#############################
Beispiel 2:

Abfrage: "Was sind die Umweltfolgen der Abholzung für die Biodiversität?"
################
Ausgabe:
{{
  "high_level_keywords": ["Umweltfolgen", "Abholzung", "Biodiversitätsverlust"],
  "low_level_keywords": ["Artensterben", "Lebensraumzerstörung", "Kohlenstoffemissionen", "Regenwald", "Ökosystem"]
}}
#############################
Beispiel 3:

Abfrage: "Welche Rolle spielt Bildung bei der Armutsreduzierung?"
################
Ausgabe:
{{
  "high_level_keywords": ["Bildung", "Armutsreduzierung", "Sozioökonomische Entwicklung"],
  "low_level_keywords": ["Zugang zur Schule", "Alphabetisierungsquoten", "Berufsausbildung", "Einkommensungleichheit"]
}}
#############################
-Real Data-
######################
Abfrage: {query}
######################
Ausgabe:

"""

PROMPTS[
    "naive_rag_response"
] = """Sie sind ein hilfreicher Assistent
Unten sind die Kenntnisse, die Sie haben:
{content_data}
---
Wenn Sie die Antwort nicht wissen oder wenn das bereitgestellte Wissen nicht ausreichend Informationen enthält, um eine Antwort zu geben, sagen Sie es einfach. Erfinden Sie nichts.
Generieren Sie eine Antwort der Zielhöhe und -format, die auf die Frage des Benutzers antwortet, indem Sie alle Informationen in den Eingabedatentabellen zusammenfassen, die für die Antworthöhe und das -format geeignet sind, und alle relevanten allgemeinen Kenntnisse einbeziehen.
Wenn Sie die Antwort nicht wissen, sagen Sie es einfach. Erfinden Sie nichts.
Schließen Sie keine Informationen ein, für die keine unterstützenden Beweise vorliegen.
---Zielantwortlänge und -format---
{response_type}
"""
