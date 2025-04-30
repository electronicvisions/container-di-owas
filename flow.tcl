#!/bin/bash
apptainer exec --bind /usr/local/share/pdk /openlane.img flow.tcl $*
