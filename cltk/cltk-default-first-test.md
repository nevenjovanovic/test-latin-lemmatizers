# Default CLTK lemmatizer: the first test

Objective: lemmatize the Book 10 of Quintilian's *Institutio oratoria* (Quint. Inst. 10).

## Preparation

+ Install CLTK
+ Install Latin corpora; use [Quintilian's Book 10 from CLTK's Latin Library repository](https://github.com/cltk/latin_text_latin_library/blob/master/quintilian/quintilian.institutio10.txt) (GitHub)
+ Install [BaseX XML DB](http://basex.org/) (because, in our case, quickly cleaning up Quintilian's text -- even from the plaintext version supplied by CLTK -- was beyond my Python skills)

## Procedure

+ Clean up the text (remove remains of HTML and editorial signs): done manually, by regex search and replace, producing the text file [q10.txt](q10.txt)
+ Tokenize into words, prepare a list of unique word forms in Quint. Inst. 10: the BaseX script [prepare-wordlist-unique-quint10.xq](prepare-wordlist-unique-quint10.xq)
+ Feed the list to the CLTK lemmatizer: Python script [test-cltk-lemmatize-quintilian10a.py](test-cltk-lemmatize-quintilian10a.py)
+ Export the results: the Python script above produces the JSON [q10.json](q10.json)
+ Analyze the results: transform JSON into CSV ([lemmatized-json-to-csv.xq](lemmatized-json-to-csv.xq)), import into LibreOffice Calc for annotation: [q10cltk-lemmatized-with-comments.ods](q10cltk-lemmatized-with-comments.ods)

## Findings

Everything works. Speed is not a problem. For someone with basic Python skills, importing and exporting are trivial. The "Raw" mode offered by the lemmatizer method (`.lemmatize(q, return_raw=True)`) is very useful and easy to postprocess.

### Issues

+ **Unclean sources**. The plaintext file prepared from Latin Library's HTML, though seemingly the most simple format, promising the quickest processing, nevertheless turned out to have HTML entities (lt, gt) and other editorial symbols (cruces, square brackets) which had to be removed in the preparatory phase.
+ **A problem with passages**. Reasonable use cases would include, for me, comparing Quintilian's vocabulary in all of the Book 10 with his vocabulary in the first chapter, introduction of new key terms, etc. For this purpose, the plaintext source has to be additionally processed, if we want to work with specific chapters, or if we want to know in which chapter a result is found.

+ **Accuracy**. Some word forms are impossible to lemmatize correctly without supervision or additional calibration. There are four possible outcomes:
  + the word form is unknown
  + there are multiple candidates for the lemma
  + there is a single, correct candidate for the lemma
  + there is a single, wrong candidate for the lemma

At the moment, CLTK's lemmatizer does not take into account these outcomes, or does not inform users about them. The lemmatizer simply supplies a lemma if it finds one, or repeats the word form (if it has not found anything). We don't know how reliable the results are (is the given lemma the only one possible for the program?), and we don't know how the lemmatizer selected the lemma (in the case of multiple candidates).

This behaviour is [documented](http://docs.cltk.org/en/latest/latin.html):

> For ambiguous forms, which could belong to several headwords, the current lemmatizer chooses the more commonly occurring headword (code here). For any errors that you spot, please open a ticket.

A further problem with this approach is that in some cases we cannot be sure whether the word has been recognized, or is the form simply repeated. For example, *animo / animo*, *accius / accius*. Of course, for some purposes this is completely acceptable ("accius" is lemma of "accius", though CLTK lemmatizer in general does not lemmatize proper names), but it is connected with the larger issue of identifying sources of lemmata (see below).

## A list of unexpected lemmatizations

Here are the first results -- lemmatizations of Quint. Inst. 10, letters A-C, which, on the first reading, strike me as unexpected, contrary to the "more commonly occurring headword" approach. The lemma may be *possible*, but it is not the one that I think of as the *most common* one.

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

A number of lemmata ends with an index number (accido1, adeo1, assiduus2, etc). Because it is not clearly documented which words / meanings are signified by these indices, they are not very useful: does "adeo1" signify "so", or "to approach"? Where can I check?

In general, the *source* of lemmata should somehow be given, documented, or cited, to enhance scholarly reliability of the tool. See below.

# Inconsistent lemma format

In lemmatization, the default CLTK lemmatizer provides verbs with prefixes which are inconsistently marked. In some cases prefixes are not separated from the stem (absum, abrumpo, absolvo); sometimes they are separated with a hyphen (see table below; I find even ad-sequor and assequor, as lemmata of adsecutus and assequi, while adsidua is lemmatized as assiduus2); sometimes they are even separated with an underscore and a hyphen (the same table). This *probably* means that the vowel is long. But vowel length is not annotated consistently in the lemmata, and it is not documented.

| Form | Lemma |
|---|---|
| adpetent | ad-peto |
| adprehendas | ad-prehendo |
| adprehenditur | ad-prehendo |
| adridens | ad-rideo |
| adsecutus | ad-sequor |
| adsignando | ad-signo |
| adsimulata | ad-simulo |
| adstrictius | ad-stringo |
| adstringere | ad-stringo |
| adsumendus | ad-sumo |
| adsumere | ad-sumo |
| adsumimus | ad-sumo |
| adsumpta | ad-sumo |
| comprensa | con-prehenso |
| concupierint | con-cupio |
| concupisset | con-cupio |
| conlocandi | con-loco |
| conlocata | con-loco |
| conrogatis | con-rogo |
| consecuta | con-sequor |
| consecuti | con-sequor |
| consecutus | con-sequor |
| derexeris | de_-rego |
| destiterat | de_-sisto |

# Improbable lemmatizations

A couple of lemmatizations seem to me not only unexpected, but wholly improbable:

| Form | Lemma |
|---|---|
| acie | acieris |
| bene |benus |


# Unrecognized forms

I would expect a number of forms to be lemmatized, but they haven't been:

| Form | Lemma |
|---|---|
| caelibum | caelibum |
| codicibus | codicibus |
| cogitaverant | cogitaverant |
| commune | commune |
| coturnos | coturnos |

# Some general observations

