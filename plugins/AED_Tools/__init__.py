# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AED_Tools
                                 A QGIS plugin
 Common Editing Tools for AED
                             -------------------
        begin                : 2014-12-26
        copyright            : (C) 2014 by Wes Byne
        email                : fbyne@watergeorgia.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AED_Tools class from file AED_Tools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .AED_Edit_Tools import AED_Tools
    return AED_Tools(iface)
