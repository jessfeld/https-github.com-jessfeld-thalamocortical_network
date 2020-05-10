/* Created by Language version: 7.7.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__inak2005mut
#define _nrn_initial _nrn_initial__inak2005mut
#define nrn_cur _nrn_cur__inak2005mut
#define _nrn_current _nrn_current__inak2005mut
#define nrn_jacob _nrn_jacob__inak2005mut
#define nrn_state _nrn_state__inak2005mut
#define _net_receive _net_receive__inak2005mut 
#define _f_trates _f_trates__inak2005mut 
#define rates rates__inak2005mut 
#define states states__inak2005mut 
#define trates trates__inak2005mut 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define gnatbar _p[0]
#define gkfbar _p[1]
#define gnablock _p[2]
#define mvhalf _p[3]
#define mk _p[4]
#define hvhalf _p[5]
#define hk _p[6]
#define svhalf _p[7]
#define sk _p[8]
#define hshift _p[9]
#define sshift _p[10]
#define mtaubase _p[11]
#define htaubase _p[12]
#define htauvhalf _p[13]
#define htauk _p[14]
#define staubase _p[15]
#define stauvhalf _p[16]
#define stauk _p[17]
#define gnat _p[18]
#define gkf _p[19]
#define inat _p[20]
#define minf _p[21]
#define hinf _p[22]
#define sinf _p[23]
#define nfinf _p[24]
#define mtau _p[25]
#define htau _p[26]
#define stau _p[27]
#define nftau _p[28]
#define m _p[29]
#define h _p[30]
#define s _p[31]
#define nf _p[32]
#define enat _p[33]
#define ekf _p[34]
#define ikf _p[35]
#define mexp _p[36]
#define hexp _p[37]
#define sexp _p[38]
#define nfexp _p[39]
#define Dm _p[40]
#define Dh _p[41]
#define Ds _p[42]
#define Dnf _p[43]
#define v _p[44]
#define _g _p[45]
#define _ion_enat	*_ppvar[0]._pval
#define _ion_inat	*_ppvar[1]._pval
#define _ion_dinatdv	*_ppvar[2]._pval
#define _ion_ekf	*_ppvar[3]._pval
#define _ion_ikf	*_ppvar[4]._pval
#define _ion_dikfdv	*_ppvar[5]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_rates(void);
 static void _hoc_states(void);
 static void _hoc_trates(void);
 static void _hoc_vtrap(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 
#define NMODL_TEXT 1
#if NMODL_TEXT
static const char* nmodl_file_text;
static const char* nmodl_filename;
extern void hoc_reg_nmodl_text(int, const char*);
extern void hoc_reg_nmodl_filename(int, const char*);
#endif

 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_inak2005mut", _hoc_setdata,
 "rates_inak2005mut", _hoc_rates,
 "states_inak2005mut", _hoc_states,
 "trates_inak2005mut", _hoc_trates,
 "vtrap_inak2005mut", _hoc_vtrap,
 0, 0
};
#define vtrap vtrap_inak2005mut
 extern double vtrap( _threadargsprotocomma_ double , double );
 
static void _check_trates(double*, Datum*, Datum*, _NrnThread*); 
static void _check_table_thread(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, int _type) {
   _check_trates(_p, _ppvar, _thread, _nt);
 }
 #define _zq10 _thread[0]._pval[0]
 /* declare global and static user variables */
#define type type_inak2005mut
 double type = 0;
