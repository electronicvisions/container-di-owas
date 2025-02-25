# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySpice(PythonPackage):
    """Simulate electronic circuit using Python and the Ngspice / Xyce
    simulators"""

    homepage = "https://pyspice.fabrice-salvaire.fr"
    pypi = "pyspice/PySpice-1.5.tar.gz"

    version("1.5", sha256="d28448accad98959e0f5932af8736e90a1f3f9ff965121c6881d24cdfca23d22")

    depends_on("py-setuptools", type="build")

    depends_on("py-pyyaml@5.3:", type=("build", "run"))
    depends_on("py-cffi@1.14:", type=("build", "run"))
    depends_on("py-matplotlib@3.2:", type=("build", "run"))
    depends_on("py-numpy@1.18:", type=("build", "run"))
    depends_on("py-ply@3.11:", type=("build", "run"))
    depends_on("py-scipy@1.4:", type=("build", "run"))

    depends_on("ngspice build=lib +xspice", type=("build", "run"))
    depends_on("xyce", type=("build", "run"))
