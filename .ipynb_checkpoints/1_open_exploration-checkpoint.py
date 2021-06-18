from ema_workbench import Scenario

def specify_levers(dike_1 = 0, dike_2 = 0, dike_3 = 0, dike_4 = 0, dike_5 = 0, 
                      rfr_0 = 0, rfr_1 = 0, rfr_2 = 0, rfr_3 = 0, rfr_4 = 0,
                      EWS = 0) :
    
    '''Specify levers for further usage'''
    
    levers_param = {'A.1_DikeIncrease': dike_1, 'A.2_DikeIncrease': dike_2, 'A.3_DikeIncrease': dike_3, 
                  'A.4_DikeIncrease': dike_4, 'A.5_DikeIncrease': dike_5,
                  '0_RfR': rfr_0, '1_RfR': rfr_1, '2_RfR': rfr_2, '3_RfR': rfr_3, '4_RfR': rfr_4,
                  'EWS_DaysToThreat': EWS}
    
    return levers_param

def specify_scenario(reference_values, dike_model) :
    scen = {}
    for key in dike_model.uncertainties:
        scen.update({key.name: reference_values[key.name]})
    reference_scenario = Scenario('reference', **scen)
    return reference_scenario

def default_scenario(dike_model) : 
    reference_values = {'Bmax': 175, 'Brate': 1.5, 'pfail': 0.5,
                        'discount rate': 3.5,
                        'ID flood wave shape': 4}
    scen1 = {}

    for key in dike_model.uncertainties:
        name_split = key.name.split('_')

        if len(name_split) == 1:
            scen1.update({key.name: reference_values[key.name]})

        else:
            scen1.update({key.name: reference_values[name_split[1]]})

    ref_scenario = Scenario('reference', **scen1)
    return ref_scenario
