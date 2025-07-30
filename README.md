# OWAS Container Build

The OWAS container provides a reproducible build environment for the OWAS project.

We manage the dependencies using the [Spack Package Manager](https://spack.io), with the notable exceptions of _LibreLane_ and _ghdl_:
* for _ghdl_, we convert the [`ghdl/ghdl:bookworm-mcode` OCI image](https://hub.docker.com/r/ghdl/ghdl) to SIF and embed it into this container
* for _LibreLane_, we use the official nix-based build flow to build and embed a SIF image into this container

## Building

An apptainer installation guide is available here:
https://apptainer.org/docs/admin/latest/installation.html

```shell
apptainer build owas.img owas-container.def
```

Please check the [collection of common problems](https://gerrit.bioai.eu/plugins/gitiles/chip-di-owas/+/refs/heads/main/doc/CommonProblems.md) in case you encounter any issue during the build.
