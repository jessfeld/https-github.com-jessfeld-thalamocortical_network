/* Created by Language version: 7.7.0 */
/* NOT VECTORIZED */
#define NRN_VECTORIZED 0
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
 
#define nrn_init _nrn_init__GABAb_S_v2
#define _nrn_initial _nrn_initial__GABAb_S_v2
#define nrn_cur _nrn_cur__GABAb_S_v2
#define _nrn_current _nrn_current__GABAb_S_v2
#define nrn_jacob _nrn_jacob__GABAb_S_v2
#define nrn_state _nrn_state__GABAb_S_v2
#define _net_receive _net_receive__GABAb_S_v2 
#define bindkin bindkin__GABAb_S_v2 
 
#define _threadargscomma_ /**/
#define _threadargsprotocomma_ /**/
#define _threadargs_ /**/
#define _threadargsproto_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define Cmax _p[0]
#define Cdur _p[1]
#define Prethresh _p[2]
#define Deadtime _p[3]
#define K1 _p[4]
#define K2 _p[5]
#define K3 _p[6]
#define K4 _p[7]
#define KD _p[8]
#define n _p[9]
#define Erev _p[10]
#define gmax _p[11]
#define i _p[12]
#define g _p[13]
#define C _p[14]
#define lastrelease _p[15]
#define TimeCount _p[16]
#define R _p[17]
#define G _p[18]
#define Gn _p[19]
#define DR _p[20]
#define DG _p[21]
#define _g _p[22]
#define _tsav _p[23]
#define _nd_area  *_ppvar[0]._pval
#define pre	*_ppvar[2]._pval
#define _p_pre	_ppvar[2]._pval
 
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
 static int hoc_nrnpointerindex =  2;
 /* external NEURON variables */
 /* declaration of user functions */
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

 extern Prop* nrn_point_prop_;
 static int _pointtype;
 static void* _hoc_create_pnt(_ho) Object* _ho; { void* create_point_process();
 return create_point_process(_pointtype, _ho);
}
 static void _hoc_destroy_pnt();
 static double _hoc_loc_pnt(_vptr) void* _vptr; {double loc_point_process();
 return loc_point_process(_pointtype, _vptr);
}
 static double _hoc_has_loc(_vptr) void* _vptr; {double has_loc_point();
 return has_loc_point(_vptr);
}
 static double _hoc_get_loc_pnt(_vptr)void* _vptr; {
 double get_loc_point_process(); return (get_loc_point_process(_vptr));
}
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata(void* _vptr) { Prop* _prop;
 _prop = ((Point_process*)_vptr)->_prop;
   _setdata(_prop);
 }
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 0,0
};
 static Member_func _member_func[] = {
 "loc", _hoc_loc_pnt,
 "has_loc", _hoc_has_loc,
 "get_loc", _hoc_get_loc_pnt,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "Cmax", "mM",
 "Cdur", "ms",
 "Deadtime", "ms",
 "K1", "/ms",
 "K2", "/ms",
 "K3", "/ms",
 "K4", "/ms",
 "Erev", "mV",
 "gmax", "umho",
 "i", "nA",
 "g", "umho",
 "C", "mM",
 "lastrelease", "ms",
 "TimeCount", "ms",
 0,0
};
 static double G0 = 0;
 static double R0 = 0;
 static double delta_t = 1;
 static double v = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
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
 static void _hoc_destroy_pnt(_vptr) void* _vptr; {
   destroy_point_process(_vptr);
}
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[4]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"GABAb_S_v2",
 "Cmax",
 "Cdur",
 "Prethresh",
 "Deadtime",
 "K1",
 "K2",
 "K3",
 "K4",
 "KD",
 "n",
 "Erev",
 "gmax",
 0,
 "i",
 "g",
 "C",
 "lastrelease",
 "TimeCount",
 0,
 "R",
 "G",
 0,
 "pre",
 0};
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
  if (nrn_point_prop_) {
	_prop->_alloc_seq = nrn_point_prop_->_alloc_seq;
	_p = nrn_point_prop_->param;
	_ppvar = nrn_point_prop_->dparam;
 }else{
 	_p = nrn_prop_data_alloc(_mechtype, 24, _prop);
 	/*initialize range parameters*/
 	Cmax = 0.5;
 	Cdur = 0.3;
 	Prethresh = 0;
 	Deadtime = 1;
 	K1 = 0.52;
 	K2 = 0.0013;
 	K3 = 0.098;
 	K4 = 0.033;
 	KD = 100;
 	n = 4;
 	Erev = -95;
 	gmax = 0;
  }
 	_prop->param = _p;
 	_prop->param_size = 24;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 5, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 
