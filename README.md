# OWAS Container Build

The OWAS container provides a reproducible build environment for this project.

We manage the dependencies using the [Spack Package Manager](https://spack.io), with the notable exception of OpenLane:
here, we extend the [OCI image provided by efabless](https://hub.docker.com/r/efabless/openlane) by the PDK installation and embed it into the OWAS container.

## Building

An apptainer installation guide is available here:
https://apptainer.org/docs/admin/latest/installation.html

```shell
apptainer build owas.img owas-container.def
```

Please check the [collection of common problems](../../doc/CommonProblems.md) in case you encounter any issue during the build.
