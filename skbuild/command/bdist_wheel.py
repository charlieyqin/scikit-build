"""This module defines custom implementation of ``bdist_wheel`` setuptools
command."""

import sys

from distutils.util import get_platform

from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

from . import set_build_base_mixin
from ..utils import new_style


class bdist_wheel(set_build_base_mixin, new_style(_bdist_wheel)):
    """Custom implementation of ``bdist_wheel`` setuptools command."""

    def finalize_options(self, *args, **kwargs):
        """Ensure MacOSX wheels include ``x86_64`` instead of ``intel``."""
        if sys.platform == 'darwin' and self.plat_name is None:
            # The following code is duplicated in setuptools_wrap
            # pylint:disable=attribute-defined-outside-init
            self.plat_name = "macosx-10.6-x86_64"
        super(bdist_wheel, self).finalize_options(*args, **kwargs)
