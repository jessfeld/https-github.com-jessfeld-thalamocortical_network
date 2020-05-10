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
 
#define nrn_init _nrn_init__inak2005a
#define _nrn_initial _nrn_initial__inak2005a
#define nrn_cur _nrn_cur__inak2005a
#define _nrn_current _nrn_current__inak2005a
#define nrn_jacob _nrn_jacob__inak2005a
#define nrn_state _nrn_state__inak2005a
#define _net_receive _net_receive__inak2005a 
#define _f_rates _f_rates__inak2005a 
#define rates rates__inak2005a 
#define states states__inak2005a 
 
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
#define Dm _p[36]
#define Dh _p[37]
#define Ds _p[38]
#define Dnf _p[39]
#define v _p[40]
#define _g _p[41]
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
 "setdata_inak2005a", _hoc_setdata,
 "rates_inak2005a", _hoc_rates,
 "vtrap_inak2005a", _hoc_vtrap,
 0, 0
};
#define vtrap vtrap_inak2005a
 extern double vtrap( _threadargsprotocomma_ double , double );
 
static void _check_rates(double*, Datum*, Datum*, _NrnThread*); 
static void _check_table_thread(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, int _type) {
   _check_rates(_p, _ppvar, _thread, _nt);
 }
 #define _zq10 _thread[0]._pval[0]
 /* declare global and static user variables */
#define type type_inak2005a
 double type = 0;
