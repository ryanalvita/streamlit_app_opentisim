"""Defaults for following objects:
- 1. Quay_wall
- 2. Berth
- 3. Cyclic_Unloader
    - STS crane
- 4. Horizontal transport
    - Tractor trailer
- 5. Containers
    - Laden
    - Reefer
    - Empty
    - OOG
- 6. Laden and reefer stack
    - RTG stack
    - RMG stack
    - SC stack
    - RS stack
- 7. Stack equipment
    - RTG
    - RMG
    - SC
    - RS
-8. Other stacks
    - OOG stack
    - Empty stack
- 8. Vessel
    - Panamax
- 9. Labour

Default values are based on Claes 2018; Corbeau 2018; Daas 2018; Juha 2018;
Kranendonk 2018; Schutz 2018; Schuurmans 2018 and Verstegen 2018

"""

# package(s) for data handling
import pandas as pd

# *** Default inputs: Quay class ***

quay_wall_data = {"name": 'Quay_01',
                  "ownership": 'Port authority',
                  "delivery_time": 2,
                  "lifespan": 50,
                  "mobilisation_min": 2_500_000,
                  "mobilisation_perc": 0.02,
                  "maintenance_perc": 0.01,
                  "insurance_perc": 0.01,
                  "freeboard": 4,
                  "Gijt_constant": 757.20,
                  "Gijt_coefficient": 1.2878,
                  "max_sinkage": 0.5,
                  "wave_motion": 0.5,
                  "safety_margin": 0.5,
                  "apron_width" : 65.5} # all values from Ijzermans, 2019, P 91

# *** Default inputs: Berth class ***

berth_data = {"name": 'Berth_01',
              "crane_type": 'Mobile cranes',
              "delivery_time": 1,
              "max_cranes": 4}  #STS cranes

# *** Default inputs: CyclicUnloader class ***

gantry_crane_data = {"name": 'Gantry_crane_01',
                     "ownership": 'Terminal operator',
                     "delivery_time": 1,
                     "lifespan": 40,
                     "unit_rate": 9_750_000,
                     "mobilisation_perc": 0.15,
                     "maintenance_perc": 0.02,
                     "consumption": 561,
                     "insurance_perc": 0.01,
                     "crew": 3,
                     "crane_type": 'Gantry crane',
                     "lifting_capacity": 50,
                     "hourly_cycles": 50,
                     "eff_fact": 0.50}  # all values from Ijzermans, 2019, P 100

harbour_crane_data = {"name": 'Harbour_crane_01',
                      "ownership": 'Terminal operator',
                      "delivery_time": 1,
                      "lifespan": 40,
                      "unit_rate": 7_880_000,
                      "mobilisation_perc": 0.15,
                      "maintenance_perc": 0.02,
                      "consumption": 210,
                      "insurance_perc": 0.01,
                      "crew": 3,
                      "crane_type": 'Harbour crane',
                      "lifting_capacity": 25,
                      "hourly_cycles": 40,
                      "eff_fact": 0.40} # all values from Ijzermans, 2019, P 100

mobile_crane_data = {"name": 'Mobile_crane_01',
                     "ownership": 'Terminal operator',
                     "delivery_time": 1,
                     "lifespan": 40,
                     "unit_rate": 3_325_000,
                     "mobilisation_perc": 0.15,
                     "maintenance_perc": 0.02,
                     "consumption": 485,
                     "insurance_perc": 0.01,
                     "crew": 3,
                     "crane_type": 'Mobile crane',
                     "lifting_capacity": 30,
                     "hourly_cycles": 25,
                     "eff_fact": 0.35} # all values from Ijzermans, 2019, P 100

sts_crane_data = {"name": 'STS_crane_01',
                     "ownership": 'Terminal operator',
                     "delivery_time": 1,
                     "lifespan": 40,
                     "unit_rate": 10_000_000,
                     "mobilisation_perc": 0.15,
                     "maintenance_perc": 0.02,
                     "consumption": 400, #based on 8 kWh/box move (kan ik dit wellicht ook vervangen met kWh per box move?)
                     "insurance_perc": 0.01,
                     "crew": 5.5, # todo is dit per shift?  #1.5 crane driver, 2 quay staff, 2 twistlock handler (per shift)
                     "crane_type": 'STS crane',
                     "lifting_capacity":2.25 , #weighted average of TEU per lift
                     "hourly_cycles": 28,
                     "eff_fact": 1} #dit is al afgevangen middels de lifting capacity

