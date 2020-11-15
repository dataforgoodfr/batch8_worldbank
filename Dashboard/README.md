# Table of Contents

1.  [<code>[0/2]</code> Prototyping](#org382e4a0)
    1.  [Features](#org655d540)
        1.  [World map](#org9413854)
        2.  [Pop-up](#orgbe5ed3b)
        3.  [World figures](#org8b27f94)
    2.  [Wireframe](#org9af7a14)
        1.  [Worldmap](#orgae6ec5b)
        2.  [Pop-up](#org2cf1f20)
        3.  [World figure](#org250bde9)
2.  [<code>[1/2]</code> Dataset](#org836de83)
    1.  [Variables](#orgaef1154)
    2.  [Data sources](#org38c57b5)
        1.  [`Decade`](#orgacd6764)
        2.  [`UN_Geosheme_Subregion`](#org450b6cc)
        3.  [`Disaster_Type`](#orgff0948c)
        4.  [`RCP`](#orgd441ad5)
        5.  [`#LoDO`](#org7c5d079)
        6.  [`#MeDO`](#orgc681b4f)
        7.  [`#HiDO`](#org95a07a2)
        8.  [`Human_Impact`](#orgbdc5180)
        9.  [`Financial_Impact`](#org2bfa9a3)
        10. [`°C`](#org70beaff)
        11. [`Geo`](#orgef742d0)
3.  [<code>[0/3]</code> Development](#org44ddc54)
    1.  [Why did we pick Dash?](#org9f545a5)
    2.  [Visual identity](#orgbfc3cd7)
    3.  [Architecture](#org30c23e7)
        1.  [`app.py`](#org9489d9c)
        2.  [`assets/style.css`](#orgbe6a2eb)
        3.  [`assets/WB_logo.jpg`](#orgc8e48fc)
4.  [<code>[0/3]</code> Project Management](#org4d03a17)
    1.  [Methodology](#orged634e9)
    2.  [tools](#orgadc9e1d)
    3.  [How to contribute](#orge30e571)

Todo : upload a screenshot of the delivered dashboard


<a id="org382e4a0"></a>

# BACKLOG <code>[0/2]</code> Prototyping


<a id="org655d540"></a>

## BACKLOG Features


<a id="org9413854"></a>

### BACKLOG World map


<a id="orgbe5ed3b"></a>

### BACKLOG Pop-up


<a id="org8b27f94"></a>

### BACKLOG World figures


<a id="org9af7a14"></a>

## BACKLOG Wireframe


<a id="orgae6ec5b"></a>

### BACKLOG Worldmap


<a id="org2cf1f20"></a>

### BACKLOG Pop-up


<a id="org250bde9"></a>

### BACKLOG World figure


<a id="org836de83"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="orgaef1154"></a>

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


<a id="org38c57b5"></a>

## STARTED Data sources


<a id="orgacd6764"></a>

### `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org450b6cc"></a>

### `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orgff0948c"></a>

### `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="orgd441ad5"></a>

### `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org7c5d079"></a>

### `#LoDO`

Todo : link to github respective workstream pages


<a id="orgc681b4f"></a>

### `#MeDO`

Todo : link to github respective workstream pages


<a id="org95a07a2"></a>

### `#HiDO`

Todo : link to github respective workstream pages


<a id="orgbdc5180"></a>

### `Human_Impact`

Todo : link to github respective workstream pages


<a id="org2bfa9a3"></a>

### `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org70beaff"></a>

### `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="orgef742d0"></a>

### `Geo`

Todo : explain


<a id="org44ddc54"></a>

# STARTED <code>[0/3]</code> Development


<a id="org9f545a5"></a>

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


<a id="orgbfc3cd7"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="org30c23e7"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org9489d9c"></a>

### `app.py`


<a id="orgbe6a2eb"></a>

### `assets/style.css`


<a id="orgc8e48fc"></a>

### `assets/WB_logo.jpg`


<a id="org4d03a17"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="orged634e9"></a>

## BACKLOG Methodology


<a id="orgadc9e1d"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="orge30e571"></a>

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
