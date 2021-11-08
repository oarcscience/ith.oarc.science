---
layout: seclanding
title: "Intangible Textual Heritage: Document Coding Standards"
---
 

### Document Encoding Standards

------------------------------------------------------------------------

<span class="p-small"> </span>

These coding standards apply to *new* files scanned at Intangible
Textual Heritage. [There is a bibliography of all files scanned at this
site here](stbib). Because these conventions have evolved over time, not
all texts will have all of the markup specified here, particularly the
page numbering and footnote conventions. We are constantly refining our
methods of document preparation and production. However, there are still
quite a few files at this site which were scanned prior to these
features being added, and many texts were developed elsewhere. These
files are incrementally being upgraded to reflect the newer standards;
this process is likely to take quite a while.

------------------------------------------------------------------------

#### General Standards

The text is, as far as practically possible, transcribed letter for
letter from the original book. The etext includes all of the original
illustrations and graphics, where possible.

The etext includes a transcription of the title page, all prefatory
material, a linked table of contents, and all footnotes and other
apparatus, except (in most cases) for the index. We omit the index
because it is sometimes impossible or difficult to convert to etext, and
once the text is on the Internet, every word is indexed by multiple
search engines. We reproduce italics and bold text using standard HTML
markup.

Etexts are posted in HTML format (and sometimes plain ASCII text) due to
open source concerns. PDF and other ebook formats are vendor-specific,
and it is often difficult to migrate text out of them, particularly with
regard to formatting.

The etexts are uncensored and uncut. In no case is any text omitted from
the transcription, even in case of egregious factual errors or language
which might be considered offensive.

Non-English passages are reproduced verbatim, and no translation is
supplied (unless the translation is part of the original text).

Each text is carefully checked against a specific printed copy of the
book. We attempt to find an early edition of the book, (if possible the
first edition). If that is not practical, a photographic reproduction of
an early edition is used. In some cases a later printing may be used, if
we have a high degree of confidence that it accurately reflects the
complete, uncut original text, with no major editing. If a later edition
is used, that will be noted. We do not normally use multiple editions of
the book to prepare the text.

Page numbers are included in the transcription. We feel that is
important to indicate page numbers so the etexts can be cited in
academic and other publications.

#### Use of Unicode

Characters not within the standard ISO-8859-1 HTML coding are
represented using the closest or exact equivalent in the

. In older files, these were transcribed systematically using close 8
bit equivalents. Such substitutions and omissions are noted on a case by
case basis.

Unicode is inserted using extended character entities, rather than
UTF-8, since this is documents the character more clearly. In some cases
UTF-8 may be employed for longer files for reasons of space.

In some cases vowel diacritics may be omitted from the transcription,
particularly in the case of well-known words such as 'Sufi' or
'Nirvana'. This will be noted.

#### Macron Vowels

Where vowels with a 'macron' (a straight line above the vowel, usually
indicating a 'long' vowel) in a text are used consistently, these may be
transcribed using the 'circumflex' (the 'hat' diacritic, such as â, ê,
etc.).

#### In-text commentary

It is the policy of this site to not add any commentary in the body of
the etext. Editorial matter written at Intangible Textual Heritage about
the text is reserved for the index page, and will have a byline. Where
it is necessary to add *brief* in-text commentary, it is printed in a
green font. Such editorial annotations may also be italicized and the
initials of the transcriber (normally, 'jbh') noted. In-text commentary
is usually limited to technical notes about the source book, such as
notes of illegible or ambiguous type, missing pages, or the redactors'
attribution paragraph on the title page.

#### Errata

Each text is spell-checked during the proof-reading stage using the
standard MS Word spell-check dictionary. Specialized vocabulary is added
to a custom dictionary on a per-text basis. The text is also vetted for
known 'OCR bums'--words that are OCRed incorrectly, but spell-check as
valid words, such as 'burn' and 'bum', 'bad' and 'had', 'arid' and
'and'.

British, archaic and dialect spelling has been retained where it occurs.
If an idiosyncratic spelling occurs more than twice in a given text, it
is normally not marked as errata.

Typos are corrected and those corrections are noted. For instance, if
'Greenland' is spelled 'Greeenland', that is considered a typo. In such
cases, the word (correctly spelled) is linked to an errata file which
documents the original spelling. This file is named 'errata' in the same
directory as the text.

In some cases minor punctuation errors have been silently corrected.
However, care has been taken to preserve as closely as possible the
original punctuation, particularly in the case of older books. Some
books (for instance the Ganguli translation of the Mahabharata) have
major problems with punctuation, particularly nested dialog, and this
has been corrected where it was deemed necessary for comprehension.

#### Poetry

Poetry often requires complex indentation to transcribe its appearance
on the printed page. This is simulated using nested DIR tags and
non-breaking spaces at the start (and in some cases the middle) of the
line. Where possible, each block of poetry has line breaks (BR) between
each line, and paragraph breaks at the end of each stanza. Page numbers
are placed within the body of a block of poetry to avoid breaking up the
layout.

