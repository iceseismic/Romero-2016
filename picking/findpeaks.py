# encoding: utf-8
'''
@author:     Jose Emilio Romero Lopez

@copyright:  2013 organization_name. All rights reserved.

@license:    LGPL

@contact:    jemromerol@gmail.com

  This file is part of AMPAPicker.

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import numpy as np
from scipy import signal


def find_peaks(x, threshold=None, order=1):
    """"""
    if threshold is not None:
        event_peaks = signal.argrelmax(x, order=int(order))[0]
        if event_peaks.size > 0:
            return event_peaks[x[event_peaks] > threshold]
        return event_peaks
    else:
        if x.size > 0:
            return np.array([np.argmax(x)])
        return np.array([])
