import streamlit as st
import pandas as pd
from datetime import datetime as dt

from opentisim.containers import container_objects
from opentisim.containers import container_defaults
from opentisim.containers import container_system

st.header("🚢 OpenTISim - Container Terminal")
st.write(
    "Open source Terminal Investment Simulation - Terminal investment strategy analysis, parametrically driven by changing demand scenarios."
)

# Input section
st.subheader("Input")
current_year = dt.now().year
col1, col2 = st.columns(2)
startyear = col1.number_input(
    "Start Year", min_value=1900, value=current_year, max_value=current_year, step=1
)
lifecycle = col2.number_input("Life Cycle", min_value=1, value=10, max_value=20, step=1)
endyear = startyear + lifecycle - 1

scenario_data = {
    "year": [year for year in range(startyear, endyear + 1)],
    "volume": [],
}

# Calculate the number of rows and columns
num_columns = min(lifecycle, 5)
num_rows = -(-lifecycle // num_columns)  # Ceiling division to calculate number of rows

# Create a list to store the input values
input_values = []

# Create the input fields in a grid layout
year = startyear
st.write("Demand input")
for row in range(num_rows):
    cols = st.columns(num_columns)
    for col in cols:
        if year <= endyear:
            scenario_data["volume"].append(
                col.number_input(
                    f"{year}",
                    min_value=0,
                    value=200000,
                    step=10000,
                    key=f"Demand {year}",
                )
            )
            year += 1

container = container_objects.Commodity(**container_defaults.container_data)
container.scenario_data = pd.DataFrame(data=scenario_data)

# Initialize vessels
fully_cellular_data = container_objects.Vessel(**container_defaults.fully_cellular_data)
panamax_data = container_objects.Vessel(**container_defaults.panamax_data)
panamax_max_data = container_objects.Vessel(**container_defaults.panamax_max_data)
post_panamax_I_data = container_objects.Vessel(**container_defaults.post_panamax_I_data)
post_panamax_II_data = container_objects.Vessel(
    **container_defaults.post_panamax_II_data
)
new_panamax_data = container_objects.Vessel(**container_defaults.new_panamax_data)
VLCS_data = container_objects.Vessel(**container_defaults.VLCS_data)
ULCS_data = container_objects.Vessel(**container_defaults.ULCS_data)
vessels = [
    fully_cellular_data,
    panamax_data,
    panamax_max_data,
    post_panamax_I_data,
    post_panamax_II_data,
    new_panamax_data,
    VLCS_data,
    ULCS_data,
]

# Simulate
demand = [container]
Terminal = container_system.System(
    startyear=startyear,
    lifecycle=lifecycle,
    elements=demand + vessels,
    operational_hours=7500,
    debug=True,
    crane_type_defaults=container_defaults.sts_crane_data,
)
Terminal.modelframe = scenario_data["year"]
Terminal.simulate()

# Plot
st.subheader("Output Plot")
st.write("Terminal Capacity")
fig = Terminal.terminal_capacity_plot()
st.pyplot(fig)

st.write("Terminal Elements")
fig = Terminal.terminal_elements_plot()
st.pyplot(fig)

st.write("Land Use")
fig = Terminal.land_use_plot()
st.pyplot(fig)

st.write("Laden Stack")
fig = Terminal.laden_stack_area_plot()
st.pyplot(fig)

# cash_flows, cash_flows_WACC_real = Terminal.add_cashflow_elements()
# st.write("Opex")
# fig = Terminal.terminal_land_use_plot(cash_flows)
# st.pyplot(fig)

st.caption(
    "For further details, check OpenTISim GitHub repo: https://github.com/TUDelft-CITG/OpenTISim"
)
