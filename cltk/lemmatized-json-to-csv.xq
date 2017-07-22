(: Run in BaseX to get a CSV of lemma / wordform pairs :)

let $f := "q10.json"
let $json := file:read-text($f)
let $csv := element csv {
for $p in json-to-xml($json)//*:array[*:string]
let $s := tokenize($p/*:string, '/')
return element tr {
  element td { 
  $s[1] },
  element td { 
  $s[2]}
} }
return csv:serialize($csv)