#define _tqitem &(_ppvar[3]._pvoid)
 static void _net_receive(Point_process*, double*, double);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _gabab_v2_reg() {
	int _vectorized = 0;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex, 0,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 24, 5);
  hoc_register_dparam_semantics(_mechtype, 0, "area");
  hoc_register_dparam_semantics(_mechtype, 1, "pntproc");
  hoc_register_dparam_semantics(_mechtype, 2, "pointer");
  hoc_register_dparam_semantics(_mechtype, 3, "netsend");
  hoc_register_dparam_semantics(_mechtype, 4, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 pnt_receive[_mechtype] = _net_receive;
 pnt_receive_size[_mechtype] = 2;
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 GABAb_S_v2 /home/jchen/Desktop/neurosim/epilepsy/x86_64/gabab_v2.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "simple GABAb receptors";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[2], _dlist1[2];
 static int bindkin(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 () {_reset=0;
 {
   DR = K1 * C * ( 1.0 - R ) - K2 * R ;
   DG = K3 * R - K4 * G ;
   }
 return _reset;
}
 static int _ode_matsol1 () {
 DR = DR  / (1. - dt*( ( K1 * C )*( ( ( - 1.0 ) ) ) - ( K2 )*( 1.0 ) )) ;
 DG = DG  / (1. - dt*( ( - ( K4 )*( 1.0 ) ) )) ;
  return 0;
}
 /*END CVODE*/
 static int bindkin () {_reset=0;
 {
    R = R + (1. - exp(dt*(( K1 * C )*( ( ( - 1.0 ) ) ) - ( K2 )*( 1.0 ))))*(- ( ( ( K1 )*( C ) )*( ( 1.0 ) ) ) / ( ( ( K1 )*( C ) )*( ( ( - 1.0 ) ) ) - ( K2 )*( 1.0 ) ) - R) ;
    G = G + (1. - exp(dt*(( - ( K4 )*( 1.0 ) ))))*(- ( ( K3 )*( R ) ) / ( ( - ( K4 )*( 1.0 ) ) ) - G) ;
   }
  return 0;
}
 
static void _net_receive (_pnt, _args, _lflag) Point_process* _pnt; double* _args; double _lflag; 
{    _p = _pnt->_prop->param; _ppvar = _pnt->_prop->dparam;
  if (_tsav > t){ extern char* hoc_object_name(); hoc_execerror(hoc_object_name(_pnt->ob), ":Event arrived out of order. Must call ParallelContext.set_maxstep AFTER assigning minimum NetCon.delay");}
 _tsav = t;   if (_lflag == 1. ) {*(_tqitem) = 0;}
 {
   if ( _args[1] ) {
     _args[1] = 0.0 ;
     C = 0.0 ;
     }
   else {
     if ( _args[0]  == 0.0 ) {
       C = 0.0 ;
       }
     else {
       C = Cmax ;
       _args[1] = 1.0 ;
       net_send ( _tqitem, _args, _pnt, t +  Cdur , _args[1] ) ;
       }
     }
   } }
 
static int _ode_count(int _type){ return 2;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
     _ode_spec1 ();
 }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 2; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 ();
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
 _ode_matsol_instance1(_threadargs_);
 }}

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
  G = G0;
  R = R0;
 {
   C = 0.0 ;
   lastrelease = - 9e9 ;
   R = 0.0 ;
   G = 0.0 ;
   TimeCount = - 1.0 ;
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _tsav = -1e20;
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
 initmodel();
}}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   Gn = pow( G , n ) ;
   g = gmax * Gn / ( Gn + KD ) ;
   i = g * ( v - Erev ) ;
   }
 _current += i;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 _g = _nrn_current(_v + .001);
 	{ _rhs = _nrn_current(_v);
 	}
 _g = (_g - _rhs)/.001;
 _g *=  1.e2/(_nd_area);
 _rhs *= 1.e2/(_nd_area);
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 { error =  bindkin();
 if(error){fprintf(stderr,"at line 147 in file gabab_v2.mod:\n	SOLVE bindkin METHOD cnexp\n"); nrn_complain(_p); abort_run(error);}
 }}}

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(R) - _p;  _dlist1[0] = &(DR) - _p;
 _slist1[1] = &(G) - _p;  _dlist1[1] = &(DG) - _p;
