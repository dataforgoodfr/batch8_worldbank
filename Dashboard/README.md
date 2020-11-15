
# Table of Contents

1.  [<code>[0/2]</code> Prototyping](#org437d0ba)
    1.  [Features](#org75e1e27)
        1.  [World map](#org13195a6)
        2.  [Pop-up](#org62a95fb)
        3.  [World figures](#org6e15473)
    2.  [Wireframe](#org5ce8abd)
        1.  [Worldmap](#org7781a55)
        2.  [Pop-up](#orgefc2af9)
        3.  [World figure](#orgae6f189)
2.  [<code>[1/2]</code> Dataset](#org1403ee7)
    1.  [Variables](#orgec5bd02)
    2.  [<code>[1/11]</code> Data sources](#org51eba77)
        1.  [`Decade`](#orgfffbee5)
        2.  [`UN_Geosheme_Subregion`](#org77e4903)
        3.  [`Disaster_Type`](#org220a3ee)
        4.  [`RCP`](#org8547d42)
        5.  [`#LoDO`](#org69955b4)
        6.  [`#MeDO`](#org565701f)
        7.  [`#HiDO`](#orge898c17)
        8.  [`Human_Impact`](#org553ba0e)
        9.  [`Financial_Impact`](#org0f33613)
        10. [`°C`](#org277b474)
        11. [`Geo`](#orga03b360)
3.  [<code>[0/3]</code> Development](#org3e8c973)
    1.  [Why did we pick Dash?](#orgf8343c4)
    2.  [Visual identity](#orgedfc6dd)
    3.  [Architecture](#org8d07af0)
        1.  [`app.py`](#org0e31102)
        2.  [`assets/style.css`](#org8127db9)
        3.  [`assets/WB_logo.jpg`](#orgf4ea0ec)
4.  [<code>[0/3]</code> Project Management](#org34b22ae)
    1.  [Methodology](#org0194659)
    2.  [tools](#org4b2cec3)
    3.  [How to contribute](#orgf9f24b1)

Todo : upload a screenshot of the delivered dashboard


<a id="org437d0ba"></a>

# BACKLOG <code>[0/2]</code> Prototyping


<a id="org75e1e27"></a>

## BACKLOG Features


<a id="org13195a6"></a>

### BACKLOG World map


<a id="org62a95fb"></a>

### BACKLOG Pop-up


<a id="org6e15473"></a>

### BACKLOG World figures


<a id="org5ce8abd"></a>

## BACKLOG Wireframe


<a id="org7781a55"></a>

### BACKLOG Worldmap


<a id="orgefc2af9"></a>

### BACKLOG Pop-up


<a id="orgae6f189"></a>

### BACKLOG World figure


<a id="org1403ee7"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="orgec5bd02"></a>

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


<a id="org51eba77"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="orgfffbee5"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org77e4903"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="org220a3ee"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org8547d42"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org69955b4"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="org565701f"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="orge898c17"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org553ba0e"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="org0f33613"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org277b474"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="orga03b360"></a>

### BACKLOG `Geo`

Todo : explain


<a id="org3e8c973"></a>

# STARTED <code>[0/3]</code> Development


<a id="orgf8343c4"></a>

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


<a id="orgedfc6dd"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="org8d07af0"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org0e31102"></a>

### `app.py`


<a id="org8127db9"></a>

### `assets/style.css`


<a id="orgf4ea0ec"></a>

### `assets/WB_logo.jpg`


<a id="org34b22ae"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="org0194659"></a>

## BACKLOG Methodology


<a id="org4b2cec3"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="orgf9f24b1"></a>

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
