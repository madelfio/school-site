Title: Automated Table Extraction
Subtitle: With CRFs
Date: 2013-02-22 22:08
Category: Demos
Summary:
Javascript: jquery, d3

<style>
  #bookmarks * {
    -webkit-transition-duration: .3s;
    -moz-transition-duration: .3s;
    -ms-transition-duration: .3s;
    transition-duration: .3s;
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
    background-color: #ddd;
    border: 2px solid #ccc;
    font-size:16px;
    margin-right:10px;
  }
  #bookmarks li.current {
    background-color: #e66;
    border-color: maroon;
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
    top:24px;
  }
  #bookmarks li.current a {
    color: #fff;
  }
  #bookmarks a:active {
    -webkit-transition-property:background-color;
    -moz-transition-property:background-color;
    -ms-transition-property:background-color;
    transition-property:background-color;
    background-color:green;
  }
</style>

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

<a id="table-structures"></a>
##Table Structures

Tables are **data-dense**. That is, you can fit a lot more *information*
into a table than you can fit into the same amount of space using prose.
The traditional table structure of 

<a id="table-features"></a>
##Table Features

<a id="crfs"></a>
##Conditional Random Fields

<a id="experiments"></a>
##Experiments

<a id="conclusions"></a>
##Conclusions

