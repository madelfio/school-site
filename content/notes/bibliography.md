Title: BibTeX Style Guidelines
Subtitle: My Personal Bibliography Style Guide
Date: 2013-02-20 16:50
Summary: Tips and tricks for collecting and formatting bibliographies.
Slug: bib-style
Category: Notes

<style>
  .body code {
    border:none;
    background:none;
    font-size:inherit;
  }
  .body strong code {
    font-size: 14px;
  }
</style>
<div markdown="1">

I generally follow the guidelines below when I put together bibliographies.

The most important objective is to be consistent.  If one reference uses
*"New York, NY, USA"* as the location of a conference, don't use *"New
York, USA"* for another reference.  Or if one reference uses *"Proceedings
of the SIGSPATIAL 2012 International Conference on Advances in Geographic
Information Systems"* as the title of conference proceedings, don't use
*"VLDB 2011"* for another.  Conference papers should have the same fields
and formats as other conference papers, and ditto for journal articles,
books, online resources, etc.

## Gather Source Information

To write a bibliography for a paper, first ensure you have the important
bibliographic details for the sources you consulted.  Some popular sources
of bibliographic information are:

  - [ACM Digital Library][1]
  - [DBLP][2]
  - [Google Scholar][3]

Unfortunately, if you sample references from these sources, it becomes
obvious that each uses a different format, with different fields for their
references.  And since they are not curated by hand, even multiple
references from the same source may be inconsistent.  So the references
must be standardized after the details are pulled.

[BibTeX][4] looks like this:

    :::bib
    @book{Anon06,
      author = "Nobody J. Anonymous",
      title = "My Book",
      year = "2006" 
    }

For this entry, **`@book`** is the entry type, **`Anon06`** is the
reference key (used to reference the source from LaTeX files), and
**`author`**, **`title`**, and **`year`** are source attributes, set to the
quoted values.  Depending on the entry type and the bibliography style used
in a LaTeX file, different attributes will be included in the generated
bibliography text.

## Bibliography Entry Types

<style>
  #entry-types {
    border: 1px solid #ccc;
    border-radius: 2px;
    box-shadow: 0 0 10px rgba(100, 100, 100, 0.8);
    background-color: #f6f6f6;
    margin:20px 10px;
    width:350px;
  }
  #entry-types .sec {
    border-bottom: 2px solid #ccc;
    border-top: 2px solid #ccc;
    background-color: #DDD;
  }
  #entry-types td {padding:1px;}
</style>

<table id="entry-types">
  <tr class="sec"><td colspan="2">***Common***</td></tr>
  <tr><td>`@article`</td><td>an article published in a journal</td></tr>
  <tr><td>`@book`</td><td></td></tr>
  <tr><td>`@inproceedings`</td><td>a paper presented at a conference</td></tr>
  <tr><td>`@misc`</td><td>URL, other publication</td></tr>
  <tr class="sec"><td colspan="2">***Less Frequent***</td></tr>
  <tr><td>`@techreport`</td><td></td></tr>
  <tr><td>`@phdthesis`</td><td></td></tr>
  <tr><td>`@mastersthesis`</td><td></td></tr>
  <tr><td>`@manual`</td><td></td></tr>
  <tr class="sec"><td colspan="2">***Used with crossref attribute***</td></tr>
  <tr><td>`@proceedings`</td><td></td></tr>
</table>

## Formatting BibTeX Entries

**Reference Keys** - Use up to four letters of the last name, followed by
the two-digit publication year, followed by a disambiguating letter when
necessary (for multiple works by the same author in the same year).
Capitalization of reference keys doesn't matter to BibTeX, but I
capitalize only the first letter of the last name for consistency.

    :::text
    - Adel11
    - Li08
    - Same12
    - Same12b
    - Same12c

**Authors** - Multiple authors should be separated by the word "and".  Full
first names should be included (rather than only the first initial), which
a bibliography style can abbreviate if necessary.  Either "Last, First" or
"First Last" may be used.

**Titles** - Ensure that acronyms and words that require capitalization are
placed within an extra pair of braces.  Otherwise they will be converted to
lower case.

    {{UNIX} Network Programming: The Sockets Networking {API}}

**Book Titles** - Many bibtex sources provide long titles for conferences
and journals.  However, there is a trend towards shorter citation names,
possibly due to the Internet 

<span class="hl hl-todo">Todo:</span> Document additional attributes
(**Pages**, **Address**, **Crossref**, **Journal**, **Month**, **Note**,
**Volume/Number**, **Year**)

## Which Fields Do I Need?

#### Conference papers

    :::bib
    @inproceedings{Same08,
      author    = {Hanan Samet and Jagan Sankaranarayanan and Houman Alborzi},
      title     = {Scalable network distance browsing in spatial databases},
      pages     = {43-54},
      crossref  = {SIGMOD08},
    }
    @proceedings{SIGMOD08,
      booktitle = {SIGMOD~'08},
      address   = {Vancouver, Canada},
      month     = june,
      year      = {2008},
    }

#### Journal articles

    :::bib
    @article{Cafa11,
      author    = {Michael J. Cafarella and Alon Y. Halevy and Jayant Madhavan},
      title     = {Structured data on the web},
      journal   = {Communications of the ACM},
      volume    = {54},
      number    = {2},
      year      = {2011},
      pages     = {72-79},
    }

#### Books

    :::bib
    @book{Same06,
      author    = {Hanan Samet},
      title     = {Foundations of multidimensional and metric data structures},
      year      = {2006},
      publisher = {Morgan Kaufmann}
    }


<span class="hl hl-todo">Todo:</span> Add examples for **Websites**,
**Online Manuals**,

### Notes

["Taming the Beast"][5] is a good reference for all things BibTeX.  Look
there for tips on BibTeX syntax, how to deal with foreign or non-standard
author names, non-ASCII characters, and other useful tricks.

BibTeX syntax highlighting on this page is done using
[bibtex-pygments-lexer][6].

[1]: http://dl.acm.org/
[2]: http://www.informatik.uni-trier.de/~ley/db/
[3]: http://scholar.google.com/
[4]: http://www.bibtex.org/
[5]: http://www.lsv.ens-cachan.fr/~markey/BibTeX/doc/ttb_en.pdf
[6]: http://www.github.com/madelfio/bibtex-pygments-lexer

</div>
