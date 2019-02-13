import healpy as hp
import numpy as np
import pysm
from add_small_scales import *

##DUST
#dustT = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/dust_T.fits')
#dustQ = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/dust_Q.fits')
#dustU = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/dust_U.fits')
#dust_pysm = np.array([dustT, dustQ, dustU])
#dust4096 = add_gaussian_small_scales(dust_pysm, 4096, pol=True)
#hp.write_map('maps/PySM_dust_TQU_ns4096.fits', dust4096, overwrite=True)
#cl_dust = hp.anafast(dust4096)
#np.save('cl_PySM_dust_TQU_ns4096.fits', cl_dust)

#SYNCH
synchT = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/synch_T.fits')
synchQ = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/synch_Q.fits')
synchU = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/synch_U.fits')
synch_pysm = np.array([synchT, synchQ, synchU])
synch4096 = add_gaussian_small_scales(synch_pysm, 4096, pol=True)
hp.write_map('maps/PySM_synch_TQU_ns4096_2.fits', synch4096, overwrite=True)
cl_synch = hp.anafast(synch4096)
np.save('cl_PySM_synch_TQU_ns4096_2.fits', cl_synch)

##FREE-FREE
#ffT = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/freefree_T.fits')
#ff4096 = add_gaussian_small_scales(ffT, 4096, pol=False)
#hp.write_map('maps/PySM_freefree_T_ns4096.fits', ff4096, overwrite=True)
#cl_ff = hp.anafast(ff4096)
#np.save('cl_PySM_freefree_T_ns4096.fits', cl_ff)

##AME 1
#ame1 = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/ame_T.fits')
#ame1_4096 = add_gaussian_small_scales(ame1, 4096, pol=False)
#hp.write_map('maps/PySM_ame1_T_ns4096.fits', ame1_4096, overwrite=True)
#cl_ame1 = hp.anafast(ame1_4096)
#np.save('cl_PySM_ame1_T_ns4096.fits', cl_ame1)

##AME 2
#ame2 = hp.read_map('/global/homes/k/krach/usr/python/PySM_public/pysm/SO_template/ame2_T.fits')
#ame2_4096 = add_gaussian_small_scales(ame2, 4096, pol=False)
#hp.write_map('maps/PySM_ame2_T_ns4096.fits', ame2_4096, overwrite=True)
#cl_ame2 = hp.anafast(ame2_4096)
#np.save('cl_PySM_ame2_T_ns4096.fits', cl_ame2)
