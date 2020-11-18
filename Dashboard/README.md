
# Table of Contents

1.  [<code>[1/2]</code> Prototyping](#org4c2ebe8)
    1.  [Features](#org3c2aba8)
    2.  [<code>[1/3]</code> Wireframe](#org8ce2162)
        1.  [World map](#orgfbe7ea8)
        2.  [Sub region pop-up](#org6ea920a)
        3.  [World figures](#orgf7934b0)
2.  [<code>[1/2]</code> Dataset](#org548b7da)
    1.  [Variables](#org477b9c5)
    2.  [<code>[1/11]</code> Data sources](#org728bc59)
        1.  [`Decade`](#org5d45020)
        2.  [`UN_Geosheme_Subregion`](#orgf7fe115)
        3.  [`Disaster_Type`](#org51227d3)
        4.  [`RCP`](#org7c36f97)
        5.  [`#LoDO`](#org28b2c28)
        6.  [`#MeDO`](#orgac1a876)
        7.  [`#HiDO`](#org70c0461)
        8.  [`Human_Impact`](#org076eb3d)
        9.  [`Financial_Impact`](#org93bed7b)
        10. [`°C`](#org8486bb5)
        11. [`Geo`](#org15bb36a)
3.  [<code>[0/3]</code> Development](#orgb7aea04)
    1.  [Why did we pick Dash?](#org02aca51)
    2.  [Visual identity](#org943ca59)
    3.  [Architecture](#orgcc73462)
        1.  [`app.py`](#orgfe21c61)
        2.  [`assets/style.css`](#org2c499b6)
        3.  [`assets/WB_logo.jpg`](#org1ab1876)
4.  [<code>[1/3]</code> Project Management](#org94e50c9)
    1.  [Methodology](#org8e4efe8)
    2.  [tools](#org371579a)
    3.  [How to contribute](#org193b56b)
        1.  [Setting up a new Git repository](#orga24c1a2)
        2.  [Adding or modifying owned files (`push`)](#org4897ab0)
        3.  [Submit proposed changes to review](#org31e7aac)
        4.  [Adding reviewed files (`merge`)](#org7efb1ee)

Todo : upload a screenshot of the delivered dashboard


<a id="org4c2ebe8"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="org3c2aba8"></a>

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


<a id="org8ce2162"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="orgfbe7ea8"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="org6ea920a"></a>

### BACKLOG Sub region pop-up


<a id="orgf7934b0"></a>

### BACKLOG World figures


<a id="org548b7da"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="org477b9c5"></a>

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


<a id="org728bc59"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="org5d45020"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="orgf7fe115"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="org51227d3"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org7c36f97"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org28b2c28"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="orgac1a876"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="org70c0461"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org076eb3d"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="org93bed7b"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org8486bb5"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org15bb36a"></a>

### BACKLOG `Geo`

Todo : explain


<a id="orgb7aea04"></a>

# STARTED <code>[0/3]</code> Development


<a id="org02aca51"></a>

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


<a id="org943ca59"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="orgcc73462"></a>

## BACKLOG Architecture

Todo : describe files


<a id="orgfe21c61"></a>

### `app.py`


<a id="org2c499b6"></a>

### `assets/style.css`


<a id="org1ab1876"></a>

### `assets/WB_logo.jpg`


<a id="org94e50c9"></a>

# STARTED <code>[1/3]</code> Project Management


<a id="org8e4efe8"></a>

## BACKLOG Methodology


<a id="org371579a"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="org193b56b"></a>

## DONE How to contribute


<a id="orga24c1a2"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub


<a id="org4897ab0"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="org31e7aac"></a>

### Submit proposed changes to review

When modifying an existing file, if you're not its owner, you have to submit the modifications to its owner (i.e. reviewer). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Owner GitHub name</th>
<th scope="col" class="org-left">File</th>
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

To submit changes reviewees have to do: 

    $ git add filename
    $ git commit
    $ hub pull-request -h revieweename:master -b dataforgoodfr:master -m -r reviewername -f

Where `revieweename` and `reviewername` are the GitHub names of the reviewee and the reviewer/owner.


<a id="org7efb1ee"></a>

### Adding reviewed files (`merge`)

-Reviewers have to do 

    hub merge PRurl 

Where `PRurl` is the url of the pull request.


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
