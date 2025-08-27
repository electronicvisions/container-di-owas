# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyOnnxscript(PythonPackage):
    """Naturally author ONNX functions and models using a subset of Python"""

    homepage = "https://microsoft.github.io/onnxscript"
    pypi = "onnxscript/onnxscript-0.4.0.tar.gz"

    license("MIT", checked_by="muffgaga")

    version("0.4.0", sha256="de618eeb6e0c57f5a70f85909ab1f829cbb2053ad55f8f2fcc2701fa29b7adfc")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-packaging", type=("build"))
    depends_on("py-typing-extensions@4.10:", type="build")

    depends_on("py-ml-dtypes", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-onnx-ir@0.1.7:1", type=("build", "run"))
    depends_on("py-onnx@1.16:", type=("build", "run"))
