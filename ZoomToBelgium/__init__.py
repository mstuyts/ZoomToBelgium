# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ZoomToBelgium
                                 A QGIS plugin
 A button to zoom to any of the Belgian Municipalities
                             -------------------
        begin                : 2017-09-19
        copyright            : (C) 2017 by Michel Stuyts
        email                : info@stuyts.xyz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    from .ZoomToBelgium import ZoomToBelgium
    return ZoomToBelgium(iface)