# *** Default inputs: ContinuousUnloader class ***

continuous_screw_data = {"name": 'Continuous_loader_01',
                         "ownership": 'Terminal operator',
                         "delivery_time": 1,
                         "lifespan": 30,
                         "unit_rate": 6_900_000,
                         "mobilisation_perc": 0.15,
                         "maintenance_perc": 0.02,
                         "consumption": 364,
                         "insurance_perc": 0.01,
                         "crew": 2,
                         "crane_type": 'Screw unloader',
                         "peak_capacity": 700,
                         "eff_fact": 0.55} # all values from Ijzermans, 2019, P 101

# *** Default inputs: Conveyor class ***

quay_conveyor_data = {"name": 'Quay_conveyor_01',
                      "type": 'quay_conveyor',
                      "length": 200,
                      "ownership": 'Terminal operator',
                      "delivery_time": 1,
                      "lifespan": 10,
                      "unit_rate_factor": 6,
                      "mobilisation": 30_000,
                      "maintenance_perc": 0.10,
                      "insurance_perc": 0.01,
                      "consumption_constant": 81,
                      "consumption_coefficient": 0.08,
                      "crew": 1,
                      "utilisation": 0.80,
                      "capacity_steps": 400} # all input values from Ijzermans, 2019, P 104

hinterland_conveyor_data = {"name": 'Hinterland_conveyor_01',
                            "type": 'hinterland_conveyor',
                            "length": 400,
                            "ownership": 'Terminal operator',
                            "delivery_time": 1,
                            "lifespan": 10,
                            "mobilisation": 30_000,
                            "unit_rate_factor": 6,
                            "maintenance_perc": 0.10,
                            "insurance_perc": 0.01,
                            "consumption_constant": 81,
                            "consumption_coefficient": 0.08,
                            "crew": 1,
                            "utilisation": 0.80,
                            "capacity_steps": 400} # all input values from Ijzermans, 2019, P 104

# Default inputs: Horizontal Transport class ***

tractor_trailer_data = {"name": 'Tractor-trailer',
                            "type": 'tractor_trailer',
                            "ownership": 'Terminal operator',
                            "delivery_time": 0,
                            "lifespan": 10,
                            "mobilisation": 1_000,
                            "unit_rate": 85_000,
                            "maintenance_perc": 0.10,
                            "insurance_perc": 0.01,
                            "crew": 1,
                            "salary": 30_000, #dummy
                            "utilisation": 0.80,
                            "fuel_consumption": 2, #liter per box move
                            "productivity": 1,
                            "required" : 5} # todo input value for tractor productivity

# *** Default inputs: Container class

laden_container_data = {"name": 'Laden container',
                        "type": 'laden_container',
                        "teu_factor" : 1.55,
                        "dwell_time" : 4,
                        "peak_factor" : 1.2,
                        "stack_occupancy" : 0.8}

reefer_container_data = {"name": 'Empty container',
                        "type": 'empty_container',
                        "teu_factor" : 1.75,
                        "dwell_time" : 4,
                        "peak_factor" : 1.2,
                        "stack_occupancy" : 0.8}

empty_container_data = {"name": 'Empty container',
                        "type": 'empty_container',
                        "teu_factor" : 1.55,
                        "dwell_time" : 10,
                        "peak_factor" : 1.2,
                        "stack_occupancy" : 0.7}

oog_container_data = {"name": 'OOG container',
                        "type": 'oog_container',
                        "teu_factor" : 1.55,
                        "dwell_time" : 5,
                        "peak_factor" : 1.2,
                        "stack_occupancy" : 0.9}

# *** Default inputs: Laden_Stack class

