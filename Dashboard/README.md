
# Table of Contents

1.  [<code>[2/2]</code> Dataset](#orgf3318a2)
    1.  [Variables](#org4b87d7c)
    2.  [<code>[11/11]</code> Data sources](#org17ca803)
        1.  [`Decade`](#org86c8d9e)
        2.  [`UN_Geosheme_Subregion`](#orga532de0)
        3.  [`Disaster_Type`](#org8423764)
        4.  [`RCP`](#org4f95b20)
        5.  [`#LoDO`](#org6b4cbef)
        6.  [`#MeDO`](#org2760493)
        7.  [`#HiDO`](#org3ff19e9)
        8.  [`Human_Impact`](#org0ce8fa1)
        9.  [`Financial_Impact`](#org3e22228)
        10. [`°C`](#org7a3cd06)
        11. [`Geo`](#orgacbbfd1)
2.  [<code>[1/2]</code> Prototyping](#org2253b79)
    1.  [Features](#org5bb0c01)
    2.  [<code>[1/3]</code> Wireframe](#org04bd5ab)
        1.  [World map](#orgf393ab7)
        2.  [Sub region pop-up](#org338e25b)
        3.  [World figures](#orgc3adaeb)
3.  [<code>[1/3]</code> Development](#orgf8691ea)
    1.  [Why did we pick Dash?](#org3a4bd9c)
    2.  [<code>[2/3]</code> Visual identity guidelines](#orga5304b8)
        1.  [Colors](#orga0f2d79)
            -   [Primary colors](#org98d56f0)
            -   [Secondary colors](#org1f1c695)
        2.  [Fonts](#orgd93b712)
            -   [Primary fonts](#org84d5fac)
            -   [Secondary fonts](#org5d8b6da)
        3.  [Logo](#orgc56b014)
    3.  [Architecture](#orge1a4d1d)
        1.  [`app.py`](#org85c65f4)
        2.  [`assets/style.css`](#org56ae0be)
        3.  [`assets/WB_logo.jpg`](#org0e31745)
4.  [<code>[1/3]</code> Project Management](#orgaea8020)
    1.  [Methodology](#org3db95b9)
    2.  [tools](#org27b21c0)
    3.  [How to contribute](#org152e789)
        1.  [Setting up a new Git repository](#org3b44116)
        2.  [Adding or modifying owned files (`push`)](#org69ae561)
        3.  [Submit proposed changes to review](#orga56ce0a)
        4.  [Adding reviewed files (`merge`)](#org477439c)

Todo : upload a screenshot of the delivered dashboard


<a id="orgf3318a2"></a>

# DONE <code>[2/2]</code> Dataset


<a id="org4b87d7c"></a>

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


<a id="org17ca803"></a>

## DONE <code>[11/11]</code> Data sources


<a id="org86c8d9e"></a>

### DONE `Decade`

-   Source: in-house
-   Values: 
    
        Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090]
-   Notes: each value represents a decade. For example, `2020` starts with the year 2020 and ends with the year 2029.


<a id="orga532de0"></a>

### DONE `UN_Geosheme_Subregion`

-   Source: [UN Geographic Intermediary Regions](https://unstats.un.org/unsd/methodology/m49/) used by the UN Statistics Division in its publications and databases.
-   Values:
    
        UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']
-   Notes: This classification is also referred as [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme) and [UN M49](https://en.wikipedia.org/wiki/UN_M49).


<a id="org8423764"></a>

### DONE `Disaster_Type`

-   Source: in-house
-   Values:

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

-   Notes: These disasters will be respectively described in the following pages : [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes)


<a id="org4f95b20"></a>

### DONE `RCP`

-   Source: [IPCC](https://www.iiasa.ac.at/web-apps/tnt/RcpDb/dsd?Action=htmlpage&page=welcome)
-   Values:

    RCP = [2.6, 4.5, 6.0, 8.5]

-   Notes: Representative Concentration Pathways (RCP) are greenhouse gas concentration (not emissions) trajectories adopted by the IPCC. Four pathways were used for climate modeling and research for the IPCC fifth Assessment Report (AR5) in 2014. The pathways describe different climate futures, all of which are considered possible depending on the volume of greenhouse gases (GHG) emitted in the years to come. The RCPs are labelled after a possible range of radiative forcing values in the year 2100.

<img src="./Pics/rcp.png" width="300px">

![img](./Pics/rcp.png)      


<a id="org6b4cbef"></a>

### DONE `#LoDO`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) **Number of Low Disaster Occurrences** (#LoDO) see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="org2760493"></a>

### DONE `#MeDO`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) **Number of Medium Disaster Occurrences** (#MeDO) see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="org3ff19e9"></a>

### DONE `#HiDO`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) **Number of High Disaster Occurrences** (#HiDO) see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="org0ce8fa1"></a>

### DONE `Human_Impact`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) Human Impact see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="org3e22228"></a>

### DONE `Financial_Impact`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) Financial Impact see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="org7a3cd06"></a>

### DONE `°C`

-   Source: [World Bank](https://climateknowledgeportal.worldbank.org/download-data)
-   Values: Temperatures


<a id="orgacbbfd1"></a>

### DONE `Geo`

-   Source: In-house (generated by [this script](https://github.com/dataforgoodfr/batch8_worldbank/blob/master/Dashboard/scripts/ContourGeneration.ipynb))


<a id="org2253b79"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="org5bb0c01"></a>

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


<a id="org04bd5ab"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="orgf393ab7"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="org338e25b"></a>

### BACKLOG Sub region pop-up


<a id="orgc3adaeb"></a>

### BACKLOG World figures


<a id="orgf8691ea"></a>

# STARTED <code>[1/3]</code> Development


<a id="org3a4bd9c"></a>

## DONE Why did we pick [Dash](https://plotly.com/dash/)?

As we wanted to use Python to build the Dashboard we had to pick among [Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck the team decided to develop the PoC with ****Dash****

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


<a id="orga5304b8"></a>

## STARTED <code>[2/3]</code> Visual identity guidelines

We will follow World Bank's visual identity guidelines for colors and fonts.


<a id="orga0f2d79"></a>

### DONE Colors


<a id="org98d56f0"></a>

#### Primary colors

<img src="./Pics/primarycolors.png" width="700px">

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Name</th>
<th scope="col" class="org-left">Hex code</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Sapphire blue</td>
<td class="org-left">#002244</td>
</tr>


<tr>
<td class="org-left">Sky blue</td>
<td class="org-left">#009FDA</td>
</tr>


<tr>
<td class="org-left">Black</td>
<td class="org-left">#000000</td>
</tr>


<tr>
<td class="org-left">White</td>
<td class="org-left">#FFFFFF</td>
</tr>
</tbody>
</table>


<a id="org1f1c695"></a>

#### Secondary colors

<img src="./Pics/secondarycolors.png" width="700px">

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Family</th>
<th scope="col" class="org-left">Hex code</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">F05023</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">FDB714</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">2EB1C2D</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">F78D28</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">009CA7</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">00AB51</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">872B90</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">00A996</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">98252B</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">E16A2D</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">B88C1D</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">614776</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">006068</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">006450</td>
</tr>
</tbody>
</table>


<a id="orgd93b712"></a>

### DONE Fonts


<a id="org84d5fac"></a>

#### Primary fonts

<img src="./Pics/primaryfonts.png" width="400px">


<a id="org5d8b6da"></a>

#### Secondary fonts

<img src="./Pics/secondaryfonts.png" width="400px">


<a id="orgc56b014"></a>

### BACKLOG Logo


<a id="orge1a4d1d"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org85c65f4"></a>

### `app.py`


<a id="org56ae0be"></a>

### `assets/style.css`


<a id="org0e31745"></a>

### `assets/WB_logo.jpg`


<a id="orgaea8020"></a>

# STARTED <code>[1/3]</code> Project Management


<a id="org3db95b9"></a>

## BACKLOG Methodology


<a id="org27b21c0"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="org152e789"></a>

## DONE How to contribute


<a id="org3b44116"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub


<a id="org69ae561"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="orga56ce0a"></a>

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


<a id="org477439c"></a>

### Adding reviewed files (`merge`)

-Reviewers have to do 

    $ hub merge PRurl 

Where `PRurl` is the url of the pull request.


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