#define usetable usetable_inak2005a
 double usetable = 1;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "usetable_inak2005a", 0, 1,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gnatbar_inak2005a", "mho/cm2",
 "gkfbar_inak2005a", "mho/cm2",
 "mvhalf_inak2005a", "mV",
 "hvhalf_inak2005a", "mV",
 "svhalf_inak2005a", "mV",
 "hshift_inak2005a", "mV",
 "sshift_inak2005a", "mV",
 "htauvhalf_inak2005a", "mV",
 "stauvhalf_inak2005a", "mV",
 "gnat_inak2005a", "mho/cm2",
 "gkf_inak2005a", "mho/cm2",
 "inat_inak2005a", "mA/cm2",
 0,0
};
 static double delta_t = 0.01;
 static double h0 = 0;
 static double m0 = 0;
 static double nf0 = 0;
 static double s0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "type_inak2005a", &type_inak2005a,
 "usetable_inak2005a", &usetable_inak2005a,
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
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[6]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"inak2005a",
 "gnatbar_inak2005a",
 "gkfbar_inak2005a",
 "gnablock_inak2005a",
 "mvhalf_inak2005a",
 "mk_inak2005a",
 "hvhalf_inak2005a",
 "hk_inak2005a",
 "svhalf_inak2005a",
 "sk_inak2005a",
 "hshift_inak2005a",
 "sshift_inak2005a",
 "mtaubase_inak2005a",
 "htaubase_inak2005a",
 "htauvhalf_inak2005a",
 "htauk_inak2005a",
 "staubase_inak2005a",
 "stauvhalf_inak2005a",
 "stauk_inak2005a",
 0,
 "gnat_inak2005a",
 "gkf_inak2005a",
 "inat_inak2005a",
 "minf_inak2005a",
 "hinf_inak2005a",
 "sinf_inak2005a",
 "nfinf_inak2005a",
 "mtau_inak2005a",
 "htau_inak2005a",
 "stau_inak2005a",
 "nftau_inak2005a",
 0,
 "m_inak2005a",
 "h_inak2005a",
 "s_inak2005a",
 "nf_inak2005a",
 0,
 0};
 static Symbol* _nat_sym;
 static Symbol* _kf_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 42, _prop);
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
 	_prop->param_size = 42;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 7, _prop);
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
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _inak2005a_reg() {
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
  hoc_register_prop_size(_mechtype, 42, 7);
  hoc_register_dparam_semantics(_mechtype, 0, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "nat_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "kf_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "kf_ion");
  hoc_register_dparam_semantics(_mechtype, 5, "kf_ion");
  hoc_register_dparam_semantics(_mechtype, 6, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 inak2005a /home/jchen/Desktop/neurosim/epilepsy/x86_64/inak2005a.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 /*Top LOCAL _zq10 */
 static double *_t_minf;
 static double *_t_hinf;
 static double *_t_sinf;
 static double *_t_nfinf;
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
static int _f_rates(_threadargsprotocomma_ double);
static int rates(_threadargsprotocomma_ double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static void _n_rates(_threadargsprotocomma_ double _lv);
 static int _slist1[4], _dlist1[4];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   rates ( _threadargscomma_ v ) ;
   Dm = ( minf - m ) / mtau ;
   Dh = ( hinf - h ) / htau ;
   Ds = ( sinf - s ) / stau ;
   Dnf = ( nfinf - nf ) / nftau ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 rates ( _threadargscomma_ v ) ;
 Dm = Dm  / (1. - dt*( ( ( ( - 1.0 ) ) ) / mtau )) ;
 Dh = Dh  / (1. - dt*( ( ( ( - 1.0 ) ) ) / htau )) ;
 Ds = Ds  / (1. - dt*( ( ( ( - 1.0 ) ) ) / stau )) ;
 Dnf = Dnf  / (1. - dt*( ( ( ( - 1.0 ) ) ) / nftau )) ;
  return 0;
}
 /*END CVODE*/
 static int states (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) { {
   rates ( _threadargscomma_ v ) ;
    m = m + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / mtau)))*(- ( ( ( minf ) ) / mtau ) / ( ( ( ( - 1.0 ) ) ) / mtau ) - m) ;
    h = h + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / htau)))*(- ( ( ( hinf ) ) / htau ) / ( ( ( ( - 1.0 ) ) ) / htau ) - h) ;
    s = s + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / stau)))*(- ( ( ( sinf ) ) / stau ) / ( ( ( ( - 1.0 ) ) ) / stau ) - s) ;
    nf = nf + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / nftau)))*(- ( ( ( nfinf ) ) / nftau ) / ( ( ( ( - 1.0 ) ) ) / nftau ) - nf) ;
   }
  return 0;
}
 static double _mfac_rates, _tmin_rates;
  static void _check_rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  static int _maktable=1; int _i, _j, _ix = 0;
  double _xi, _tmax;
  static double _sav_celsius;
  if (!usetable) {return;}
  if (_sav_celsius != celsius) { _maktable = 1;}
  if (_maktable) { double _x, _dx; _maktable=0;
   _tmin_rates =  - 100.0 ;
   _tmax =  100.0 ;
   _dx = (_tmax - _tmin_rates)/200.; _mfac_rates = 1./_dx;
   for (_i=0, _x=_tmin_rates; _i < 201; _x += _dx, _i++) {
    _f_rates(_p, _ppvar, _thread, _nt, _x);
    _t_minf[_i] = minf;
    _t_hinf[_i] = hinf;
    _t_sinf[_i] = sinf;
    _t_nfinf[_i] = nfinf;
    _t_mtau[_i] = mtau;
    _t_htau[_i] = htau;
    _t_stau[_i] = stau;
    _t_nftau[_i] = nftau;
   }
   _sav_celsius = celsius;
  }
 }

 static int rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv) { 
#if 0
_check_rates(_p, _ppvar, _thread, _nt);
#endif
 _n_rates(_p, _ppvar, _thread, _nt, _lv);
 return 0;
 }

 static void _n_rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv){ int _i, _j;
 double _xi, _theta;
 if (!usetable) {
 _f_rates(_p, _ppvar, _thread, _nt, _lv); return; 
}
 _xi = _mfac_rates * (_lv - _tmin_rates);
 if (isnan(_xi)) {
  minf = _xi;
  hinf = _xi;
  sinf = _xi;
  nfinf = _xi;
  mtau = _xi;
  htau = _xi;
  stau = _xi;
  nftau = _xi;
  return;
 }
 if (_xi <= 0.) {
 minf = _t_minf[0];
 hinf = _t_hinf[0];
 sinf = _t_sinf[0];
 nfinf = _t_nfinf[0];
 mtau = _t_mtau[0];
 htau = _t_htau[0];
 stau = _t_stau[0];
 nftau = _t_nftau[0];
 return; }
 if (_xi >= 200.) {
 minf = _t_minf[200];
 hinf = _t_hinf[200];
 sinf = _t_sinf[200];
 nfinf = _t_nfinf[200];
 mtau = _t_mtau[200];
 htau = _t_htau[200];
 stau = _t_stau[200];
 nftau = _t_nftau[200];
 return; }
 _i = (int) _xi;
 _theta = _xi - (double)_i;
 minf = _t_minf[_i] + _theta*(_t_minf[_i+1] - _t_minf[_i]);
 hinf = _t_hinf[_i] + _theta*(_t_hinf[_i+1] - _t_hinf[_i]);
 sinf = _t_sinf[_i] + _theta*(_t_sinf[_i+1] - _t_sinf[_i]);
 nfinf = _t_nfinf[_i] + _theta*(_t_nfinf[_i+1] - _t_nfinf[_i]);
 mtau = _t_mtau[_i] + _theta*(_t_mtau[_i+1] - _t_mtau[_i]);
 htau = _t_htau[_i] + _theta*(_t_htau[_i+1] - _t_htau[_i]);
 stau = _t_stau[_i] + _theta*(_t_stau[_i+1] - _t_stau[_i]);
 nftau = _t_nftau[_i] + _theta*(_t_nftau[_i+1] - _t_nftau[_i]);
 }

 
