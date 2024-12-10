import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from plotly.express import line 
import plotly.express as px


np.random.seed()

df = pd.read_csv('filtered_data_test.csv')

regions = df['continent'].dropna().unique()

populations_dict = {
    'Africa': 536239200, #1340598000 %60 rural area,
    'Asia': 4600000000,
    'Europe': 747636026,
    'North America': 579024000,
    'South America': 422535000,
    'Oceania': 43111704
}

populations = np.array([populations_dict[r] for r in regions])

# Initial conditions
initial_S = populations.copy()
initial_I = np.zeros(len(regions))
initial_R = np.zeros(len(regions))
initial_D = np.zeros(len(regions))

# Başlangıç enfekte sayısı Asya'da 1 kişi
for idx, region in enumerate(regions):
    if region == 'Asia':
        initial_I[idx] = 1
        initial_S[idx] -= 1
        break

# Model parametreleri
R0_values = np.random.uniform(2.5, 3, size=len(regions))  # Daha düşük ve gerçekçi R0
gamma = np.random.uniform(0.05, 0.1, size=len(regions))  # İyileşme oranı
beta = R0_values * gamma  # Bulaşma katsayısı

# Ölüm oranları
death_rates = {
    'Africa': 0.01,
    'Asia': 0.02,
    'Europe': 0.03,
    'North America': 0.025,
    'South America': 0.015,
    'Oceania': 0.01
}

# Seyahat oranları
base_travel_rates = {
    'Africa': 0.0001, 
    'Asia': 0.005,
    'Europe': 0.010,
    'North America': 0.005,
    'South America': 0.003,
    'Oceania': 0.002
}

# Seyahat azaltma faktörleri
travel_reduction_factors = {
    'Africa': 0.5,
    'Asia': 0.5,
    'Europe': 0.4,
    'North America': 0.6,
    'South America': 0.5,
    'Oceania': 0.7
}

# Enfeksiyon ve ölüm eşikleri
infection_thresholds = {
    'Africa': 0.002,
    'Asia': 0.005,
    'Europe': 0.004,
    'North America': 0.004,
    'South America': 0.003,
    'Oceania': 0.002
}

death_thresholds = {
    'Africa': 0.0001,
    'Asia': 0.0002,
    'Europe': 0.0003,
    'North America': 0.0004,
    'South America': 0.0003,
    'Oceania': 0.0002
}

days = 360  # 1 yıl simülasyonu
iterations = 100  # Monte Carlo simülasyon sayısı

# Seyahat matrisi 
def create_travel_matrix(regions, base_travel_rates):
    n = len(regions)
    travel_matrix = np.zeros((n, n))
    for i, src_region in enumerate(regions):
        src_rate = base_travel_rates[src_region]
        per_dest_rate = src_rate / (n - 1)
        for j in range(n):
            if i != j:
                travel_matrix[i, j] = per_dest_rate
    return travel_matrix

# Seyahat oranlarını eşiklere göre ayarlanması
def adjust_travel_rates(travel_matrix, I, D, populations, regions, infection_thresholds, death_thresholds, travel_reduction_factors):
    for region_idx, region_name in enumerate(regions):
        infection_rate = I[region_idx] / populations[region_idx]
        death_rate = D[region_idx] / populations[region_idx]

        if infection_rate > infection_thresholds[region_name] or death_rate > death_thresholds[region_name]:
            factor = travel_reduction_factors[region_name]
            travel_matrix[region_idx] *= factor
    return travel_matrix

