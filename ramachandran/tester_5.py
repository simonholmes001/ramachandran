import os

import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

import matplotlib.pyplot as plt

# with open('../data/5f0s_psi_statistics.pickle', 'rb') as labels_file:
#     df_1 = pd.read_pickle(labels_file)
#
# with open('../data/5f0b_psi_statistics.pickle', 'rb') as labels_file:
#     df_2 =  pd.read_pickle(labels_file)
#
# with open('../data/5f0a_psi_statistics.pickle', 'rb') as labels_file:
#     df_3 =  pd.read_pickle(labels_file)
#
# with open('../data/5f0c_psi_statistics.pickle', 'rb') as labels_file:
#     df_4 =  pd.read_pickle(labels_file)

# input_path = '../data'
# output_path = '../output'
input_path = '/media/simon/disk/protein_folding/phi_angle_statistics'
output_path = '/media/simon/disk/protein_folding/phi_statistics'

ala = []
arg = []
asn = []
asp = []
cys = []
gln = []
glu = []
gly = []
his = []
ile = []
leu = []
lys = []
met = []
phe = []
pro = []
ser = []
thr = []
trp = []
tyr = []
val = []
sec = []
pyl = []
unk = []

for root, dirs, files in os.walk(input_path, topdown=False):
    for file in tqdm(files):
        with open(input_path + '/' + file, 'rb') as labels_file:
            try:
                df = pd.read_pickle(labels_file)
                df_1 = np.array(np.split(df, len(df)/2))
            except:
                pass
            try:
                for i in df_1:
                    if i[0] == '0.0: ':
                        ala.append(i[1])
                    if i[0] == '1.0: ':
                        arg.append(i[1])
                    if i[0] == '2.0: ':
                        asn.append(i[1])
                    if i[0] == '3.0: ':
                        asp.append(i[1])
                    if i[0] == '4.0: ':
                        cys.append(i[1])
                    if i[0] == '5.0: ':
                        gln.append(i[1])
                    if i[0] == '6.0: ':
                        glu.append(i[1])
                    if i[0] == '7.0: ':
                        gly.append(i[1])
                    if i[0] == '8.0: ':
                        his.append(i[1])
                    if i[0] == '9.0: ':
                        ile.append(i[1])
                    if i[0] == '10.0: ':
                        leu.append(i[1])
                    if i[0] == '11.0: ':
                        lys.append(i[1])
                    if i[0] == '12.0: ':
                        met.append(i[1])
                    if i[0] == '13.0: ':
                        phe.append(i[1])
                    if i[0] == '14.0: ':
                        pro.append(i[1])
                    if i[0] == '15.0: ':
                        ser.append(i[1])
                    if i[0] == '16.0: ':
                        thr.append(i[1])
                    if i[0] == '17.0: ':
                        trp.append(i[1])
                    if i[0] == '18.0: ':
                        tyr.append(i[1])
                    if i[0] == '19.0: ':
                        val.append(i[1])
                    if i[0] == '20.0: ':
                        sec.append(i[1])
                    if i[0] == '21.0: ':
                        pyl.append(i[1])
                    if i[0] == '22.0: ':
                        unk.append(i[1])
            except:
                pass

alphabet = [ala,arg,asn,asp,cys,gln,glu,gly,his,ile,leu,lys,met,phe,pro,ser,thr,trp,tyr,val,sec,pyl,unk]

stat_ala = np.array(ala)
stat_ala_2 = stat_ala.astype(np.float)
with open(output_path + '/' + 'ala_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_ala_2, file, protocol=4)

stat_arg = np.array(arg)
stat_2 = stat_arg.astype(np.float)
with open(output_path + '/' + 'arg_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_asn = np.array(asn)
stat_2 = stat_asn.astype(np.float)
with open(output_path + '/' + 'asn_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_asp = np.array(asp)
stat_2 = stat_asp.astype(np.float)
with open(output_path + '/' + 'asp_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_cys = np.array(cys)
stat_2 = stat_cys.astype(np.float)
with open(output_path + '/' + 'cys_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_gln = np.array(gln)
stat_2 = stat_gln.astype(np.float)
with open(output_path + '/' + 'gln_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_glu = np.array(glu)
stat_2 = stat_glu.astype(np.float)
with open(output_path + '/' + 'glu_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_gly = np.array(gly)
stat_2 = stat_gly.astype(np.float)
with open(output_path + '/' + 'gly_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_his = np.array(his)
stat_2 = stat_his.astype(np.float)
with open(output_path + '/' + 'his_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_ile = np.array(ile)
stat_2 = stat_ile.astype(np.float)
with open(output_path + '/' + 'ile_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_leu = np.array(leu)
stat_2 = stat_leu.astype(np.float)
with open(output_path + '/' + 'leu_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_lys = np.array(lys)
stat_2 = stat_lys.astype(np.float)
with open(output_path + '/' + 'lys_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_met = np.array(met)
stat_2 = stat_met.astype(np.float)
with open(output_path + '/' + 'met_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_phe = np.array(phe)
stat_2 = stat_phe.astype(np.float)
with open(output_path + '/' + 'phe_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_pro = np.array(pro)
stat_2 = stat_pro.astype(np.float)
with open(output_path + '/' + 'pro_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_ser = np.array(ser)
stat_2 = stat_ser.astype(np.float)
with open(output_path + '/' + 'ser_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_thr = np.array(thr)
stat_2 = stat_thr.astype(np.float)
with open(output_path + '/' + 'thr_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_trp = np.array(trp)
stat_2 = stat_trp.astype(np.float)
with open(output_path + '/' + 'trp_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_tyr = np.array(tyr)
stat_2 = stat_tyr.astype(np.float)
with open(output_path + '/' + 'tyr_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_val = np.array(val)
stat_2 = stat_val.astype(np.float)
with open(output_path + '/' + 'val_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_sec = np.array(sec)
stat_2 = stat_sec.astype(np.float)
with open(output_path + '/' + 'sec_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_pyl = np.array(unk)
stat_2 = stat_pyl.astype(np.float)
with open(output_path + '/' + 'pyl_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)

stat_unk = np.array(unk)
stat_2 = stat_unk.astype(np.float)
with open(output_path + '/' + 'unk_phi_statistics.pickle', 'wb', buffering=500000000) as file:
    pickle.dump(stat_2, file, protocol=4)
