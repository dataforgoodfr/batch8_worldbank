
# Table of Contents

1.  [<code>[1/2]</code> Prototyping](#org327b1a2)
    1.  [Features](#orgdab6759)
    2.  [<code>[1/3]</code> Wireframe](#orgad15512)
        1.  [World map](#orge7ba55a)
        2.  [Sub region pop-up](#orgd327e99)
        3.  [World figures](#org4e37bad)
2.  [<code>[1/2]</code> Dataset](#org6e780bc)
    1.  [Variables](#org3fa7b9d)
    2.  [<code>[1/11]</code> Data sources](#org1765aa1)
        1.  [`Decade`](#org02d678f)
        2.  [`UN_Geosheme_Subregion`](#org1b32acc)
        3.  [`Disaster_Type`](#orgb2ad901)
        4.  [`RCP`](#org9928003)
        5.  [`#LoDO`](#org9ffb017)
        6.  [`#MeDO`](#org347b08e)
        7.  [`#HiDO`](#orgb95a7f9)
        8.  [`Human_Impact`](#org136c670)
        9.  [`Financial_Impact`](#orgf121c93)
        10. [`°C`](#orgbd12210)
        11. [`Geo`](#org75f7e90)
3.  [<code>[0/3]</code> Development](#org5e561fb)
    1.  [Why did we pick Dash?](#org0a68c13)
    2.  [Visual identity](#org39380cc)
    3.  [Architecture](#org7301307)
        1.  [`app.py`](#org4df560a)
        2.  [`assets/style.css`](#org5e1d4c7)
        3.  [`assets/WB_logo.jpg`](#orga237f10)
4.  [<code>[0/3]</code> Project Management](#orgdff2f41)
    1.  [Methodology](#org45fa989)
    2.  [tools](#org65e8cb8)
    3.  [How to contribute](#org6a617c3)

Todo : upload a screenshot of the delivered dashboard


<a id="org327b1a2"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="orgdab6759"></a>

## DONE Features

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Feature name</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Main layout</td>
<td class="org-left">Organise features and widgets on the main page</td>
</tr>


<tr>
<td class="org-left">World map</td>
<td class="org-left">Displays the world map, with UN sub regions</td>
</tr>


<tr>
<td class="org-left">World map dataviz</td>
<td class="org-left">Displays data on the worldmap, with a legend</td>
</tr>


<tr>
<td class="org-left">RCP thermometer</td>
<td class="org-left">To choose among the 4 RCP</td>
</tr>


<tr>
<td class="org-left">Disaster toggle</td>
<td class="org-left">To choose among 1 over 3 disaster type</td>
</tr>


<tr>
<td class="org-left">Impact toggle</td>
<td class="org-left">To choose between human or financial impact</td>
</tr>


<tr>
<td class="org-left">Selectable timeframe</td>
<td class="org-left">To choose from 1 to 20 decades</td>
</tr>


<tr>
<td class="org-left">Sub region mouseover</td>
<td class="org-left">Mouseover on a sub region triggers a popup</td>
</tr>


<tr>
<td class="org-left">Sub region popup</td>
<td class="org-left">Shows region's figures</td>
</tr>


<tr>
<td class="org-left">World figures</td>
<td class="org-left">Shows world figures</td>
</tr>


<tr>
<td class="org-left">World figures expand</td>
<td class="org-left">Button that triggers world figures popup</td>
</tr>


<tr>
<td class="org-left">World figures popup</td>
<td class="org-left">Expends world figures additional figures</td>
</tr>


<tr>
<td class="org-left">Play/Pause toggle</td>
<td class="org-left">launch a per decade animation on the world map</td>
</tr>
</tbody>
</table>


<a id="orgad15512"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="orge7ba55a"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="orgd327e99"></a>

### BACKLOG Sub region pop-up


<a id="org4e37bad"></a>

### BACKLOG World figures


<a id="org6e780bc"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="org3fa7b9d"></a>

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


<a id="org1765aa1"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="org02d678f"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org1b32acc"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orgb2ad901"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org9928003"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org9ffb017"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="org347b08e"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="orgb95a7f9"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org136c670"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="orgf121c93"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="orgbd12210"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org75f7e90"></a>

### BACKLOG `Geo`

Todo : explain


<a id="org5e561fb"></a>

# STARTED <code>[0/3]</code> Development


<a id="org0a68c13"></a>

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


<a id="org39380cc"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="org7301307"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org4df560a"></a>

### `app.py`


<a id="org5e1d4c7"></a>

### `assets/style.css`


<a id="orga237f10"></a>

### `assets/WB_logo.jpg`


<a id="orgdff2f41"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="org45fa989"></a>

## BACKLOG Methodology


<a id="org65e8cb8"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="org6a617c3"></a>

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
    
        hub pull-request -h revieweename:master -b dataforgoodfr:master -m -r reviewername -f
    
    Where `revieweename` and `reviewername` are the names of the reviewee and the reviewer on GitHub
-   Reviewers have to do 
    
        hub merge PRurl 
    
    Where `PRurl` is the url of the pull request


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
