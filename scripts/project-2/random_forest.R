rm(list=ls(all=TRUE))

# install.packages("raster", dependencies = TRUE)
# install.packages("sf", dependencies = TRUE)
# install.packages("tidyverse", dependencies = TRUE)
# install.packages("exactextractr")

library(sf)
library(raster)
library(tidyverse)
library(exactextractr)

setwd("~/Tresors/teaching/project_folder/data/")

### Import Administrative Boundaries ###

# lbr_int  <- read_sf("gadm36_LBR_0.shp")
# lbr_adm1  <- read_sf("gadm36_LBR_1.shp")
# lbr_adm2  <- read_sf("gadm36_LBR_2.shp")
lbr_adm3  <- read_sf("gadm36_LBR_3.shp")

### Import Land Use Land Cover, Night Time Lights and Settlements Covariates ###

f <- list.files(pattern="lbr_esaccilc_dst", recursive=TRUE)
lulc <- stack(lapply(f, function(i) raster(i, band=1)))

nms <- sub("_100m_2015.tif", "", sub("lbr_esaccilc_", "", f))
names(lulc) <- nms

topo <- raster("lbr_srtm_topo_100m.tif")
slope <- raster("lbr_srtm_slope_100m.tif")
ntl <- raster("lbr_viirs_100m_2015.tif")
pop19 <- raster("lbr_ppp_2019.tif")

# add hrsl

lulc <- addLayer(lulc, topo, slope, ntl, pop19)

names(lulc)[c(1,10:13)] <- c("water","topo","slope", "ntl", "pop19")

lulc_adm3 <- exact_extract(lulc, lbr_adm3, fun=c('sum', 'mean'))

