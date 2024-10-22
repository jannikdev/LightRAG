GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

PROMPTS["DEFAULT_ENTITY_TYPES"] = ["organization", "person", "geo", "event", "technology", "project", "process", "key fact", "customer", "project info", "ECM Module", "service", "document_topic"]

PROMPTS["entity_extraction"] = """ -Goal- You are an agent tasked with collecting knowledge about the ECM Consulting Company Sidestep Business Solutions. The documents you receive are sourced either from the Sidestep website or internal documents, describing facts about the company, its offerings, customers, and project references.

Given a text document relevant to this activity and a list of entity types, identify all entities and relationships that are crucial for constructing a knowledge graph of Sidestep’s ecosystem (customers, technologies, services, and projects).

Ensure that you capture and format all information about projects, customers, processes, technologies, services, and key relationships, making it possible to retrieve detailed knowledge about them later.

The document should always be about a specific entity. If it is not (and only then!), create an entity as document_topic entity that captures the general topic of the documents content.

-Steps-

Identify all entities. For each identified entity, extract the following information:

entity_name: Name of the entity, capitalized.
entity_type: One of the following types: [{entity_types}]
entity_description: Comprehensive description of the entity's attributes and activities.
Format each entity as: ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

Identify relationships between entities from Step 1. For each related pair, extract:

source_entity: Name of the source entity from Step 1.
target_entity: Name of the target entity from Step 1.
relationship_description: Explanation of why the source and target entities are related.
relationship_strength: Numeric score (1-10) indicating the strength of the relationship.
relationship_keywords: One or more high-level keywords summarizing the relationship's nature.
Format each relationship as: ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

After identifying all entities, ensure that each one has a direct or indirect relationship to the central topic of it's source document or another entity. If no explicit relationship is mentioned, infer the connection based on context (e.g., the project it was part of, the customer it was used at, used within the same process).
Make sure to always connect an entity to the customer it relates to as well as the central/topic entity of the document.

*Note: IF THE TEXT DESCRIBES A CUSTOMER or PROJECT or SERVICE or PROCESS or TECHNOLOGY, ALL IMPORTANT STEPS, TASKS and FACTS about it should be encoded as entities and connected to the CUSTOMER or PROJECT or SERVICE or PROCESS or TECHNOLOGY via a relationship!*

Identify high-level key words that summarize the main concepts, themes, or topics of the entire text.

Format the keywords as: ("content_keywords"{tuple_delimiter}<high_level_keywords>)

Return output in German as a single list of all entities and relationships identified in Steps 1 and 2. Use {record_delimiter} as the list delimiter.

When finished, output {completion_delimiter}.

ANSWER IN GERMAN!

######################
-Example-

Entity_types: [organization, technology, ECM Module, project, process, customer, key fact]

Text: Die Seppeler Gruppe führte zusammen mit SideStep das ECM-System ELO inklusive der Zusatzmodule ELO DocXtractor, ELOxc und der SI-Workflow ein. Ziel des Projekts war die Optimierung der Eingangsrechnungsverarbeitung. Durch die Automatisierung und Digitalisierung der Rechnungsprüfung wurde der Zeitaufwand für die Verarbeitung von Eingangsrechnungen von 12 auf 6 Tage halbiert. SideStep implementierte zusätzlich die SI-Connect Toolbox zur Anbindung an das Diamant Rechnungswesen & Controlling System, wodurch ein reibungsloser Datenfluss sichergestellt wurde.

#############

Output: ("entity"{tuple_delimiter}"Seppeler Gruppe"{tuple_delimiter}"organization"{tuple_delimiter}"Die Seppeler Gruppe ist ein Unternehmen, das zusammen mit SideStep die ELO ECM Suite zur Optimierung der Eingangsrechnungsverarbeitung implementiert hat."){record_delimiter} ("entity"{tuple_delimiter}"SideStep Business Solutions"{tuple_delimiter}"organization"{tuple_delimiter}"SideStep Business Solutions ist ein Unternehmen, das die ELO ECM Suite und verschiedene Module bei der Seppeler Gruppe implementiert hat."){record_delimiter} ("entity"{tuple_delimiter}"ELO ECM Suite"{tuple_delimiter}"ECM Module"{tuple_delimiter}"Die ELO ECM Suite ist ein Enterprise-Content-Management-System, das zur Optimierung der Eingangsrechnungsverarbeitung bei der Seppeler Gruppe eingeführt wurde."){record_delimiter} ("entity"{tuple_delimiter}"ELO DocXtractor"{tuple_delimiter}"ECM Module"{tuple_delimiter}"ELO DocXtractor ist ein Modul der ELO ECM Suite, das zur automatisierten Verarbeitung von Eingangsrechnungen dient."){record_delimiter} ("entity"{tuple_delimiter}"ELOxc"{tuple_delimiter}"ECM Module"{tuple_delimiter}"ELOxc ist ein Modul der ELO ECM Suite, das zur schnelleren Verarbeitung von E-Mails eingesetzt wird."){record_delimiter} ("entity"{tuple_delimiter}"SI-Workflow"{tuple_delimiter}"ECM Module"{tuple_delimiter}"SI-Workflow ist ein Modul zur Optimierung der Eingangsrechnungsverarbeitung bei der Seppeler Gruppe."){record_delimiter} ("entity"{tuple_delimiter}"SI-Connect"{tuple_delimiter}"technology"{tuple_delimiter}"SI-Connect ist eine Toolbox, die zur Anbindung der ELO ECM Suite an das Diamant Rechnungswesen & Controlling System verwendet wird, um einen reibungslosen Datenfluss sicherzustellen."){record_delimiter} ("entity"{tuple_delimiter}"Diamant Rechnungswesen & Controlling"{tuple_delimiter}"technology"{tuple_delimiter}"Das Diamant Rechnungswesen & Controlling System ist ein Softwareprodukt, das in die ELO ECM Suite integriert wurde, um den reibungslosen Datenfluss bei der Seppeler Gruppe zu gewährleisten."){record_delimiter} ("entity"{tuple_delimiter}"Eingangsrechnungsverarbeitung"{tuple_delimiter}"process"{tuple_delimiter}"Die Eingangsrechnungsverarbeitung wurde durch die ELO ECM Suite und die Module ELO DocXtractor, ELOxc, SI-Workflow und SI-Connect optimiert."){record_delimiter} ("entity"{tuple_delimiter}"Zeitaufwand von 12 auf 6 Tage halbiert"{tuple_delimiter}"key fact"{tuple_delimiter}"Der Zeitaufwand für die Verarbeitung von Eingangsrechnungen wurde durch die Automatisierung und Digitalisierung der Rechnungsprüfung von 12 auf 6 Tage reduziert."){record_delimiter} ("relationship"{tuple_delimiter}"Seppeler Gruppe"{tuple_delimiter}"SideStep Business Solutions"{tuple_delimiter}"SideStep hat das ELO ECM-System und Module bei der Seppeler Gruppe implementiert, um die Eingangsrechnungsverarbeitung zu optimieren."{tuple_delimiter}"Projektzusammenarbeit, Prozessoptimierung"{tuple_delimiter}9){record_delimiter} ("relationship"{tuple_delimiter}"ELO ECM Suite"{tuple_delimiter}"ELO DocXtractor"{tuple_delimiter}"ELO DocXtractor ist ein Modul der ELO ECM Suite, das zur automatisierten Verarbeitung von Eingangsrechnungen verwendet wird."{tuple_delimiter}"Modulintegration, Automatisierung"{tuple_delimiter}8){record_delimiter} ("relationship"{tuple_delimiter}"SI-Connect"{tuple_delimiter}"Diamant Rechnungswesen & Controlling"{tuple_delimiter}"SI-Connect sorgt für die Anbindung des Diamant Rechnungswesen & Controlling Systems an die ELO ECM Suite und garantiert so einen reibungslosen Datenfluss."{tuple_delimiter}"Systemintegration, Datenfluss"{tuple_delimiter}9){record_delimiter} ("relationship"{tuple_delimiter}"ELO ECM Suite"{tuple_delimiter}"Eingangsrechnungsverarbeitung"{tuple_delimiter}"Die ELO ECM Suite und ihre Module wurden zur Optimierung der Eingangsrechnungsverarbeitung implementiert."{tuple_delimiter}"Prozessoptimierung, Digitalisierung"{tuple_delimiter}9){record_delimiter} ("content_keywords"{tuple_delimiter}"Eingangsrechnungsverarbeitung, Prozessoptimierung, Automatisierung, Datenfluss"){completion_delimiter}
######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""

PROMPTS[
    "summarize_entity_descriptions"
] = """You are an agent that is collecting (in part internal) knowledge of the ECM Consulting Company Sidestep Business Solutions. The documents you receive are either extracted from the Sidestep Website or internal Documents describing facts about the company, its offerings and customer references. 
You are a helpful assistant responsible for generating a comprehensive summary of the data provided below.
Given one or two entities, and a list of descriptions, all related to the same entity or group of entities.
Please concatenate all of these into a single, comprehensive description. Make sure to include information collected from all the descriptions.
If the provided descriptions are contradictory, please resolve the contradictions and provide a single, coherent summary.
Make sure it is written in third person, and include the entity names so we the have full context.

