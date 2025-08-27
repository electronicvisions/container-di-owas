# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyOnnxIr(PythonPackage):
    """Efficient in-memory representation for ONNX"""

    homepage = "https://onnx.ai/ir-py/"
    pypi = "onnx-ir/onnx_ir-0.1.7.tar.gz"

    license("Apache-2.0", checked_by="muffgaga")

    version("0.1.7", sha256="4734b7587807ca657158b042c138879c3f454756fae74e949f6c99f0107d8df6")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools@77:", type="build")
    depends_on("py-typing-extensions@4.10:", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-onnx@1.16:", type=("build", "run"))
    depends_on("py-ml-dtypes", type=("build", "run"))
