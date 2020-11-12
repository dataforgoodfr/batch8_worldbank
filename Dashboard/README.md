
# Table of Contents

1.  [Prototype/Wireframe](#org81e9ea7)
    1.  [Features](#org3165407)
        1.  [Worldmap](#org8f2dbb4)
        2.  [Pop-up](#org52e8948)
        3.  [World figure](#orga55a996)
2.  [Dataset](#org10732bf)
    1.  [Variables](#orgf9cbb30)
    2.  [Data sources](#org8ecd002)
        1.  [`Decade`](#org62b9047)
        2.  [`UN_Geosheme_Subregion`](#org2595123)
        3.  [`Disaster_Type`](#org15fb3d8)
        4.  [`RCP`](#org99f595c)
        5.  [`#LoDO`](#org2216c84)
        6.  [`#MeDO`](#org296092c)
        7.  [`#HiDO`](#orgf2274d8)
        8.  [`Human_Impact`](#org0f73303)
        9.  [`Financial_Impact`](#org21a4ca1)
        10. [`°C`](#orgb232565)
        11. [`Geo`](#orgd54272f)
3.  [The Dashboard](#orge49ff3b)
    1.  [Why did we pick Dash?](#org9aba4f6)
    2.  [Design](#orgd34cb95)
    3.  [Required files to run it](#orge351727)
        1.  [`app.py`](#org6a4b293)
        2.  [`assets/style.css`](#orgd48f6b5)
        3.  [`assets/WB_logo.jpg`](#org0da6b09)
4.  [Project Management](#orgfb973c1)
    1.  [Methodology](#orgddf3664)
    2.  [tools](#org437ee25)
    3.  [How to contribute](#org579cdc8)

Todo : upload a screenshot of the delivered dashboard


<a id="org81e9ea7"></a>

# Prototype/Wireframe


<a id="org3165407"></a>

## Features


<a id="org8f2dbb4"></a>

### Worldmap


<a id="org52e8948"></a>

### Pop-up


<a id="orga55a996"></a>

### World figure


<a id="org10732bf"></a>

# Dataset


<a id="orgf9cbb30"></a>

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


<a id="org8ecd002"></a>

## Data sources


<a id="org62b9047"></a>

### `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org2595123"></a>

### `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="org15fb3d8"></a>

### `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org99f595c"></a>

### `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org2216c84"></a>

### `#LoDO`

Todo : link to github respective workstream pages


<a id="org296092c"></a>

### `#MeDO`

Todo : link to github respective workstream pages


<a id="orgf2274d8"></a>

### `#HiDO`

Todo : link to github respective workstream pages


<a id="org0f73303"></a>

### `Human_Impact`

Todo : link to github respective workstream pages


<a id="org21a4ca1"></a>

### `Financial_Impact`

Todo : link to github respective workstream pages


<a id="orgb232565"></a>

### `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="orgd54272f"></a>

### `Geo`

Todo : explain


<a id="orge49ff3b"></a>

# The Dashboard


<a id="org9aba4f6"></a>

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


<a id="orgd34cb95"></a>

## Design

Todo mention World Bank Visual Identity Guidelines


<a id="orge351727"></a>

## Required files to run it

Todo : describe files


<a id="org6a4b293"></a>

### `app.py`


<a id="orgd48f6b5"></a>

### `assets/style.css`


<a id="org0da6b09"></a>

### `assets/WB_logo.jpg`


<a id="orgfb973c1"></a>

# Project Management


<a id="orgddf3664"></a>

## Methodology


<a id="org437ee25"></a>

## tools

-   Notion
-   Slack
-   Zoom


<a id="org579cdc8"></a>

## How to contribute

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
    
        $ git
-   Reviewers have to do 
    
        $ git


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