static int  _f_rates ( _threadargsprotocomma_ double _lv ) {
   double _lalpha , _lbeta , _lsum , _lvhs , _lvss ;
 _zq10 = pow( 3.0 , ( ( celsius - 6.3 ) / 10.0 ) ) ;
   _lvhs = _lv - hshift ;
   _lvss = _lv - sshift ;
   minf = 1.0 / ( 1.0 + exp ( - ( _lv + mvhalf ) / mk ) ) ;
   mtau = mtaubase ;
   hinf = 1.0 / ( 1.0 + exp ( ( _lvhs + hvhalf ) / hk ) ) ;
   htau = htaubase * exp ( - 0.5 * pow( ( ( _lv + htauvhalf ) / htauk ) , 2.0 ) ) ;
   sinf = 1.0 / ( 1.0 + exp ( ( _lvss + svhalf ) / sk ) ) ;
   stau = staubase * exp ( - 0.5 * pow( ( ( _lv + stauvhalf ) / stauk ) , 2.0 ) ) ;
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
 
#if 1
 _check_rates(_p, _ppvar, _thread, _nt);
#endif
 _r = 1.;
 rates ( _p, _ppvar, _thread, _nt, *getarg(1) );
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
 
static int _ode_count(int _type){ return 4;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  enat = _ion_enat;
  ekf = _ion_ekf;
     _ode_spec1 (_p, _ppvar, _thread, _nt);
   }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 4; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  enat = _ion_enat;
  ekf = _ion_ekf;
 _ode_matsol_instance1(_threadargs_);
 }}
 
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
   rates ( _threadargscomma_ v ) ;
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
 _check_rates(_p, _ppvar, _thread, _nt);
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
 {   states(_p, _ppvar, _thread, _nt);
  }  }}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(m) - _p;  _dlist1[0] = &(Dm) - _p;
 _slist1[1] = &(h) - _p;  _dlist1[1] = &(Dh) - _p;
 _slist1[2] = &(s) - _p;  _dlist1[2] = &(Ds) - _p;
 _slist1[3] = &(nf) - _p;  _dlist1[3] = &(Dnf) - _p;
   _t_minf = makevector(201*sizeof(double));
   _t_hinf = makevector(201*sizeof(double));
   _t_sinf = makevector(201*sizeof(double));
   _t_nfinf = makevector(201*sizeof(double));
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
static const char* nmodl_filename = "/home/jchen/Desktop/neurosim/epilepsy/mods/inak2005a.mod";
static const char* nmodl_file_text = 
  ":  ichanWT2005.mod \n"
  ":   Alan Goldin Lab, University of California, Irvine; Jay Lickfett - Last Modified: 6 July 2005\n"
  ":  This file is the Nav1.1 wild-type channel model described in:\n"
  ":		Barela et al. An Epilepsy Mutation in the Sodium Channel SCN1A That Decreases Channel Excitability.  J. Neurosci. 26(10): p. 2714-2723 \n"
  ": Spampanato et al. 2004 Increased Neuronal Firing in Computer Simulations of Sodium Channel Mutations that Cause Generalized Epilepsy with Febrile Seizures Plus. J Neurophys 91:2040-2050\n"
  ": Spampanato et al. 2004 A Novel Epilepsy Mutation in the Sodium Channel SCN1A Identifies a Cytoplasmic Domain for Beta Subunit Interaction. J. Neurosci. 24:10022-10034\n"
  "\n"
  "NEURON { \n"
  "    SUFFIX inak2005a\n"
  "    USEION nat READ enat WRITE inat CHARGE 1\n"
  "    USEION kf READ ekf WRITE ikf  CHARGE 1\n"
  "    RANGE gnat, gkf\n"
  "    RANGE gnatbar, gkfbar, gnablock\n"
  "    RANGE minf, mtau, hshift, sshift, mvhalf, mk, hvhalf, hk, svhalf, sk, mtaubase, htauk, htauvhalf, htauk, stauvhalf, stauk, hinf, htau, sinf, stau, nfinf, nftau, inat\n"
  "    RANGE m, h, s, htaubase, staubase\n"
  "}\n"
  "\n"
  "PARAMETER {\n"
  "    celsius\n"
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
  "    mtaubase = 0.15\n"
  "    htaubase = 23.12\n"
  "    htauvhalf = 77.58 (mV)\n"
  "    htauk = 43.92\n"
  "    staubase = 140400\n"
  "    stauvhalf = 71.3 (mV)\n"
  "    stauk = 30.9\n"
  "}\n"
  "\n"
  "ASSIGNED {\n"
  "    v (mV) \n"
  "    gnat (mho/cm2) \n"
  "    gkf (mho/cm2)\n"
  "    inat (mA/cm2)\n"
  "    ikf (mA/cm2)\n"
  "    minf hinf sinf nfinf\n"
  "    mtau htau stau nftau\n"
  "} \n"
  "\n"
  "STATE { m h s nf }\n"
  " \n"
  "BREAKPOINT {\n"
  "    SOLVE states METHOD cnexp\n"
  "    gnat = gnatbar*gnablock*m*m*m*h*s  \n"
  "    inat = gnat*(v - enat)\n"
  "    gkf = gkfbar*nf*nf*nf*nf\n"
  "    ikf = gkf*(v-ekf)\n"
  "}\n"
  "\n"
  "INITIAL {\n"
  "    rates(v)\n"
  "    m = minf\n"
  "    h = hinf\n"
  "    s = sinf\n"
  "    nf = nfinf\n"
  "}\n"
  "\n"
  "DERIVATIVE states {\n"
  "    rates(v)           \n"
  "    m' = (minf - m) / mtau\n"
  "    h' = (hinf - h) / htau\n"
  "    s' = (sinf - s) / stau\n"
  "    nf' = (nfinf - nf) / nftau\n"
  "}\n"
  " \n"
  "LOCAL q10\n"
  "\n"
  "PROCEDURE rates(v (mV)) {   :Computes rate and other constants at current v. Call once from HOC to initialize inf at resting v.\n"
  "    LOCAL  alpha, beta, sum, vhs, vss\n"
  "    TABLE minf, hinf, sinf,  nfinf, mtau, htau, stau, nftau DEPEND celsius FROM -100 TO 100 WITH 200\n"
  "    q10 = 3^((celsius - 6.3)/10)\n"
  "    vhs = v - hshift\n"
  "    vss = v - sshift\n"
  "    :\"m\" sodium activation system\n"
  "    minf = 1/(1+exp(-(v+mvhalf)/mk))		\n"
  "    mtau = mtaubase\n"
  "\n"
  "    :\"h\" sodium fast inactivation system\n"
  "    hinf = 1/(1+exp((vhs+hvhalf)/hk))				\n"
  "    htau = htaubase*exp(-0.5*((v+htauvhalf)/htauk)^2) 	\n"
  "       \n"
  "    :\"s\" sodium slow inactivation system\n"
  "    sinf = 1/(1+exp((vss+svhalf)/sk))						\n"
  "    stau = staubase*exp(-0.5*((v+stauvhalf)/stauk)^2)	\n"
  "\n"
  "    :\"nf\" fKDR activation system				\n"
  "    alpha = -0.07*vtrap((v+65-47),-6)\n"
  "    beta = 0.264/exp((v+65-22)/40)\n"
  "    sum = alpha+beta        \n"
  "    nftau = 1/sum      \n"
  "    nfinf = alpha/sum\n"
  "}\n"
  " \n"
  "FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.\n"
  "    if (fabs(x/y) < 1e-6) {\n"
  "        vtrap = y*(1 - x/y/2)\n"
  "    }else{  \n"
  "        vtrap = x/(exp(x/y) - 1)\n"
  "    }\n"
  "}\n"
  ;
#endif