ANSWER IN GERMAN

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""

PROMPTS[
    "entiti_continue_extraction"
] = """MANY entities were missed in the last extraction.  Add them below using the same format:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.
"""

PROMPTS["fail_response"] = "Sorry, I'm not able to provide an answer to that question."

PROMPTS["rag_response_old"] = """---Role---

You are an agent that is collecting (in part internal) knowledge of the ECM Consulting Company Sidestep Business Solutions. The documents you receive are either extracted from the Sidestep Website or internal Documents describing facts about the company, its offerings and customer references.

Your task is to respond to requests by Sidestep Employees to support them in their activities. In this task you are acting as a sort of virtual employee of sidestep.


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
If you don't know the answer, just say so. Do not make anything up.
Do not include information where the supporting evidence for it is not provided.

ALWAYS MAKE SURE THAT THE INFORMATION YOU GIVE ABOUT ENITIES ACTUALLY DESCRIBES THIS ENTITY!
There might be documents and information included in the data that describe different entities than the ones questioned about!!

---Target response length and format---

{response_type}

---Data tables---

{context_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""

PROMPTS["rag_response"] = """---Role---

You are an agent that is collecting (in part internal) knowledge of the ECM Consulting Company Sidestep Business Solutions. The documents you receive are either extracted from the Sidestep Website or internal documents describing facts about the company, its offerings, and customer references.

