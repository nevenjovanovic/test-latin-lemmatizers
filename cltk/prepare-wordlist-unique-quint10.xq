(: prepare wordlist for plaintext Quint. Inst. 10, clean up a lot of junk. Run in BaseX :)

let $f := 'quintilian.institutio10.txt'
let $file := file:read-text($f)
let $text := normalize-space($file)
let $tokens := distinct-values (
for $t in tokenize($text, '\s')
let $w := replace($t, '\W', '')
order by $w
return $w
)
return $tokens