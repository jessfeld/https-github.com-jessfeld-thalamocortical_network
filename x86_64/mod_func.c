#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _ampa_reg(void);
extern void _cadecay_reg(void);
extern void _gabaa_reg(void);
extern void _gabaat_reg(void);
extern void _gabab_as_reg(void);
extern void _gabab_reg(void);
extern void _gabab_v1_reg(void);
extern void _gabab_v2_reg(void);
extern void _gapJ_reg(void);
extern void _HH2_reg(void);
extern void _Ih_reg(void);
extern void _IM_reg(void);
extern void _inak2005a_reg(void);
extern void _inak2005b_reg(void);
extern void _inak2005_reg(void);
extern void _inak2005mut_reg(void);
extern void _IT2_reg(void);
extern void _IT_reg(void);
extern void _ITREcustom_reg(void);
extern void _ITTCcustom_reg(void);
extern void _kleak_reg(void);
extern void _nmda_reg(void);
extern void _vecevent_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," mods/ampa.mod");
    fprintf(stderr," mods/cadecay.mod");
    fprintf(stderr," mods/gabaa.mod");
    fprintf(stderr," mods/gabaat.mod");
    fprintf(stderr," mods/gabab_as.mod");
    fprintf(stderr," mods/gabab.mod");
    fprintf(stderr," mods/gabab_v1.mod");
    fprintf(stderr," mods/gabab_v2.mod");
    fprintf(stderr," mods/gapJ.mod");
    fprintf(stderr," mods/HH2.mod");
    fprintf(stderr," mods/Ih.mod");
    fprintf(stderr," mods/IM.mod");
    fprintf(stderr," mods/inak2005a.mod");
    fprintf(stderr," mods/inak2005b.mod");
    fprintf(stderr," mods/inak2005.mod");
    fprintf(stderr," mods/inak2005mut.mod");
    fprintf(stderr," mods/IT2.mod");
    fprintf(stderr," mods/IT.mod");
    fprintf(stderr," mods/ITREcustom.mod");
    fprintf(stderr," mods/ITTCcustom.mod");
    fprintf(stderr," mods/kleak.mod");
    fprintf(stderr," mods/nmda.mod");
    fprintf(stderr," mods/vecevent.mod");
    fprintf(stderr, "\n");
  }
  _ampa_reg();
  _cadecay_reg();
  _gabaa_reg();
  _gabaat_reg();
  _gabab_as_reg();
  _gabab_reg();
  _gabab_v1_reg();
  _gabab_v2_reg();
  _gapJ_reg();
  _HH2_reg();
  _Ih_reg();
  _IM_reg();
  _inak2005a_reg();
  _inak2005b_reg();
  _inak2005_reg();
  _inak2005mut_reg();
  _IT2_reg();
  _IT_reg();
  _ITREcustom_reg();
  _ITTCcustom_reg();
  _kleak_reg();
  _nmda_reg();
  _vecevent_reg();
}
