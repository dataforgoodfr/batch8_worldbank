
# Table of Contents

1.  [Prototype/Wireframe](#org4a04fb0)
    1.  [Features](#org6e515ac)
        1.  [Worldmap](#orgdcdd0ed)
        2.  [Pop-up](#orgb5d1860)
        3.  [World figure](#orgf1f26d7)
2.  [Dataset](#orga97cfc3)
    1.  [Variables](#orga6acd98)
    2.  [Data sources](#orgdcd7710)
        1.  [Decade](#orgd669953)
        2.  [UN<sub>Geosheme</sub><sub>Subregion</sub>](#orga97914b)
        3.  [Disaster<sub>Type</sub>](#orgccefc77)
        4.  [RCP](#org5e70083)
        5.  [#LoDO](#orge4a0e37)
        6.  [#MeDO](#orge3e88fc)
        7.  [#HiDO](#org11841bb)
        8.  [Human<sub>Impact</sub>](#org0691afb)
        9.  [Financial<sub>mpact</sub>](#orge7611de)
        10. [°C](#orgdf3d9cc)
        11. [Geo](#org6ae1813)
3.  [The Dashboard](#org8dc4499)
    1.  [Why did we pick Dash?](#orgfc48739)
    2.  [Design](#org01f0a4d)
    3.  [Required files to run it](#org2df2f73)
        1.  [app.py](#org4be09d9)
        2.  [assets/style.css](#orgef5cab0)
        3.  [assets/WB<sub>logo.jpg</sub>](#org676f795)
4.  [Project Management](#orga29404f)
    1.  [Methodology](#orgc538e1a)
    2.  [tools](#org6c2c864)
    3.  [How to contribute](#orgae3fc98)

Todo : upload a screenshot of the delivered dashboard


<a id="org4a04fb0"></a>

# Prototype/Wireframe


<a id="org6e515ac"></a>

## Features


<a id="orgdcdd0ed"></a>

### Worldmap


<a id="orgb5d1860"></a>

### Pop-up


<a id="orgf1f26d7"></a>

### World figure


<a id="orga97cfc3"></a>

# Dataset


<a id="orga6acd98"></a>

## DONE Variables

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Variable name</td>
<td class="org-left">Data type</td>
<td class="org-left">Description/Example</td>
</tr>


<tr>
<td class="org-left">:----------------&#x2013;&#x2014;:+:----&#x2013;&#x2014;:+:-------------------------------------------------------------&#x2013;&#x2014; :</td>
</tr>


<tr>
<td class="org-left">Decade</td>
<td class="org-left">int64</td>
<td class="org-left">1900, 1910, &#x2026;, 2080, 2090</td>
</tr>


<tr>
<td class="org-left">UN<sub>Geosheme</sub><sub>Subregion</sub></td>
<td class="org-left">str</td>
<td class="org-left">'Australia and New Zealand', 'Caribbean', etc., see [M49 sub regions](https://unstats.un.org/unsd/methodology/m49/)</td>
</tr>


<tr>
<td class="org-left">Disaster<sub>Type</sub></td>
<td class="org-left">str</td>
<td class="org-left">Either 'Floods', 'Droughts' or 'Storms'</td>
</tr>


<tr>
<td class="org-left">RCP</td>
<td class="org-left">float64</td>
<td class="org-left">NaN for the past, either 2.6, 4.5, 6.0 or 8.5 for the future</td>
</tr>


<tr>
<td class="org-left">#LoDO</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of low impact disasters<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">#MeDO</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of medium impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">#HiDO</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of high impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">Human<sub>Impact</sub></td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of impacted people<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">Financial<sub>mpact</sub></td>
<td class="org-left">int64</td>
<td class="org-left">Provides the financial impact<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">°C</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the temperature in Celsius degrees<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup></td>
</tr>


<tr>
<td class="org-left">Geo</td>
<td class="org-left">GeoPandas</td>
<td class="org-left">Geospatial data delimitating geoscheme sub regions on the map</td>
</tr>
</tbody>
</table>


<a id="orgdcd7710"></a>

## BACKLOG Data sources


<a id="orgd669953"></a>

### Decade

Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]
For example `2020` starts in 2020 and ends in 2029


<a id="orga97914b"></a>

### UN<sub>Geosheme</sub><sub>Subregion</sub>

UN<sub>Geosheme</sub><sub>Subregion</sub>=['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']
Todo : take from 

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide link  


<a id="orgccefc77"></a>

### Disaster<sub>Type</sub>

Disaster<sub>Type</sub> = ['Droughts', 'Floods', 'Storms']
Todo : link to github respective workstream pages


<a id="org5e70083"></a>

### RCP

RCP = [2.6,4.5,6.0,8.5]
TODO : take from <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link


<a id="orge4a0e37"></a>

### #LoDO

Todo : link to github respective workstream pages


<a id="orge3e88fc"></a>

### #MeDO

Todo : link to github respective workstream pages


<a id="org11841bb"></a>

### #HiDO

Todo : link to github respective workstream pages


<a id="org0691afb"></a>

### Human<sub>Impact</sub>

Todo : link to github respective workstream pages


<a id="orge7611de"></a>

### Financial<sub>mpact</sub>

Todo : link to github respective workstream pages


<a id="orgdf3d9cc"></a>

### °C

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org6ae1813"></a>

### Geo

Todo : explain


<a id="org8dc4499"></a>

# The Dashboard


<a id="orgfc48739"></a>

## Why did we pick [Dash](https://plotly.com/dash/)?

[List of Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck team decided to develop the PoC with ****Dash****

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Maturity</th>
<th scope="col" class="org-left">Popularity</th>
<th scope="col" class="org-left">Simplicity</th>
<th scope="col" class="org-left">Adaptability</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Streamlit</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>


<tr>
<td class="org-left">Dash</td>
<td class="org-left">B</td>
<td class="org-left">A</td>
<td class="org-left">B</td>
<td class="org-left">B</td>
</tr>


<tr>
<td class="org-left">Voila</td>
<td class="org-left">C</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>
</tbody>
</table>

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the library.

****Adaptability****: Based on how flexible and opinionated the library is.


<a id="org01f0a4d"></a>

## Design

Todo mention World Bank Visual Identity Guidelines


<a id="org2df2f73"></a>

## Required files to run it

Todo : describe files


<a id="org4be09d9"></a>

### app.py


<a id="orgef5cab0"></a>

### assets/style.css


<a id="org676f795"></a>

### assets/WB<sub>logo.jpg</sub>


<a id="orga29404f"></a>

# Project Management


<a id="orgc538e1a"></a>

## Methodology


<a id="org6c2c864"></a>

## tools

-   Notion
-   Slack
-   Zoom


<a id="orgae3fc98"></a>

## How to contribute

-   Get our project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub
-   When adding a new file do
    
        $ git add newfilename
        $ git commit
        $ git push origin master

-   When modifying an existing file do 
    
        ???


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