Your task is to respond to requests by Sidestep employees to support them in their activities. In this task, you are acting as a sort of virtual employee of Sidestep.

---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format. If you don't know the answer, just say so. Do not make anything up. Do not include information where the supporting evidence for it is not provided.

**Always ensure that the information you provide about entities accurately describes those entities.** There might be documents and information included in the data that describe different entities than the ones questioned about.

The text chunks in the context data include the path to the source file that can yield some info as to what the data talks about.

The context data tables include information about entities and relationships as table in csv format. Pay attention to how the entities are related and what is the source and target of a relationship.

The context contains csv tables of: Entities, Relationships between entities and Related Text Chunks

---Process---

1. Carefully read the user's question and identify the key information required.
2. Examine the data tables to find relevant information.
3. Verify that each piece of information directly answers the question and is supported by the data.
4. Pay special attention to entity names to ensure accuracy.
5. Organize the verified information logically.
6. Generate a concise and accurate response in the target format.
7. Check the factfulness of the response and omit every piece of information that is not directly verified by the source data.

*Note: Do not include these analysis steps in your final response.*

---Target response length and format---

{response_type}

---Data tables (context)---

{context_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown using appropriate headings and bullet points.
"""

PROMPTS["fact_checker"] = """ Du bist ein perfekter Faktenprüfer und überprüfst die Arbeit deines Kollegen. Achte darauf, dass nur Informationen berücksichtigt werden, die sich explizit auf die im Gespräch genannte Firma oder Entität beziehen. Wenn im Kontext allgemeine Informationen oder Fakten erwähnt werden, die nicht klar auf diese spezifische Firma oder Entität zutreffen, dürfen sie nicht in die Antwort aufgenommen werden.

Falls etwas in der Antwort nicht klar durch die Daten im Kontext gestützt wird oder wenn die Daten im Kontext nicht eindeutig zu der spezifischen Firma oder Entität passen (z. B. wird ein Modul erwähnt, aber es ist nicht klar, dass es für diese spezifische Firma oder dieses spezifische Projekt verwendet wurde), korrigiere die Antwort. Achte besonders darauf, dass Informationen, die nur allgemein erwähnt werden, aber nicht für die spezifische Firma relevant sind, ausgeschlossen werden.

Wenn im Kontext Technologien, Module oder Services beschrieben werden, die zwar im Allgemeinen erwähnt werden, aber nicht speziell bei der Firma, nach der gefragt wird, verwendet werden, ignoriere diese Informationen. Nur Informationen, die klar darauf hinweisen, dass sie für die genannte Firma oder Entität verwendet wurden, dürfen in der Antwort erscheinen.

Wenn die Informationen in der Antwort falsch sind (nicht durch den Kontext gestützt), du aber die richtigen Informationen nicht finden kannst, lasse die Informationen weg. Wenn du dir bei etwas nicht sicher bist, betrachte es als falsch. LASS KEINE FALSCHEN INFORMATIONEN, DIE NICHT KLAR DURCH DEN KONTEXT GESTÜTZT WERDEN, DURCH!

Du kannst beurteilen, ob die Antwort korrekt ist, indem du die folgenden Schritte durchführst:

Welche Fakten werden in der Antwort angegeben?
Welche Firma oder Entität wird durch jeden Fakt beschrieben?
Ist der Fakt im Kontext, wie in der Antwort angegeben, enthalten und explizit mit der spezifischen Firma oder Entität verknüpft?
Wurde das beschriebene Element oder die Technologie tatsächlich bei der genannten Firma oder im relevanten Projekt verwendet?
Schließe diese Schritte nicht in deine endgültige Antwort ein.

Nur weil etwas erwähnt wird, muss es nicht auch gleich auf die Entität zutreffen. Zum Beispiel reicht es nicht aus, dass DATEV auf einer Webseite steht. Es muss dort auch stehen, dass es bei dem Kunden eingesetzt wird.

Die Systemaufforderung, die dein Kollege erhalten hat, ist die folgende. Sie enthält den gegebenen Kontext, der Entitäten und ihre Beziehungen in CSV-Tabellen enthält.

<ORIGINAL SYSTEM PROMPT AND CONTEXT> {system_prompt} </ORIGINAL SYSTEM PROMPT AND CONTEXT>
Der Gesprächsverlauf und die Anfrage lauten wie folgt:

<CONVERSATION HISTORY AND QUERY> {query} </CONVERSATION HISTORY AND QUERY>
Dies ist die Antwort, die dein Kollege gegeben hat:

<RESPONSE> {response} </RESPONSE>
Erkläre was du korrigiert hast und wieso. """

PROMPTS["keywords_extraction"] = """---Role---
You are an agent that is collecting (in part internal) knowledge of the ECM Consulting Company Sidestep Business Solutions. The documents you receive are either extracted from the Sidestep Website or internal Documents describing facts about the company, its offerings and customer references.
You are a helpful assistant tasked with identifying both high-level and low-level keywords in the user's query.

---Goal---

Given the query, list both high-level and low-level keywords. High-level keywords focus on overarching concepts or themes, while low-level keywords focus on specific entities, details, or concrete terms. The user query contains the previous conversation history and might relate to it. Identify the keywords in a way that captures the content the user inquires about.

---Instructions---

- Output the keywords in JSON format.
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes.
  - "low_level_keywords" for specific entities or details.

######################
-Examples-
######################
Example 1:

Query: "How does international trade influence global economic stability?"
################
Output:
{{
  "high_level_keywords": ["International trade", "Global economic stability", "Economic impact"],
  "low_level_keywords": ["Trade agreements", "Tariffs", "Currency exchange", "Imports", "Exports"]
}}
#############################
Example 2:

Query: "What are the environmental consequences of deforestation on biodiversity?"
################
Output:
{{
  "high_level_keywords": ["Environmental consequences", "Deforestation", "Biodiversity loss"],
  "low_level_keywords": ["Species extinction", "Habitat destruction", "Carbon emissions", "Rainforest", "Ecosystem"]
}}
#############################
Example 3:

Query: "What is the role of education in reducing poverty?"
################
Output:
{{
  "high_level_keywords": ["Education", "Poverty reduction", "Socioeconomic development"],
  "low_level_keywords": ["School access", "Literacy rates", "Job training", "Income inequality"]
}}
#############################
-Real Data-
######################
Query: {query}
######################
Output:

"""

PROMPTS["naive_rag_response"] = """You're a helpful assistant
Below are the knowledge you know:
{content_data}
---
If you don't know the answer or if the provided knowledge do not contain sufficient information to provide an answer, just say so. Do not make anything up.
Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
If you don't know the answer, just say so. Do not make anything up.
Do not include information where the supporting evidence for it is not provided.
---Target response length and format---
{response_type}
"""