_first = 0;
}

#if NMODL_TEXT
static const char* nmodl_filename = "/home/jchen/Desktop/neurosim/epilepsy/mods/gabab_v2.mod";
static const char* nmodl_file_text = 
  ": $Id: gababS.mod,v 1.4 2004/06/17 18:38:24 billl Exp $\n"
  "TITLE simple GABAb receptors\n"
  "\n"
  "COMMENT\n"
  "-----------------------------------------------------------------------------\n"
  "\n"
  "	Kinetic model of GABA-B receptors\n"
  "	=================================\n"
  "\n"
  "  MODEL OF SECOND-ORDER G-PROTEIN TRANSDUCTION AND FAST K+ OPENING\n"
  "  WITH COOPERATIVITY OF G-PROTEIN BINDING TO K+ CHANNEL\n"
  "\n"
  "  PULSE OF TRANSMITTER\n"
  "\n"
  "  SIMPLE KINETICS WITH NO DESENSITIZATION\n"
  "\n"
  "	Features:\n"
  "\n"
  "  	  - peak at 100 ms; time course fit to Tom Otis' PSC\n"
  "	  - SUMMATION (psc is much stronger with bursts)\n"
  "\n"
  "\n"
  "	Approximations:\n"
  "\n"
  "	  - single binding site on receptor	\n"
  "	  - model of alpha G-protein activation (direct) of K+ channel\n"
  "	  - G-protein dynamics is second-order; simplified as follows:\n"
  "		- saturating receptor\n"
  "		- no desensitization\n"
  "		- Michaelis-Menten of receptor for G-protein production\n"
  "		- \"resting\" G-protein is in excess\n"
  "		- Quasi-stat of intermediate enzymatic forms\n"
  "	  - binding on K+ channel is fast\n"
  "\n"
  "\n"
  "	Kinetic Equations:\n"
  "\n"
  "	  dR/dt = K1 * T * (1-R-D) - K2 * R\n"
  "\n"
  "	  dG/dt = K3 * R - K4 * G\n"
  "\n"
  "	  R : activated receptor\n"
  "	  T : transmitter\n"
  "	  G : activated G-protein\n"
  "	  K1,K2,K3,K4 = kinetic rate cst\n"
  "\n"
  "  n activated G-protein bind to a K+ channel:\n"
  "\n"
  "	n G + C <-> O		(Alpha,Beta)\n"
  "\n"
  "  If the binding is fast, the fraction of open channels is given by:\n"
  "\n"
  "	O = G^n / ( G^n + KD )\n"
  "\n"
  "  where KD = Beta / Alpha is the dissociation constant\n"
  "\n"
  "-----------------------------------------------------------------------------\n"
  "\n"
  "  Parameters estimated from patch clamp recordings of GABAB PSP's in\n"
  "  rat hippocampal slices (Otis et al, J. Physiol. 463: 391-407, 1993).\n"
  "\n"
  "-----------------------------------------------------------------------------\n"
  "\n"
  "  PULSE MECHANISM\n"
  "\n"
  "  Kinetic synapse with release mechanism as a pulse.  \n"
  "\n"
  "  Warning: for this mechanism to be equivalent to the model with diffusion \n"
  "  of transmitter, small pulses must be used...\n"
  "\n"
  "  see details at http://cns.iaf.cnrs-gif.fr\n"
  "\n"
  "  Written by A. Destexhe, 1995\n"
  "  27-11-2002: the pulse is implemented using a counter, which is more\n"
  "	stable numerically (thanks to Yann LeFranc)\n"
  "\n"
  "-----------------------------------------------------------------------------\n"
  "ENDCOMMENT\n"
  "\n"
  "\n"
  "\n"
  "INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}\n"
  "\n"
  "NEURON {\n"
  "	POINT_PROCESS GABAb_S_v2\n"
  "	POINTER pre\n"
  "	RANGE C, R, G, g, gmax, lastrelease, TimeCount\n"
  "	NONSPECIFIC_CURRENT i\n"
  "	:GLOBAL Cmax, Cdur, Prethresh, Deadtime\n"
  "	RANGE Cmax, Cdur, Prethresh, Deadtime\n"
  "	:GLOBAL K1, K2, K3, K4, KD, Erev\n"
  "	RANGE K1, K2, K3, K4, KD, n, Erev\n"
  "}\n"
  "UNITS {\n"
  "	(nA) = (nanoamp)\n"
  "	(mV) = (millivolt)\n"
  "	(umho) = (micromho)\n"
  "	(mM) = (milli/liter)\n"
  "}\n"
  "\n"
  "PARAMETER {\n"
  "	dt		(ms)\n"
  "	Cmax	= 0.5	(mM)		: max transmitter concentration\n"
  "	Cdur	= 0.3	(ms)		: transmitter duration (rising phase)\n"
  "	Prethresh = 0 			: voltage level nec for release\n"
  "	Deadtime = 1	(ms)		: mimimum time between release events\n"
  ":\n"
  ":	From Kfit with long pulse (5ms 0.5mM)\n"
  ":\n"
  "	K1	= 0.52	(/ms mM)	: forward binding rate to receptor\n"
  "	K2	= 0.0013 (/ms)		: backward (unbinding) rate of receptor\n"
  "	K3	= 0.098 (/ms)		: rate of G-protein production\n"
  "	K4	= 0.033 (/ms)		: rate of G-protein decay\n"
  "	KD	= 100			: dissociation constant of K+ channel\n"
  "	n	= 4			: nb of binding sites of G-protein on K+\n"
  "	Erev	= -95	(mV)		: reversal potential (E_K)\n"
  "	gmax		(umho)		: maximum conductance\n"
  "}\n"
  "\n"
  "ASSIGNED {\n"
  "	v		(mV)		: postsynaptic voltage\n"
  "	i 		(nA)		: current = g*(v - Erev)\n"
  "	g 		(umho)		: conductance\n"
  "	C		(mM)		: transmitter concentration\n"
  "	Gn\n"
  "	pre 				: pointer to presynaptic variable\n"
  "	lastrelease	(ms)		: time of last spike\n"
  "	TimeCount	(ms)		: time counter\n"
  "}\n"
  "\n"
  "STATE {\n"
  "	R				: fraction of activated receptor\n"
  "	G				: fraction of activated G-protein\n"
  "}\n"
  "\n"
  "\n"
  "INITIAL {\n"
  "	C = 0\n"
  "	lastrelease = -9e9\n"
  "\n"
  "	R = 0\n"
  "	G = 0\n"
  "	TimeCount=-1\n"
  "}\n"
  "\n"
  "BREAKPOINT {\n"
  "	SOLVE bindkin METHOD cnexp\n"
  "	Gn = G^n\n"
  "	g = gmax * Gn / (Gn+KD)\n"
  "	i = g*(v - Erev)\n"
  "}\n"
  "\n"
  "DERIVATIVE bindkin {\n"
  "	R' = K1 * C * (1-R) - K2 * R\n"
  "	G' = K3 * R - K4 * G\n"
  "}\n"
  "\n"
  "NET_RECEIVE(weight ,on) {\n"
  "  if (on) { : at end of Cdur pulse so turn off\n"
  "    on = 0\n"
  "    C = 0\n"
  "  } else {\n"
  "    if (weight==0) { : do nothing\n"
  "      C=0 \n"
  "    } else {\n"
  "      C=Cmax\n"
  "      on=1\n"
  "      net_send(Cdur, on)\n"
  "    }\n"
  "  }\n"
  "}\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  ;
#endif
