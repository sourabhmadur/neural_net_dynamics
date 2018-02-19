from neuron import h, gui
import matplotlib.pyplot as plt
import numpy as np
from tempCorr import *
from nernst import *
from matplotlib.collections import LineCollection
from plots import *
# from run import *


tstop = 1

h.tstop = tstop
h.dt=0.0001
h.celsius = (T-273)




def define_geometry(icc):

	icc.diam = 6.827*2
	icc.L = 200					
	icc.nseg = 11
	icc.cm = 25
	icc.Ra = 50



def insert_mechanisms(icc):

	icc.insert('pas')
	icc.g_pas = .1
	icc(0.5).g_pas=0

	icc.insert('Na')
	icc.nai = nai
	icc.nao = nao
	icc.G_Na_Na= 0		#20
	icc.tau_f_Na_Na = tau_f_Na
	icc.tau_d_Na_Na = tau_d_Na

	icc.insert('nscc')
	icc.G_NSCC_nscc = 0	#12.15
	icc.tau_NSCC_nscc = tau_NSCC

	icc.insert('ERG')
	icc.G_ERG_ERG = 0	#2.5
	icc.tau_ERG_ERG = tau_ERG 
	icc.ki= ki	#23
	icc.ko= ko	#23

	icc.insert('bk')
	icc.G_bk_bk= 0 #23+T_correction_BK

	icc.insert('Kb')
	icc.G_Kb_Kb=0	#.15

	icc.insert('kv11')
	icc.G_Kv11_kv11=0   #6.3
	icc.tau_d_kv11_kv11 = tau_d_kv11
	icc.tau_f_kv11_kv11 = tau_f_kv11

	icc.insert('vddr')
	icc.G_Ca_VDDR_vddr=0	#3
	icc.cao = 2.5
	icc.tau_d_VDDR_vddr = tau_d_VDDR
	icc.tau_f_VDDR_vddr = tau_f_VDDR

	icc.insert('ltype')
	icc.G_Ca_Ltype_ltype=0 #2
	icc.tau_f_Ltype_ltype = tau_f_Ltype
	icc.tau_d_Ltype_ltype = tau_d_Ltype
	icc.tau_f_Ca_Ltype_ltype = tau_f_Ca_Ltype

	icc.insert('pmca')
	icc.J_max_PMCA_pmca= 0 #0.088464


	icc.insert('concyto')
	J_max_leak=0.01
	icc.J_max_leak_concyto= 0	#0.01(mM/s) 

	icc.insert('conpu')
	icc.J_max_leak_conpu= 0 #0.01(mM/s) 
	icc.Jmax_serca_conpu = 0		# 1.8333	
	icc.J_ERleak_conpu = 0		# 1.666667	

	icc.Jmax_IP3_conpu = 	0		#50000  (1/s)
	icc.Jmax_NaCa_conpu =  0 	#0.05(mM/s)
	icc.Jmax_uni_conpu = 0 		#5000 mM/s
	icc.insert('ano1')
	icc.g_Ano1_ano1 = 0	#20
	icc.cli = cli_
	icc.clo = clo_
	icc.ecl = ecl_

	icc.insert('cacl')
	icc.G_Cacl_cacl = 0	#10.1
	icc.tau_act_Cacl_cacl = tau_act_Cacl


	active_sites = [0.5]

	a = 0.01

	for i in active_sites:


		icc(i).G_Na_Na= 20		#20

		icc(i).G_NSCC_nscc = 12.15	#12.15

		icc(i).G_ERG_ERG = 2.5	#2.5

		icc(i).G_bk_bk= 23+T_correction_BK #23+T_correction_BK

		icc(i).G_Kb_Kb=0.15	#.15

		icc(i).G_Kv11_kv11=6.3   #6.3

		icc(i).G_Ca_VDDR_vddr=3	#3

		icc(i).G_Ca_Ltype_ltype=2 #2

		icc(i).J_max_PMCA_pmca= 0.088464 #0.088464

		icc(i).J_max_leak_concyto= J_max_leak	#0.01(mM/s) 

		icc(i).J_max_leak_conpu= J_max_leak #0.01(mM/s) 

		icc(i).Jmax_serca_conpu = 1.8333		# 1.8333	

		icc(i).J_ERleak_conpu = 1.666667		# 1.666667	

		icc(i).Jmax_IP3_conpu = 	50000		#50000  (1/s)

		icc(i).Jmax_NaCa_conpu =  0.05 	#0.05(mM/s)

		icc(i).Jmax_uni_conpu = 5000 		#5000 mM/s



		icc(i).g_Ano1_ano1 = 20	#20

		icc(i).G_Cacl_cacl = 10.1	#10.1


