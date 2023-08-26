#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from osgeo import gdal, gdalconst

ds = gdal.Open('./image.tif', gdalconst.GA_ReadOnly)

print(ds.RasterXSize)
print(ds.RasterYSize)
print(ds.RasterCount)