#define usetable usetable_inak2005mut
 double usetable = 1;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "usetable_inak2005mut", 0, 1,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gnatbar_inak2005mut", "mho/cm2",
 "gkfbar_inak2005mut", "mho/cm2",
 "mvhalf_inak2005mut", "mV",
 "hvhalf_inak2005mut", "mV",
 "svhalf_inak2005mut", "mV",
 "hshift_inak2005mut", "mV",
 "sshift_inak2005mut", "mV",
 "mtaubase_inak2005mut", "ms",
 "htaubase_inak2005mut", "ms",
 "htauvhalf_inak2005mut", "mV",
 "staubase_inak2005mut", "ms",
 "stauvhalf_inak2005mut", "mV",
 "gnat_inak2005mut", "mho/cm2",
 "gkf_inak2005mut", "mho/cm2",
 "inat_inak2005mut", "mA/cm2",
 "mtau_inak2005mut", "ms",
 "htau_inak2005mut", "ms",
 "stau_inak2005mut", "ms",
 "nftau_inak2005mut", "ms",
 0,0
};
 static double delta_t = 1;
 static double h0 = 0;
 static double m0 = 0;
 static double nf0 = 0;
 static double s0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "type_inak2005mut", &type_inak2005mut,
 "usetable_inak2005mut", &usetable_inak2005mut,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"inak2005mut",
 "gnatbar_inak2005mut",
 "gkfbar_inak2005mut",
 "gnablock_inak2005mut",
 "mvhalf_inak2005mut",
 "mk_inak2005mut",
 "hvhalf_inak2005mut",
 "hk_inak2005mut",
 "svhalf_inak2005mut",
 "sk_inak2005mut",
 "hshift_inak2005mut",
 "sshift_inak2005mut",
 "mtaubase_inak2005mut",
 "htaubase_inak2005mut",
 "htauvhalf_inak2005mut",
 "htauk_inak2005mut",
 "staubase_inak2005mut",
 "stauvhalf_inak2005mut",
 "stauk_inak2005mut",
 0,
 "gnat_inak2005mut",
 "gkf_inak2005mut",
 "inat_inak2005mut",
 "minf_inak2005mut",
 "hinf_inak2005mut",
 "sinf_inak2005mut",
 "nfinf_inak2005mut",
 "mtau_inak2005mut",
 "htau_inak2005mut",
 "stau_inak2005mut",
 "nftau_inak2005mut",
 0,
 "m_inak2005mut",
 "h_inak2005mut",
 "s_inak2005mut",
 "nf_inak2005mut",
 0,
 0};
 static Symbol* _nat_sym;
 static Symbol* _kf_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 46, _prop);
 	/*initialize range parameters*/
 	gnatbar = 0;
 	gkfbar = 0;
 	gnablock = 1;
 	mvhalf = 27.4;
 	mk = 5.4043;
 	hvhalf = 41.9;
 	hk = 6.7;
 	svhalf = 46;
 	sk = 6.6;
 	hshift = 0;
 	sshift = 0;
 	mtaubase = 0.15;
 	htaubase = 23.12;
 	htauvhalf = 77.58;
 	htauk = 43.92;
 	staubase = 140400;
 	stauvhalf = 71.3;
 	stauk = 30.9;
 	_prop->param = _p;
 	_prop->param_size = 46;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 6, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_nat_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* enat */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* inat */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dinatdv */
 prop_ion = need_memb(_kf_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[3]._pval = &prop_ion->param[0]; /* ekf */
 	_ppvar[4]._pval = &prop_ion->param[3]; /* ikf */
 	_ppvar[5]._pval = &prop_ion->param[4]; /* _ion_dikfdv */
 
}
 static void _initlists();
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _inak2005mut_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("nat", 1.0);
 	ion_reg("kf", 1.0);
 	_nat_sym = hoc_lookup("nat_ion");
 	_kf_sym = hoc_lookup("kf_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 2);
  _extcall_thread = (Datum*)ecalloc(1, sizeof(Datum));
  _thread_mem_init(_extcall_thread);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 1, _thread_mem_init);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
     _nrn_thread_table_reg(_mechtype, _check_table_thread);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 46, 6);
  hoc_register_dparam_semantics(_mechtype, 0, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "kf_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "kf_ion");
  hoc_register_dparam_semantics(_mechtype, 5, "kf_ion");
 	hoc_register_cvode(_mechtype, _ode_count, 0, 0, 0);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 inak2005mut /home/jchen/Desktop/neurosim/epilepsy/x86_64/inak2005mut.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double FARADAY = 96520.0;
 static double R = 8.3134;
 /*Top LOCAL _zq10 */
 static double *_t_minf;
 static double *_t_mexp;
 static double *_t_hinf;
 static double *_t_hexp;
 static double *_t_sinf;
 static double *_t_sexp;
 static double *_t_nfinf;
 static double *_t_nfexp;
 static double *_t_mtau;
 static double *_t_htau;
 static double *_t_stau;
 static double *_t_nftau;
static int _reset;
static char *modelname = "";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int _f_trates(_threadargsprotocomma_ double);
static int rates(_threadargsprotocomma_ double);
static int states(_threadargsproto_);
static int trates(_threadargsprotocomma_ double);
 static void _n_trates(_threadargsprotocomma_ double _lv);
 
static int  states ( _threadargsproto_ ) {
   trates ( _threadargscomma_ v ) ;
   m = m + mexp * ( minf - m ) ;
   h = h + hexp * ( hinf - h ) ;
   s = s + sexp * ( sinf - s ) ;
   nf = nf + nfexp * ( nfinf - nf ) ;
    return 0; }
 
static void _hoc_states(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 states ( _p, _ppvar, _thread, _nt );
 hoc_retpushx(_r);
}
 
static int  rates ( _threadargsprotocomma_ double _lv ) {
   double _lalpha , _lbeta , _lsum , _lvhs , _lvss ;
 _zq10 = pow( 3.0 , ( ( celsius - 6.3 ) / 10.0 ) ) ;
   _lvhs = _lv - hshift ;
   _lvss = _lv - sshift ;
   minf = 1.0 / ( 1.0 + exp ( - ( _lv + mvhalf ) / mk ) ) ;
   mtau = mtaubase ;
   hinf = 1.0 / ( 1.0 + exp ( ( _lvhs + hvhalf ) / hk ) ) ;
   htau = htaubase * exp ( - 0.5 * pow( ( ( _lvhs + htauvhalf ) / htauk ) , 2.0 ) ) ;
   sinf = 1.0 / ( 1.0 + exp ( ( _lvss + svhalf ) / sk ) ) ;
   stau = staubase * exp ( - 0.5 * pow( ( ( _lvss + stauvhalf ) / stauk ) , 2.0 ) ) ;
   _lalpha = - 0.07 * vtrap ( _threadargscomma_ ( _lv + 65.0 - 47.0 ) , - 6.0 ) ;
   _lbeta = 0.264 / exp ( ( _lv + 65.0 - 22.0 ) / 40.0 ) ;
   _lsum = _lalpha + _lbeta ;
   nftau = 1.0 / _lsum ;
   nfinf = _lalpha / _lsum ;
    return 0; }
 
static void _hoc_rates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 rates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 static double _mfac_trates, _tmin_trates;
  static void _check_trates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  static int _maktable=1; int _i, _j, _ix = 0;
  double _xi, _tmax;
  static double _sav_dt;
  static double _sav_celsius;
  if (!usetable) {return;}
  if (_sav_dt != dt) { _maktable = 1;}
  if (_sav_celsius != celsius) { _maktable = 1;}
  if (_maktable) { double _x, _dx; _maktable=0;
   _tmin_trates =  - 100.0 ;
   _tmax =  100.0 ;
   _dx = (_tmax - _tmin_trates)/200.; _mfac_trates = 1./_dx;
   for (_i=0, _x=_tmin_trates; _i < 201; _x += _dx, _i++) {
    _f_trates(_p, _ppvar, _thread, _nt, _x);
    _t_minf[_i] = minf;
    _t_mexp[_i] = mexp;
    _t_hinf[_i] = hinf;
    _t_hexp[_i] = hexp;
    _t_sinf[_i] = sinf;
    _t_sexp[_i] = sexp;
    _t_nfinf[_i] = nfinf;
    _t_nfexp[_i] = nfexp;
    _t_mtau[_i] = mtau;
    _t_htau[_i] = htau;
    _t_stau[_i] = stau;
    _t_nftau[_i] = nftau;
   }
   _sav_dt = dt;
   _sav_celsius = celsius;
  }
 }

 static int trates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv) { 
#if 0
_check_trates(_p, _ppvar, _thread, _nt);
#endif
 _n_trates(_p, _ppvar, _thread, _nt, _lv);
 return 0;
 }

 static void _n_trates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv){ int _i, _j;
 double _xi, _theta;
 if (!usetable) {
 _f_trates(_p, _ppvar, _thread, _nt, _lv); return; 
}
 _xi = _mfac_trates * (_lv - _tmin_trates);
 if (isnan(_xi)) {
  minf = _xi;
  mexp = _xi;
  hinf = _xi;
  hexp = _xi;
  sinf = _xi;
  sexp = _xi;
  nfinf = _xi;
  nfexp = _xi;
  mtau = _xi;
  htau = _xi;
  stau = _xi;
  nftau = _xi;
  return;
 }
 if (_xi <= 0.) {
 minf = _t_minf[0];
 mexp = _t_mexp[0];
 hinf = _t_hinf[0];
 hexp = _t_hexp[0];
 sinf = _t_sinf[0];
 sexp = _t_sexp[0];
 nfinf = _t_nfinf[0];
 nfexp = _t_nfexp[0];
 mtau = _t_mtau[0];
 htau = _t_htau[0];
 stau = _t_stau[0];
 nftau = _t_nftau[0];
 return; }
 if (_xi >= 200.) {
 minf = _t_minf[200];
 mexp = _t_mexp[200];
 hinf = _t_hinf[200];
 hexp = _t_hexp[200];
 sinf = _t_sinf[200];
 sexp = _t_sexp[200];
 nfinf = _t_nfinf[200];
 nfexp = _t_nfexp[200];
 mtau = _t_mtau[200];
 htau = _t_htau[200];
 stau = _t_stau[200];
 nftau = _t_nftau[200];
 return; }
 _i = (int) _xi;
 _theta = _xi - (double)_i;
 minf = _t_minf[_i] + _theta*(_t_minf[_i+1] - _t_minf[_i]);
 mexp = _t_mexp[_i] + _theta*(_t_mexp[_i+1] - _t_mexp[_i]);
 hinf = _t_hinf[_i] + _theta*(_t_hinf[_i+1] - _t_hinf[_i]);
 hexp = _t_hexp[_i] + _theta*(_t_hexp[_i+1] - _t_hexp[_i]);
 sinf = _t_sinf[_i] + _theta*(_t_sinf[_i+1] - _t_sinf[_i]);
 sexp = _t_sexp[_i] + _theta*(_t_sexp[_i+1] - _t_sexp[_i]);
 nfinf = _t_nfinf[_i] + _theta*(_t_nfinf[_i+1] - _t_nfinf[_i]);
 nfexp = _t_nfexp[_i] + _theta*(_t_nfexp[_i+1] - _t_nfexp[_i]);
 mtau = _t_mtau[_i] + _theta*(_t_mtau[_i+1] - _t_mtau[_i]);
 htau = _t_htau[_i] + _theta*(_t_htau[_i+1] - _t_htau[_i]);
 stau = _t_stau[_i] + _theta*(_t_stau[_i+1] - _t_stau[_i]);
 nftau = _t_nftau[_i] + _theta*(_t_nftau[_i+1] - _t_nftau[_i]);
 }

 
