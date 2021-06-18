# The following function is used to aggregate the outcomes into the KPI we want
# This iterates over all the locations and round numbers, and creates a new column summing the values per location and round.
# If we want to aggregate over the location, "aggregate" equals "location" and therefore the KPI is added per location and not in total.
# If we want to aggregate over the province, "aggregate" equals "province" and therefore the KPI is added per province.
# On the contrary, if aggregate equals "total", the total value is appended to the dataframe.
def aggregate_kpi(data, kpi, aggregate):
    locations = ["A.1", "A.2", "A.3", "A.4", "A.5"]
    provinces = ["Overijssel", "Gelderland"]
    kpi_columns = []
    
    if kpi == "RfR Total Costs" or kpi == "Expected Evacuation Costs":
        kpi_columns.append(kpi + " 0")
        kpi_columns.append(kpi + " 1")
        kpi_columns.append(kpi + " 2")
        
        data[kpi] = data[kpi_columns].sum(axis=1)
    else:
        if aggregate == "total":
            for location in locations:
                kpi_columns.append(location + "_" + kpi + " 0")
                kpi_columns.append(location + "_" + kpi + " 1")
                kpi_columns.append(location + "_" + kpi + " 2")

            data[kpi] = data[kpi_columns].sum(axis=1)
            
        elif aggregate == "province":
            for province in provinces:
                if province == 'Overijssel':
                    kpi_columns = []
                    kpi_columns.append("A.4" + "_" + kpi + " 0")
                    kpi_columns.append("A.4" + "_" + kpi + " 1")
                    kpi_columns.append("A.4" + "_" + kpi + " 2")
                    kpi_columns.append("A.5" + "_" + kpi + " 0")
                    kpi_columns.append("A.5" + "_" + kpi + " 1")
                    kpi_columns.append("A.5" + "_" + kpi + " 2")                    
                    
                    data["Overijssel" + "_" + kpi] = data[kpi_columns].sum(axis=1)
      
           
                else:
                    kpi_columns = []
                    kpi_columns.append("A.1" + "_" + kpi + " 0")
                    kpi_columns.append("A.1" + "_" + kpi + " 1")
                    kpi_columns.append("A.1" + "_" + kpi + " 2")
                    kpi_columns.append("A.2" + "_" + kpi + " 0")
                    kpi_columns.append("A.2" + "_" + kpi + " 1")
                    kpi_columns.append("A.2" + "_" + kpi + " 2") 
                    kpi_columns.append("A.3" + "_" + kpi + " 0")
                    kpi_columns.append("A.3" + "_" + kpi + " 1")
                    kpi_columns.append("A.3" + "_" + kpi + " 2")                    

                    data["Gelderland" + "_" + kpi] = data[kpi_columns].sum(axis=1)
            
        else:
            for location in locations:
                kpi_columns = []
                kpi_columns.append(location + "_" + kpi + " 0")
                kpi_columns.append(location + "_" + kpi + " 1")
                kpi_columns.append(location + "_" + kpi + " 2")

                data[location + "_" + kpi] = data[kpi_columns].sum(axis=1)
                
    return data