# Monte Carlo 
def monte_carlo_simulation_covid(days, regions, populations, initial_S, initial_I, initial_R, initial_D, 
                                beta, gamma, iterations, infection_thresholds, death_thresholds, 
                                base_travel_rates, travel_reduction_factors, death_rates):

    S_results = np.zeros((iterations, len(regions), days))
    I_results = np.zeros((iterations, len(regions), days))
    R_results = np.zeros((iterations, len(regions), days))
    D_results = np.zeros((iterations, len(regions), days))

    for it in range(iterations):
        S = np.zeros((len(regions), days))
        I = np.zeros((len(regions), days))
        R = np.zeros((len(regions), days))
        D = np.zeros((len(regions), days))

        S[:, 0] = initial_S
        I[:, 0] = initial_I
        R[:, 0] = initial_R
        D[:, 0] = initial_D

        travel_matrix = create_travel_matrix(regions, base_travel_rates)

        for day in range(1, days):
            N = S[:, day - 1] + I[:, day - 1] + R[:, day - 1] + D[:, day - 1]

            new_infected = beta * (S[:, day - 1] * I[:, day - 1]) / N
            new_infected = np.clip(new_infected, 0, S[:, day - 1])

            recoveries = gamma * I[:, day - 1]
            new_deaths = np.array([death_rates[region] * I[:, day - 1][ri] for ri, region in enumerate(regions)])

            current_infected = I[:, day - 1]
            outflow = (travel_matrix.sum(axis=1) * current_infected)
            inflow = travel_matrix.T @ current_infected

            S[:, day] = S[:, day - 1] - new_infected
            I[:, day] = I[:, day - 1] + new_infected - recoveries - new_deaths + inflow - outflow
            R[:, day] = R[:, day - 1] + recoveries
            D[:, day] = D[:, day - 1] + new_deaths

            S[:, day] = np.clip(S[:, day], 0, populations)
            I[:, day] = np.clip(I[:, day], 0, populations)
            R[:, day] = np.clip(R[:, day], 0, populations)
            D[:, day] = np.clip(D[:, day], 0, populations)

            travel_matrix = adjust_travel_rates(
                travel_matrix, I[:, day], D[:, day], populations, regions,
                infection_thresholds, death_thresholds, travel_reduction_factors
            )

        S_results[it] = S
        I_results[it] = I
        R_results[it] = R
        D_results[it] = D

    mean_S = S_results.mean(axis=0)
    mean_I = I_results.mean(axis=0)
    mean_R = R_results.mean(axis=0)
    mean_D = D_results.mean(axis=0)

    return mean_S, mean_I, mean_R, mean_D

mean_S, mean_I, mean_R, mean_D = monte_carlo_simulation_covid(
    days=days,
    regions=regions,
    populations=populations,
    initial_S=initial_S,
    initial_I=initial_I,
    initial_R=initial_R,
    initial_D=initial_D,
    beta=beta,
    gamma=gamma,
    iterations=iterations,
    infection_thresholds=infection_thresholds,
    death_thresholds=death_thresholds,
    base_travel_rates=base_travel_rates,
    travel_reduction_factors=travel_reduction_factors,
    death_rates=death_rates
)

# # Plot the infected results
# plt.figure(figsize=(12, 8))
# for i, region in enumerate(regions):
#     plt.plot(range(days), mean_I[i], label=f"{region}")

# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
# plt.title('COVID-19 Infection Spread (SIRD Model) with Region-Specific Travel')
# plt.xlabel('Days')
# plt.ylabel('Infected Population')
# plt.legend(title='Regions')
# plt.grid(True)
# plt.show()  



# Plotly visualization
data = {
    'Days': np.tile(range(days), len(regions)),
    'Infected': mean_I.flatten(),
    'Region': np.repeat(regions, days)
}
df_plotly = pd.DataFrame(data)

# Line chart with Plotly
fig = px.line(
    df_plotly,
    x='Days',
    y='Infected',
    color='Region',
    title='COVID-19 Infection Spread (SIRD Model) with Region-Specific Travel - Variant - 2 ',
    labels={'Infected': 'Infected Population', 'Days': 'Days'},
    template='plotly_white'
)

# Formatting the axes
fig.update_layout(
    yaxis=dict(
        title="Infected Population",
        tickformat=","
    ),
    xaxis=dict(
        title="Days"
    )
)
fig.update_yaxes(tickformat="d")


# # Plot deaths
# plt.figure(figsize=(12, 8))
# for i, region in enumerate(regions):
#     plt.plot(range(days), mean_D[i], label=f"{region} (Deaths)")
# plt.title('COVID-19 Deaths (SIRD Model) with Region-Specific Travel')
# plt.xlabel('Days')
# plt.ylabel('Deaths')
# plt.legend(title='Regions')
# plt.grid(True)
# plt.show()



# fig.add_trace(
#     px.line(df_plotly, x='Days', y=mean_D.flatten(), color='Region', labels={'y': 'Cumulative Deaths'})
# )


# Display the graph
fig.show()