rtg_stack_data = {"name": 'RTG Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 25_000,
                    "maintenance_perc": 0.1,
                    "width": 6, #TEU
                    "height": 5, #TEU
                    "length": 30, #TEU
                    "capacity": 900 , #TEU
                    "gross_tgs": 18,
                    "area_factor": 2.04 , # Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY

rmg_stack_data = {"name": 'RMG Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 50_000,
                    "maintenance_perc": 0.1,
                    "width": 6, #TEU
                    "height": 5, #TEU
                    "length": 40, #TEU
                    "capacity": 1200 , #TEU
                    "gross_tgs": 18.67,
                    "area_factor": 2.79 , # Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY

sc_stack_data = {"name": 'SC Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 50_000,
                    "maintenance_perc": 0.1,
                    "width": 48, #TEU
                    "height": 4, #TEU
                    "length": 20, #TEU
                    "capacity": 3840 , #TEU
                    "gross_tgs": 26.46,
                    "area_factor": 1.45 , #Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY

rs_stack_data = {"name": 'RS Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 10_000,
                    "maintenance_perc": 0.1,
                    "width": 4, #TEU
                    "height": 4, #TEU
                    "length": 20, #TEU
                    "capacity": 320 , #TEU
                    "gross_tgs": 18,
                    "area_factor": 3.23 , # Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY


# *** Default inputs: Other_Stack class

empty_stack_data = {"name": 'Empty Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 25_000,
                    "maintenance_perc": 0.1,
                    "width": 8, #TEU
                    "height": 6, #TEU
                    "length": 10, #TEU
                    "capacity": 480 , #TEU
                    "gross_tgs": 18,
                    "area_factor": 2.04 , # Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY

oog_stack_data = {"name": 'OOG Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 25_000,
                    "maintenance_perc": 0.1,
                    "width": 10, #TEU
                    "height": 1, #TEU
                    "length": 10, #TEU
                    "capacity": 100 , #TEU
                    "gross_tgs": 64,
                    "area_factor": 1.05 , # Based on grasshopper layout
                    "pavement": 200, #DUMMY
                    "drainage": 50} #DUMMY

# *** Default inputs: Stack_Equipment class
#RTG # todo add eRTG

rtg_data = {"name": 'RTG',
            "type": 'rtg',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 1_400_000,
            "mobilisation": 5000,
            "maintenance_perc": 0.1, #dummy
            "insurance_perc": 0,
            "crew": 1, #dummy
            "salary": 50_000, #dummy
            "required": 3,
            "fuel_consumption": 1, #dummy
            "power_consumption": 0
            }

#RMG
rmg_data = {"name": 'RMG',
            "type": 'rmg',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 2_500_000,
            "mobilisation": 5000,
            "maintenance_perc": 0.1, #dummy
            "insurance_perc": 0,
            "crew": 0, #dummy
            "salary": 50_000, #dummy
            "required": 1, #one per stack
            "fuel_consumption": 0, #dummy
            "power_consumption": 15 #kWh/box move
            }

#Straddle carrier #
sc_data = {"name": 'Straddle carrier',
            "type": 'sc',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 2_000_000, #dummy
            "mobilisation": 5000,
            "maintenance_perc": 0.1, #dummy
            "insurance_perc": 0,
            "crew": 0, #dummy
            "salary": 50_000, #dummy
            "required": 5,
            "fuel_consumption": 15, #dummy
            "power_consumption": 0
            }

#Reach stacker
rs_data = {"name": 'Reach stacker',
            "type": 'rs',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 500_000,
            "mobilisation": 5000,
            "maintenance_perc": 0.1, #dummy
            "insurance_perc": 0,
            "crew": 2, #dummy
            "salary": 50_000, #dummy
            "required": 4,
            "fuel_consumption": 1, #dummy
            "power_consumption": 0
            }


# *** Default inputs: Storage class ***

silo_data = {"name": 'Silo_01',
             "type": 'silo',
             "ownership": 'Terminal operator',
             "delivery_time": 1,
             "lifespan": 30,
             "unit_rate": 60,
             "mobilisation_min": 200_000,
             "mobilisation_perc": 0.003,
             "maintenance_perc": 0.02,
             "crew": 1,
             "insurance_perc": 0.01,
             "storage_type": 'Silos',
             "consumption": 0.002,
             "capacity": 6_000} # all input values from Ijzermans, 2019, P 102

warehouse_data = {"name": 'Warehouse_01',
                  "style": 'warehouse',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 30,
                  "unit_rate": 140,
                  "mobilisation_min": 200_000,
                  "mobilisation_perc": 0.001,
                  "maintenance_perc": 0.01,
                  "crew": 3,
                  "insurance_perc": 0.01,
                  "storage_type": 'Warehouse',
                  "consumption": 0.002,
                  "silo_capacity": 'n/a'}

# *** Default inputs: Unloading_station class ***


hinterland_station_data = {"name": 'Hinterland_station_01',
                           "ownership": 'Terminal operator',
                           "delivery_time": 1,
                           "lifespan": 15,
                           "unit_rate": 800_000,
                           "mobilisation": 200_000,
                           "maintenance_perc": 0.02,
                           "consumption": 100,
                           "insurance_perc": 0.01,
                           "crew": 2,
                           "production": 800,
                           "wagon_payload" : 60,
                           "number_of_wagons": 60,
                           "prep_time": 2}

# *** Default inputs: Gate class ***

gate_data = {"name": 'Gate',
                 "type": 'gate',
               "ownership" :  "Terminal operator",
               "delivery_time": 1,
               "lifespan": 15,
               "unit_rate": 30_000,
               "mobilisation": 5000,
               "maintenance_perc": 0.02,
               "crew": 2,
               "salary": 30_000, #dummy
                "canopy_costs" : 250, #USD/m2 dummy
               "area": 288.75 , #PIANC WG135
                "staff_gates" : 1,
               "service_gates": 1,
                "design_capacity" : 0.98,
               "exit_inspection_time": 2,#min #dummy
                "entry_inspection_time" : 2, #min #dummy
               "peak_hour": 0.25,#dummy
                "peak_day" : 0.1,#dummy
               "peak_factor": 1.2,
                "truck_moves" : 0.75,
               "operating_days": 6,
             "capacity": 60}


# *** Default inputs: Commodity class ***
# TODO vervang soybean, maze en wheat door reefer, empty en oog dmv input value modal split


# soybean_data = {"name": 'Soybeans',
#                 "handling_fee": 9.8,
#                 "handysize_perc": 50,
#                 "handymax_perc": 50,
#                 "panamax_perc": 0,
#                 "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
#                                                     'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}
#
# wheat_data = {"name": 'Wheat',
#               "handling_fee": 9.8,
#               "handysize_perc": 0,
#               "handymax_perc": 0,
#               "panamax_perc": 100,
#               "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
#                                                   'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}

container_data = {"name": 'Laden',
                "handling_fee": 500,
                "handysize_perc": 0,
                "handymax_perc": 0,
                "panamax_perc": 100,
                "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
                                                    'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}




# *** Default inputs: Vessel class ***

handysize_data = {"name": 'Handysize_1',
                  "type": 'Handysize',
                  "call_size": 35_000,
                  "LOA": 130,
                  "draft": 10,
                  "beam": 24,
                  "max_cranes": 2,
                  "all_turn_time": 24,
                  "mooring_time": 3,
                  "demurrage_rate": 600}

handymax_data = {"name": 'Handymax_1',
                 "type": 'Handymax',
                 "call_size": 55_000,
                 "LOA": 180,
                 "draft": 11.5,
                 "beam": 28,
                 "max_cranes": 2,
                 "all_turn_time": 24,
                 "mooring_time": 3,
                 "demurrage_rate": 750}

panamax_data = {"name": 'Panamax_1',
                "type": 'Panamax',
                "call_size": 3000,#TEU
                "LOA": 290,
                "draft": 13,
                "beam": 32.2,
                "max_cranes": 4,#STS cranes
                "all_turn_time": 31,#UNCTAD geeft deze waarde voor container schepen
                "mooring_time": 6, #berthing + deberthing time
                "demurrage_rate": 730}


# *** Default inputs: Labour class ***

labour_data = {"name": 'Labour',
               "international_salary": 105_000,
               "international_staff": 4,
               "local_salary": 18_850,
               "local_staff": 10,
               "operational_salary": 16_750,
               "shift_length": 6.5,
               "annual_shifts": 200,
               "daily_shifts": 5}

# *** Default inputs: Energy class ***

energy_data = {"name": 'Energy',
               "price": 0.10}

# *** Default inputs: Train class ***

train_data = {"wagon_payload": 60,
              "number_of_wagons": 60}
