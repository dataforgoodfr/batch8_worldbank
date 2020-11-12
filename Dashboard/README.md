
# Table of Contents

1.  [Prototype/Wireframe](#org2a1b173)
    1.  [Features](#org36c6c72)
        1.  [Worldmap](#org6875512)
        2.  [Pop-up](#orgd023185)
        3.  [World figure](#org3453d51)
2.  [Dataset](#org81956ae)
    1.  [Variables](#orgcb12757)
    2.  [Data sources](#org2ab3892)
        1.  [`Decade`](#org34bf763)
        2.  [`UN_Geosheme_Subregion`](#org4972f10)
        3.  [`Disaster_Type`](#orgfb02003)
        4.  [`RCP`](#org605d0cb)
        5.  [`#LoDO`](#orgb1dd6d2)
        6.  [`#MeDO`](#org9c69bd4)
        7.  [`#HiDO`](#org5550849)
        8.  [`Human_Impact`](#org4a24e2a)
        9.  [`Financial_Impact`](#org715d24b)
        10. [`°C`](#org833bcb6)
        11. [`Geo`](#org17375e9)
3.  [The Dashboard](#org4b48432)
    1.  [Why did we pick Dash?](#org31745be)
    2.  [Design](#orgfb2ecaf)
    3.  [Required files to run it](#orgca3c347)
        1.  [`app.py`](#orgc69b781)
        2.  [`assets/style.css`](#org5158cf9)
        3.  [`assets/WB_logo.jpg`](#org09d2d72)
4.  [Project Management](#orge3518ce)
    1.  [Methodology](#org9730c32)
    2.  [tools](#orgc637fad)
    3.  [How to contribute](#org80e3b33)

Todo : upload a screenshot of the delivered dashboard


<a id="org2a1b173"></a>

# Prototype/Wireframe


<a id="org36c6c72"></a>

## Features


<a id="org6875512"></a>

### Worldmap


<a id="orgd023185"></a>

### Pop-up


<a id="org3453d51"></a>

### World figure


<a id="org81956ae"></a>

# Dataset


<a id="orgcb12757"></a>

## Variables

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
<td class="org-left">'Australia and New Zealand', 'Caribbean', etc., see [M49 sub regions](https://unstats.un.org/unsd/methodology/m49/)</td>
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


<a id="org2ab3892"></a>

## Data sources


<a id="org34bf763"></a>

### `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org4972f10"></a>

### `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orgfb02003"></a>

### `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org605d0cb"></a>

### `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="orgb1dd6d2"></a>

### `#LoDO`

Todo : link to github respective workstream pages


<a id="org9c69bd4"></a>

### `#MeDO`

Todo : link to github respective workstream pages


<a id="org5550849"></a>

### `#HiDO`

Todo : link to github respective workstream pages


<a id="org4a24e2a"></a>

### `Human_Impact`

Todo : link to github respective workstream pages


<a id="org715d24b"></a>

### `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org833bcb6"></a>

### `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org17375e9"></a>

### `Geo`

Todo : explain


<a id="org4b48432"></a>

# The Dashboard


<a id="org31745be"></a>

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


<a id="orgfb2ecaf"></a>

## Design

Todo mention World Bank Visual Identity Guidelines


<a id="orgca3c347"></a>

## Required files to run it

Todo : describe files


<a id="orgc69b781"></a>

### `app.py`


<a id="org5158cf9"></a>

### `assets/style.css`


<a id="org09d2d72"></a>

### `assets/WB_logo.jpg`


<a id="orge3518ce"></a>

# Project Management


<a id="org9730c32"></a>

## Methodology


<a id="orgc637fad"></a>

## tools

-   Notion
-   Slack
-   Zoom


<a id="org80e3b33"></a>

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