static int  _f_trates ( _threadargsprotocomma_ double _lv ) {
   double _ltinc ;
 rates ( _threadargscomma_ _lv ) ;
   _ltinc = - dt * _zq10 ;
   mexp = 1.0 - exp ( _ltinc / mtau ) ;
   hexp = 1.0 - exp ( _ltinc / htau ) ;
   sexp = 1.0 - exp ( _ltinc / stau ) ;
   nfexp = 1.0 - exp ( _ltinc / nftau ) ;
    return 0; }
 
static void _hoc_trates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 
#if 1
 _check_trates(_p, _ppvar, _thread, _nt);
#endif
 _r = 1.;
 trates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
double vtrap ( _threadargsprotocomma_ double _lx , double _ly ) {
   double _lvtrap;
 if ( fabs ( _lx / _ly ) < 1e-6 ) {
     _lvtrap = _ly * ( 1.0 - _lx / _ly / 2.0 ) ;
     }
   else {
     _lvtrap = _lx / ( exp ( _lx / _ly ) - 1.0 ) ;
     }
   
return _lvtrap;
 }
 
static void _hoc_vtrap(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r =  vtrap ( _p, _ppvar, _thread, _nt, *getarg(1) , *getarg(2) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ hoc_execerror("inak2005mut", "cannot be used with CVODE"); return 0;}
 
static void _thread_mem_init(Datum* _thread) {
   _thread[0]._pval = (double*)ecalloc(1, sizeof(double));
 }
 
static void _thread_cleanup(Datum* _thread) {
   free((void*)(_thread[0]._pval));
 }
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_nat_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_nat_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_nat_sym, _ppvar, 2, 4);
   nrn_update_ion_pointer(_kf_sym, _ppvar, 3, 0);
   nrn_update_ion_pointer(_kf_sym, _ppvar, 4, 3);
   nrn_update_ion_pointer(_kf_sym, _ppvar, 5, 4);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  h = h0;
  m = m0;
  nf = nf0;
  s = s0;
 {
   trates ( _threadargscomma_ v ) ;
   m = minf ;
   h = hinf ;
   s = sinf ;
   nf = nfinf ;
   }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];

