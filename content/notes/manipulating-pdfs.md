Title: Manipulating PDFs
Date: 2013-02-08 12:59
Summary: LaTeX files and their PDF-document offspring can be obstinate beasts.  When you need to extract or combine parts of documents at the page level, sometimes it's easier to manipulate the output PDF rather than the source TeX.  Here are a couple of helper functions that I have in my .bashrc for this.
Category: Notes

####"PDF Jujitsu"

LaTeX files and their PDF document offspring can be obstinate beasts.  When
you need to extract or combine parts of documents *at the page level*,
sometimes it's easier to manipulate the output PDF rather than the source
TeX.  Here are a couple of helper functions that I have in my `.bashrc` for
this.

    :::bash
    # source: http://www.linuxjournal.com/content/tech-tip-extract-pages-pdf
    function pdfextract()
    {
      # arguments:
      #   $1 is the first page of the range to extract
      #   $2 is the last page of the range to extract
      #   $3 is the input file
      #   output file will be named "inputfile_pXX-pYY.pdf"
      gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
      -dFirstPage=${1} -dLastPage=${2} \
      -sOutputFile=${3%.pdf}_p${1}-p${2}.pdf \
      ${3}
    }

    # by marco. complements pdfextract
    function pdfmerge()
    {
      # arguments:
      #   $1 is the name of the output file
      #   $2+ are the names of the input files
      OUT=${1}
      shift
      gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
      -sOutputFile=$OUT \
      $@  
    }

####Examples

You can use `pdfextract` to extract pages 1-3 of a PDF:

    :::console
    $ ls
    my-long-document.pdf
    $ pdfextract 1 3 ./my-long-document.pdf
    $ ls
    my-long-document_p1-p3.pdf  my-long-document.pdf
 
Or use `pdfmerge` to merge a cover letter, proposal, and CV into a single PDF:
 
    :::console
    $ ls
    cover-letter.pdf  cv.pdf  proposal.pdf
    $ pdfmerge submission.pdf cover-letter.pdf proposal.pdf cv.pdf
    $ ls
    cover-letter.pdf  cv.pdf  proposal.pdf  submission.pdf
