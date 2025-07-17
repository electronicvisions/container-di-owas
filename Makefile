owas-container.img: librelane.img ghdl.img

ghdl.img:
        @SINGULARITY_BIND="" APPTAINER_BIND="" apptainer pull ghdl.img docker://ghdl/ghdl:bookworm-mcode

%.img : %.def
	$(ECHO) ### building $@ from $< ###
	@SINGULARITY_BIND="" APPTAINER_BIND="" apptainer build --fakeroot $@ $<