#if 0
 _check_trates(_p, _ppvar, _thread, _nt);
#endif
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  enat = _ion_enat;
  ekf = _ion_ekf;
 initmodel(_p, _ppvar, _thread, _nt);
  }
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   gnat = gnatbar * gnablock * m * m * m * h * s ;
   inat = gnat * ( v - enat ) ;
   gkf = gkfbar * nf * nf * nf * nf ;
   ikf = gkf * ( v - ekf ) ;
   }
 _current += inat;
 _current += ikf;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  enat = _ion_enat;
  ekf = _ion_ekf;
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ double _dikf;
 double _dinat;
  _dinat = inat;
  _dikf = ikf;
 _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
  _ion_dinatdv += (_dinat - inat)/.001 ;
  _ion_dikfdv += (_dikf - ikf)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_inat += inat ;
  _ion_ikf += ikf ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}
 
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  enat = _ion_enat;
  ekf = _ion_ekf;
 {  { states(_p, _ppvar, _thread, _nt); }
  }  }}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
   _t_minf = makevector(201*sizeof(double));
   _t_mexp = makevector(201*sizeof(double));
   _t_hinf = makevector(201*sizeof(double));
   _t_hexp = makevector(201*sizeof(double));
   _t_sinf = makevector(201*sizeof(double));
   _t_sexp = makevector(201*sizeof(double));
   _t_nfinf = makevector(201*sizeof(double));
   _t_nfexp = makevector(201*sizeof(double));
   _t_mtau = makevector(201*sizeof(double));
   _t_htau = makevector(201*sizeof(double));
   _t_stau = makevector(201*sizeof(double));
   _t_nftau = makevector(201*sizeof(double));
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "/home/jchen/Desktop/neurosim/epilepsy/mods/inak2005mut.mod";
static const char* nmodl_file_text = 
  ":\n"
  ":  ichanWT2005.mod \n"
  ":\n"
  ":   Alan Goldin Lab, University of California, Irvine\n"
  ":   Jay Lickfett - Last Modified: 6 July 2005\n"
  ":\n"
  ":  This file is the Nav1.1 wild-type channel model described in:\n"
  ":\n"
  ":		Barela et al. An Epilepsy Mutation in the Sodium Channel SCN1A That Decreases\n"
  ":	    Channel Excitability.  J. Neurosci. 26(10): p. 2714-2723 \n"
  ":\n"
  ":\n"
  ":   The model is derived from the one described in:\n"
  ":\n"
  ":    	Spampanato et al. (2004a) Increased Neuronal Firing in Computer Simulations \n"
  ":		of Sodium Channel Mutations that Cause Generalized Epilepsy with Febrile Seizures Plus.\n"
  ":		Journal of Neurophysiology 91:2040-2050\n"
  ":\n"
  ":	and\n"
  ":\n"
  ":	 	Spampanato et al. (2004b) A Novel Epilepsy Mutation \n"
  ":   	in the Sodium Channel SCN1A Identifies a Cytoplasmic Domain for \n"
  ":		Beta Subunit Interaction. J. Neurosci. 24(44):10022-10034\n"
  ":\n"
  " \n"
  "\n"
  "UNITS {\n"
  "    (mA) = (milliamp)\n"
  "    (mV) = (millivolt)\n"
  "    (uF) = (microfarad)\n"
  "    (molar) = (1/liter)\n"
  "    (nA) = (nanoamp)\n"
  "    (mM) = (millimolar)\n"
  "    (um) = (micron)\n"
  "    (S) = (siemens)\n"
  "    FARADAY = 96520 (coul)\n"
  "    R = 8.3134  (joule/degC)\n"
  "\n"
  "}\n"
  "\n"
  " \n"
  "NEURON { \n"
  "    SUFFIX inak2005mut \n"
  "    USEION nat READ enat WRITE inat VALENCE 1\n"
  "    USEION kf READ ekf WRITE ikf  VALENCE 1\n"
  ":    NONSPECIFIC_CURRENT il \n"
  "    RANGE gnat, gkf\n"
  "    RANGE gnatbar, gkfbar, gnablock\n"
  ":    RANGE gl, el\n"
  "    RANGE minf, mtau, hshift, sshift, mvhalf, mk, hvhalf, hk, svhalf, sk, mtaubase, htauk, htauvhalf, htauk, stauvhalf, stauk, hinf, htau, sinf, stau, nfinf, nftau, inat, m, h, s, htaubase, staubase\n"
  "}\n"
  "\n"
  " \n"
  "INDEPENDENT {t FROM 0 TO 100 WITH 100 (ms)}\n"
  "\n"
  " \n"
  "PARAMETER {\n"
  "    \n"
  "    celsius = 6.3 (degC)\n"
  "    dt (ms) \n"
  "    enat  (mV)\n"
  "    gnatbar (mho/cm2)   \n"
  "    ekf  (mV)\n"
  "    gkfbar (mho/cm2)\n"
  "    type = 0       : 0 is WT, 1 is T875M, 2 is W1204R, 3 is R1648H, 4 is R859C\n"
  "    gnablock = 1.0\n"
  "    mvhalf = 27.4 (mV)\n"
  "    mk = 5.4043\n"
  "    hvhalf = 41.9 (mV)\n"
  "    hk = 6.7\n"
  "    svhalf = 46.0 (mV)\n"
  "    sk = 6.6\n"
  "    hshift = 0 (mV)\n"
  "    sshift = 0 (mV)\n"
  "    mtaubase = 0.15 (ms)\n"
  "    htaubase = 23.12 (ms)\n"
  "    htauvhalf = 77.58 (mV)\n"
  "    htauk = 43.92\n"
  "    staubase = 140400 (ms)\n"
  "    stauvhalf = 71.3 (mV)\n"
  "    stauk = 30.9\n"
  ":    gl (mho/cm2)    \n"
  ":    el (mV)\n"
  "}\n"
  "\n"
  "\n"
  "ASSIGNED {\n"
  "      \n"
  "    v (mV) \n"
  "    gnat (mho/cm2) \n"
  "    gkf (mho/cm2)\n"
  "    inat (mA/cm2)\n"
  "    ikf (mA/cm2)\n"
  ":    il (mA/cm2)\n"
  "    minf hinf sinf nfinf\n"
  "    mtau (ms) htau (ms) stau (ms) nftau (ms)\n"
  "    mexp hexp sexp nfexp\n"
  "} \n"
  "\n"
  "\n"
  "STATE {\n"
  "    m h s nf\n"
  "}\n"
  " \n"
  "\n"
  "BREAKPOINT {\n"
  "    SOLVE states\n"
  "    gnat = gnatbar*gnablock*m*m*m*h*s  \n"
  "    inat = gnat*(v - enat)\n"
  "    gkf = gkfbar*nf*nf*nf*nf\n"
  "    ikf = gkf*(v-ekf)\n"
  ":    il = gl*(v-el)\n"
  "}\n"
  "\n"
  " \n"
  "UNITSOFF\n"
  "\n"
  " \n"
  "INITIAL {\n"
  "\n"
  "    trates(v)\n"
  "    \n"
  "    m = minf\n"
  "    h = hinf\n"
  "    s = sinf\n"
  "\n"
  "    nf = nfinf\n"
  "    \n"
  "}\n"
  "\n"
  "\n"
  "PROCEDURE states() {        : Computes state variables m, h, s and n \n"
  "                            : at the current v and dt.        \n"
  "    trates(v)           \n"
  "\n"
  "    m = m + mexp*(minf-m)\n"
  "    h = h + hexp*(hinf-h)\n"
  "    s = s + sexp*(sinf-s)\n"
  "    nf = nf + nfexp*(nfinf-nf)\n"
  "    \n"
  "}\n"
  " \n"
  "\n"
  "LOCAL q10\n"
  "\n"
  "\n"
  "PROCEDURE rates(v (mV)) {   :Computes rate and other constants at current v.\n"
  "                            :Call once from HOC to initialize inf at resting v.\n"
  "\n"
  "    LOCAL  alpha, beta, sum, vhs, vss\n"
  "    q10 = 3^((celsius - 6.3)/10)\n"
  "    \n"
  "    vhs = v - hshift\n"
  "    vss = v - sshift\n"
  "\n"
  "    :\"m\" sodium activation system\n"
  "    minf = 1/(1+exp(-(v+mvhalf)/mk))		\n"
  "    mtau = mtaubase\n"
  "\n"
  "    :\"h\" sodium fast inactivation system\n"
  "    hinf = 1/(1+exp((vhs+hvhalf)/hk))				\n"
  "    htau = htaubase*exp(-0.5*((vhs+htauvhalf)/htauk)^2) 	\n"
  "       \n"
  "    :\"s\" sodium slow inactivation system\n"
  "    sinf = 1/(1+exp((vss+svhalf)/sk))						\n"
  "    stau = staubase*exp(-0.5*((vss+stauvhalf)/stauk)^2)	\n"
  "\n"
  "    :\"nf\" fKDR activation system				\n"
  "    alpha = -0.07*vtrap((v+65-47),-6)\n"
  "    beta = 0.264/exp((v+65-22)/40)\n"
  "    sum = alpha+beta        \n"
  "    nftau = 1/sum      \n"
  "    nfinf = alpha/sum\n"
  "}\n"
  " \n"
  "\n"
  "PROCEDURE trates(v (mV)) {  :Build table with rate and other constants at current v.\n"
  "                            :Call once from HOC to initialize inf at resting v.\n"
  "    LOCAL tinc\n"
  " \n"
  "    TABLE minf, mexp, hinf, hexp, sinf, sexp, nfinf, nfexp, mtau, htau, stau, nftau\n"
  "        DEPEND dt, celsius FROM -100 TO 100 WITH 200\n"
  "                           \n"
  "    rates(v)    : not consistently executed from here if usetable_hh == 1\n"
  "                : so don't expect the tau values to be tracking along with\n"
  "                : the inf values in hoc\n"
  "\n"
  "    tinc = -dt * q10\n"
  "    mexp = 1 - exp(tinc/mtau)\n"
  "    hexp = 1 - exp(tinc/htau)\n"
  "    sexp = 1 - exp(tinc/stau)\n"
  "    nfexp = 1 - exp(tinc/nftau)\n"
  "}\n"
  "\n"
  " \n"
  "FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.\n"
  "\n"
  "    if (fabs(x/y) < 1e-6) {\n"
  "        vtrap = y*(1 - x/y/2)\n"
  "    }else{  \n"
  "        vtrap = x/(exp(x/y) - 1)\n"
  "    }\n"
  "}\n"
  " \n"
  "\n"
  "UNITSON\n"
  "\n"
  ;
#endif
