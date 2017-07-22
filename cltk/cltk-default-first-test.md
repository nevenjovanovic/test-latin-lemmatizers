# Default CLTK lemmatizer: the first test

Objective: lemmatize the Book 10 of Quintilian's *Institutio oratoria* (Quint. Inst. 10).

## Preparation

+ Install CLTK
+ Install Latin corpora
+ Install BaseX (in our case, cleaning up Quintilian's text -- even from the plaintext Latin Library version supplied by CLTK -- seemed beyond our Python skills)

## Procedure

+ Clean up the text (remove remains of HTML and editorial signs): done manually, by regex search and replace, producing the text file [q10.txt](q10.txt)
+ Tokenize into words, prepare a list of unique word forms in Quint. Inst. 10: the BaseX script [prepare-wordlist-unique-quint10.xq](prepare-wordlist-unique-quint10.xq)
+ Feed the list to the CLTK lemmatizer: Python script [test-cltk-lemmatize-quintilian10a.py](test-cltk-lemmatize-quintilian10a.py)
+ Export the results: the Python script above produces the JSON [q10.json](q10.json)
+ Analyze the results: transform JSON into CSV ([lemmatized-json-to-csv.xq](lemmatized-json-to-csv.xq)), import into LibreOffice Calc for annotation: [q10cltk-lemmatized-with-comments.ods](q10cltk-lemmatized-with-comments.ods)

## Findings

Everything works. Speed is not a problem. For someone with sufficient Python skills, importing and exporting are trivial. The "Raw" mode offered by the lemmatizer method (`.lemmatize(q, return_raw=True)`) is very useful and easy to postprocess.

### Issues

+ Unclean sources. The plaintext file prepared from Latin Library's HTML, though the most simple, nevertheless still has HTML entities (lt, gt) and other editorial signs (cruces, square brackets) which have to be removed in the preparatory phase.
+ A segmenting problem. Reasonable use cases would include, for example, comparing Quintilian's vocabulary in all of the Book 10 with his vocabulary in the first chapter, introduction of new key terms, etc. For this purpose, the plaintext source has to be additionally processed.

+ Accuracy. Some word forms are impossible to lemmatize correctly without supervision or additional calibration. There are four possible outcomes:
  + the word form is unknown
  + there are multiple candidates for the lemma
  + there is a single, correct candidate for the lemma
  + there is a single, wrong candidate for the lemma

At the moment, CLTK's lemmatizer does not take into account these outcomes. It simply supplies a lemma (if it finds one), or repeats the word form (if it has not found a lemma). We don't know how reliable the results are, and we don't know how the lemmatizer selected the lemma (in the case of multiple candidates).

This behaviour is [documented](http://docs.cltk.org/en/latest/latin.html):

> For ambiguous forms, which could belong to several headwords, the current lemmatizer chooses the more commonly occurring headword (code here). For any errors that you spot, please open a ticket.

## A list of unexpected lemmatizations

Here are the first results -- lemmatizations of Quint. Inst. 10, letters A-C, which, on the first reading, strike me as unexpected. This may be a *possible* lemma, but not the one that I think of as the *most common* one.

| Form | Lemma |
|---|---|
| afer | a-for |
| aliquando | aliqua |
| aliquo | aliqua |
| alte | alo |
| animalia | animalis |
| arma | armo |
| artes | arto |
| artis | artus1 |
| auctorem | auctoro |
| auctores | auctoro |
| auctorum | augeo |
| aures | auro |
| bella | bellus |
| bellavit | bellor |
| belli | bellus |
| bellum | bellus |
| caesius | caesus1 |
| calor | calo1 |
| canentem | caneo |
| caneret | caneo |
| cantus | cano |
| capita | capitum |
| cassius | cassus |
| casus | cado |
| catius | catus1 |
| cato | catus1 |
| caute | caveo |
| cera | cero |
| ceras | cero |
| ceris | cera |
| certa | certo2 |
| cetera | ceter |
| ceteraque | ceter |
| ceterarum | ceter |
| ceteri | ceter |
| ceteris | ceter |
| ceterisque | ceter |
| ceteros | ceter |
| ceterum | ceter |
| ci | cichorium |
| cii | cichorium |
| circa | circo |
| circaque | circo |
| circumspecto | circumspicio |
| citius | cieo |
| cito | cieo |
| citra | citer |
| clamor | clamo |
| codicem | co-dico1 |
| codices | co-dico2 |
| color | colo1 |
| colorem | coloro |
| concisa | concaedes |
| concitatior | concito |
| conditae | condio |
| conditorum | condio |
| confecta | confacio |
| consilio | consilior |
| conspectu | conspicio1 |
| constantia | consto |
| continua | continuo2 |
| continuas | continuo2 |
| continuo | continuo2 |
| crassi | crassus1 |
| crassus | crassus1 |
| cultu | colo1 |
| culturam | colo1 |
| cuncta | cuncto |
| cura | curo |
| cursu | curro |
| cursus | curro |

# Unclear lemma format

# Inconsistent lemma format


