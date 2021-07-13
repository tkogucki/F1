import fastf1 as ff1
from matplotlib import pyplot as plt
import numpy as np

ff1.Cache.enable_cache(r'/home/tim/Projects/F1_cache')  # optional but highly recommended

austria_quali = ff1.get_session(2021, 'Austria', 'Q')

laps = austria_quali.load_laps(with_telemetry=True)

# Verstappen
fast_ver = laps.pick_driver('VER').pick_fastest()
ver_car_data = fast_ver.get_car_data()
ver_pos_data = fast_ver.get_pos_data()
# converting time data format
t = ver_car_data['Time']/np.timedelta64(1, 's')
verVel = ver_car_data['Speed']
brakeVel = ver_car_data['Brake']
throtVel = ver_car_data['Throttle']
x_Ver = ver_pos_data['X']
y_Ver = ver_pos_data['Y']

# Hamilton
fast_ham = laps.pick_driver('HAM').pick_fastest()
ham_car_data = fast_ham.get_car_data()
ham_pos_data = fast_ham.get_pos_data()
# converting time data format
t_ham = ham_car_data['Time']/np.timedelta64(1, 's')
hamVel = ham_car_data['Speed']
brakeHam = ham_car_data['Brake']
throtHAM = ham_car_data['Throttle']
x_Ham = ham_pos_data['X']
y_Ham = ham_pos_data['Y']

# Plotting Speed
fig, ax = plt.subplots(1,1)
ax.plot(t, verVel, label='VER')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Austria Qualifing')
ax.plot(t_ham, hamVel, label='HAM')
ax.legend()

# Plotting Location
fig2, ax2 = plt.subplots(1,1)
ax2.plot(x_Ver, y_Ver, label = 'VER')
ax2.set_title('Austria Qualifying')
ax2.set_xlabel('X [m]')
ax2.set_ylabel('Y [m]')
ax2.plot(x_Ham, y_Ham, label = 'HAM')
ax2.legend()


# Plotting Location
fig2, ax2 = plt.subplots(2,1)
ax2[0].plot(t, brakeVel, label = 'VER Brake')
ax2[1].plot(t, throtVel, label = 'VER Throttle')
ax2[0].set_title('Austria Qualifying')
ax2[0].set_xlabel('Time [s]')
ax2[0].set_ylabel('Percentage')
ax2[0].plot(t_ham, brakeHam, label = 'HAM Brake')
ax2[1].plot(t_ham, throtHAM, label = 'HAM Throttle')
ax2[0].legend()
plt.show()
