"""Several wrappers for generating various types of plots easier."""

from .tools import pcolorgrid
from . import DEFAULT_CMAP


def ppcolormesh(ax, x, y, z, cmap=DEFAULT_CMAP, make_grid=True, **kw):
    if make_grid:
        _x, _y = pcolorgrid(x, y)
    else:
        _x, _y = x, y

    im = ax.pcolormesh(_x, _y, z, cmap=cmap, **kw)
    ax.set_xlim(_x.min(), _x.max())
    ax.set_ylim(_y.min(), _y.max())

    return im