#### Quotation Marks

Where a space appears on both sides of a double or single quote, the
inner space is deleted:

" Look at the size of that thing! ", said Wedge.  
  

is transcribed  
  

"Look at the size of that thing!", said Wedge.  
  

For the most part, only 'straight' quotes are used, except where it may
be required to resolve ambiguity such as

'‘til Tuesday', she said.

Very rarely, curved quotes will be used in specialized transcriptions,
(typically indicating a glottal stop), and the straight quote is
reserved for an accent mark. Backquote (\`) is only used in specialized
transcriptions of non-English texts.

#### Page Breaks, Numbering and Continuations

Page breaks are indicated as p. NNN, where NNN is the page number. The
HTML page markup is as follows:

&lt;P&gt;&lt;A NAME="page\_91"&gt;&lt;FONT SIZE=1 COLOR=GREEN&gt;p.
91&lt;/FONT&gt;&lt;/A&gt;&lt;/P&gt;

Thus you could link to this specific page using the HTML anchor
'page\_91'. For instance, if the name of the file was 'foo42' in the
directory 'https://ith.oarc.science/bar' you could link to it using the
following HTML markup:

&lt;A HREF="https://ith.oarc.science/bar/foo42.htm\#page\_91"&gt;On page
91&lt;/A&gt; we are warned not to run with scissors...

No attempt is made currently to add indentation to the start of
paragraphs, due to the limitations of vanilla HTML. We have a system for
resolving whether a paragraph that begins at the start of a page is a
new or continued paragraph.

The page number is placed in a paragraph by itself, left indented. If
the page break occurs within or between paragraphs, it looks like this:

Fred was sure it wouldn't

p\. 45

rain that afternoon.

------------------------------------------------------------------------

The Queen was pacing back and forth.

p\. 45

In the next paragraph, a shot rang out.

If the page break occurs between two sentences in the same paragraph, or
if the first word on the successive page does not begin with a lower
case letter (including numbers, quotation marks and so on), a
continuation is noted as follows:

This paragraph continues on the next page.

p\. 45

\[paragraph continues\] This sentence is part of the paragraph on the
previous page.

------------------------------------------------------------------------

"Now wait just one minute", said

p\. 45

\[paragraph continues\]Fred, emphatically.

------------------------------------------------------------------------

There are

p\. 45

\[paragraph continues\]17 reasons not to run with scissors...

------------------------------------------------------------------------

The Queen commanded Fred,

p\. 45

\[paragraph continues\]"Don't run with scissors!"

------------------------------------------------------------------------

The continuation is added even if a human being could recognize the
paragraph continuation from context. This is so that the text could be
broken down into paragraphs correctly by a computer program.

If a paragraph continues midpage after a blockquote or an illustration
(that is, it is not indented in the book and doesn't begin with a
lowercase letter), the continuation is noted in the same way.

  
  

There was a young lady named Bright  
Who travelled much faster than light...  

\[paragraph continues\]This is one of the best limericks about
relativity.

#### Hyphenation

An em hyphen is transcribed as two successive ASCII hyphens (--).

In general, hyphenated words in the original text which appear because
of line breaks are joined. This is to facilitate search engines. If a
page break occurs in the middle of a word, any words hyphenated across
the page boundary are concatenated on the prior page. For instance, if
the word 'abracadbra' appears on page 42 hyphenated as 'abra-' and
continued on page 43 as 'cadabra', it is transcribed as:

abracadabra,

p\. 42

The one exception to this standard is if a hyphenated word is footnoted,
and the footnote is on the successive page, then the word is
concatenated and moved to the successive page, to avoid moving the
footnote.

A paragraph continuation is inserted if the concatenation creates one.

#### Footnotes

The following terms are used in this document to describe footnotes. The
location in the body of the text is called a 'footnote reference' or
just 'footref'. The term 'footnote' means the actual text of the
footnote.

Footrefs are hyperlinked to the corresponding footnote. All footnotes in
a chapter are moved to the end of the chapter. They are anchored using
the concatenated page number and footref on that page. The number next
to the footnote is linked back to the *first* instance of the footref
that references it. If a footnote continues over more than one page, a
page number is inserted into the body of the footnote text in small
green text. This does not have an HTML anchor markup.

In the case where asterisk, virgule, dagger, etc. are used for
footnotes, these are retranscribed silently as simple numerals.

In older files, footnotes are indicated using square brackets, as in
etext produced by Project Gutenberg. This was abandoned because it is
difficult or impossible to distinguish between a footref and a footnote
marked in this way using a computer program and it makes the text clumsy
to read.

In some cases, books have footnotes placed in another logical chapter
than the footref ('endnotes'). Normally these are not relocated in the
etext. In this case, the footrefs will appear as normal, but the
footnote will be in a separate file, in the sequence it was found in the
book. The endnote footnote numbers are not currently linked back to the
footref; to get back to the original location after reading the
footnote, you will need to use the 'back' button on your browser.
