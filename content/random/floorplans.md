Title: A.V. Williams Building
Subtitle: Floorplans
Date: 2013-02-23 14:46
Category: Random
Summary:
Javascript: d3

<style>
  svg {height:665px; width:750px;}
  #floorplan-wrapper {
    background-color:#fff;
    width:750px;
    padding:15px;
    border:1px solid #999;
    box-shadow:3px 3px 3px #aaa;
  }
  g.floor:hover {
    cursor:pointer;
  }
  #content {
    width: auto;
  }
</style>

<div id="floorplan-wrapper" >
  <svg></svg>
  <div id="clear"></div>
</div>

<script>
"use strict";

var svg = d3.select('svg'),
    floor_numbers = d3.range(1,5),
    maximized = false;

floor_numbers.reverse();

var floors = svg.selectAll('g.floor').data(floor_numbers)
  .enter().append('g')
  .attr('class', 'floor')
  .attr('transform', function(d) {return 'translate(0,' + (100 * (4-d)) + ')';})
  .attr('opacity', 1.0);

var imgs = floors.append('image')
  .attr('xlink:href', function (d) {return siteurl + '/static/files/floorplans/115-' + d + '-transparent.png';})
  .attr('x', 0)
  .attr('y', 0)
  .attr('height', 350)
  .attr('width', function(d) {return d==1 ? 510 : d==3 ? 517 : 490;})
  .attr('transform', 'skewX(35)')
  .on('mouseover', function(d, i) {
    if (maximized) {return;}
    floors.filter(function(d2) {return d2 != d;})
      .transition().duration(200)
      .attr('opacity', 0.2);
    floors.filter(function(d2) {return d2 == d;})
      .attr('opacity', 1.0);
  })
  .on('mouseout', function(d, i) {
    if (maximized) {return;}
    floors
      .transition()
      .attr('opacity', 1.0);
  })
  .on('click', function(d, i) {
    if (!maximized) {
      maximized = true;
      floors.filter(function(d2) {return d2 != d;})
        .transition()
        .attr('opacity', 0);
      floors.filter(function(d2) {return d2 == d;})
        .transition()
        .attr('transform', 'translate(0,0)');
      d3.select(this)
        .transition()
        .attr('height', 495)
        .attr('width', 693)
        .attr('transform', 'skewX(0)');
    } else {
      maximized = false;
      floors.transition()
        .attr('transform', function(d) {return 'translate(0,' + (100 * (4-d)) + ')';})
        .attr('opacity', 1.0);
      imgs.transition()
        .attr('height', 350)
        .attr('width', function(d) {return d==1 ? 510 : d==3 ? 517 : 490;})
        .attr('transform', 'skewX(35)');
    }

  });

// reverse floor order
floors.sort(function(a,b) {return a>b;});
</script>
