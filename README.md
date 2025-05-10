# CI4FAIR Workshop, Purdue University, August 4-5, 2025

This is a tutorial explaning how to develop Geospatial **E**xtensible **D**ata **F**ramework (**GeoEDF**) workflows.

GeoEDF is a Python-based extensible data framework designed to simplify data wrangling in geospatial research workflows. GeoEDF enables researchers 
to define scientific workflows as a logical sequence of data acquisition and processing steps. Reusable building blocks termed _data 
connectors_ and _data processors_ implement data acquisition from various repositories using various data access protocols, and a range 
of domain-agnostic or domain-specific geospatial processing operations respectively. These open source connectors and processors are community 
contributed and managed in the GeoEDF GitHub repositories. A CI/CD pipeline automatically packages these connectors and processors as Singularity 
containers in order to manage their respective software dependencies. Researchers can use any of these existing connectors or processors; 
or else build and contribute their own for use in their workflows or by others.

The GeoEDF _framework_ defines the syntax and semantics of connectors and processors, while the _engine_ implements the validation, transformation, 
job planning, and execution of declarative GeoEDF workflows encoded in YAML syntax. GeoEDF utilizes the Pegasus Workflow Management System (WMS) 
for planning and executing GeoEDF workflows on diverse compute resources (local machine, Condor pool, or HPC system).

This tutorial is self-contained and will illustrate the intuitive workflow YAML syntax, and the use of the GeoEDF workflow engine to execute 
these workflows. Specifically, this demo includes the following two Jupyter notebooks:

1. A notebook demonstrating a hydrologic data preparation workflow that utilizes pre-existing data connectors and processors to acquire MODIS data from a NASA DAAC and aggregate it across each of the polygons in a given watershed shapefile.
2. A notebook demonstrating how a new Shapefile2GeoJSON processor can be built and subsequently used in a new workflow that post-processes the resulting shapefile from step 1 to make it easier to visualize using map libraries like Folium.

This tutorial is designed to be launched in a Jupyter notebook environment that contains the various GeoEDF libraries and dependencies such as Pegasus WMS and Condor.

## Usage

[Launch tutorial notebook](https://jupyter.iguidedev.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fgeoedf%2FCI4FAIR&urlpath=lab%2Ftree%2FCI4FAIR%2FGeoEDF_Tutorial_01.ipynb+&branch=main)

## Supplemental Information

1. A paper describing GeoEDF can be found [here](https://dl.acm.org/doi/abs/10.1145/3311790.3396631). 
2. Currently contributed connectors and processors can be found [here](https://geoedf.readthedocs.io/).