def run_and_record(icc,v,ina,t,ik,ica,icl,eca,ins,cai,cao,ek,capui,caeri,cami,cli,clo,oano,ecl,ena,ica_vddr,icl_ano1, icl_cacl, ina_Na, ik_kv11, ik_bk, ica_ltype, i_nscc, ik_Kb, ica_pmca, ik_ERG):



	v.record(icc(0.5)._ref_v)
	t.record(h._ref_t)
	ina.record(icc(.5)._ref_ina)
	# # ik.record(icc(.5)._ref_ik)
	# icl.record(icc(.5)._ref_icl)
	# ica.record(icc(.5)._ref_ica)
	# ins.record(icc(.5)._ref_i_nscc)
	# eca.record(icc(.5)._ref_eca)
	# cai.record(icc(.5)._ref_cai)
	# cao.record(icc(.5)._ref_cao)
	# ek.record(icc(.5)._ref_ek)
	# capui.record(icc(.5)._ref_capui)
	# caeri.record(icc(.5)._ref_caeri)
	# cami.record(icc(.5)._ref_cami)
	# cli.record(icc(.5)._ref_cli)
	# clo.record(icc(.5)._ref_clo)
	# oano.record(icc(.5)._ref_O_Ano1_ano1)
	# ecl.record(icc(.5)._ref_ecl)
	# ena.record(icc(.5)._ref_ena)
	
	# ica_vddr.record(icc(.5)._ref_ica_vddr)
	# icl_ano1.record(icc(.5)._ref_icl_ano1)
	# icl_cacl.record(icc(.5)._ref_icl_cacl)
	# ina_Na.record(icc(.5)._ref_ina_Na)
	# ik_kv11.record(icc(.5)._ref_ik_kv11)
	# ik_bk.record(icc(.5)._ref_ik_bk)
	# ica_ltype.record(icc(.5)._ref_ica_ltype)
	# i_nscc.record(icc(.5)._ref_i_nscc)
	# ik_Kb.record(icc(.5)._ref_ik_Kb)
	# ica_pmca.record(icc(.5)._ref_ica_pmca)
	# ik_ERG.record(icc(.5)._ref_ik_ERG)

	h.run()




v = h.Vector()             # Membrane potential vector
t = h.Vector()             # Time stamp vector

cai =h.Vector()
cao =h.Vector()
capui =h.Vector()
caeri = h.Vector()
cami = h.Vector()
cli = h.Vector()
clo = h.Vector()


eca =h.Vector()
ek = h.Vector()
ecl = h.Vector()
ena = h.Vector()

oano = h.Vector()

ina = h.Vector()			#uA/c
ik = h.Vector()
ica = h.Vector()
ins = h.Vector()
icl = h.Vector()

ica_vddr = h.Vector()
icl_ano1 = h.Vector()
icl_cacl= h.Vector()
ina_Na = h.Vector() 
ik_kv11= h.Vector() 
ik_bk= h.Vector()
ica_ltype= h.Vector()
i_nscc= h.Vector() 
ik_Kb= h.Vector() 
ica_pmca= h.Vector() 
ik_ERG= h.Vector()

variables = [v,ina,t,ik,ica,icl,eca,ins,cai,cao,ek,capui,caeri,cami,cli,clo,oano,ecl,ena,ica_vddr,icl_ano1, icl_cacl, ina_Na, ik_kv11, ik_bk, ica_ltype, i_nscc, ik_Kb, ica_pmca, ik_ERG]
# v,ina,t,ik,ica,icl,eca,ins,cai,cao,ek,capui,caeri,cami,cli,clo,oano,ecl,ena,ica_vddr,icl_ano1, icl_cacl, ina_Na, ik_kv11, ik_bk, ica_ltype, i_nscc, ik_Kb, ica_pmca, ik_ERG = runThisAlready(icc,v,ina,t,ik,ica,icl,eca,ins,cai,cao,ek,capui,caeri,cami,cli,clo,oano,ecl,ena,ica_vddr,icl_ano1, icl_cacl, ina_Na, ik_kv11, ik_bk, ica_ltype, i_nscc, ik_Kb, ica_pmca, ik_ERG)



icc = h.Section(name='icc')
define_geometry(icc)
insert_mechanisms(icc)

# icc1 = h.Section(name='icc1')
# icc1.nseg=1001
# icc1.insert('pas')
# icc1.L = 5000
# icc1.diam=1
# icc1.connect(icc(1))
# icc1.cm=25
v_e = h.Vector()
v_e1 = h.Vector()
v_e2 = h.Vector()
v_e3 = h.Vector()
v_e4 = h.Vector()
v_e.record(icc(0.6)._ref_v)
v_e1.record(icc(0.7)._ref_v)
v_e2.record(icc(.8)._ref_v)
v_e3.record(icc(.9)._ref_v)
v_e4.record(icc(1)._ref_v)



# vclamp = h.SEClamp(icc(0.5))
# vclamp.dur1 = tstop
# vclamp.amp1=-50.0
# vclamp.rs=.00001
h.v_init = -70



run_and_record(icc,*variables)


plt.figure()
plt.plot(t,v , label = 'v(0.5)', color= 'red')
plt.plot(t,v_e , label = 'v(0.6)', color= 'blue')
plt.plot(t,v_e1 , label = 'v(0.7)', color= 'green')
plt.plot(t,v_e2 , label = 'v(0.8)', color= 'yellow')
plt.plot(t,v_e3 , label = 'v(0.9)', color= 'black')
plt.plot(t,v_e4 , label = 'v(1)', color= 'brown')
plt.legend(loc = 'upper right')


# plt.plot(t,ina)


plt.show()


