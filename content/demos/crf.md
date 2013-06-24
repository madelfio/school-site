Title: Automated Table Extraction
Subtitle: With CRFs
Date: 2013-02-22 22:08
Category: Demos
Summary:
Javascript: jquery, d3

<style>
  #bookmarks * {
    -webkit-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -ms-transition-duration: .2s;
    transition-duration: .2s;
  }
  #bookmarks ul {
    margin-left:0;
  }
  #bookmarks li {
    display: inline-block;
    width: 100px;
    height: 100px;
    border-radius: 50px;
    text-align:center;
    vertical-align: middle;
    background-color: #eee;
    font-size:16px;
    margin-right:17px;
    -webkit-transition: background-color .2s linear;
    -moz-transition: background-color .2s linear;
    -ms-transition: background-color .2s linear;
    -o-transition: background-color .2s linear;
    transition: background-color .2s linear;
  }
  #bookmarks li.current {
    background-color: #e66;
  }
  #bookmarks a {
    display:block;
    width:100px;
    height:100px;
    border-radius:50px;
    line-height: 1;
    color: #888;
  }
  #bookmarks span {
    position:relative;
    top:38px;
  }
  #bookmarks .dbl span {
    top:30px;
  }
  #bookmarks .tpl span {
    top:26px;
  }
  #bookmarks li.current a {
    color: #fff;
  }
  #bookmarks li.current a:hover {
    text-decoration:none;
  }

  /*#bookmarks a:active {
    -webkit-transition-property:background-color;
    -moz-transition-property:background-color;
    -ms-transition-property:background-color;
    transition-property:background-color;
    background-color:green;
  }*/

  .example {
    width: inherit;
    display: inline-block;
             border-radius: 2px;
             box-shadow: 0 0 10px rgba(100, 100, 100, 0.8);
             background-color: #f6f6f6;
    margin: 5px 10px;
    float: right;
  }
  .example th, .example td {padding: 1px 5px; border: 1px solid #ccc;}
  .complex th {background-color: #c33; color: white;}

  .complex .title {font-weight: bold; color: darkblue;}
  .complex .non-relational {color: #888; font-size: 0.9em;}
  .complex .aggregate {font-style: italic;}
  .complex .group-header td {
    background-color: #ddd;
    border-bottom: 2px solid #ccc;
    font-weight: bold;
    font-style: italic;
  }

  .complex .m {text-align: center;}
  .complex .r {text-align: right;}

</style>

<script>
  function updateVisibleSection() {
    var section = window.location.hash || '#table-structures';
    $('.section').hide();
    $(section).show();
    $('.headline a').parent().removeClass('current');
    $('a[href$="'+section+'"]').parent().addClass('current');
  }
  $(window).bind('hashchange', updateVisibleSection);
  $(updateVisibleSection);
</script>

<div id="bookmarks" markdown="1">
  <ul class="headline">
    <li class="dbl current"><a href="#table-structures"><span>
      Table<br />Structures
    </span></a></li>
    <li class="dbl"><a href="#table-features"><span>
      Table<br />Features
    </span></a></li>
    <li class="tpl"><a href="#crfs"><span>
      Conditional<br />Random Fields
    </span></a></li>
    <li><a href="#experiments"><span>
      Experiments
    </span></a></li>
    <li><a href="#conclusions"><span>
      Conclusions
    </span></a></li>
  </ul>
</div>

<div id="table-structures" class="section" markdown="1">
##Table Structures

Tables are a **data-dense** presentation format. You can communicate more
information using a table than you can in the same amount of space using
prose.

A table consists of a 2-dimensional grid of table cells, which can each
contain a value and can optionally exhibit a variety of cell attributes,
such as text color, font face, or font style.<a></a><sup>1</sup>

There are many ways of creating a table and many ways file formats that can
include tables.  Some common formats are spreadsheets (where Microsoft
Excel is dominant), HTML tables, PDF tables, and ASCII text tables.

While there are many purposes for using a grid of table cells, we focus on
**relational tables**, meaning tables that describe a collection of objects or
entities and a common set of related attributes for each.  Although HTML
tables used as calendars or spreadsheets used as data-entry forms may have
tabular structure, in this discussion we ignore such **non-relational
tables**.

### Simple Tables

<table class="example">
  <tr><th>Last</th><th>First</th><th>Gender</th><th>Age</th></tr>
  <tr><td>Doe</td><td>John</td><td>Male</td><td>29</td></tr>
  <tr><td>Doe</td><td>Jane</td><td>Female</td><td>30</td></tr>
  <tr><td>Smith</td><td>Kate</td><td>Female</td><td>42</td></tr>
</table>

The simple, standard table format contains a single row of *k* cells that
comprise the table header, followed by a *k x n* rectangle of cells that
comprise the table data.  Each row of data cells describes attributes of a
single entity, and the type of attribute within each column is defined by
the header cell for that column.

### Complex Tables
<table class="example complex">
  <tr class="title"><td colspan="3">Patent Applications by Residents</td></tr>
  <tr class="non-relational"><td colspan="3">Data Source: worldbank.org</td></tr>
  <tr class="non-relational"><td colspan="3">(showing top countries in each continent)</td></tr>
  <tr class="header"><th>Country</th><th>Residents</th><th>Applications</th></tr>
  <tr class="group-header"><td>North America</td><td></td><td></td></tr>
  <tr><td class="m">United States</td><td class="r">307,007,000</td><td class="r">224,912</td></tr>
  <tr><td class="m">Canada</td><td class="r">33,739,900</td><td class="r">5,067</td></tr>
  <tr><td class="m">Mexico</td><td class="r">112,033,369</td><td class="r">822</td></tr>
  <tr class="aggregate"><td></td><td>N.A. Total</td><td class="r">230,801</td></tr>
  <tr class="group-header"><td>Asia</td><td></td><td></td></tr>
  <tr><td class="m">Japan</td><td class="r">127,557,958</td><td class="r">295,315</td></tr>
  <tr><td class="m">China</td><td class="r">1,331,380,000</td><td class="r">229,096</td></tr>
  <tr><td class="m">South Korea</td><td class="r">48,747,000</td><td class="r">127,316</td></tr>
  <tr class="aggregate"><td></td><td>Asia Total</td><td class="r">651,727</td></tr>
  <tr><td>&nbsp;</td><td></td><td></td></tr>
  <tr class="non-relational"><td colspan="2">Note: data from 2009</td><td></td></tr>
</table>

Complex structures are also found in data tables.  For example, the table at
right contains much more than a single header row followed by only data rows.
To aid in understanding the functions of different table rows, we categorize
the purpose of each row as one of the following.

  - **Header** rows are used to communicate the column headings.
  - **Data** rows contain relational data values.
  - **Title** rows provide captions or titles for an entire table.
  - **Group header** rows provide captions or titles for sections of a table.
  - **Aggregate** rows are used for totals or sub-totals.
  - **Non-relational** rows are used to add comments or notes to the table but
    are not part of the table's relational structure.
  - **Blank** rows contain no data or values (but can still be meaningful in the
    table's formatting).

As with any free-form human communication medium, the functional
classification of rows is imperfect.  Some rows may not be described by any of
the above labels, while other rows may be described accurately by multiple
labels.  Our study of a large sample of web tables, however, has found that
this set of labels covers the vast majority of rows with little ambiguity.

<hr width="100" style="clear:both;" />

1. A "table" has different meanings in different contexts.  Here "table"
   always means a grid-based form of presenting data, not a database table
   or lookup table data structure.

</div>
<div id="table-features" class="section" markdown="1">
##Table Features

</div>
<div id="crfs" class="section" markdown="1">
##Conditional Random Fields

</div>
<div id="experiments" class="section" markdown="1">
##Experiments

<!--- Put an animation here for the Automaton Method, stepping through the
rows of the table and simultaneously highlighting the state in the automaton
state machine  --->

</div>
<div id="conclusions" class="section" markdown="1">
##Conclusions

</div>
