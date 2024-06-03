
import tellurium as te

# module_list = ['EGFR_module.ant', 'GAB_module.ant', 'GAREM_module.ant', 'SHC_module.ant', 'SOS_module2.ant']
# module_list = ['EGFR_module_hsw.ant']
# module_list = ['EGFR_module.ant']
# module_list = ['EGFR_Reference_Model.ant']
# module_list = ['RAF_activation_2022.ant']
# module_list = ['RAF_activation_2022_1.ant']
# module_list = ['RAF_activation_2022_erk_fit.ant']
# module_list = ['GAREM_module.ant']
# module_list = ['GAREM_module_m.ant']
# module_list = ['GAREM_module_1.ant']
# module_list = ['GAB_module.ant']
# module_list = ['GAB_module_1.ant']
# module_list = ['EGFR_combined_1.ant']
# module_list = ['GAB_module_m.ant']
# module_list = ['SHC_MA_module.ant']
# module_list = ['SHC_module.ant']
# module_list = ['SHC_MA_module_m.ant']
# module_list = ['SHC_module_1.ant']
# module_list = ['SOS_module.ant']
# module_list = ['SOS_module_1.ant']
# module_list = ['RAS_module_1.ant']
# module_list = ['SOS_RAS_module_1.ant']
# module_list = ['SOS_module2_m.ant']
# module_list = ['RAF_activation_2022_mek.ant']

# module_list = ['EGFR_sequential_fit_egfr.ant']
# module_list = ['EGFR_sequential_fit_2.ant']
# module_list = ['EGFR_sequential_fit_3.ant']
# module_list = ['EGFR_sequential_fit_4.ant']
# module_list = ['EGFR_sequential_fit_4a.ant']
# module_list = ['EGFR_sequential_fit_4b.ant']
# module_list = ['EGFR_sequential_fit_4c.ant']
# module_list = ['EGFR_sequential_fit_4d.ant']
# module_list = ['EGFR_sequential_fit_4e.ant']
# module_list = ['EGFR_sequential_fit_4e2.ant']
# module_list = ['EGFR_sequential_fit_4f.ant']
# module_list = ['EGFR_sequential_fit_4g.ant']
# module_list = ['EGFR_sequential_fit_4h.ant']
# module_list = ['EGFR_sequential_fit_full.ant']
# module_list = ['EGFR_1_4.ant']
# module_list = ['EGFR_2_4.ant']
# module_list = ['EGFR_4_HSW.ant']
# module_list = ['EGFR_4_HSW_1.ant']
# module_list = ['EGFR_5_HSW_MK_rev.ant']
# module_list = ['EGFR_5_HSW_MK_rev_2.ant']
# module_list = ['EGFR_5_HSW_MK_rev_3.ant']
# module_list = ['EGFR_5_HSW_MK-rev.ant']
module_list = ['EGFR_8a.ant', 'EGFR_8b.ant']
# module_list = ['EGFR_8b.ant']

for module in module_list:
    r = te.loada(module)
    r.exportToSBML(module[:-4] + '.xml')
