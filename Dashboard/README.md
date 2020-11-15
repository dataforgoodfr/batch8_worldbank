
# Table of Contents

1.  [<code>[0/2]</code> Prototyping](#org2762742)
    1.  [Features](#orge54726e)
        1.  [World map](#org728bc69)
        2.  [Pop-up](#org451f1cb)
        3.  [World figures](#orgd4de20d)
    2.  [Wireframe](#org4c2257b)
        1.  [World map](#org0e9b28c)
        2.  [Pop-up](#org6a6771b)
        3.  [World figure](#org5ca31a5)
2.  [<code>[1/2]</code> Dataset](#orgc302dd8)
    1.  [Variables](#org8620993)
    2.  [<code>[1/11]</code> Data sources](#org9da6063)
        1.  [`Decade`](#org6716c4b)
        2.  [`UN_Geosheme_Subregion`](#orgce35def)
        3.  [`Disaster_Type`](#orge421c25)
        4.  [`RCP`](#org2706912)
        5.  [`#LoDO`](#orgae0aff8)
        6.  [`#MeDO`](#org72cf612)
        7.  [`#HiDO`](#org0e603b9)
        8.  [`Human_Impact`](#org7643191)
        9.  [`Financial_Impact`](#org9bfa0d6)
        10. [`°C`](#orgd2a77e9)
        11. [`Geo`](#org82a0cde)
3.  [<code>[0/3]</code> Development](#org9d2f66e)
    1.  [Why did we pick Dash?](#orgfc11170)
    2.  [Visual identity](#orga108fec)
    3.  [Architecture](#org3f3f5a7)
        1.  [`app.py`](#org668529a)
        2.  [`assets/style.css`](#org7d5b749)
        3.  [`assets/WB_logo.jpg`](#org5593867)
4.  [<code>[0/3]</code> Project Management](#org38f8e19)
    1.  [Methodology](#orgb8ee354)
    2.  [tools](#orgaddc72d)
    3.  [How to contribute](#org8d8de19)

Todo : upload a screenshot of the delivered dashboard


<a id="org2762742"></a>

# BACKLOG <code>[0/2]</code> Prototyping


<a id="orge54726e"></a>

## BACKLOG Features


<a id="org728bc69"></a>

### BACKLOG World map


<a id="org451f1cb"></a>

### BACKLOG Pop-up


<a id="orgd4de20d"></a>

### BACKLOG World figures


<a id="org4c2257b"></a>

## BACKLOG Wireframe


<a id="org0e9b28c"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="org6a6771b"></a>

### BACKLOG Pop-up


<a id="org5ca31a5"></a>

### BACKLOG World figure


<a id="orgc302dd8"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="org8620993"></a>

## DONE Variables

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Variable name</th>
<th scope="col" class="org-left">Data type</th>
<th scope="col" class="org-left">Description/Example</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">`Decade`</td>
<td class="org-left">int64</td>
<td class="org-left">1900, 1910, &#x2026;, 2080, 2090</td>
</tr>


<tr>
<td class="org-left">`UN_Geosheme_Subregion`</td>
<td class="org-left">str</td>
<td class="org-left">'Australia and New Zealand', 'Caribbean', etc.</td>
</tr>


<tr>
<td class="org-left">`Disaster_Type`</td>
<td class="org-left">str</td>
<td class="org-left">Either 'Floods', 'Droughts' or 'Storms'</td>
</tr>


<tr>
<td class="org-left">`RCP`</td>
<td class="org-left">float64</td>
<td class="org-left">NaN for the past, either 2.6, 4.5, 6.0 or 8.5 for the future</td>
</tr>


<tr>
<td class="org-left">`#LoDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of low impact disasters<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`#MeDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of medium impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`#HiDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of high impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Human_Impact`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of impacted people<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Financial_mpact`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the financial impact<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`°C`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the temperature in Celsius degrees<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup></td>
</tr>


<tr>
<td class="org-left">`Geo`</td>
<td class="org-left">GeoPandas</td>
<td class="org-left">Geospatial data delimitating geoscheme sub regions on the map</td>
</tr>
</tbody>
</table>


<a id="org9da6063"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="org6716c4b"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="orgce35def"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orge421c25"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org2706912"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="orgae0aff8"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="org72cf612"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="org0e603b9"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org7643191"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="org9bfa0d6"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="orgd2a77e9"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org82a0cde"></a>

### BACKLOG `Geo`

Todo : explain


<a id="org9d2f66e"></a>

# STARTED <code>[0/3]</code> Development


<a id="orgfc11170"></a>

## STARTED Why did we pick [Dash](https://plotly.com/dash/)?

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


<a id="orga108fec"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="org3f3f5a7"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org668529a"></a>

### `app.py`


<a id="org7d5b749"></a>

### `assets/style.css`


<a id="org5593867"></a>

### `assets/WB_logo.jpg`


<a id="org38f8e19"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="orgb8ee354"></a>

## BACKLOG Methodology


<a id="orgaddc72d"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="org8d8de19"></a>

## STARTED How to contribute

-   Clone our project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub
-   When adding a new file do
    
        $ git add newfilename
        $ git commit
        $ git push
-   When modifying an existing file, you have to submit modifications to its reviewer (i.e. owner). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">owner</th>
<th scope="col" class="org-left">file</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">mahdiqb</td>
<td class="org-left">`./app.py`</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">`./README.md`</td>
</tr>


<tr>
<td class="org-left">alencon</td>
<td class="org-left">`./asset/style.css`</td>
</tr>
</tbody>
</table>

-   reviewees have to do
    
        add git command
-   Reviewers have to do 
    
        add git command


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
